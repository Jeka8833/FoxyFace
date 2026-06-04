import logging

from PySide6.QtCore import QTimer, Qt

from src.config.ConfigManager import ConfigManager
from src.config.schemas.core.MediaPipeTongueConfig import MediaPipeTongueConfig
from src.pipline.MediaPipeTonguePipeline import MediaPipeTonguePipeline
from src.ui.FoxyWindow import FoxyWindow
from src.ui.qtcreator.ui_MediaPipeTongueSettings import Ui_MediaPipeTongueSettings
from src.util import OnnxUtil

_logger = logging.getLogger(__name__)


class MediaPipeTongueSettingsWindow(FoxyWindow):
    def __init__(self, config_manager: ConfigManager, tongue_pipeline: MediaPipeTonguePipeline):
        super().__init__()

        self.__config_manager = config_manager
        self.__tongue_pipeline = tongue_pipeline

        self.__ui = Ui_MediaPipeTongueSettings()
        self.__ui.setupUi(self)

        self.__ui.apply_and_save_btn.clicked.connect(self.__save)
        self.__ui.full_reset_btn.clicked.connect(self.__full_reset)

        self.__set_default_values()

        self.__timer = QTimer(self, interval=1000, timerType=Qt.TimerType.VeryCoarseTimer)
        self.__timer.timeout.connect(self.__update_model_status)
        self.__timer.start()

        self.show()

    def closeEvent(self, event, /):
        super().closeEvent(event)

        self.__timer.stop()

        self.__ui.apply_and_save_btn.clicked.disconnect(self.__save)
        self.__ui.full_reset_btn.clicked.disconnect(self.__full_reset)

    def __set_default_values(self):
        self.__ui.use_nn_cb.setChecked(self.__config_manager.config.media_pipe_tongue.enabled)
        self.__ui.mincutoff_dsb.setValue(self.__config_manager.config.media_pipe_tongue.mincutoff)
        self.__ui.beta_dsb.setValue(self.__config_manager.config.media_pipe_tongue.beta)
        self.__ui.left_right_pad_sb.setValue(self.__config_manager.config.media_pipe_tongue.padding_x)
        self.__ui.top_pad_sb.setValue(self.__config_manager.config.media_pipe_tongue.padding_top)
        self.__ui.bottom_pad_sb.setValue(self.__config_manager.config.media_pipe_tongue.padding_bottom)
        self.__ui.cpu_spin.setChecked(self.__config_manager.config.media_pipe_tongue.allow_spinning)
        self.__ui.cpu_threads_sb.setValue(self.__config_manager.config.media_pipe_tongue.intra_op_num_threads)
        self.__ui.gpu_id_sb.setValue(self.__config_manager.config.media_pipe_tongue.device_id)

        self.__update_model_status()
        self.__update_provider()

    def __full_reset(self):
        try:
            self.__config_manager.config.media_pipe_tongue = MediaPipeTongueConfig()
            self.__config_manager.write()
            self.__set_default_values()
        except Exception:
            _logger.warning("Failed to reset MediaPipe Tongue settings", exc_info=True, stack_info=True)

    def __save(self):
        try:
            self.__config_manager.config.media_pipe_tongue.enabled = self.__ui.use_nn_cb.isChecked()
            self.__config_manager.config.media_pipe_tongue.mincutoff = self.__ui.mincutoff_dsb.value()
            self.__config_manager.config.media_pipe_tongue.beta = self.__ui.beta_dsb.value()
            self.__config_manager.config.media_pipe_tongue.padding_x = self.__ui.left_right_pad_sb.value()
            self.__config_manager.config.media_pipe_tongue.padding_top = self.__ui.top_pad_sb.value()
            self.__config_manager.config.media_pipe_tongue.padding_bottom = self.__ui.bottom_pad_sb.value()
            self.__config_manager.config.media_pipe_tongue.allow_spinning = self.__ui.cpu_spin.isChecked()
            self.__config_manager.config.media_pipe_tongue.intra_op_num_threads = self.__ui.cpu_threads_sb.value()
            self.__config_manager.config.media_pipe_tongue.provider = self.__get_provider()
            self.__config_manager.config.media_pipe_tongue.device_id = self.__ui.gpu_id_sb.value()

            self.__config_manager.write()
        except Exception:
            _logger.warning("Failed to save camera settings", exc_info=True, stack_info=True)

    def __update_model_status(self):
        try:
            if self.__tongue_pipeline.good_started:
                self.__ui.error_message_lb.hide()
            else:
                self.__ui.error_message_lb.setText("Fail to load model")
                self.__ui.error_message_lb.show()
        except Exception:
            _logger.warning("Failed to update thread", exc_info=True, stack_info=True)

    def __update_provider(self):
        self.__ui.provider_cb.clear()

        self.__ui.provider_cb.addItem("Auto")
        for provider in OnnxUtil.AVAILABLE_PROVIDERS:
            self.__ui.provider_cb.addItem(provider)

        for i in range(self.__ui.provider_cb.count()):
            if self.__ui.provider_cb.itemText(i) == self.__config_manager.config.media_pipe_tongue.provider:
                self.__ui.provider_cb.setCurrentIndex(i)
                return

        self.__ui.provider_cb.setCurrentIndex(0)

    def __get_provider(self) -> str | None:
        selected_text = self.__ui.provider_cb.currentText()
        if selected_text in OnnxUtil.AVAILABLE_PROVIDERS:
            return selected_text

        return None
