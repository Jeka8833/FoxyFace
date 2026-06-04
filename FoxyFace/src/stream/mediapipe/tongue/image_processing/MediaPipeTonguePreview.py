import logging
import threading

from PySide6.QtGui import QImage

from src.pipline.MediaPipePipeline import MediaPipePipeline
from src.stream.core.StreamReadOnly import StreamReadOnly
from src.stream.core.components.SingleBufferStream import SingleBufferStream
from src.stream.mediapipe.face.core.MediaPipeFrame import MediaPipeFrame
from src.stream.mediapipe.face.core.MediaPipeStream import MediaPipeStream
from src.stream.mediapipe.tongue.image_processing.MediaPipeTongueImageProcessing import MediaPipeTongueImageProcessing
from src.stream.mediapipe.tongue.image_processing.MediaPipeTongueProcessingOptions import \
    MediaPipeTongueProcessingOptions
from src.stream.postprocessing.frames.ImageFrame import ImageFrame
from src.ui.windows.ImagePreviewWindow import ImagePreviewWindow

_logger = logging.getLogger(__name__)


class MediaPipeTonguePreview:
    def __init__(self, mediapipe_stream: MediaPipeStream | MediaPipePipeline,
                 processing_options: MediaPipeTongueProcessingOptions, frame_timeout: float | None = 1.0):
        self.__mediapipe_stream: MediaPipeStream | MediaPipePipeline = mediapipe_stream
        self.__processing_options: MediaPipeTongueProcessingOptions = processing_options
        self.__frame_timeout: float | None = frame_timeout

        self.__single_buffer_stream: SingleBufferStream[MediaPipeFrame] = SingleBufferStream[MediaPipeFrame]()
        self.__image_stream: StreamReadOnly[ImageFrame] = MediaPipeTongueImageProcessing(self.__single_buffer_stream,
                                                                                         self.__processing_options)

        self.__window: ImagePreviewWindow = ImagePreviewWindow(title="MediaPipe Tongue Preview")

        self.__thread = threading.Thread(target=self.__loop, daemon=True, name="MediaPipe Tongue Preview")
        self.__thread.start()

        self.__mediapipe_stream.register_stream(self.__single_buffer_stream)

    def is_closed(self) -> bool:
        return self.__window.is_closed.is_set()

    def close(self, do_join: bool = True):
        self.__window.is_closed.set()
        self.__window.close_event.emit()

        if do_join:
            try:
                if self.__frame_timeout is None:
                    self.__thread.join(5.0)
                else:
                    self.__thread.join(self.__frame_timeout * 2.0)
            except Exception:
                _logger.warning("Failed to join MediaPipe Tongue Preview thread", exc_info=True, stack_info=True)

        self.__mediapipe_stream.unregister_stream(self.__single_buffer_stream)
        self.__single_buffer_stream.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __loop(self):
        while not self.is_closed():
            try:
                image = self.__image_stream.poll(self.__frame_timeout).image

                # noinspection PyTypeChecker
                im = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format.Format_RGB888)

                self.__window.set_image_event.emit(im)
            except TimeoutError:
                self.__window.set_image_event.emit(None)
            except InterruptedError:
                break
            except Exception:
                _logger.warning("Exception in MediaPipe Tongue Preview loop", exc_info=True, stack_info=True)

                self.__window.is_closed.wait(0.001)

        self.close(False)
