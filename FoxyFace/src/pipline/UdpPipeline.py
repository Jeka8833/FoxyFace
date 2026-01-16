from typing import Any, Callable

from src.config.ConfigManager import ConfigManager
from src.config.ConfigUpdateListener import ConfigUpdateListener
from config.schemas.main.Config import Config
from src.pipline.ProcessingPipeline import ProcessingPipeline
from src.stream.vrcft.VRCFTUdpSocket import VRCFTUdpSocket
from src.stream.vrcft.VrcftAutoConnect import VrcftAutoConnect
from src.stream.vrcft.VrcftInterfaceOptions import VrcftInterfaceOptions
from src.stream.vrcft.VrcftPacketEncoderStream import VrcftPacketEncoderStream


class UdpPipeline:
    def __init__(self, config_manager: ConfigManager, processing_pipeline: ProcessingPipeline):
        self.__config_manager = config_manager
        self.__processing_pipeline = processing_pipeline

        self.__options = VrcftInterfaceOptions()

        encoder_stream = VrcftPacketEncoderStream(self.__processing_pipeline.get_udp_stream(), self.__options)

        self.__stream = VRCFTUdpSocket(encoder_stream)
        self.__options_listener = self.__register_change_options()
        self.__auto_connect = VrcftAutoConnect(self.__config_manager)
        self.__auto_connect_listener = self.__register_auto_connect_change()

    def has_error(self) -> bool:
        return self.__stream.has_error()

    def get_pps(self) -> float:
        return self.__stream.get_pps()

    def close(self):
        self.__stream.close()

        self.__options_listener.unregister()
        self.__auto_connect_listener.unregister()

        self.__auto_connect.stop()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __register_change_options(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = []

        return self.__config_manager.create_update_listener(self.__update_options, watch_array, True)

    def __update_options(self, config_manager: ConfigManager):
        pass

    def __register_auto_connect_change(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = []

        return self.__config_manager.create_update_listener(self.__update_auto_connect, watch_array, True)

    def __update_auto_connect(self, config_manager: ConfigManager):
        pass
