import logging

from src.config.ConfigManager import ConfigManager
from src.ui.FoxyWindow import FoxyWindow
from src.ui.qtcreator.ui_camerasettings import Ui_CameraSettings

_logger = logging.getLogger(__name__)


class CameraSettingsWindow(FoxyWindow):
    def __init__(self, config_manager: ConfigManager):
        super().__init__()

        self.__config_manager = config_manager

        self.__ui = Ui_CameraSettings()
        self.__ui.setupUi(self)

        self.__ui.apply_and_save_btn.clicked.connect(self.__save)
        self.__ui.height_sp.valueChanged.connect(self.__height_sp_value_changed)
        self.__ui.width_sp.valueChanged.connect(self.__width_sp_value_changed)

        self.__set_default_values()

        self.show()

    def closeEvent(self, event, /):
        super().closeEvent(event)

        self.__ui.apply_and_save_btn.clicked.disconnect(self.__save)
        self.__ui.height_sp.valueChanged.disconnect(self.__height_sp_value_changed)
        self.__ui.width_sp.valueChanged.disconnect(self.__width_sp_value_changed)

    def __set_default_values(self):
        self.__ui.camera_id_sp.setValue(self.__config_manager.config.camera.camera_id)
        self.__ui.width_sp.setValue(self.__config_manager.config.camera.width)
        self.__ui.height_sp.setValue(self.__config_manager.config.camera.height)
        self.__ui.horizontal_flip_cb.setChecked(self.__config_manager.config.camera.mirror_x)
        self.__ui.vertical_flip_cb.setChecked(self.__config_manager.config.camera.mirror_y)
        self.__ui.rotate_90_cb.setChecked(self.__config_manager.config.camera.rotate_ninety)

    def __save(self):
        try:
            self.__config_manager.config.camera.camera_id = self.__ui.camera_id_sp.value()
            self.__config_manager.config.camera.width = self.__ui.width_sp.value()
            self.__config_manager.config.camera.height = self.__ui.height_sp.value()
            self.__config_manager.config.camera.mirror_x = self.__ui.horizontal_flip_cb.isChecked()
            self.__config_manager.config.camera.mirror_y = self.__ui.vertical_flip_cb.isChecked()
            self.__config_manager.config.camera.rotate_ninety = self.__ui.rotate_90_cb.isChecked()

            self.__config_manager.write()
        except Exception:
            _logger.warning("Failed to save camera settings", exc_info=True, stack_info=True)

    def __height_sp_value_changed(self, value):
        if value % 2 != 0:
            self.__ui.height_sp.setValue(value + 1)

    def __width_sp_value_changed(self, value):
        if value % 2 != 0:
            self.__ui.width_sp.setValue(value + 1)
