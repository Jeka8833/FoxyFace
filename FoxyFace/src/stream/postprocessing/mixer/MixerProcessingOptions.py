from dataclasses import dataclass, field

from src.stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum
from src.stream.postprocessing.mixer import MixBlockList
from src.stream.postprocessing.mixer.MixSelectEnum import MixSelectEnum


@dataclass(slots=True)
class MixerProcessingOptions:
    enable: dict[GeneralBlendShapeEnum, MixSelectEnum] = field(default_factory=dict)

    def get_enabled(self) -> dict[GeneralBlendShapeEnum, MixSelectEnum]:
        new_list = self.enable.copy()

        for key, value in MixBlockList.block_list.items():
            if self.enable.get(key) != MixSelectEnum.Disabled:
                new_list[value] = MixSelectEnum.Disabled

        return new_list
