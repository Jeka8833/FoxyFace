from dataclasses import dataclass, field

from foxyface.stream.babble.BabbleBlendshapeEnum import BabbleBlendshapeEnum
from foxyface.stream.mediapipe.face.MediaPipeBlendshapeEnum import MediaPipeBlendshapeEnum
from foxyface.stream.mediapipe.tongue.MediaPipeTongueBlendshapeEnum import MediaPipeTongueBlendshapeEnum


@dataclass(frozen=True, slots=True)
class GeneralBlendShapeOption:
    same_as: list[MediaPipeBlendshapeEnum | BabbleBlendshapeEnum | MediaPipeTongueBlendshapeEnum] = field(
        default_factory=list[MediaPipeBlendshapeEnum | BabbleBlendshapeEnum | MediaPipeTongueBlendshapeEnum])
    min_value: float = 0.0
    max_value: float = 1.0
    has_center: bool = False
    disable_calibration: bool = False
