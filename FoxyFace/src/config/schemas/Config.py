from dataclasses import dataclass, field

from dataclass_wizard import JSONWizard

from AppConstants import AppConstants
from src.config.schemas.core.BabbleConfig import BabbleConfig
from src.config.schemas.core.CameraConfig import CameraConfig
from src.config.schemas.core.MediaPipeConfig import MediaPipeConfig
from src.config.schemas.core.ProcessingConfig import ProcessingConfig
from src.config.schemas.core.SocketConfig import SocketConfig
from src.config.schemas.gui.GuiConfig import GuiConfig


@dataclass(slots=True)
class Config(JSONWizard):
    file_version: str = str(AppConstants.VERSION)

    gui: GuiConfig = field(default_factory=GuiConfig)

    camera: CameraConfig = field(default_factory=CameraConfig)
    media_pipe: MediaPipeConfig = field(default_factory=MediaPipeConfig)
    babble: BabbleConfig = field(default_factory=BabbleConfig)
    processing: ProcessingConfig = field(default_factory=ProcessingConfig)
    socket: SocketConfig = field(default_factory=SocketConfig)
