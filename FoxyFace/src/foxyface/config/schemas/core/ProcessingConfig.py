from dataclasses import dataclass, field

from foxyface.config.schemas.core.enums.GeneralBlendShapeEnumConfig import GeneralBlendShapeEnumConfig
from foxyface.stream.postprocessing.calibration.BlendShapeOption import BlendShapeOption
from foxyface.stream.postprocessing.mixer.MixerRoute import MixerRoute


@dataclass(slots=True)
class ProcessingConfig:
    source: dict[GeneralBlendShapeEnumConfig, MixerRoute] = field(
        default_factory=lambda: {GeneralBlendShapeEnumConfig.HeadX: MixerRoute.DISABLED})
    calibration: dict[GeneralBlendShapeEnumConfig, BlendShapeOption] = field(default_factory=dict)
