from dataclasses import dataclass, field

from dataclass_wizard import JSONWizard

from foxyface.AppConstants import AppConstants
from foxyface.config.schemas.core.AutoRunConfig import AutoRunConfig
from foxyface.config.schemas.core.BabbleConfig import BabbleConfig
from foxyface.config.schemas.core.CameraConfig import CameraConfig
from foxyface.config.schemas.core.MediaPipeConfig import MediaPipeConfig
from foxyface.config.schemas.core.MediaPipeTongueConfig import MediaPipeTongueConfig
from foxyface.config.schemas.core.ProcessingConfig import ProcessingConfig
from foxyface.config.schemas.core.SocketConfig import SocketConfig
from foxyface.config.schemas.gui.GuiConfig import GuiConfig


@dataclass(slots=True)
class Config(JSONWizard):
    file_version: str = str(AppConstants.VERSION)

    gui: GuiConfig = field(default_factory=GuiConfig)
    auto_run: AutoRunConfig = field(default_factory=AutoRunConfig)

    camera: CameraConfig = field(default_factory=CameraConfig)
    media_pipe: MediaPipeConfig = field(default_factory=MediaPipeConfig)
    media_pipe_tongue: MediaPipeTongueConfig = field(default_factory=MediaPipeTongueConfig)
    babble: BabbleConfig = field(default_factory=BabbleConfig)
    processing: ProcessingConfig = field(default_factory=ProcessingConfig)
    socket: SocketConfig = field(default_factory=SocketConfig)
