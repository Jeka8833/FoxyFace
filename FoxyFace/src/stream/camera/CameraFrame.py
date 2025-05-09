from dataclasses import dataclass

from cv2.typing import MatLike


@dataclass(frozen=True, slots=True)
class CameraFrame:
    frame: MatLike
    timestamp_ns: int
