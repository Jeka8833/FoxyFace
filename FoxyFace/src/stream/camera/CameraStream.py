import logging
import platform
import time
from threading import Event, Thread

import cv2

from src.stream.camera.CameraFrame import CameraFrame
from src.stream.camera.CameraEnumerator import CameraEnumerator
from src.stream.core.StreamWriteOnly import StreamWriteOnly
from src.stream.core.components.WriteStreamSplitter import WriteStreamSplitter

_logger = logging.getLogger(__name__)


class CameraStream:
    def __init__(self):
        self.__stream_root = WriteStreamSplitter[CameraFrame]()

        self.__camera: cv2.VideoCapture | None = None

        self.__close_event = Event()

        self.__thread = Thread(target=self.__start_loop, daemon=True, name="Camera Stream")
        self.__thread.start()

    def start_new_camera(self, camera_id: int, width: int, height: int, camera_name: str = ""):
        """
        Start a new camera stream.
        
        Args:
            camera_id: Camera index (used as fallback if camera_name is not found)
            width: Desired frame width
            height: Desired frame height
            camera_name: Optional camera name to search for (preferred over camera_id)
        """
        if self.__close_event.is_set():
            raise RuntimeError("CameraStream is closed")

        if not isinstance(width, int) or width <= 0 or width % 2 != 0:
            raise ValueError("Invalid width")

        if not isinstance(height, int) or height <= 0 or height % 2 != 0:
            raise ValueError("Invalid height")

        # Try to find camera by name if provided
        actual_camera_id = camera_id
        if camera_name:
            found_id = CameraEnumerator.find_camera_by_name(camera_name)
            if found_id is not None:
                actual_camera_id = found_id
                _logger.info(f"Found camera '{camera_name}' at index {actual_camera_id}")
            else:
                _logger.warning(f"Camera '{camera_name}' not found, falling back to camera_id {camera_id}")

        if not isinstance(actual_camera_id, int) or actual_camera_id < 0:
            raise ValueError("Invalid camera id")

        camera = self.__camera
        if camera is not None:
            camera.release()

        if platform.system() == "Windows":
            camera = cv2.VideoCapture(actual_camera_id, cv2.CAP_DSHOW)
        else:
            camera = cv2.VideoCapture(actual_camera_id)

        camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        self.__camera = camera

        _logger.info(f"Camera started (id: {actual_camera_id}, name: {camera_name or 'N/A'})")


    def register_stream(self, stream: StreamWriteOnly[CameraFrame]) -> None:
        self.__stream_root.register_stream(stream)

    def unregister_stream(self, stream: StreamWriteOnly[CameraFrame]) -> None:
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

                        packet = CameraFrame(numpy_frame_from_opencv, current_time)

                        self.__stream_root.put(packet)
                        continue
            except Exception:
                _logger.warning("Exception", exc_info=True, stack_info=True)

            self.__close_event.wait(0.01)
