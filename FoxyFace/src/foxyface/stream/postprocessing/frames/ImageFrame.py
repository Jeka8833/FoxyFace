from dataclasses import dataclass

from cv2.typing import MatLike


@dataclass(frozen=True, slots=True)
class ImageFrame:
    image: MatLike
    timestamp_ns: int
