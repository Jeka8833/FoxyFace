from enum import Enum, unique

from src.stream.babble.BabbleBlendShapeEnum import BabbleBlendShapeEnum
from src.stream.mediapipe.MediaPipeBlendShapeEnum import MediaPipeBlendShapeEnum


@unique
class MixSelectEnum(Enum):
    Disabled = None
    MediaPipe = MediaPipeBlendShapeEnum
    Babble = BabbleBlendShapeEnum
