import sys

if __name__ != '__main__':
    sys.exit(0)  # You're doing something wrong, think about it

# I'll answer why it's in the first few lines: To show the user that the application is running while the neural networks are loading. +- 5-8 seconds
from src.LoggerManager import LoggerManager

import logging

LoggerManager.init(logging.DEBUG if '--debug' in sys.argv else logging.INFO)

from PySide6.QtWidgets import QApplication, QSplashScreen

from src.ui import UiImageUtil

__app = QApplication(sys.argv)

__icon = UiImageUtil.get_window_icon()
if __icon is not None:
    __splash = QSplashScreen(__icon)
    __splash.show()
else:
    __splash = None

# Do time-consuming things

from pathlib import Path
from src.ui.windows.MainWindow import MainWindow
from src.pipline.calibration.AutoCalibrationEndpoint import AutoCalibrationEndpoint
from src.pipline.BabblePipeline import BabblePipeline
from src.pipline.CameraPipeline import CameraPipeline
from src.pipline.MediaPipePipeline import MediaPipePipeline
from src.pipline.UdpPipeline import UdpPipeline
from src.pipline.ProcessingPipeline import ProcessingPipeline
from src.config.ConfigManager import ConfigManager

_logger = logging.getLogger(__name__)


class RunMainStream:
    def __init__(self, splash_screen: QSplashScreen = None):
        self.__config_manager: ConfigManager = ConfigManager(Path("config.json"))
        self.__config_manager.load(wait=True)

        self.__camera_pipeline: CameraPipeline = CameraPipeline(self.__config_manager)
        self.__media_pipe_pipeline: MediaPipePipeline = MediaPipePipeline(self.__config_manager, self.__camera_pipeline)
        self.__babble_pipeline: BabblePipeline = BabblePipeline(self.__config_manager, self.__media_pipe_pipeline)
        self.__processing_pipeline: ProcessingPipeline = ProcessingPipeline(self.__config_manager,
                                                                            self.__media_pipe_pipeline,
                                                                            self.__babble_pipeline)
        self.__udp_pipeline: UdpPipeline = UdpPipeline(self.__config_manager, self.__processing_pipeline)
        self.__auto_calibration_endpoint: AutoCalibrationEndpoint = AutoCalibrationEndpoint(self.__config_manager,
                                                                                            self.__media_pipe_pipeline,
                                                                                            self.__processing_pipeline)

        self.__main_window: MainWindow = MainWindow(self.__config_manager, self.__camera_pipeline,
                                                    self.__media_pipe_pipeline, self.__babble_pipeline,
                                                    self.__processing_pipeline, self.__udp_pipeline,
                                                    self.__auto_calibration_endpoint)

        if splash_screen is not None:
            splash_screen.finish(self.__main_window)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__config_manager.close()

        self.__babble_pipeline.close()
        self.__media_pipe_pipeline.close()
        self.__camera_pipeline.close()
        self.__processing_pipeline.close()
        self.__udp_pipeline.close()
        self.__auto_calibration_endpoint.close()


UiImageUtil.allow_change_windows_icon()
__app.setStyle('Fusion')

with RunMainStream(__splash):
    sys.exit(__app.exec())
