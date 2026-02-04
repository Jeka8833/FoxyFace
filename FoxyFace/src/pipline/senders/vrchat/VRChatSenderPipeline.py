import logging
from collections.abc import Callable
from ipaddress import ip_address
from threading import Lock, Event, Thread
from typing import Any

from blendshape_router.VRChatBuilder import VRChatBuilder
from blendshape_router.facades.vrchat.VRChat import VRChat
from blendshape_router.plugin.endpoints.vrchat.AvatarInfo import AvatarInfo
from blendshape_router.plugin.endpoints.vrchat.connection.receive.ConnectionNode import ConnectionNode
from blendshape_router.plugin.endpoints.vrchat.connection.receive.VRChatConnectionPool import VRChatConnectionPool
from blendshape_router.preset.ARKitGraph import ARKitGraph
from blendshape_router.preset.ARKitParameter import ARKitParameter
from blendshape_router.preset.BaseParameter import BaseParameter
from blendshape_router.router.EndpointEncoderInterface import EndpointEncoderInterface
from blendshape_router.solver.SolverPath import SolverPath
from blendshape_router.solver.graph.SolverNode import SolverNode
from blendshape_router.solver.model.loader.ModelLoader import ModelLoader
from zeroconf import Zeroconf

from config.ConfigManager import ConfigManager
from config.ConfigUpdateListener import ConfigUpdateListener
from config.schemas.avatar.AvatarConfig import AvatarConfig
from config.schemas.main.Config import Config
from pipline.senders.vrchat.FindInstanceItem import FindInstanceItem
from stream.core.StreamWriteOnly import StreamWriteOnly
from stream.postprocessing.BlendShapesFrame import BlendShapesFrame
from stream.senders.config.VRchatAvatarConfigManager import VRChatAvatarConfigManager
from util.PathUtil import PathUtil

_logger = logging.getLogger(__name__)


class VRChatSenderPipeline(StreamWriteOnly[BlendShapesFrame[BaseParameter | ARKitParameter]]):
    __FIND_RETRY_COUNT: int = 10

    def __init__(self, config_manager: ConfigManager[Config], avatar_config_manager: VRChatAvatarConfigManager):
        self.__config_manager: ConfigManager[Config] = config_manager
        self.__avatar_config_manager: VRChatAvatarConfigManager = avatar_config_manager

        self.__zeroconf: Zeroconf = Zeroconf()
        self.__connection_pool: VRChatConnectionPool = VRChatConnectionPool()
        self.__vrchat: VRChat | None = None

        self.__config_list_changed_lock: Lock = Lock()
        self.__config_listeners: dict[ConnectionNode, ConfigUpdateListener[AvatarConfig]] = {}

        self.__find_instance_lock: Lock = Lock()
        self.__config_find_instance: dict[ConnectionNode, FindInstanceItem] = {}
        self.__find_instance_close_event: Event = Event()
        self.__find_instance_thread: Thread = Thread(target=self.__find_instance_thread_start, daemon=True,
                                                     name="Find VRChat Instance Thread")
        self.__find_instance_thread.start()

        self.__main_config_listener: ConfigUpdateListener = self.__register_main_config_change_update()
        avatar_config_manager.subscribe_change(self.__avatar_config_list_changed)

    def put(self, value: BlendShapesFrame[BaseParameter | ARKitParameter]) -> bool:
        vrchat = self.__vrchat
        if vrchat is not None:
            for node, node_value in value.blend_shapes.items():
                if node_value is None:
                    continue

                vrchat.set_parameter(node, node_value)

            vrchat.flush()

        return True

    def close(self):
        self.__main_config_listener.unregister()

        self.__vrchat.close()

        self.__zeroconf.close()
        self.__connection_pool.close()

    def __register_main_config_change_update(self) -> ConfigUpdateListener[Config]:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.sender.vrchat]

        return self.__config_manager.create_update_listener(self.__main_config_changed, watch_array, True)

    def __main_config_changed(self, config_manager: ConfigManager[Config]):
        if self.__vrchat is not None:
            self.__vrchat.close()
            self.__vrchat = None

        if not config_manager.config.sender.vrchat.enabled:
            return

        self.__vrchat = (VRChatBuilder(self.__zeroconf, self.__connection_pool)
                         .with_ip_filter(self.__ip_filter)
                         .with_avatar_parameter_filter(self.__avatar_parameter_filter)
                         .with_connection_closed_listener(self.__connection_closed)

                         .with_avatar_update_period(config_manager.config.sender.vrchat.avatar_update_period)
                         .with_avatar_error_sleep_time(config_manager.config.sender.vrchat.avatar_error_sleep_time)
                         .with_avatar_close_connection_after_retries(
            config_manager.config.sender.vrchat.avatar_close_connection_after_retries)
                         .with_zeroconf_timeout(config_manager.config.sender.vrchat.zeroconf_timeout)
                         .with_osc_cache_invalidate_timeout(
            config_manager.config.sender.vrchat.cache_invalidate_timeout)
                         .with_osc_cache_full_sync_period(config_manager.config.sender.vrchat.cache_full_sync_period)
                         .with_osc_cache_float_precision(config_manager.config.sender.vrchat.cache_float_precision)
                         .with_osc_bundle_size(config_manager.config.sender.vrchat.osc_bundle_size)
                         .with_legacy_graph(config_manager.config.sender.vrchat.allow_legacy_graph)
                         .with_parser_max_binary_bits(config_manager.config.sender.vrchat.parser_max_binary_bits)
                         .with_test_send_period(config_manager.config.sender.vrchat.test_send_period)
                         .with_test_animation_period(config_manager.config.sender.vrchat.test_animation_period)

                         .add_graph(ARKitGraph())

                         .build())

    def __avatar_config_list_changed(self, connection: ConnectionNode,
                                     avatar_config_manager: ConfigManager[AvatarConfig],
                                     created: bool):
        with self.__config_list_changed_lock:
            if created:
                if connection in self.__config_listeners:
                    return

                watch_array: list[Callable[[AvatarConfig], Any]] = [lambda config: config.disable_solver_input_nodes,
                                                                    lambda config: config.disable_solver_output_nodes,
                                                                    lambda config: config.disable_output_encoders]

                self.__config_listeners[connection] = avatar_config_manager.create_update_listener(
                    lambda config, connection_=connection: self.__avatar_config_changed(connection_, config),
                    watch_array, True)

            else:
                value = self.__config_listeners.pop(connection)

                if value is not None:
                    value.unregister()

    def __avatar_config_changed(self, connection: ConnectionNode, avatar_config_manager: ConfigManager[AvatarConfig]):
        with self.__find_instance_lock:
            self.__config_find_instance[connection] = FindInstanceItem(0, avatar_config_manager)

    def __ip_filter(self, node: ConnectionNode) -> bool:
        for ip in self.__config_manager.config.sender.vrchat.blocked_ips:
            try:
                parsed_ip = ip_address(ip)

                if parsed_ip is node.send_address.host:
                    _logger.info(f"Ip {parsed_ip} is blocked")

                    return False
            except Exception:
                _logger.warning("Fail to parse VRChat blocked IP")

        return True

    def __avatar_parameter_filter(self, node: ConnectionNode, avatar: AvatarInfo) -> frozenset[
        EndpointEncoderInterface[dict[str, float | bool | list[float]]]]:
        _logger.info(f"Get or load avatar config {avatar.avatar_id}, connection: {node.name}")

        config_manager = self.__avatar_config_manager.get_config_or_load(node, avatar)

        encoders: set[EndpointEncoderInterface[dict[str, float | bool | list[float]]]] = set(avatar.endpoints)
        for encoder in avatar.endpoints:
            if encoder.id_str() in config_manager.config.disable_output_encoders:
                encoders.remove(encoder)

        _logger.info(f"For avatar {avatar.avatar_id} filtered endpoints: {encoders}")

        return avatar.endpoints

    def __connection_closed(self, node: ConnectionNode):
        self.__avatar_config_manager.close_connection(node)

    def __find_instance_thread_start(self):
        while not self.__find_instance_close_event.is_set():
            try:
                for key, value in self.__config_find_instance.copy().items():
                    instance = self.__vrchat.get_instances().get(key)

                    if instance is None:
                        value.retry_count += 1

                        if value.retry_count >= self.__FIND_RETRY_COUNT:
                            self.__config_find_instance.pop(key)

                        continue

                    if self.__config_manager.config.sender.vrchat.solver_enabled:
                        model = ModelLoader(
                            PathUtil.to_path_or_default(self.__config_manager.config.sender.vrchat.solver_model_path,
                                                        SolverPath.get_default_asset_path()))

                        if model is not None:
                            clamped_percentage = max(0.0, min(1.0,
                                                              self.__config_manager.config.sender.vrchat.solver_interleaved_vertices_percentage))

                            vertices_count = max(1, int(model.get_vertices_count() * clamped_percentage))

                            id_to_node: dict[str, SolverNode] = {node.id: node for node in model.get_blendshapes()}

                            disabled_inputs: set[SolverNode] = set()
                            for node_id in value.config.config.disable_solver_input_nodes:
                                try:
                                    disabled_inputs.add(id_to_node[node_id])
                                except Exception:
                                    _logger.warning(f"Failed to disable input node {node_id}")

                            disabled_outputs: set[SolverNode] = set()
                            for node_id in value.config.config.disable_solver_output_nodes:
                                try:
                                    disabled_outputs.add(id_to_node[node_id])
                                except Exception:
                                    _logger.warning(f"Failed to disable output node {node_id}")

                            instance.set_solver(solver_model=model,
                                                threads=self.__config_manager.config.sender.vrchat.solver_threads,
                                                interleaved_vertices_count=vertices_count,
                                                max_cps=self.__config_manager.config.sender.vrchat.solver_max_cps,
                                                disable_input_nodes=disabled_inputs,
                                                disable_output_nodes=disabled_outputs)
            except InterruptedError:
                return
            except Exception:
                _logger.warning("VRchat find thread error", exc_info=True, stack_info=True)

            self.__find_instance_close_event.wait(0.01)
