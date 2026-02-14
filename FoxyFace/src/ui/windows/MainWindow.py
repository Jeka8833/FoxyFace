import logging
import threading

from PySide6.QtCore import QTimer, Qt, Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from packaging.version import Version

from AppConstants import AppConstants
from src.autorun.SteamAutoRun import SteamAutoRun
from src.config.ConfigManager import ConfigManager
from src.config.schemas.avatar.AvatarConfig import AvatarConfig
from src.pipline.BabblePipeline import BabblePipeline
from src.pipline.CameraPipeline import CameraPipeline
from src.pipline.MediaPipePipeline import MediaPipePipeline
from src.pipline.ProcessingPipeline import ProcessingPipeline
from src.pipline.calibration.AutoCalibrationEndpoint import AutoCalibrationEndpoint
from src.pipline.senders.SenderRouterPipeline import SenderRouterPipeline
from src.stream.senders.vrchat.VRchatAvatarConfigManager import VRChatAvatarConfigManager
from src.ui import UiImageUtil
from src.ui.FoxyWindow import FoxyWindow
from src.ui.qtcreator.ui_MainWindow import Ui_MainWindow
from src.ui.windows.AutoCalibrationWindow import AutoCalibrationWindow
from src.ui.windows.AutoRunSettingsWindow import AutoRunSettingsWindow
from src.ui.windows.AvatarCalibrationWindow import AvatarCalibrationWindow
from src.ui.windows.BabbleSettingsWindow import BabbleSettingsWindow
from src.ui.windows.CalibrationWindow import CalibrationWindow
from src.ui.windows.CameraSettingsWindow import CameraSettingsWindow
from src.ui.windows.HasUpdateWindow import HasUpdateWindow
from src.ui.windows.MediaPipeSettingsWindow import MediaPipeSettingsWindow
from src.ui.windows.SenderSettingsWindow import SenderSettingsWindow

_logger = logging.getLogger(__name__)


class MainWindow(FoxyWindow):
    camera_fps_signal = Signal(str)
    mediapipe_fps_signal = Signal(str)
    mediapipe_latency_signal = Signal(str)
    babble_fps_signal = Signal(str)
    babble_latency_signal = Signal(str)
    has_update_signal = Signal(object)

    def __init__(self, config_manager: ConfigManager, camera_pipeline: CameraPipeline,
                 mediapipe_pipeline: MediaPipePipeline, babble_pipeline: BabblePipeline,
                 processing_pipeline: ProcessingPipeline, auto_calibration_endpoint: AutoCalibrationEndpoint,
                 steam_auto_run: SteamAutoRun, sender_manager: SenderRouterPipeline,
                 vrchat_config_manager: VRChatAvatarConfigManager,
                 ifacialmocap_config_manager: ConfigManager[AvatarConfig],
                 foxyface_config_manager: ConfigManager[AvatarConfig],
                 meowface_config_manager: ConfigManager[AvatarConfig]):
        super().__init__()

        self.is_closed: threading.Event = threading.Event()

        self.__config_manager = config_manager
        self.__camera_pipeline = camera_pipeline
        self.__media_pipe_pipeline = mediapipe_pipeline
        self.__babble_pipeline = babble_pipeline
        self.__processing_pipeline = processing_pipeline
        self.__auto_calibration_endpoint = auto_calibration_endpoint
        self.__steam_auto_run = steam_auto_run
        self.__sender_manager = sender_manager
        self.__vrchat_config_manager = vrchat_config_manager
        self.__ifacialmocap_config_manager = ifacialmocap_config_manager
        self.__foxyface_config_manager = foxyface_config_manager
        self.__meowface_config_manager = meowface_config_manager

        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)

        self.__register_events()
        self.__register_signals()

        self.__timer: QTimer = QTimer(self, interval=1000, timerType=Qt.TimerType.VeryCoarseTimer)
        self.__timer.timeout.connect(self.__update_thread)
        self.__timer.start()

        self.setWindowTitle("FoxyFace v" + str(AppConstants.VERSION) + " #StandWithUkraine")

        self.__camera_settings_window: CameraSettingsWindow | None = None
        self.__media_pipe_settings_window: MediaPipeSettingsWindow | None = None
        self.__babble_settings_window: BabbleSettingsWindow | None = None
        self.__sender_settings_window: SenderSettingsWindow | None = None
        self.__auto_calibration_window: AutoCalibrationWindow | None = None
        self.__calibration_window: CalibrationWindow | None = None
        self.__sender_avatar_calibration_window: AvatarCalibrationWindow | None = None
        self.__auto_run_window: AutoRunSettingsWindow | None = None
        self.__has_update_window: HasUpdateWindow | None = None

        self.show()

    def closeEvent(self, event):
        super().closeEvent(event)

        self.__unregister_signals()

        self.__timer.stop()

        QApplication.closeAllWindows()

    def __update_thread(self):
        try:
            self.camera_fps_signal.emit(f"FPS: {self.__camera_pipeline.get_fps():.1f}")
            self.mediapipe_fps_signal.emit(f"FPS: {self.__media_pipe_pipeline.get_fps():.1f}")
            self.babble_fps_signal.emit(f"FPS: {self.__babble_pipeline.get_fps():.1f}")

            self.mediapipe_latency_signal.emit(f"Latency: {self.__media_pipe_pipeline.get_latency() * 1000.0:.0f} ms")
            self.babble_latency_signal.emit(f"Latency: {self.__babble_pipeline.get_latency() * 1000.0:.0f} ms")

            model = self.__babble_pipeline.get_model_loader().model
            if model is None or model.is_default_model:
                warning_icon = UiImageUtil.get_warning_icon()
                if warning_icon is not None:
                    self.__ui.open_babble_setting_btn.setIcon(warning_icon)
            else:
                self.__ui.open_babble_setting_btn.setIcon(QIcon())
        except Exception:
            _logger.warning("Failed to update thread", exc_info=True, stack_info=True)

    def __register_signals(self):
        self.camera_fps_signal.connect(self.__ui.camera_fps_lbl.setText)
        self.mediapipe_fps_signal.connect(self.__ui.mediapipe_fps_lbl.setText)
        self.mediapipe_latency_signal.connect(self.__ui.mediapipe_latency_lbl.setText)
        self.babble_fps_signal.connect(self.__ui.babble_fps_lbl.setText)
        self.babble_latency_signal.connect(self.__ui.babble_latency_lbl.setText)
        self.has_update_signal.connect(self.__has_update)

    def __unregister_signals(self):
        self.camera_fps_signal.disconnect(self.__ui.camera_fps_lbl.setText)
        self.mediapipe_fps_signal.disconnect(self.__ui.mediapipe_fps_lbl.setText)
        self.mediapipe_latency_signal.disconnect(self.__ui.mediapipe_latency_lbl.setText)
        self.babble_fps_signal.disconnect(self.__ui.babble_fps_lbl.setText)
        self.babble_latency_signal.disconnect(self.__ui.babble_latency_lbl.setText)
        self.has_update_signal.disconnect(self.__has_update)

    def __register_events(self):
        self.__ui.open_camera_preview_btn.clicked.connect(self.__open_camera_preview)
        self.__ui.open_camera_settings_btn.clicked.connect(self.__open_camera_setting)

        self.__ui.open_mediapipe_preview_btn.clicked.connect(self.__open_mediapipe_preview)
        self.__ui.open_mediapipe_settings_btn.clicked.connect(self.__open_mediapipe_setting)

        self.__ui.open_babble_preview_btn.clicked.connect(self.__open_babble_preview)
        self.__ui.open_babble_setting_btn.clicked.connect(self.__open_babble_setting_btn)

        self.__ui.open_processing_calibration_btn.clicked.connect(self.__open_processing_calibration)
        self.__ui.open_processing_settings_btn.clicked.connect(self.__open_processing_settings)

        self.__ui.open_avatar_calibration_btn.clicked.connect(self.__open_avatar_calibration)
        self.__ui.open_sender_settings_btn.clicked.connect(self.__open_sender_settings)

        self.__ui.actionSetup_AutoRun.triggered.connect(self.__open_auto_run_window)

    def __open_camera_preview(self):
        try:
            self.__camera_pipeline.trigger_view_preview()
        except Exception:
            _logger.warning("Failed to open camera preview", exc_info=True, stack_info=True)

    def __open_camera_setting(self):
        try:
            if self.__camera_settings_window is None or self.__camera_settings_window.is_closed.is_set():
                self.__camera_settings_window = CameraSettingsWindow(self.__config_manager)
            else:
                self.__camera_settings_window.close_event.emit()
        except Exception:
            _logger.warning("Failed to open camera settings", exc_info=True, stack_info=True)

    def __open_mediapipe_preview(self):
        try:
            self.__media_pipe_pipeline.trigger_view_preview()
        except Exception:
            _logger.warning("Failed to open mediapipe preview", exc_info=True, stack_info=True)

    def __open_mediapipe_setting(self):
        try:
            if self.__media_pipe_settings_window is None or self.__media_pipe_settings_window.is_closed.is_set():
                self.__media_pipe_settings_window = MediaPipeSettingsWindow(self.__config_manager)
            else:
                self.__media_pipe_settings_window.close_event.emit()
        except Exception:
            _logger.warning("Failed to open mediapipe settings", exc_info=True, stack_info=True)

    def __open_babble_preview(self):
        try:
            self.__babble_pipeline.trigger_view_preview()
        except Exception:
            _logger.warning("Failed to open babble preview", exc_info=True, stack_info=True)

    def __open_babble_setting_btn(self):
        try:
            if self.__babble_settings_window is None or self.__babble_settings_window.is_closed.is_set():
                self.__babble_settings_window = BabbleSettingsWindow(self.__config_manager,
                                                                     self.__babble_pipeline.get_model_loader())
            else:
                self.__babble_settings_window.close_event.emit()
        except Exception:
            _logger.warning("Failed to open babble settings", exc_info=True, stack_info=True)

    def __open_processing_calibration(self):
        try:
            if self.__auto_calibration_window is None or self.__auto_calibration_window.is_closed.is_set():
                self.__auto_calibration_window = AutoCalibrationWindow(self.__config_manager,
                                                                       self.__auto_calibration_endpoint)
            else:
                self.__auto_calibration_window.close_event.emit()
        except Exception:
            _logger.warning("Failed to open processing calibration", exc_info=True, stack_info=True)

    def __open_processing_settings(self):
        try:
            if self.__calibration_window is None or self.__calibration_window.is_closed.is_set():
                self.__calibration_window = CalibrationWindow(self.__config_manager, self.__processing_pipeline)
            else:
                self.__calibration_window.close_event.emit()
        except Exception:
            _logger.warning("Failed to open processing settings", exc_info=True, stack_info=True)

    def __open_auto_run_window(self):
        try:
            if self.__auto_run_window is None or self.__auto_run_window.is_closed.is_set():
                self.__auto_run_window = AutoRunSettingsWindow(self.__config_manager, self.__steam_auto_run)
            else:
                self.__auto_run_window.close_event.emit()
        except Exception:
            _logger.warning("Failed to open auto run settings", exc_info=True, stack_info=True)

    def __open_sender_settings(self):
        try:
            if self.__sender_settings_window is None or self.__sender_settings_window.is_closed.is_set():
                self.__sender_settings_window = SenderSettingsWindow(self.__config_manager)
            else:
                self.__sender_settings_window.close_event.emit()
        except Exception:
            _logger.warning("Failed to open sender settings", exc_info=True, stack_info=True)

    def __open_avatar_calibration(self):
        try:
            if (self.__sender_avatar_calibration_window is None or
                    self.__sender_avatar_calibration_window.is_closed.is_set()):
                self.__sender_avatar_calibration_window = AvatarCalibrationWindow(
                    config_manager=self.__config_manager,
                    open_connection_setting=self.__open_sender_settings,
                    sender_manager=self.__sender_manager,
                    vrchat_config_manager=self.__vrchat_config_manager,
                    ifacialmocap_config_manager=self.__ifacialmocap_config_manager,
                    meowface_config_manager=self.__meowface_config_manager,
                    foxyface_config_manager=self.__foxyface_config_manager,
                )
            else:
                self.__sender_avatar_calibration_window.close_event.emit()
        except Exception:
            _logger.warning("Failed to open sender avatar calibration", exc_info=True, stack_info=True)

    def __has_update(self, founded_version: Version):
        try:
            if self.__has_update_window is None or self.__has_update_window.is_closed.is_set():
                self.__has_update_window = HasUpdateWindow(self.__config_manager, founded_version)
        except Exception:
            _logger.warning("Failed to open has update window", exc_info=True, stack_info=True)
