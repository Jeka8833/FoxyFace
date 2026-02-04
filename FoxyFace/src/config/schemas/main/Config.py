from dataclasses import dataclass, field

from dataclass_wizard import JSONWizard

from AppConstants import AppConstants
from src.config.schemas.main.core.AutoRunConfig import AutoRunConfig
from src.config.schemas.main.core.BabbleConfig import BabbleConfig
from src.config.schemas.main.core.CameraConfig import CameraConfig
from src.config.schemas.main.core.MediaPipeConfig import MediaPipeConfig
from src.config.schemas.main.core.ProcessingConfig import ProcessingConfig
from src.config.schemas.main.core.sender.SenderConfig import SenderConfig
from src.config.schemas.main.gui.GuiConfig import GuiConfig


@dataclass(slots=True)
class Config(JSONWizard):
    file_version: str = str(AppConstants.VERSION)

    gui: GuiConfig = field(default_factory=GuiConfig)
    auto_run: AutoRunConfig = field(default_factory=AutoRunConfig)

    camera: CameraConfig = field(default_factory=CameraConfig)
    media_pipe: MediaPipeConfig = field(default_factory=MediaPipeConfig)
    babble: BabbleConfig = field(default_factory=BabbleConfig)
    processing: ProcessingConfig = field(default_factory=ProcessingConfig)
    sender: SenderConfig = field(default_factory=SenderConfig)
