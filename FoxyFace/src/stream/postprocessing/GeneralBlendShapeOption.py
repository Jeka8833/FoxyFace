from dataclasses import dataclass, field

from src.stream.babble.BabbleBlendShapeEnum import BabbleBlendShapeEnum
from src.stream.mediapipe.MediaPipeBlendShapeEnum import MediaPipeBlendShapeEnum


@dataclass(frozen=True, slots=True)
class GeneralBlendShapeOption:
    same_as: list[MediaPipeBlendShapeEnum | BabbleBlendShapeEnum] = field(
        default_factory=list[MediaPipeBlendShapeEnum | BabbleBlendShapeEnum])
    min_value: float = 0.0
    max_value: float = 1.0
    has_center: bool = False
    disable_calibration: bool = False
