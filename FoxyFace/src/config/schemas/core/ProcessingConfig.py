from dataclasses import dataclass, field

from src.config.schemas.core.enums.GeneralBlendShapeEnumConfig import GeneralBlendShapeEnumConfig
from src.config.schemas.core.enums.MixSelectEnumConfig import MixSelectEnumConfig
from src.stream.postprocessing.calibration.BlendShapeOption import BlendShapeOption


@dataclass(slots=True)
class ProcessingConfig:
    source: dict[GeneralBlendShapeEnumConfig, MixSelectEnumConfig] = field(
        default_factory=lambda: {GeneralBlendShapeEnumConfig.CheekPuff: MixSelectEnumConfig.Disabled,
                                 GeneralBlendShapeEnumConfig.HeadX: MixSelectEnumConfig.Disabled})
    calibration: dict[GeneralBlendShapeEnumConfig, BlendShapeOption] = field(default_factory=dict)
