from enum import Enum, unique

from src.stream.babble.BabbleBlendShapeEnum import BabbleBlendShapeEnum
from src.stream.mediapipe.face.MediaPipeBlendShapeEnum import MediaPipeBlendShapeEnum
from src.stream.mediapipe.tongue.MediaPipeTongueBlendShapeEnum import MediaPipeTongueBlendShapeEnum


@unique
class MixSelectEnum(Enum):
    Disabled = None
    MediaPipe = MediaPipeBlendShapeEnum
    MediaPipeTongue = MediaPipeTongueBlendShapeEnum
    Babble = BabbleBlendShapeEnum
