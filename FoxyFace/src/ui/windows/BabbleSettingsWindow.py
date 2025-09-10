import logging

from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QFileDialog

from src.config.ConfigManager import ConfigManager
from src.config.schemas.core.BabbleConfig import BabbleConfig
from src.stream.babble.BabbleModelLoader import BabbleModelLoader
from src.ui.FoxyWindow import FoxyWindow
from src.ui.qtcreator.ui_BabbleSettings import Ui_BabbleSettings

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
        self.__ui.try_use_gpu_cb.setChecked(self.__config_manager.config.babble.try_use_gpu)
        self.__ui.gpu_device_id_sb.setValue(self.__config_manager.config.babble.device_id)
        self.__ui.allow_spinning_cb.setChecked(self.__config_manager.config.babble.allow_spinning)
        self.__ui.thread_count_sp.setValue(self.__config_manager.config.babble.intra_op_num_threads)

        self.__update_model_status()

    def __full_reset(self):
        self.__config_manager.config.babble = BabbleConfig()
        self.__config_manager.write()
        self.__set_default_values()

    def __path_selector(self):
        filename, window_filter = QFileDialog.getOpenFileName(parent=self, caption='Open Babble Model', dir='.',
                                                              filter='*.onnx')

        if filename:
            self.__ui.selected_path_le.setText(filename)

    def __save(self):
        try:
            self.__config_manager.config.babble.enabled = self.__ui.use_babble_cb.isChecked()
            self.__config_manager.config.babble.max_head_rotation_x = self.__ui.max_head_rotation_x_sp.value()
            self.__config_manager.config.babble.max_head_rotation_y = self.__ui.max_head_rotation_y_sp.value()
            self.__config_manager.config.babble.mincutoff = self.__ui.mincutoff_sp.value()
            self.__config_manager.config.babble.beta = self.__ui.beta_sp.value()
            self.__config_manager.config.babble.model_path = self.__ui.selected_path_le.text()
            self.__config_manager.config.babble.try_use_gpu = self.__ui.try_use_gpu_cb.isChecked()
            self.__config_manager.config.babble.device_id = self.__ui.gpu_device_id_sb.value()
            self.__config_manager.config.babble.allow_spinning = self.__ui.allow_spinning_cb.isChecked()
            self.__config_manager.config.babble.intra_op_num_threads = self.__ui.thread_count_sp.value()

            self.__config_manager.write()
        except Exception:
            _logger.warning("Failed to save camera settings", exc_info=True, stack_info=True)

    def __update_model_status(self):
        if self.__model_loader.model is None:
            self.__ui.model_status_lb.setText("Fail to load model")
            self.__ui.model_status_lb.show()
        elif self.__model_loader.model.is_default_model:
            self.__ui.model_status_lb.setText("Update the model for better face tracking!")
            self.__ui.model_status_lb.show()
        else:
            self.__ui.model_status_lb.hide()

        selected_path = self.__ui.selected_path_le.text()

        self.__ui.reset_model_path_btn.setVisible(bool(selected_path))
