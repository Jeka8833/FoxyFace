from dataclasses import dataclass, field

from src.config.schemas.main.gui.GuiAutoCalibrationWindowConfig import GuiAutoCalibrationWindowConfig


@dataclass(slots=True)
class GuiConfig:
    auto_updater_version_skip: str = ""

    auto_calibration_window: GuiAutoCalibrationWindowConfig = field(default_factory=GuiAutoCalibrationWindowConfig)
