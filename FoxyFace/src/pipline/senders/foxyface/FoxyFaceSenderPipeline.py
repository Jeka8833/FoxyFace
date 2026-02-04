from typing import Callable, Any

from src.config.ConfigManager import ConfigManager
from src.config.ConfigUpdateListener import ConfigUpdateListener
from src.config.schemas.main.Config import Config
from src.stream.core.StreamWriteOnly import StreamWriteOnly
from src.stream.postprocessing.BlendShapesFrame import BlendShapesFrame
from src.stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum


class FoxyFaceSenderPipeline(StreamWriteOnly[BlendShapesFrame[GeneralBlendShapeEnum]]):
    def __init__(self, config_manager: ConfigManager, foxyface_config_manager: ConfigManager):
        self.__config_manager: ConfigManager = config_manager

        self.__stream_listener: ConfigUpdateListener = self.__register_change_update()

    def put(self, value: BlendShapesFrame[GeneralBlendShapeEnum]) -> bool:
        pass

    def close(self):
        self.__stream_listener.unregister()

    def __register_change_update(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.sender.foxyface]

        return self.__config_manager.create_update_listener(self.__foxyface_changed, watch_array, True)

    def __foxyface_changed(self, config_manager: ConfigManager):
        pass
