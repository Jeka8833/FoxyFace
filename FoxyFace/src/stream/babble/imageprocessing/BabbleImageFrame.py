from dataclasses import dataclass

from cv2.typing import MatLike


@dataclass(frozen=True, slots=True)
class BabbleImageFrame:
    processed_frame: MatLike
    timestamp_ns: int
