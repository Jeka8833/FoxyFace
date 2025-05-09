from dataclasses import dataclass, field


@dataclass(slots=True)
class GuiAutoCalibrationWindowConfig:
    selection_neutral_position: list[str] = field(
        default_factory=lambda: ["CheekPuffLeft", "CheekPuffRight", "CheekSuckLeft", "CheekSuckRight", "TongueOut",
                                 "EyeXLeft", "EyeXRight", "EyeYLeft", "EyeYRight", "HeadX", "HeadY", "HeadZ",
                                 "HeadRotation"])
    selection_max_position: list[str] = field(
        default_factory=lambda: ["CheekPuffLeft", "CheekPuffRight", "CheekSuckLeft", "CheekSuckRight", "TongueOut",
                                 "TongueUp", "TongueDown", "TongueLeft", "TongueRight", "TongueRoll", "TongueBendDown",
                                 "TongueCurlUp", "TongueSquish", "TongueFlat", "TongueTwistLeft", "TongueTwistRight"])
    delay_neutral_position: int = 4
