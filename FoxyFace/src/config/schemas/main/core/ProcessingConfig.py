from dataclasses import dataclass, field

from config.schemas.main.core.enums.GeneralBlendShapeEnumConfig import GeneralBlendShapeEnumConfig
from config.schemas.main.core.enums.MixSelectEnumConfig import MixSelectEnumConfig
from src.stream.postprocessing.calibration.BlendShapeOption import BlendShapeOption


@dataclass(slots=True)
class ProcessingConfig:
    source: dict[GeneralBlendShapeEnumConfig, MixSelectEnumConfig] = field(
        default_factory=lambda: {GeneralBlendShapeEnumConfig.CheekPuff: MixSelectEnumConfig.Disabled,
                                 GeneralBlendShapeEnumConfig.HeadX: MixSelectEnumConfig.Disabled})
    calibration: dict[GeneralBlendShapeEnumConfig, BlendShapeOption] = field(default_factory=dict)
