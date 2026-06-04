import multiprocessing
import sys

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
    from src.config.ConfigManager import ConfigManager
    from src.config.schemas.avatar.AvatarConfig import AvatarConfig
    from src.config.schemas.avatar.AvatarConfigMigrationManager import AvatarConfigMigrationManager
    from src.config.schemas.main.Config import Config
    from src.config.schemas.main.ConfigMigrationManager import MainConfigMigrationManager
    from src.pipline.BabblePipeline import BabblePipeline
    from src.pipline.CameraPipeline import CameraPipeline
    from src.pipline.MediaPipeTonguePipeline import MediaPipeTonguePipeline
    from src.pipline.MediaPipePipeline import MediaPipePipeline
    from src.pipline.ProcessingPipeline import ProcessingPipeline
    from src.pipline.senders.SenderRouterPipeline import SenderRouterPipeline
    from src.stream.senders.vrchat.VRchatAvatarConfigManager import VRChatAvatarConfigManager
    from src.pipline.calibration.AutoCalibrationEndpoint import AutoCalibrationEndpoint
    from src.ui.windows.MainWindow import MainWindow
    import sys

    logger = logging.getLogger(__name__)

    class RunMainStream:
        def __init__(self, splash_screen=None):
            logger.info(f"Hello, I'm FoxyFace {str(AppConstants.VERSION)}")

            self.__config_manager: ConfigManager[Config] = ConfigManager[Config](
                path=Path("configs/config.json"), config_cls=Config, migration_manager=MainConfigMigrationManager())
            self.__config_manager.load(wait=True)

            self.__ifacialmocap_config: ConfigManager[AvatarConfig] = ConfigManager[AvatarConfig](
                path=Path("configs/ifacialmocap.json"), config_cls=AvatarConfig,
                migration_manager=AvatarConfigMigrationManager())
            self.__ifacialmocap_config.load(wait=True)

            self.__foxyface_config: ConfigManager[AvatarConfig] = ConfigManager[AvatarConfig](
                path=Path("configs/foxyface.json"), config_cls=AvatarConfig,
                migration_manager=AvatarConfigMigrationManager())
            self.__foxyface_config.load(wait=True)

            self.__meowface_config: ConfigManager[AvatarConfig] = ConfigManager[AvatarConfig](
                path=Path("configs/meowface.json"), config_cls=AvatarConfig,
                migration_manager=AvatarConfigMigrationManager())
            self.__meowface_config.load(wait=True)

            self.__vrchat_config: VRChatAvatarConfigManager = VRChatAvatarConfigManager(Path("configs/vrchat"))

            self.__camera_pipeline: CameraPipeline = CameraPipeline(self.__config_manager)
            self.__media_pipe_pipeline: MediaPipePipeline = MediaPipePipeline(self.__config_manager, self.__camera_pipeline)
            self.__media_pipe_tongue_pipeline = MediaPipeTonguePipeline(self.__config_manager, self.__media_pipe_pipeline)
            self.__babble_pipeline: BabblePipeline = BabblePipeline(self.__config_manager, self.__media_pipe_pipeline)
            self.__processing_pipeline: ProcessingPipeline = ProcessingPipeline(self.__config_manager,
                                                                                self.__media_pipe_pipeline,
                                                                                self.__media_pipe_tongue_pipeline,
                                                                                self.__babble_pipeline)
            self.__sender_router_pipeline: SenderRouterPipeline = SenderRouterPipeline(self.__config_manager,
                                                                                       self.__processing_pipeline,
                                                                                       self.__vrchat_config,
                                                                                       self.__ifacialmocap_config,
                                                                                       self.__foxyface_config,
                                                                                       self.__meowface_config)
            self.__auto_calibration_endpoint: AutoCalibrationEndpoint = AutoCalibrationEndpoint(self.__config_manager,
                                                                                                self.__media_pipe_pipeline,
                                                                                                self.__processing_pipeline)
            
            self.__steam_auto_run = SteamAutoRun(self.__config_manager)

            self.__main_window: MainWindow = MainWindow(config_manager=self.__config_manager,
                                                        camera_pipeline=self.__camera_pipeline,
                                                        mediapipe_pipeline=self.__media_pipe_pipeline,
                                                        mediapipe_tongue_pipeline=self.__media_pipe_tongue_pipeline,
                                                        babble_pipeline=self.__babble_pipeline,
                                                        processing_pipeline=self.__processing_pipeline,
                                                        auto_calibration_endpoint=self.__auto_calibration_endpoint,
                                                        steam_auto_run=self.__steam_auto_run,
                                                        sender_manager=self.__sender_router_pipeline)

            if splash_screen is not None:
                splash_screen.finish(self.__main_window)

            self.__update_checker: UpdateChecker = UpdateChecker(self.__config_manager, self.__main_window)
            self.__steam_auto_run.run()
            self.__update_checker.startup_check()

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.__config_manager.close()
            self.__ifacialmocap_config.close()
            self.__foxyface_config.close()
            self.__meowface_config.close()
            self.__vrchat_config.close()

            self.__babble_pipeline.close()
            self.__media_pipe_pipeline.close()
            self.__media_pipe_tongue_pipeline.close()
            self.__camera_pipeline.close()
            self.__processing_pipeline.close()
            self.__sender_router_pipeline.close()
            self.__auto_calibration_endpoint.close()

            self.__update_checker.close()
            self.__steam_auto_run.close()

    with RunMainStream(splash):
        sys.exit(app.exec())

if __name__ == '__main__':
    multiprocessing.freeze_support()

    app_instance, splash_instance = show_splash()

    initialize_and_run(app_instance, splash_instance)
