from enum import StrEnum, unique

from src.stream.postprocessing.mixer.MixSelectEnum import MixSelectEnum


@unique
class MixSelectEnumConfig(StrEnum):
    Disabled = MixSelectEnum.Disabled.name
    MediaPipe = MixSelectEnum.MediaPipe.name
    MediaPipeTongue = MixSelectEnum.MediaPipeTongue.name
    Babble = MixSelectEnum.Babble.name

    def to_original(self) -> MixSelectEnum:
        return MixSelectEnum[self.name]

    @staticmethod
    def from_original(original: MixSelectEnum) -> 'MixSelectEnumConfig':
        return MixSelectEnumConfig(original.name)
