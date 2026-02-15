import ipaddress
import logging
from threading import Lock
from typing import Callable, Any

from blendshape_router.FoxyFaceBuilder import FoxyFaceBuilder
from blendshape_router.facades.foxyface.FoxyFace import FoxyFace
from blendshape_router.plugin.endpoints.foxyface.graph.FoxyFaceGraph import FoxyFaceGraph
from blendshape_router.preset.ARKitGraph import ARKitGraph
from blendshape_router.preset.ARKitParameter import ARKitParameter
from blendshape_router.preset.BaseParameter import BaseParameter
from blendshape_router.router.EndpointEncoderInterface import EndpointEncoderInterface
from blendshape_router.solver.SolverPath import SolverPath
from blendshape_router.solver.graph.SolverNode import SolverNode
from blendshape_router.solver.model.loader.ModelLoader import ModelLoader
from blendshape_router.util.HostAddress import HostAddress

from src.config.ConfigManager import ConfigManager
from src.config.ConfigUpdateListener import ConfigUpdateListener
from src.config.schemas.avatar.AvatarConfig import AvatarConfig
from src.config.schemas.main.Config import Config
from src.config.schemas.main.core.sender.FoxyFaceSenderConfig import FoxyFaceSenderConfig
from src.stream.postprocessing.BlendShapesFrame import BlendShapesFrame
from src.stream.senders.AvatarEndpoint import AvatarEndpoint
from src.stream.senders.SenderInterface import SenderInterface
from src.util.PathUtil import PathUtil

_logger = logging.getLogger(__name__)


class FoxyFaceSenderPipeline(SenderInterface):
    def __init__(self, config_manager: ConfigManager[Config], avatar_config_manager: ConfigManager[AvatarConfig]):
        self.__config_manager: ConfigManager[Config] = config_manager
        self.__avatar_config_manager: ConfigManager[AvatarConfig] = avatar_config_manager

        self.__create_lock: Lock = Lock()
        self.__foxyface: FoxyFace | None = None
        self.__avatar_endpoint: frozenset[AvatarEndpoint] = frozenset()

        self.__main_config_listener: ConfigUpdateListener = self.__register_change_update()
        self.__avatar_config_listener: ConfigUpdateListener = self.__register_avatar_change_update()

    def put(self, value: BlendShapesFrame[BaseParameter | ARKitParameter]) -> bool:
        foxyface = self.__foxyface
        if foxyface is not None:
            for node, node_value in value.blend_shapes.items():
                if node_value is None:
                    continue

                foxyface.set_parameter(node, node_value)

            foxyface.flush()

        return True

    def get_endpoints(self) -> frozenset[AvatarEndpoint]:
        return self.__avatar_endpoint

    def close(self):
        self.__main_config_listener.unregister()
        self.__avatar_config_listener.unregister()

        with self.__create_lock:
            if self.__foxyface is not None:
                self.__foxyface.close()

    def __register_change_update(self) -> ConfigUpdateListener[Config]:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.sender.foxyface]

        return self.__config_manager.create_update_listener(lambda config: self.__foxyface_changed(),
                                                            watch_array, False)

    def __register_avatar_change_update(self) -> ConfigUpdateListener[AvatarConfig]:
        watch_array: list[Callable[[AvatarConfig], Any]] = [lambda config: config.disable_solver_input_nodes,
                                                            lambda config: config.disable_solver_output_nodes,
                                                            lambda config: config.disable_output_encoders]

        return self.__avatar_config_manager.create_update_listener(lambda config: self.__foxyface_changed(),
                                                                   watch_array, True)

    def __foxyface_changed(self):
        with self.__create_lock:
            if self.__foxyface is not None:
                self.__foxyface.close()

                self.__foxyface = None
                self.__avatar_endpoint = frozenset()

            foxyface_config: FoxyFaceSenderConfig = self.__config_manager.config.sender.foxyface

            if not foxyface_config.enabled:
                return

            solver_model: ModelLoader | None = None
            vertices_count = 1
            disabled_inputs: set[SolverNode] = set()
            disabled_outputs: set[SolverNode] = set()

            if foxyface_config.solver_enabled:
                solver_model = ModelLoader(
                    PathUtil.to_path_or_default(foxyface_config.solver_model_path, SolverPath.get_default_asset_path()))

                clamped_percentage = max(0.0, min(1.0,
                                                  foxyface_config.solver_interleaved_vertices_percentage))

                vertices_count = max(1, int(solver_model.get_vertices_count() * clamped_percentage))

                id_to_node: dict[str, SolverNode] = {node.id: node for node in solver_model.get_blendshapes()}

                for node_id in self.__avatar_config_manager.config.disable_solver_input_nodes:
                    try:
                        disabled_inputs.add(id_to_node[node_id])
                    except Exception:
                        _logger.warning(f"Failed to disable input node {node_id}")

                for node_id in self.__avatar_config_manager.config.disable_solver_output_nodes:
                    try:
                        disabled_outputs.add(id_to_node[node_id])
                    except Exception:
                        _logger.warning(f"Failed to disable output node {node_id}")

            disabled_encoders: set[EndpointEncoderInterface[dict[str, float]]] = set(FoxyFace.get_available_endpoints())
            for encoder in disabled_encoders.copy():
                if encoder.id_str() not in self.__avatar_config_manager.config.disable_output_encoders:
                    disabled_encoders.remove(encoder)

            self.__foxyface = (FoxyFaceBuilder()
                               .with_udp_address(HostAddress(ipaddress.ip_address(foxyface_config.ip),
                                                             foxyface_config.port))
                               .with_auto_connect(foxyface_config.auto_connect_enabled)
                               .with_auto_connect_port(foxyface_config.auto_connect_port)
                               .with_host_read_timeout(foxyface_config.host_read_timeout)
                               .with_udp_ping_interval(foxyface_config.udp_ping_interval)
                               .with_udp_cache_invalidate_timeout(foxyface_config.cache_invalidate_timeout)
                               .with_udp_cache_full_sync_period(foxyface_config.cache_full_sync_period)
                               .with_udp_cache_float_precision(foxyface_config.cache_float_precision)
                               .with_test_send_period(foxyface_config.test_send_period)
                               .with_test_animation_period(foxyface_config.test_animation_period)
                               .with_solver_model(solver_model)
                               .with_solver_threads(foxyface_config.solver_threads)
                               .with_solver_interleaved_vertices_count(vertices_count)
                               .with_solver_max_cps(foxyface_config.solver_max_cps)
                               .disable_solver_input_nodes(disabled_inputs)
                               .disable_solver_output_nodes(disabled_outputs)
                               .disable_output_endpoints(disabled_encoders)

                               .add_graph(ARKitGraph())

                               .build())

            all_nodes = (FoxyFaceGraph() + ARKitGraph()).get_all_nodes()
            all_solver_inputs = frozenset(solver_model.load_input_functions(all_nodes))
            all_solver_outputs = frozenset(solver_model.load_output_functions(all_nodes))

            self.__avatar_endpoint = frozenset(
                [AvatarEndpoint(endpoint_name="FoxyFace", config_manager=self.__avatar_config_manager,
                                endpoints=FoxyFace.get_available_endpoints(),
                                solver_inputs=all_solver_inputs,
                                solver_outputs=all_solver_outputs)])
