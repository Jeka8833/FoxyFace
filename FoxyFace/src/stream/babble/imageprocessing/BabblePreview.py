import logging
import threading

from PySide6.QtGui import QImage

from src.pipline.MediaPipePipeline import MediaPipePipeline
from src.stream.babble.BabbleModelLoader import BabbleModelLoader
from src.stream.babble.imageprocessing.BabbleImageFrame import BabbleImageFrame
from src.stream.babble.imageprocessing.BabbleImageProcessing import BabbleImageProcessing
from src.stream.babble.imageprocessing.BabbleImageProcessingOptions import BabbleImageProcessingOptions
from src.stream.core.StreamReadOnly import StreamReadOnly
from src.stream.core.components.SingleBufferStream import SingleBufferStream
from src.stream.mediapipe.core.MediaPipeFrame import MediaPipeFrame
from src.stream.mediapipe.core.MediaPipeStream import MediaPipeStream
from src.ui.windows.ImagePreviewWindow import ImagePreviewWindow

_logger = logging.getLogger(__name__)


class BabblePreview:
    def __init__(self, mediapipe_stream: MediaPipeStream | MediaPipePipeline,
                 processing_options: BabbleImageProcessingOptions, model_loader: BabbleModelLoader,
                 frame_timeout: float | None = 1.0):
        self.__mediapipe_stream: MediaPipeStream | MediaPipePipeline = mediapipe_stream
        self.__processing_options: BabbleImageProcessingOptions = processing_options
        self.__model_loader: BabbleModelLoader = model_loader
        self.__frame_timeout: float | None = frame_timeout

        self.__single_buffer_stream: SingleBufferStream[MediaPipeFrame] = SingleBufferStream[MediaPipeFrame]()
        self.__image_stream: StreamReadOnly[BabbleImageFrame] = BabbleImageProcessing(self.__single_buffer_stream,
                                                                                      self.__processing_options,
                                                                                      self.__model_loader)

        self.__window: ImagePreviewWindow = ImagePreviewWindow(title="Babble Camera Preview")

        self.__thread = threading.Thread(target=self.__loop, daemon=True, name="Babble Preview")
        self.__thread.start()

        self.__mediapipe_stream.register_stream(self.__single_buffer_stream)

    def is_closed(self) -> bool:
        return self.__window.is_closed.is_set()

    def close(self, do_join: bool = True):
        self.__window.is_closed.set()
        self.__window.close_event.emit()

        if do_join:
            try:
                self.__thread.join(self.__frame_timeout * 2.0)
            except Exception:
                _logger.warning("Failed to join Babble Preview thread", exc_info=True, stack_info=True)

        self.__mediapipe_stream.unregister_stream(self.__single_buffer_stream)
        self.__single_buffer_stream.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __loop(self):
        while not self.is_closed():
            try:
                image = self.__image_stream.poll(self.__frame_timeout).processed_frame

                # noinspection PyTypeChecker
                im = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format.Format_Grayscale8)

                self.__window.set_image_event.emit(im)
            except TimeoutError:
                self.__window.set_image_event.emit(None)
            except InterruptedError:
                break
            except Exception:
                _logger.warning("Exception in Babble Preview loop", exc_info=True, stack_info=True)

                self.__window.is_closed.wait(0.001)

        self.close(False)
