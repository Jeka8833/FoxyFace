from enum import unique, StrEnum, Enum

from src.stream.babble.BabbleBlendShapeEnum import BabbleBlendShapeEnum
from src.stream.mediapipe.face.MediaPipeBlendShapeEnum import MediaPipeBlendShapeEnum
from src.stream.mediapipe.tongue.MediaPipeTongueBlendShapeEnum import MediaPipeTongueBlendShapeEnum


@unique
class MixerRoute(StrEnum):
    DISABLED = "Disabled"
    AUTO = "Auto"
    MEDIA_PIPE = "MediaPipe"
    MEDIA_PIPE_TONGUE = "MediaPipe Tongue"
    BABBLE = "Babble"
    MEOW_FACE = "MeowFace"

    @property
    def encoder_enum(self) -> type[Enum] | None:
        match self:
            case MixerRoute.DISABLED | MixerRoute.AUTO:
                return None
            case MixerRoute.MEDIA_PIPE:
                return MediaPipeBlendShapeEnum
            case MixerRoute.MEDIA_PIPE_TONGUE:
                return MediaPipeTongueBlendShapeEnum
            case MixerRoute.BABBLE:
                return BabbleBlendShapeEnum
            case MixerRoute.MEOW_FACE:
                return None
            case _:
                raise ValueError(f"Unsupported MixerRoute: {self}")

    @classmethod
    def _missing_(cls, value: object):
        return cls.AUTO
