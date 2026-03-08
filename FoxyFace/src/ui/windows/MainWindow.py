import logging
import threading

from PySide6.QtCore import QTimer, Qt, Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from packaging.version import Version

from AppConstants import AppConstants
from src.autorun.SteamAutoRun import SteamAutoRun
from src.config.ConfigManager import ConfigManager
from src.pipline.BabblePipeline import BabblePipeline
from src.pipline.CameraPipeline import CameraPipeline
from src.pipline.MediaPipePipeline import MediaPipePipeline
from src.pipline.ProcessingPipeline import ProcessingPipeline
from src.pipline.UdpPipeline import UdpPipeline
from src.stream.camera.CameraProcessingOption import CameraProcessingOption
from src.stream.camera.CameraStream import CameraStream
from src.stream.camera.CameraEnumerator import CameraEnumerator
from src.stream.core.StreamWriteOnly import StreamWriteOnly
from src.stream.core.components.WriteCpsCounter import WriteCpsCounter
from src.pipline.calibration.AutoCalibrationEndpoint import AutoCalibrationEndpoint
from src.ui import UiImageUtil
from src.ui.FoxyWindow import FoxyWindow
from src.ui.qtcreator.ui_mainwindow import Ui_MainWindow
from src.ui.windows.AutoCalibrationWindow import AutoCalibrationWindow
from src.ui.windows.BabbleSettingsWindow import BabbleSettingsWindow
from src.ui.windows.CalibrationWindow import CalibrationWindow
from src.ui.windows.CameraSettingsWindow import CameraSettingsWindow
from src.ui.windows.HasUpdateWindow import HasUpdateWindow
from src.ui.windows.MediaPipeSettingsWindow import MediaPipeSettingsWindow
from src.ui.windows.VrcftSettingsWindow import VrcftSettingsWindow

_logger = logging.getLogger(__name__)


class MainWindow(FoxyWindow):
    camera_fps_signal = Signal(str)
    mediapipe_fps_signal = Signal(str)
    mediapipe_latency_signal = Signal(str)
    babble_fps_signal = Signal(str)
    babble_latency_signal = Signal(str)
    udp_pps_signal = Signal(str)
    udp_status_signal = Signal(str)
    has_update_signal = Signal(object)
    camera_list_ready_signal = Signal()

    def __init__(
        self,
        config_manager: ConfigManager,
        camera_pipeline: CameraPipeline,
        mediapipe_pipeline: MediaPipePipeline,
        babble_pipeline: BabblePipeline,
        processing_pipeline: ProcessingPipeline,
        udp_pipeline: UdpPipeline,
        auto_calibration_endpoint: AutoCalibrationEndpoint,
        steam_auto_run: SteamAutoRun,
    ):
        super().__init__()

        self.is_closed: threading.Event = threading.Event()

        self.__config_manager = config_manager
        self.__camera_pipeline = camera_pipeline
        self.__media_pipe_pipeline = mediapipe_pipeline
        self.__babble_pipeline = babble_pipeline
        self.__processing_pipeline = processing_pipeline
        self.__udp_pipeline = udp_pipeline
        self.__auto_calibration_endpoint = auto_calibration_endpoint
        self.__steam_auto_run = steam_auto_run

        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)

        self.__ui.open_camera_settings_btn.setEnabled(False)

        self.__register_events()
        self.__register_signals()

        self.__timer: QTimer = QTimer(
            self, interval=1000, timerType=Qt.TimerType.VeryCoarseTimer
        )
        self.__timer.timeout.connect(self.__update_thread)
        self.__timer.start()

        self.setWindowTitle(
            "FoxyFace v" + str(AppConstants.VERSION) + " #StandWithUkraine"
        )

        self.__camera_settings_window: CameraSettingsWindow | None = None
        self.__media_pipe_settings_window: MediaPipeSettingsWindow | None = None
        self.__babble_settings_window: BabbleSettingsWindow | None = None
        self.__vrcft_settings_window: VrcftSettingsWindow | None = None
        self.__auto_calibration_window: AutoCalibrationWindow | None = None
        self.__calibration_window: CalibrationWindow | None = None
        self.__has_update_window: HasUpdateWindow | None = None

        threading.Thread(target=self.__warmup_camera_list, daemon=True).start()

        self.show()

    def __warmup_camera_list(self):
        try:
            CameraEnumerator.get_available_cameras()
        except Exception:
            pass
        finally:
            self.camera_list_ready_signal.emit()

    def __on_camera_list_ready(self):
        self.__ui.open_camera_settings_btn.setEnabled(True)

    def closeEvent(self, event):
        self.is_closed.set()

        self.__unregister_signals()

        self.__timer.stop()

        QApplication.closeAllWindows()

        event.accept()

    def __update_thread(self):
        try:
            self.camera_fps_signal.emit(f"FPS: {self.__camera_pipeline.get_fps():.1f}")
            self.mediapipe_fps_signal.emit(
                f"FPS: {self.__media_pipe_pipeline.get_fps():.1f}"
            )
            self.babble_fps_signal.emit(f"FPS: {self.__babble_pipeline.get_fps():.1f}")

            self.mediapipe_latency_signal.emit(
                f"Latency: {self.__media_pipe_pipeline.get_latency() * 1000.0:.0f} ms"
            )
            self.babble_latency_signal.emit(
                f"Latency: {self.__babble_pipeline.get_latency() * 1000.0:.0f} ms"
            )

            self.udp_pps_signal.emit(f"PPS: {self.__udp_pipeline.get_pps():.1f}")
            self.udp_status_signal.emit(
                "Status: {}".format(
                    "IP Error" if self.__udp_pipeline.has_error() else "Sending"
                )
            )

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
        self.udp_pps_signal.connect(self.__ui.vrcft_pps_lbl.setText)
        self.udp_status_signal.connect(self.__ui.vrcft_status_lbl.setText)
        self.has_update_signal.connect(self.__has_update)
        self.camera_list_ready_signal.connect(self.__on_camera_list_ready)

    def __unregister_signals(self):
        self.camera_fps_signal.disconnect(self.__ui.camera_fps_lbl.setText)
        self.mediapipe_fps_signal.disconnect(self.__ui.mediapipe_fps_lbl.setText)
        self.mediapipe_latency_signal.disconnect(
            self.__ui.mediapipe_latency_lbl.setText
        )
        self.babble_fps_signal.disconnect(self.__ui.babble_fps_lbl.setText)
        self.babble_latency_signal.disconnect(self.__ui.babble_latency_lbl.setText)
        self.udp_pps_signal.disconnect(self.__ui.vrcft_pps_lbl.setText)
        self.udp_status_signal.disconnect(self.__ui.vrcft_status_lbl.setText)
        self.has_update_signal.disconnect(self.__has_update)

    def __register_events(self):
        self.__ui.open_camera_preview_btn.clicked.connect(self.__open_camera_preview)
        self.__ui.open_camera_settings_btn.clicked.connect(self.__open_camera_setting)

        self.__ui.open_mediapipe_preview_btn.clicked.connect(
            self.__open_mediapipe_preview
        )
        self.__ui.open_mediapipe_settings_btn.clicked.connect(
            self.__open_mediapipe_setting
        )

        self.__ui.open_babble_preview_btn.clicked.connect(self.__open_babble_preview)
        self.__ui.open_babble_setting_btn.clicked.connect(
            self.__open_babble_setting_btn
        )

        self.__ui.open_processing_calibration_btn.clicked.connect(
            self.__open_processing_calibration
        )
        self.__ui.open_processing_settings_btn.clicked.connect(
            self.__open_processing_settings
        )

        self.__ui.open_vrcft_settings_btn.clicked.connect(self.__open_vrcft_settings)

    def __open_camera_preview(self):
        try:
            self.__camera_pipeline.trigger_view_preview()
        except Exception:
            _logger.warning(
                "Failed to open camera preview", exc_info=True, stack_info=True
            )

    def __open_camera_setting(self):
        try:
            if (
                self.__camera_settings_window is None
                or self.__camera_settings_window.is_closed.is_set()
            ):
                try:
                    self.__camera_settings_window = CameraSettingsWindow(
                        self.__config_manager
                    )
                    # Reset the closed event if it was set
                    if self.__camera_settings_window.is_closed.is_set():
                        self.__camera_settings_window.is_closed.clear()
                except Exception:
                    _logger.error(
                        "Failed to initialize camera settings window", exc_info=True
                    )
                    self.__camera_settings_window = None
            else:
                self.__camera_settings_window.close_event.emit()
        except Exception:
            _logger.warning(
                "Failed to open camera settings", exc_info=True, stack_info=True
            )

    def __open_mediapipe_preview(self):
        try:
            self.__media_pipe_pipeline.trigger_view_preview()
        except Exception:
            _logger.warning(
                "Failed to open mediapipe preview", exc_info=True, stack_info=True
            )

    def __open_mediapipe_setting(self):
        try:
            if (
                self.__media_pipe_settings_window is None
                or self.__media_pipe_settings_window.is_closed.is_set()
            ):
                self.__media_pipe_settings_window = MediaPipeSettingsWindow(
                    self.__config_manager
                )
            else:
                self.__media_pipe_settings_window.close_event.emit()
        except Exception:
            _logger.warning(
                "Failed to open mediapipe settings", exc_info=True, stack_info=True
            )

    def __open_babble_preview(self):
        try:
            self.__babble_pipeline.trigger_view_preview()
        except Exception:
            _logger.warning(
                "Failed to open babble preview", exc_info=True, stack_info=True
            )

    def __open_babble_setting_btn(self):
        try:
            if (
                self.__babble_settings_window is None
                or self.__babble_settings_window.is_closed.is_set()
            ):
                self.__babble_settings_window = BabbleSettingsWindow(
                    self.__config_manager, self.__babble_pipeline.get_model_loader()
                )
            else:
                self.__babble_settings_window.close_event.emit()
        except Exception:
            _logger.warning(
                "Failed to open babble settings", exc_info=True, stack_info=True
            )

    def __open_processing_calibration(self):
        try:
            if (
                self.__auto_calibration_window is None
                or self.__auto_calibration_window.is_closed.is_set()
            ):
                self.__auto_calibration_window = AutoCalibrationWindow(
                    self.__config_manager, self.__auto_calibration_endpoint
                )
            else:
                self.__auto_calibration_window.close_event.emit()
        except Exception:
            _logger.warning(
                "Failed to open processing calibration", exc_info=True, stack_info=True
            )

    def __open_processing_settings(self):
        try:
            if (
                self.__calibration_window is None
                or self.__calibration_window.is_closed.is_set()
            ):
                self.__calibration_window = CalibrationWindow(
                    self.__config_manager, self.__processing_pipeline
                )
            else:
                self.__calibration_window.close_event.emit()
        except Exception:
            _logger.warning(
                "Failed to open processing settings", exc_info=True, stack_info=True
            )

    def __open_vrcft_settings(self):
        try:
            if (
                self.__vrcft_settings_window is None
                or self.__vrcft_settings_window.is_closed.is_set()
            ):
                self.__vrcft_settings_window = VrcftSettingsWindow(
                    self.__config_manager, self.__steam_auto_run
                )
            else:
                self.__vrcft_settings_window.close_event.emit()
        except Exception:
            _logger.warning(
                "Failed to open vrcft settings", exc_info=True, stack_info=True
            )

    def __has_update(self, founded_version: Version):
        try:
            if (
                self.__has_update_window is None
                or self.__has_update_window.is_closed.is_set()
            ):
                self.__has_update_window = HasUpdateWindow(
                    self.__config_manager, founded_version
                )
        except Exception:
            _logger.warning(
                "Failed to open has update window", exc_info=True, stack_info=True
            )
