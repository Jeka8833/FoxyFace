import logging
import time
from threading import Event, Thread

import cv2

from src.stream.camera.info.CameraEntry import CameraEntry
from src.stream.camera.info.CameraList import CameraList
from src.stream.core.StreamWriteOnly import StreamWriteOnly
from src.stream.core.components.WriteStreamSplitter import WriteStreamSplitter
from src.stream.postprocessing.frames.ImageFrame import ImageFrame

_logger = logging.getLogger(__name__)


class CameraStream:
    def __init__(self, camera_list: CameraList):
        self.__camera_list: CameraList = camera_list

        self.__stream_root = WriteStreamSplitter[ImageFrame]()

        self.__camera: cv2.VideoCapture | None = None

        self.__close_event = Event()

        self.__thread = Thread(target=self.__start_loop, daemon=True, name="Camera Stream")
        self.__thread.start()

    def start_new_camera(self, camera_info: CameraEntry, width: int, height: int):
        if self.__close_event.is_set():
            raise RuntimeError("CameraStream is closed")

        if not isinstance(width, int) or width <= 0 or width % 2 != 0:
            raise ValueError("Invalid width")

        if not isinstance(height, int) or height <= 0 or height % 2 != 0:
            raise ValueError("Invalid height")

        best_camera = self.__camera_list.find_best(camera_info)

        camera = self.__camera
        if camera is not None:
            camera.release()

        camera = cv2.VideoCapture(best_camera.index, best_camera.backend)

        camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        self.__camera = camera

        _logger.info(f"Camera {best_camera} started")

    def register_stream(self, stream: StreamWriteOnly[ImageFrame]) -> None:
        self.__stream_root.register_stream(stream)

    def unregister_stream(self, stream: StreamWriteOnly[ImageFrame]) -> None:
        self.__stream_root.unregister_stream(stream)

    def close(self) -> None:
        self.__close_event.set()

        if self.__camera is not None:
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
                if self.__camera is not None and self.__camera.isOpened():
                    success, numpy_frame_from_opencv = self.__camera.read()  # fast close not guaranteed
                    if success:
                        current_time = time.perf_counter_ns()

                        packet = ImageFrame(numpy_frame_from_opencv, current_time)

                        self.__stream_root.put(packet)
                        continue
            except Exception:
                _logger.warning("Exception", exc_info=True, stack_info=True)

            self.__close_event.wait(0.01)
