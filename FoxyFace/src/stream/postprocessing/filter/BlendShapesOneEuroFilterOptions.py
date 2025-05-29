from dataclasses import dataclass


@dataclass(slots=True)
class BlendShapesOneEuroFilterOptions:
    mincutoff: float = 3.0
    beta: float = 0.9
    dcutoff: float = 1.0
