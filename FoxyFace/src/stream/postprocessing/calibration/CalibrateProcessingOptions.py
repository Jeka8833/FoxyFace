from dataclasses import dataclass, field

from src.stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum
from src.stream.postprocessing.calibration.BlendShapeOption import BlendShapeOption


@dataclass(slots=True)
class CalibrateProcessingOptions:
    blend_shape_options: dict[GeneralBlendShapeEnum, BlendShapeOption] = field(default_factory=dict)
