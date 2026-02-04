import logging
from threading import Event, Thread

from src.config.ConfigManager import ConfigManager
from src.pipline.ProcessingPipeline import ProcessingPipeline
from src.pipline.senders.GeneralToBlendshapeRouterMapper import GeneralToBlendshapeRouterMapper
from src.pipline.senders.foxyface.FoxyFaceSenderPipeline import FoxyFaceSenderPipeline
from src.pipline.senders.vrchat.VRChatSenderPipeline import VRChatSenderPipeline
from src.stream.postprocessing.BlendShapesFrame import BlendShapesFrame
from src.stream.senders.config.VRchatAvatarConfigManager import VRChatAvatarConfigManager

_logger = logging.getLogger(__name__)


class SenderRouterPipeline:
    def __init__(self, config_manager: ConfigManager, processing_pipeline: ProcessingPipeline,
                 vrchat_config_manager: VRChatAvatarConfigManager, ifacialmocap_config_manager: ConfigManager,
                 foxyface_config_manager: ConfigManager, meowface_config_manager: ConfigManager):
        self.__processing_pipeline = processing_pipeline

        self.__sender_list = [FoxyFaceSenderPipeline(config_manager, foxyface_config_manager),
                              VRChatSenderPipeline(config_manager, vrchat_config_manager)
                              ]

        self.__close_event: Event = Event()

        self.__thread: Thread = Thread(target=self.__start_loop, daemon=True, name="Sender Manager Pipeline")
        self.__thread.start()

    def close(self):
        self.__close_event.set()

        for sender in self.__sender_list:
            try:
                sender.close()
            except Exception:
                _logger.warning("Failed to close sender", exc_info=True, stack_info=True)

    def __start_loop(self):
        while not self.__close_event.is_set():
            try:
                data = self.__processing_pipeline.get_udp_stream().poll()

                blendshapes = GeneralToBlendshapeRouterMapper.convert(data.blend_shapes)

                blendshape_frame = BlendShapesFrame(blendshapes, data.timestamp_ns)

                for sender in self.__sender_list:
                    try:
                        sender.put(blendshape_frame)
                    except Exception:
                        _logger.warning("Exception in sender", exc_info=True, stack_info=True)
            except InterruptedError:
                return
            except Exception:
                _logger.warning("Sender pipeline error", exc_info=True, stack_info=True)

            self.__close_event.wait(0.01)
