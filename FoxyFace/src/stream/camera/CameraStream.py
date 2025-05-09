import logging
import threading
import time

import cv2

from src.stream.camera.CameraFrame import CameraFrame
from src.stream.core.StreamWriteOnly import StreamWriteOnly
from src.stream.core.components.WriteStreamSplitter import WriteStreamSplitter

_logger = logging.getLogger(__name__)


class CameraStream:
    def __init__(self, camera_id: int = 0, width: int = 640, height: int = 480):
        self.camera_id: int = camera_id
        self.width: int = width
        self.height: int = height

        self.__stream_root = WriteStreamSplitter[CameraFrame]()

        self.__camera = cv2.VideoCapture()
        self.recreate_camera()

        self.__close_event = threading.Event()
        self.__thread = threading.Thread(target=self.__start_loop, daemon=True, name="Camera Stream")
        self.__thread.start()

    def recreate_camera(self):
        if not isinstance(self.camera_id, int) or self.camera_id < 0:
            raise ValueError("Invalid camera id")

        if not isinstance(self.width, int) or self.width <= 0:
            raise ValueError("Invalid width")

        if not isinstance(self.height, int) or self.height <= 0:
            raise ValueError("Invalid height")

        self.__camera.release()
        self.__camera.open(self.camera_id)
        self.__camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.__camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

    def register_stream(self, stream: StreamWriteOnly[CameraFrame]) -> None:
        self.__stream_root.register_stream(stream)

    def unregister_stream(self, stream: StreamWriteOnly[CameraFrame]) -> None:
        self.__stream_root.unregister_stream(stream)

    def close(self) -> None:
        self.__close_event.set()

        self.__camera.release()

        self.__thread.join()

        self.__stream_root.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __start_loop(self):
        while not self.__close_event.is_set():
            try:
                if self.__camera.isOpened():
                    success, numpy_frame_from_opencv = self.__camera.read()  # fast close not guaranteed
                    if success:
                        current_time = time.perf_counter_ns()

                        packet = CameraFrame(numpy_frame_from_opencv, current_time)

                        self.__stream_root.put(packet)
                        continue
            except Exception:
                _logger.warning("Exception", exc_info=True, stack_info=True)

            self.__close_event.wait(0.001)
