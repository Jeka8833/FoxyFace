from typing import Callable, Any

from config.ConfigManager import ConfigManager
from config.ConfigUpdateListener import ConfigUpdateListener
from config.schemas.Config import Config
from stream.core.StreamWriteOnly import StreamWriteOnly
from stream.postprocessing.BlendShapesFrame import BlendShapesFrame
from stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum


class FoxyFaceSenderPipeline(StreamWriteOnly[BlendShapesFrame[GeneralBlendShapeEnum]]):
    def __init__(self, config_manager: ConfigManager):
        pass

    def put(self, value: BlendShapesFrame[GeneralBlendShapeEnum]) -> bool:
        pass

    def close(self):
        pass

    def __register_change_update(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.sender.foxyface]

        return self.__config_manager.create_update_listener(self.__sender_toggled_callback, watch_array, True)