from enum import unique, StrEnum, Enum

from foxyface.stream.babble.BabbleBlendshapeEnum import BabbleBlendshapeEnum
from foxyface.stream.mediapipe.face.MediaPipeBlendshapeEnum import MediaPipeBlendshapeEnum
from foxyface.stream.mediapipe.tongue.MediaPipeTongueBlendshapeEnum import MediaPipeTongueBlendshapeEnum


@unique
class MixerRoute(StrEnum):
    DISABLED = "Disabled"
    AUTO = "Auto"
    MEDIA_PIPE = "MediaPipe"
    MEDIA_PIPE_TONGUE = "MediaPipe Tongue"
    BABBLE = "Babble"

    @property
    def encoder_enum(self) -> type[Enum] | None:
        match self:
            case MixerRoute.DISABLED | MixerRoute.AUTO:
                return None
            case MixerRoute.MEDIA_PIPE:
                return MediaPipeBlendshapeEnum
            case MixerRoute.MEDIA_PIPE_TONGUE:
                return MediaPipeTongueBlendshapeEnum
            case MixerRoute.BABBLE:
                return BabbleBlendshapeEnum
            case _:
                raise ValueError(f"Unsupported MixerRoute: {self}")

    @classmethod
    def _missing_(cls, value: object):
        return cls.AUTO
