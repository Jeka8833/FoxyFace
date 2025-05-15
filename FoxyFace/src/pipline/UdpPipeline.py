from typing import Any, Callable

from src.config.ConfigManager import ConfigManager
from src.config.ConfigUpdateListener import ConfigUpdateListener
from src.config.schemas.Config import Config
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
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.socket.ip,
                                                      lambda config: config.socket.port,
                                                      lambda config: config.socket.udp_read_timeout,
                                                      lambda config: config.socket.bypass_other_modules_block]

        return self.__config_manager.create_update_listener(self.__update_options, watch_array, True)

    def __update_options(self, config_manager: ConfigManager):
        self.__options.udp_read_timeout_ms = config_manager.config.socket.udp_read_timeout
        self.__options.bypass_other_modules_block = config_manager.config.socket.bypass_other_modules_block

        self.__stream.ping_connection_time = config_manager.config.socket.udp_read_timeout / 4000.0
        self.__stream.target_address = (config_manager.config.socket.ip, config_manager.config.socket.port)

    def __register_auto_connect_change(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.socket.auto_connect]

        return self.__config_manager.create_update_listener(self.__update_auto_connect, watch_array, True)

    def __update_auto_connect(self, config_manager: ConfigManager):
        if config_manager.config.socket.auto_connect:
            self.__auto_connect.start()
        else:
            self.__auto_connect.stop()