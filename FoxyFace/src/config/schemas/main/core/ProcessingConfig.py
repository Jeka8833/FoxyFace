from dataclasses import dataclass, field

from src.config.schemas.core.enums.GeneralBlendShapeEnumConfig import GeneralBlendShapeEnumConfig
from src.stream.postprocessing.calibration.BlendShapeOption import BlendShapeOption
from src.stream.postprocessing.mixer.MixerRoute import MixerRoute


@dataclass(slots=True)
class ProcessingConfig:
    source: dict[GeneralBlendShapeEnumConfig, MixerRoute] = field(
        default_factory=lambda: {GeneralBlendShapeEnumConfig.HeadX: MixerRoute.DISABLED})
    calibration: dict[GeneralBlendShapeEnumConfig, BlendShapeOption] = field(default_factory=dict)
