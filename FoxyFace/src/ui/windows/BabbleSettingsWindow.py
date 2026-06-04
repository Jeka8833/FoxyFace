import logging

from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QFileDialog

from src.config.ConfigManager import ConfigManager
from src.config.schemas.main.core.BabbleConfig import BabbleConfig
from src.stream.babble.BabbleModelLoader import BabbleModelLoader
from src.ui.FoxyWindow import FoxyWindow
from src.ui.qtcreator.ui_BabbleSettings import Ui_BabbleSettings
from src.util import OnnxUtil

_logger = logging.getLogger(__name__)


class BabbleSettingsWindow(FoxyWindow):
    def __init__(self, config_manager: ConfigManager, model_loader: BabbleModelLoader):
        super().__init__()

        self.__config_manager = config_manager
        self.__model_loader = model_loader

        self.__ui = Ui_BabbleSettings()
        self.__ui.setupUi(self)

        self.__ui.save_btn.clicked.connect(self.__save)
        self.__ui.select_path_btn.clicked.connect(self.__path_selector)
        self.__ui.full_reset_btn.clicked.connect(self.__full_reset)
        self.__ui.selected_path_le.textChanged.connect(self.__update_model_status)

        self.__set_default_values()

        self.__timer = QTimer(self, interval=1000, timerType=Qt.TimerType.VeryCoarseTimer)
        self.__timer.timeout.connect(self.__update_model_status)
        self.__timer.start()

        self.show()

    def closeEvent(self, event, /):
        super().closeEvent(event)

        self.__timer.stop()

        self.__ui.save_btn.clicked.disconnect(self.__save)
        self.__ui.select_path_btn.clicked.disconnect(self.__path_selector)
        self.__ui.full_reset_btn.clicked.disconnect(self.__full_reset)
        self.__ui.selected_path_le.textChanged.disconnect(self.__update_model_status)

    def __set_default_values(self):
        self.__ui.use_babble_cb.setChecked(self.__config_manager.config.babble.enabled)
        self.__ui.max_head_rotation_x_sp.setValue(self.__config_manager.config.babble.max_head_rotation_x)
        self.__ui.max_head_rotation_y_sp.setValue(self.__config_manager.config.babble.max_head_rotation_y)
        self.__ui.mincutoff_sp.setValue(self.__config_manager.config.babble.mincutoff)
        self.__ui.beta_sp.setValue(self.__config_manager.config.babble.beta)
        self.__ui.selected_path_le.setText(self.__config_manager.config.babble.model_path)
        self.__ui.gpu_device_id_sb.setValue(self.__config_manager.config.babble.device_id)
        self.__ui.allow_spinning_cb.setChecked(self.__config_manager.config.babble.allow_spinning)
        self.__ui.thread_count_sp.setValue(self.__config_manager.config.babble.intra_op_num_threads)

        self.__update_model_status()
        self.__update_provider()

    def __full_reset(self):
        try:
            self.__config_manager.config.babble = BabbleConfig()
            self.__config_manager.write()
            self.__set_default_values()
        except Exception:
            _logger.warning("Failed to reset babble settings", exc_info=True, stack_info=True)

    def __path_selector(self):
        try:
            filename, window_filter = QFileDialog.getOpenFileName(parent=self, caption='Open Babble Model', dir='.',
                                                                  filter='*.onnx')

            if filename:
                self.__ui.selected_path_le.setText(filename)
        except Exception:
            _logger.warning("Failed to select model path", exc_info=True, stack_info=True)

    def __save(self):
        try:
            self.__config_manager.config.babble.enabled = self.__ui.use_babble_cb.isChecked()
            self.__config_manager.config.babble.max_head_rotation_x = self.__ui.max_head_rotation_x_sp.value()
            self.__config_manager.config.babble.max_head_rotation_y = self.__ui.max_head_rotation_y_sp.value()
            self.__config_manager.config.babble.mincutoff = self.__ui.mincutoff_sp.value()
            self.__config_manager.config.babble.beta = self.__ui.beta_sp.value()
            self.__config_manager.config.babble.model_path = self.__ui.selected_path_le.text()
            self.__config_manager.config.babble.device_id = self.__ui.gpu_device_id_sb.value()
            self.__config_manager.config.babble.allow_spinning = self.__ui.allow_spinning_cb.isChecked()
            self.__config_manager.config.babble.intra_op_num_threads = self.__ui.thread_count_sp.value()
            self.__config_manager.config.babble.provider = self.__get_provider()

            self.__config_manager.write()
        except Exception:
            _logger.warning("Failed to save camera settings", exc_info=True, stack_info=True)

    def __update_model_status(self):
        try:
            model = self.__model_loader.model

            if model is None:
                self.__ui.model_status_lb.setText("Fail to load model")
                self.__ui.model_status_lb.show()
            elif model.is_default_model:
                self.__ui.model_status_lb.setText("Update the model for better face tracking!")
                self.__ui.model_status_lb.show()
            else:
                self.__ui.model_status_lb.hide()

            selected_path = self.__ui.selected_path_le.text()

            self.__ui.reset_model_path_btn.setVisible(bool(selected_path))
        except Exception:
            _logger.warning("Failed to update thread", exc_info=True, stack_info=True)

    def __update_provider(self):
        self.__ui.provider_cb.clear()

        self.__ui.provider_cb.addItem("Auto")
        for provider in OnnxUtil.AVAILABLE_PROVIDERS:
            self.__ui.provider_cb.addItem(provider)

        for i in range(self.__ui.provider_cb.count()):
            if self.__ui.provider_cb.itemText(i) == self.__config_manager.config.babble.provider:
                self.__ui.provider_cb.setCurrentIndex(i)
                return

        self.__ui.provider_cb.setCurrentIndex(0)

    def __get_provider(self) -> str | None:
        selected_text = self.__ui.provider_cb.currentText()
        if selected_text in OnnxUtil.AVAILABLE_PROVIDERS:
            return selected_text

        return None
