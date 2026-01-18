import logging
from collections.abc import Callable
from typing import Any

from blendshape_router.VRChatBuilder import VRChatBuilder
from blendshape_router.plugin.endpoints.vrchat.connection.receive.VRChatConnectionPool import VRChatConnectionPool
from blendshape_router.solver.SolverPath import SolverPath
from blendshape_router.solver.model.loader.ModelLoader import ModelLoader
from zeroconf import Zeroconf

from config.ConfigManager import ConfigManager
from config.ConfigUpdateListener import ConfigUpdateListener
from config.schemas.avatar.AvatarConfig import AvatarConfig
from config.schemas.main.Config import Config
from stream.core.StreamWriteOnly import StreamWriteOnly
from stream.postprocessing.BlendShapesFrame import BlendShapesFrame
from stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum
from stream.senders.config.VRchatAvatarConfigManager import VRChatAvatarConfigManager
from util.PathUtil import PathUtil

_logger = logging.getLogger(__name__)


class VRChatSenderPipeline(StreamWriteOnly[BlendShapesFrame[GeneralBlendShapeEnum]]):
    def __init__(self, config_manager: ConfigManager, avatar_config_manager: VRChatAvatarConfigManager):
        self.__config_manager: ConfigManager = config_manager
        self.__avatar_config_manager: VRChatAvatarConfigManager = avatar_config_manager

        self.__main_config_listener: ConfigUpdateListener = self.__register_main_config_change_update()

        self.__zeroconf: Zeroconf = Zeroconf()
        self.__connection_pool: VRChatConnectionPool = VRChatConnectionPool()

    def put(self, value: BlendShapesFrame[GeneralBlendShapeEnum]) -> bool:
        pass

    def close(self):
        self.__main_config_listener.unregister()

        self.__zeroconf.close()

    def __register_main_config_change_update(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.sender.vrchat]

        return self.__config_manager.create_update_listener(self.__main_config_changed, watch_array, True)

    def __register_avatar_config_change_update(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[AvatarConfig], Any]] = [lambda config: config.disable_solver_input_nodes,
                                                            lambda config: config.disable_solver_output_nodes,
                                                            lambda config: config.disable_output_encoders]

        return self.__

    def __main_config_changed(self, config_manager: ConfigManager[Config]):
        builder = (VRChatBuilder(self.__zeroconf, self.__connection_pool)
                   .with_avatar_update_period(config_manager.config.sender.vrchat.avatar_update_period)
                   .with_avatar_error_sleep_time(config_manager.config.sender.vrchat.avatar_error_sleep_time)
                   .with_avatar_close_connection_after_retries(
            config_manager.config.sender.vrchat.avatar_close_connection_after_retries)
                   .with_zeroconf_timeout(config_manager.config.sender.vrchat.zeroconf_timeout)
                   .with_osc_cache_invalidate_timeout(config_manager.config.sender.vrchat.cache_invalidate_timeout)
                   .with_osc_cache_full_sync_period(config_manager.config.sender.vrchat.cache_full_sync_period)
                   .with_osc_cache_float_precision(config_manager.config.sender.vrchat.cache_float_precision)
                   .with_osc_bundle_size(config_manager.config.sender.vrchat.osc_bundle_size)

                   )

        if config_manager.config.sender.vrchat.solver_enabled:
            model = self.__get_model(config_manager.config.sender.vrchat.solver_model_path)

            if model is not None:
                clamped_percentage = max(0.0, min(1.0,
                                                  config_manager.config.sender.vrchat.solver_interleaved_vertices_percentage))

                vertices_count = max(1, int(model.get_vertices_count() * clamped_percentage))

                (builder
                 .with_solver_model(model)
                 .with_solver_threads(config_manager.config.sender.vrchat.solver_threads)
                 .with_solver_max_cps(config_manager.config.sender.vrchat.solver_max_cps)
                 .with_solver_interleaved_vertices_count(vertices_count))

    def __avatar_config_changed(self, avatar_config_manager: ConfigManager):
        pass

    @staticmethod
    def __get_model(custom_model_path: str) -> ModelLoader | None:
        model_path = PathUtil.to_path_or_default(custom_model_path, SolverPath.get_default_asset_path())

        try:
            return ModelLoader(model_path)
        except Exception:
            _logger.warning("Failed to load custom model", exc_info=True, stack_info=True)

        return None
