import logging
from typing import Any, Callable

from src.config.ConfigManager import ConfigManager
from src.config.ConfigUpdateListener import ConfigUpdateListener
from src.config.schemas.Config import Config
from src.stream.camera.CameraFrame import CameraFrame
from src.stream.camera.CameraPreview import CameraPreview
from src.stream.camera.CameraProcessingOption import CameraProcessingOption
from src.stream.camera.CameraStream import CameraStream
from src.stream.core.StreamWriteOnly import StreamWriteOnly
from src.stream.core.components.WriteCpsCounter import WriteCpsCounter

_logger = logging.getLogger(__name__)


class CameraPipeline:
    def __init__(self, config_manager: ConfigManager):
        self.__config_manager: ConfigManager = config_manager

        self.__stream: CameraStream = CameraStream()
        self.__stream_listener: ConfigUpdateListener = self.__register_change_camera_options()

        self.__processing_options: CameraProcessingOption = CameraProcessingOption()
        self.__processing_options_listener: ConfigUpdateListener = self.__register_change_processing_options()

        self.__fps_counter = WriteCpsCounter()
        self.__stream.register_stream(self.__fps_counter)

        self.__preview_window: CameraPreview | None = None

    def register_stream(self, stream: StreamWriteOnly[CameraFrame]) -> None:
        self.__stream.register_stream(stream)

    def unregister_stream(self, stream: StreamWriteOnly[CameraFrame]) -> None:
        self.__stream.unregister_stream(stream)

    def trigger_view_preview(self):
        if self.__preview_window is None or self.__preview_window.is_closed():
            self.__preview_window = CameraPreview(self.__stream, self.__processing_options)
        else:
            self.__preview_window.close()

    def get_processing_options(self) -> CameraProcessingOption:
        return self.__processing_options

    def get_fps(self):
        return self.__fps_counter.get_cps()

    def close(self):
        if self.__preview_window is not None:
            self.__preview_window.close()

        self.__stream.unregister_stream(self.__fps_counter)

        self.__stream_listener.unregister()
        self.__processing_options_listener.unregister()

        self.__stream.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __register_change_processing_options(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.camera.mirror_x,
                                                      lambda config: config.camera.mirror_y,
                                                      lambda config: config.camera.rotate_ninety]

        return self.__config_manager.create_update_listener(self.__update_processing_options, watch_array, True)

    def __update_processing_options(self, config_manager: ConfigManager):
        self.__processing_options.mirror_x = config_manager.config.camera.mirror_x
        self.__processing_options.mirror_y = config_manager.config.camera.mirror_y
        self.__processing_options.rotate_ninety = config_manager.config.camera.rotate_ninety

    def __register_change_camera_options(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.camera.width,
                                                      lambda config: config.camera.height,
                                                      lambda config: config.camera.camera_id,
                                                      lambda config: config.camera.camera_name]

        return self.__config_manager.create_update_listener(self.__update_camera_options, watch_array, True)

    def __update_camera_options(self, config_manager: ConfigManager):
        try:
            self.__stream.start_new_camera(config_manager.config.camera.camera_id,
                                           (config_manager.config.camera.width // 2) * 2,
                                           (config_manager.config.camera.height // 2) * 2,
                                           config_manager.config.camera.camera_name)
        except Exception:
            _logger.warning("Failed to recreate camera", exc_info=True, stack_info=True)
