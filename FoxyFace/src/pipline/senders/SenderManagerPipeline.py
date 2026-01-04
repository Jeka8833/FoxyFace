import logging
from collections.abc import Callable
from threading import Event, Thread, Lock
from typing import Any

from config.ConfigManager import ConfigManager
from config.ConfigUpdateListener import ConfigUpdateListener
from config.schemas.Config import Config
from pipline.ProcessingPipeline import ProcessingPipeline
from pipline.senders.foxyface.FoxyFaceSenderPipeline import FoxyFaceSenderPipeline
from stream.core.StreamWriteOnly import StreamWriteOnly
from stream.postprocessing.BlendShapesFrame import BlendShapesFrame
from stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum

_logger = logging.getLogger(__name__)


class SenderManagerPipeline:
    def __init__(self, config_manager: ConfigManager, processing_pipeline: ProcessingPipeline):
        self.__config_manager = config_manager
        self.__processing_pipeline = processing_pipeline

        self.__sender_update_listener: ConfigUpdateListener = self.__register_sender_toggle_update()

        self.__sender_active_set: dict[str, StreamWriteOnly[BlendShapesFrame[GeneralBlendShapeEnum]]] = {}
        self.__lock: Lock = Lock()
        self.__close_event: Event = Event()

        self.__thread: Thread = Thread(target=self.__start_loop, daemon=True, name="Sender Manager Pipeline")
        self.__thread.start()

    def close(self):
        self.__close_event.set()

        self.__sender_update_listener.unregister()

    def __register_sender_toggle_update(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.sender.foxyface.enabled,
                                                      lambda config: config.sender.ifacialmocap.enabled,
                                                      lambda config: config.sender.meowface.enabled,
                                                      lambda config: config.sender.vrchat.enabled]

        return self.__config_manager.create_update_listener(self.__sender_toggled_callback, watch_array, True)

    def __sender_toggled_callback(self, config_manager: ConfigManager):
        with self.__lock:
            if config_manager.config.sender.foxyface.enabled:
                if "FoxyFace" not in self.__sender_active_set:
                    self.__sender_active_set["FoxyFace"] = FoxyFaceSenderPipeline(config_manager=config_manager)
            else:
                value = self.__sender_active_set.pop("FoxyFace", None)

                if value is not None:
                    value.close()

            if config_manager.config.sender.ifacialmocap.enabled:
                if "iFacialMocap" not in self.__sender_active_set:
                    self.__sender_active_set["iFacialMocap"] = None
            else:
                if "iFacialMocap" in self.__sender_active_set:
                    value = self.__sender_active_set.pop("iFacialMocap", None)

                    if value is not None:
                        value.close()

            if config_manager.config.sender.meowface.enabled:
                if "MeowFace" not in self.__sender_active_set:
                    self.__sender_active_set["MeowFace"] = None
            else:
                if "MeowFace" in self.__sender_active_set:
                    value = self.__sender_active_set.pop("MeowFace", None)

                    if value is not None:
                        value.close()

            if config_manager.config.sender.vrchat.enabled:
                if "VRChat" not in self.__sender_active_set:
                    self.__sender_active_set["VRChat"] = None
            else:
                if "VRChat" in self.__sender_active_set:
                    value = self.__sender_active_set.pop("VRChat", None)

                    if value is not None:
                        value.close()

    def __start_loop(self):
        while not self.__close_event.is_set():
            try:
                data = self.__processing_pipeline.get_udp_stream().poll()

                with self.__lock:
                    for sender in self.__sender_active_set.values():
                        sender.put(data)
            except Exception:
                _logger.warning("Exception", exc_info=True, stack_info=True)

            self.__close_event.wait(0.01)
