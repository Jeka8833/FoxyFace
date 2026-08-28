import logging

import cv2

from foxyface.stream.camera.info.CameraBackend import CameraBackend
from foxyface.stream.camera.info.CameraEntry import CameraEntry

_logger = logging.getLogger(__name__)


class CameraList:
    def __init__(self):
        self.__is_loaded = self.__try_enable_lib()
        self.__backends: dict[int, CameraBackend] = self.__get_all_backends()

    @property
    def is_loaded(self) -> bool:
        return self.__is_loaded

    @property
    def backends(self) -> dict[int, CameraBackend]:
        return self.__backends

    def get_all_cameras(self) -> list[CameraEntry]:
        if not self.is_loaded:
            return []

        import cv2_enumerate_cameras
        cameras_info = cv2_enumerate_cameras.enumerate_cameras()

        camera_entries = [CameraEntry.create_using_camera_info(info) for info in cameras_info]

        return [entry for entry in camera_entries if entry.backend in self.backends]

    def find_or_create_by_backend_and_index(self, backend: int, index: int | str) -> CameraEntry:
        all_cameras = self.get_all_cameras()

        for camera in all_cameras:
            if camera.backend == backend and camera.index == index:
                return camera.change_manual(True)

        return CameraEntry.create_using_backend_and_index(backend, index)

    def find_best(self, selected_camera: CameraEntry) -> CameraEntry:
        if selected_camera.manual:
            return self.find_or_create_by_backend_and_index(selected_camera.backend, selected_camera.index)

        all_cameras = self.get_all_cameras()

        if not all_cameras:
            return self.find_or_create_by_backend_and_index(selected_camera.backend, selected_camera.index)

        return max(all_cameras, key=lambda camera: camera.compare(selected_camera))

    @staticmethod
    def __get_all_backends() -> dict[int, CameraBackend]:
        backends = cv2.videoio_registry.getCameraBackends()
        result: dict[int, CameraBackend] = {}

        for backend_id in backends:
            try:
                if CameraList.__is_backend_functional(backend_id):
                    result[backend_id] = CameraBackend(
                        name=cv2.videoio_registry.getBackendName(backend_id),
                        index=backend_id,
                        input_type=CameraList.__backend_2_input_type(backend_id)
                    )
            except Exception as e:
                _logger.info(f"Failed to check backend {backend_id}: {e}")

        return result

    @staticmethod
    def __is_backend_functional(backend_id: int) -> bool:
        if backend_id == cv2.CAP_GSTREAMER:
            cap = cv2.VideoCapture("videotestsrc ! appsink", cv2.CAP_GSTREAMER)
            try:
                return cap.isOpened()
            finally:
                cap.release()

        if not cv2.videoio_registry.isBackendBuiltIn(backend_id):
            try:
                if backend_id in cv2.videoio_registry.getCameraBackends():
                    if not cv2.videoio_registry.getCameraBackendPluginVersion(backend_id)[0]:
                        return False
            except Exception:
                return False

        return True

    @staticmethod
    def __try_enable_lib() -> bool:
        try:
            import cv2_enumerate_cameras
            raw_cameras = cv2_enumerate_cameras.enumerate_cameras()  # Test

            _logger.info(f"Available raw cameras: {raw_cameras}")

            return True
        except Exception:

            _logger.exception("Failed to load cv2_enumerate_cameras", exc_info=True)
            return False

    @staticmethod
    def __backend_2_input_type(index) -> frozenset[type[str | int]]:
        match index:
            case (cv2.CAP_FFMPEG
                  | cv2.CAP_IMAGES
                  | cv2.CAP_OPENCV_MJPEG
                  | cv2.CAP_INTEL_MFX
                  | cv2.CAP_XINE):
                return frozenset([str])

            case (cv2.CAP_FIREWIRE
                  | cv2.CAP_FIREWARE
                  | cv2.CAP_IEEE1394
                  | cv2.CAP_DC1394
                  | cv2.CAP_CMU1394
                  | cv2.CAP_DSHOW
                  | cv2.CAP_PVAPI
                  | cv2.CAP_ANDROID
                  | cv2.CAP_XIAPI
                  | cv2.CAP_WINRT
                  | cv2.CAP_INTELPERC
                  | cv2.CAP_REALSENSE
                  | cv2.CAP_GPHOTO2
                  | cv2.CAP_ARAVIS
                  | cv2.CAP_UEYE
                  | cv2.CAP_OBSENSOR):
                return frozenset([int])
            case _:
                return frozenset([str, int])
