import logging
import platform
from dataclasses import dataclass

import cv2

_logger = logging.getLogger(__name__)


@dataclass
class CameraInfo:
    """Information about an available camera."""

    index: int
    name: str


class CameraEnumerator:
    """Utility class to enumerate available cameras and their names."""

    _pygrabber_disabled = False
    _cached_device_names: list[str] | None = None

    @staticmethod
    def get_available_cameras(
        max_cameras: int = 10, force_refresh_names: bool = False
    ) -> list[CameraInfo]:
        """
        Enumerate available cameras on the system.

        Args:
            max_cameras: Maximum number of camera indices to check (default: 10)
            force_refresh_names: Whether to force refresh of device names (default: False)

        Returns:
            List of CameraInfo objects containing camera index and name
        """
        if force_refresh_names:
            CameraEnumerator._cached_device_names = None

        available_cameras = []
        is_windows = platform.system() == "Windows"
        backend = cv2.CAP_DSHOW if is_windows else cv2.CAP_ANY
        windows_device_names = (
            CameraEnumerator._get_windows_device_names() if is_windows else []
        )

        for camera_index in range(max_cameras):
            try:
                camera = cv2.VideoCapture(camera_index, backend)
                if camera.isOpened():
                    # Try to get camera name/description
                    camera_name = CameraEnumerator._get_camera_name(
                        camera=camera,
                        camera_index=camera_index,
                        backend=backend,
                        windows_device_names=windows_device_names,
                    )
                    available_cameras.append(
                        CameraInfo(index=camera_index, name=camera_name)
                    )
                    camera.release()
            except Exception:
                _logger.debug(f"Failed to check camera {camera_index}", exc_info=True)
                continue

        return available_cameras

    @staticmethod
    def _get_camera_name(
        camera: cv2.VideoCapture,
        camera_index: int,
        backend: int,
        windows_device_names: list[str] | None = None,
    ) -> str:
        """
        Get the name/description of a camera.

        Args:
            camera: Opened VideoCapture object
            camera_index: Index of the camera
            backend: OpenCV backend being used

        Returns:
            Camera name or a default name based on index
        """
        # On Windows, try using pygrabber if available to get actual device names
        if platform.system() == "Windows" and windows_device_names:
            if 0 <= camera_index < len(windows_device_names):
                device_name = windows_device_names[camera_index]
                if device_name and device_name.strip():
                    return device_name

        # Fallback: Use simple index-based name
        return f"Camera {camera_index}"

    @staticmethod
    def _get_windows_device_names() -> list[str]:
        """Return a list of camera device names on Windows, or an empty list."""
        if CameraEnumerator._pygrabber_disabled:
            return []

        if CameraEnumerator._cached_device_names is not None:
            return CameraEnumerator._cached_device_names

        try:
            from pygrabber.dshow_graph import FilterGraph

            CameraEnumerator._cached_device_names = (
                FilterGraph().get_input_devices() or []
            )
            return CameraEnumerator._cached_device_names
        except ImportError:
            CameraEnumerator._pygrabber_disabled = True
            return []
        except Exception:
            _logger.warning("Failed to get camera names using pygrabber", exc_info=True)
            CameraEnumerator._pygrabber_disabled = True
            return []

    @staticmethod
    def find_camera_by_name(
        camera_name: str, available_cameras: list[CameraInfo] | None = None
    ) -> int | None:
        """
        Find a camera index by its name.

        Args:
            camera_name: Name of the camera to find
            available_cameras: Optional list of available cameras (will enumerate if not provided)

        Returns:
            Camera index if found, None otherwise
        """
        if available_cameras is None:
            available_cameras = CameraEnumerator.get_available_cameras()

        for camera_info in available_cameras:
            if camera_info.name == camera_name:
                return camera_info.index

        return None
