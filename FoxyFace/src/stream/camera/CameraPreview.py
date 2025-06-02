import logging
import threading

from PySide6.QtGui import QImage

from src.stream.camera.CameraFrame import CameraFrame
from src.stream.camera.CameraProcessing import CameraProcessing
from src.stream.camera.CameraProcessingOption import CameraProcessingOption
from src.stream.camera.CameraStream import CameraStream
from src.stream.core.StreamReadOnly import StreamReadOnly
from src.stream.core.components.SingleBufferStream import SingleBufferStream
from src.ui.windows.ImagePreviewWindow import ImagePreviewWindow

_logger = logging.getLogger(__name__)


class CameraPreview:
    def __init__(self, camera_stream_root: CameraStream, post_processing_options: CameraProcessingOption,
                 frame_timeout: float | None = 1.0):
        self.__camera_stream: CameraStream = camera_stream_root
        self.__frame_timeout: float | None = frame_timeout

        self.__single_buffer_image_stream: SingleBufferStream[CameraFrame] = SingleBufferStream[CameraFrame]()
        self.__image_stream: StreamReadOnly[CameraFrame] = CameraProcessing(self.__single_buffer_image_stream,
                                                                            post_processing_options)

        self.__window: ImagePreviewWindow = ImagePreviewWindow(title="Camera Preview")

        self.__thread = threading.Thread(target=self.__loop, daemon=True, name="Camera Preview")
        self.__thread.start()

        self.__camera_stream.register_stream(self.__single_buffer_image_stream)

    def is_closed(self) -> bool:
        return self.__window.is_closed.is_set()

    def close(self, do_join: bool = True):
        self.__window.is_closed.set()
        self.__window.close_event.emit()

        if do_join:
            try:
                self.__thread.join(self.__frame_timeout * 2.0)
            except Exception:
                _logger.warning("Failed to join Camera Preview thread", exc_info=True, stack_info=True)

        self.__camera_stream.unregister_stream(self.__single_buffer_image_stream)
        self.__single_buffer_image_stream.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __loop(self):
        while not self.is_closed():
            try:
                image = self.__image_stream.poll(self.__frame_timeout).frame

                # noinspection PyTypeChecker
                im = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format.Format_RGB888)

                self.__window.set_image_event.emit(im)
            except TimeoutError:
                self.__window.set_image_event.emit(None)
            except InterruptedError:
                break
            except Exception:
                _logger.warning("Exception in Camera Preview loop", exc_info=True, stack_info=True)

                self.__window.is_closed.wait(0.001)

        self.close(False)
