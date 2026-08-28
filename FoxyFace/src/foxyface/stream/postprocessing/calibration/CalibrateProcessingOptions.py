from dataclasses import dataclass, field

from foxyface.stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum
from foxyface.stream.postprocessing.calibration.BlendShapeOption import BlendShapeOption


@dataclass(slots=True)
class CalibrateProcessingOptions:
    blend_shape_options: dict[GeneralBlendShapeEnum, BlendShapeOption] = field(default_factory=dict)
