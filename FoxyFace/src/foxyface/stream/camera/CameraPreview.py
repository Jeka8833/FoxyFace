import logging
import threading

from PySide6.QtGui import QImage

from foxyface.stream.camera.CameraProcessing import CameraProcessing
from foxyface.stream.camera.CameraProcessingOption import CameraProcessingOption
from foxyface.stream.camera.CameraStream import CameraStream
from foxyface.stream.core.StreamReadOnly import StreamReadOnly
from foxyface.stream.core.components.SingleBufferStream import SingleBufferStream
from foxyface.stream.postprocessing.frames.ImageFrame import ImageFrame
from foxyface.ui.windows.ImagePreviewWindow import ImagePreviewWindow

_logger = logging.getLogger(__name__)


class CameraPreview:
    def __init__(self, camera_stream_root: CameraStream, post_processing_options: CameraProcessingOption,
                 frame_timeout: float | None = 1.0):
        self.__camera_stream: CameraStream = camera_stream_root
        self.__frame_timeout: float | None = frame_timeout

        self.__single_buffer_image_stream: SingleBufferStream[ImageFrame] = SingleBufferStream[ImageFrame]()
        self.__image_stream: StreamReadOnly[ImageFrame] = CameraProcessing(self.__single_buffer_image_stream,
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
                if self.__frame_timeout is None:
                    self.__thread.join(5.0)
                else:
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
                image = self.__image_stream.poll(self.__frame_timeout).image

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
