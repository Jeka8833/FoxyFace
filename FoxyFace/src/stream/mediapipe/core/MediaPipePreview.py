import logging
import threading

import cv2
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QWidget

from src.stream.core.components.SingleBufferStream import SingleBufferStream
from src.stream.mediapipe.core.MediaPipeFrame import MediaPipeFrame
from src.stream.mediapipe.core.MediaPipeStream import MediaPipeStream
from src.ui.windows.ImagePreviewWindow import ImagePreviewWindow

_logger = logging.getLogger(__name__)


class MediaPipePreview:
    def __init__(self, mediapipe_stream: MediaPipeStream, frame_timeout: float | None = 1.0):
        self.__mediapipe_stream: MediaPipeStream = mediapipe_stream
        self.__frame_timeout: float | None = frame_timeout

        self.__single_buffer_stream: SingleBufferStream[MediaPipeFrame] = SingleBufferStream[MediaPipeFrame]()

        self.__window: ImagePreviewWindow = ImagePreviewWindow(title="MediaPipe Camera Preview")

        self.__thread = threading.Thread(target=self.__loop, daemon=True, name="MediaPipe Camera Preview")
        self.__thread.start()

        self.__mediapipe_stream.register_stream(self.__single_buffer_stream)

    def is_closed(self) -> bool:
        return self.__window.is_closed.is_set()

    def close(self):
        self.__window.is_closed.set()

        self.__mediapipe_stream.unregister_stream(self.__single_buffer_stream)
        self.__single_buffer_stream.close()

        try:
            self.__thread.join()
        except Exception:
            pass

        self.__window.close_event.emit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __loop(self):
        while not self.is_closed():
            try:
                frame = self.__single_buffer_stream.poll(self.__frame_timeout)

                image = frame.camera_frame.frame.copy()

                if frame.face_landmarker_result.face_landmarks:
                    for points in frame.face_landmarker_result.face_landmarks[0]:
                        if points.x > 1.0 or points.y > 1.0 or points.x < 0.0 or points.y < 0.0:
                            continue

                        x = int(points.x * image.shape[1])
                        y = int(points.y * image.shape[0])
                        size = max(0, min(4, int(4 + points.z * -10)))

                        cv2.circle(image, (x, y), size, (0, 255, 0), -1)

                im = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format.Format_RGB888)

                self.__window.image_event.emit(QPixmap.fromImage(im))
            except TimeoutError:
                self.__window.noimage_event.emit()
            except InterruptedError:
                self.close()

                return
            except Exception:
                _logger.warning("Exception in MediaPipe Preview loop", exc_info=True, stack_info=True)

                self.__window.is_closed.wait(0.001)
