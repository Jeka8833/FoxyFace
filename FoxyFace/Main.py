import multiprocessing


def show_splash():
    import logging
    import sys
    from src.LoggerManager import LoggerManager
    from PySide6.QtWidgets import QApplication, QSplashScreen
    from src.ui import UiImageUtil

    LoggerManager.init(logging.DEBUG if '--debug' in sys.argv else logging.INFO)

    app = QApplication(sys.argv)
    UiImageUtil.allow_change_windows_icon()
    app.setStyle('Fusion')

    icon = UiImageUtil.get_window_icon()
    if icon is not None:
        splash = QSplashScreen(icon)
        splash.show()

        app.processEvents()
    else:
        splash = None

    return app, splash


def initialize_and_run(app, splash):
    from pathlib import Path
    import logging
    from AppConstants import AppConstants
    from src.UpdateChecker import UpdateChecker
    from src.autorun.SteamAutoRun import SteamAutoRun
    from src.ui.windows.MainWindow import MainWindow
    from src.pipline.calibration.AutoCalibrationEndpoint import AutoCalibrationEndpoint
    from src.pipline.BabblePipeline import BabblePipeline
    from src.pipline.CameraPipeline import CameraPipeline
    from src.pipline.MediaPipeTonguePipeline import MediaPipeTonguePipeline
    from src.pipline.MediaPipePipeline import MediaPipePipeline
    from src.pipline.UdpPipeline import UdpPipeline
    from src.pipline.ProcessingPipeline import ProcessingPipeline
    from src.config.ConfigManager import ConfigManager
    import sys

    logger = logging.getLogger(__name__)

    class RunMainStream:
        def __init__(self, splash_screen=None):
            logger.info(f"Hello, I'm FoxyFace {str(AppConstants.VERSION)}")

            self.__config_manager = ConfigManager(Path("config.json"))
            self.__config_manager.load(wait=True)

            self.__camera_pipeline = CameraPipeline(self.__config_manager)
            self.__media_pipe_pipeline = MediaPipePipeline(self.__config_manager, self.__camera_pipeline)
            self.__media_pipe_tongue_pipeline = MediaPipeTonguePipeline(
                self.__config_manager,
                self.__media_pipe_pipeline
            )
            self.__babble_pipeline = BabblePipeline(self.__config_manager, self.__media_pipe_pipeline)
            self.__processing_pipeline = ProcessingPipeline(
                self.__config_manager,
                self.__media_pipe_pipeline,
                self.__media_pipe_tongue_pipeline,
                self.__babble_pipeline
            )
            self.__udp_pipeline = UdpPipeline(self.__config_manager, self.__processing_pipeline)
            self.__auto_calibration_endpoint = AutoCalibrationEndpoint(
                self.__config_manager,
                self.__media_pipe_pipeline,
                self.__processing_pipeline
            )

            self.__steam_auto_run = SteamAutoRun(self.__config_manager)

            self.__main_window = MainWindow(
                self.__config_manager,
                self.__camera_pipeline,
                self.__media_pipe_pipeline,
                self.__media_pipe_tongue_pipeline,
                self.__babble_pipeline,
                self.__processing_pipeline,
                self.__udp_pipeline,
                self.__auto_calibration_endpoint,
                self.__steam_auto_run
            )

            if splash_screen is not None:
                splash_screen.finish(self.__main_window)

            self.__update_checker = UpdateChecker(self.__config_manager, self.__main_window)
            self.__steam_auto_run.run()
            self.__update_checker.startup_check()

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.__config_manager.close()
            self.__babble_pipeline.close()
            self.__media_pipe_pipeline.close()
            self.__media_pipe_tongue_pipeline.close()
            self.__camera_pipeline.close()
            self.__processing_pipeline.close()
            self.__udp_pipeline.close()
            self.__auto_calibration_endpoint.close()
            self.__update_checker.close()
            self.__steam_auto_run.close()

    with RunMainStream(splash):
        sys.exit(app.exec())


if __name__ == '__main__':
    multiprocessing.freeze_support()

    app_instance, splash_instance = show_splash() # Must be without any heavy imports, danke

    initialize_and_run(app_instance, splash_instance)
