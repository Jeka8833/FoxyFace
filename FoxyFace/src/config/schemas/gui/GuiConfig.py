from dataclasses import dataclass, field

from src.config.schemas.gui.GuiAutoCalibrationWindowConfig import GuiAutoCalibrationWindowConfig


@dataclass(slots=True)
class GuiConfig:
    auto_calibration_window : GuiAutoCalibrationWindowConfig = field(default_factory=GuiAutoCalibrationWindowConfig)