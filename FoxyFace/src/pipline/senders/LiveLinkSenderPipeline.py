import ipaddress
import logging
from collections.abc import Callable
from fractions import Fraction
from threading import Lock
from typing import Any

from blendshape_router.LiveLinkBuilder import LiveLinkBuilder
from blendshape_router.facades.livelink.LiveLink import LiveLink
from blendshape_router.graph.Node import Node
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
from src.config.schemas.main.core.sender.LiveLinkSenderConfig import LiveLinkSenderConfig
from src.stream.postprocessing.frames.BlendShapesFrame import BlendShapesFrame
from src.stream.senders.AvatarEndpoint import AvatarEndpoint
from src.stream.senders.SenderInterface import SenderInterface
from src.util.PathUtil import PathUtil

_logger = logging.getLogger(__name__)


class LiveLinkSenderPipeline(SenderInterface):
    def __init__(self, config_manager: ConfigManager[Config], livelink_config_manager: ConfigManager[AvatarConfig]):
        self.__config_manager: ConfigManager[Config] = config_manager
        self.__avatar_config_manager: ConfigManager[AvatarConfig] = livelink_config_manager

        self.__create_lock: Lock = Lock()
        self.__livelink: LiveLink | None = None
        self.__avatar_endpoint: frozenset[AvatarEndpoint] = frozenset()

        self.__main_config_listener: ConfigUpdateListener = self.__register_change_update()
        self.__avatar_config_listener: ConfigUpdateListener = self.__register_avatar_change_update()

    def put(self, value: BlendShapesFrame[BaseParameter | ARKitParameter]):
        livelink = self.__livelink
        if livelink is not None:
            for node, node_value in value.blend_shapes.items():
                if node_value is None:
                    continue

                livelink.set_parameter(node, node_value)

            livelink.flush()

    def get_endpoints(self) -> frozenset[AvatarEndpoint]:
        return self.__avatar_endpoint

    def close(self):
        self.__main_config_listener.unregister()
        self.__avatar_config_listener.unregister()

        with self.__create_lock:
            if self.__livelink is not None:
                self.__livelink.close()

    def __register_change_update(self) -> ConfigUpdateListener[Config]:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.sender.livelink]

        return self.__config_manager.create_update_listener(lambda config: self.__livelink_changed(),
                                                            watch_array, False)

    def __register_avatar_change_update(self) -> ConfigUpdateListener[AvatarConfig]:
        watch_array: list[Callable[[AvatarConfig], Any]] = [lambda config: config.disable_solver_input_nodes,
                                                            lambda config: config.disable_solver_output_nodes,
                                                            lambda config: config.disable_output_encoders]

        return self.__avatar_config_manager.create_update_listener(lambda config: self.__livelink_changed(),
                                                                   watch_array, True)

    def __livelink_changed(self):
        with self.__create_lock:
            if self.__livelink is not None:
                self.__livelink.close()

            livelink_config: LiveLinkSenderConfig = self.__config_manager.config.sender.livelink

            if not livelink_config.enabled:
                self.__livelink = None
                self.__avatar_endpoint = frozenset()

                return

            solver_model: ModelLoader | None = None
            vertices_count: int = 1

            disabled_inputs = {SolverNode(node_id) for node_id in
                               self.__avatar_config_manager.config.disable_solver_input_nodes}
            disabled_outputs = {Node(node_id) for node_id in
                                self.__avatar_config_manager.config.disable_solver_output_nodes}

            if livelink_config.solver_enabled:
                solver_model = ModelLoader(
                    PathUtil.to_path_or_default(livelink_config.solver_model_path,
                                                SolverPath.get_default_asset_path()))

                clamped_percentage = max(0.0, min(1.0,
                                                  livelink_config.solver_interleaved_vertices_percentage))

                vertices_count = max(1, int(solver_model.get_vertices_count() * clamped_percentage))

            disabled_encoders: set[EndpointEncoderInterface[dict[str, float]]] = {
                encoder for encoder in LiveLink.get_available_endpoints()
                if encoder.id_str() in self.__avatar_config_manager.config.disable_output_encoders
            }

            fps = Fraction(livelink_config.fps_numerator, livelink_config.fps_denominator)

            self.__livelink = (LiveLinkBuilder(
                HostAddress(ipaddress.ip_address(livelink_config.ip), livelink_config.port))
                                   .with_subject_name(livelink_config.subject_name)
                                   .with_device_id(livelink_config.device_id)
                                   .with_fps(fps)
                                   .with_udp_ping_interval(livelink_config.udp_ping_interval)
                                   .with_udp_cache_invalidate_timeout(livelink_config.cache_invalidate_timeout)
                                   .with_udp_cache_full_sync_period(livelink_config.cache_full_sync_period)
                                   .with_udp_cache_float_precision(livelink_config.cache_float_precision)
                                   .with_crash_sleep_time(livelink_config.crash_sleep_time)
                                   .with_test_send_period(livelink_config.test_send_period)
                                   .with_test_animation_period(livelink_config.test_animation_period)
                                   .with_solver_model(solver_model)
                                   .with_solver_threads(livelink_config.solver_threads)
                                   .with_solver_interleaved_vertices_count(vertices_count)
                                   .with_solver_max_cps(livelink_config.solver_max_cps)
                                   .disable_solver_input_nodes(disabled_inputs)
                                   .disable_solver_output_nodes(disabled_outputs)
                                   .disable_output_endpoints(disabled_encoders)

                                   .add_graph(ARKitGraph())

                                   .build())

            all_solver_inputs = frozenset(self.__livelink.get_all_solver_input_functions())
            all_solver_outputs = frozenset(self.__livelink.get_all_solver_output_functions())

            self.__avatar_endpoint = frozenset(
                [AvatarEndpoint(endpoint_name="LiveLink", config_manager=self.__avatar_config_manager,
                                endpoints=LiveLink.get_available_endpoints(),
                                solver_inputs=all_solver_inputs,
                                solver_outputs=all_solver_outputs,
                                graphs=self.__livelink.get_graphs,
                                test_endpoint_callable=self.__livelink.enable_parameter_testing,
                                stop_all_test_endpoint_callable=self.__livelink.disable_parameter_testing)])
