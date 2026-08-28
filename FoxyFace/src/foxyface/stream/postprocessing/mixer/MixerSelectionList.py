from dataclasses import dataclass

from foxyface.stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum
from foxyface.stream.postprocessing.mixer.MixerRoute import MixerRoute


@dataclass(slots=True, frozen=True)
class MixerSelectionList:
    selected: MixerRoute
    current_route: MixerRoute  # Can't be AUTO
    collision: GeneralBlendShapeEnum | None
    all_routes: list[MixerRoute]
    blocked_routes: set[MixerRoute]
