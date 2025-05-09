import logging

from src.config.ConfigManager import ConfigManager
from src.ui.FoxyWindow import FoxyWindow
from src.ui.qtcreator.ui_VrcftSettings import Ui_VrcftSettings

_logger = logging.getLogger(__name__)


class VrcftSettingsWindow(FoxyWindow):
    def __init__(self, config_manager: ConfigManager):
        super().__init__()

        self.__config_manager = config_manager

        self.__ui = Ui_VrcftSettings()
        self.__ui.setupUi(self)

        self.__ui.save_btn.clicked.connect(self.__save)

        self.__set_default_values()

        self.show()

    def __set_default_values(self):
        self.__ui.ip_le.setText(self.__config_manager.config.socket.ip)
        self.__ui.port_sp.setValue(self.__config_manager.config.socket.port)
        self.__ui.read_timeout_sp.setValue(self.__config_manager.config.socket.udp_read_timeout)
        self.__ui.bypass_cb.setChecked(self.__config_manager.config.socket.bypass_other_modules_block)

    def __save(self):
        try:
            self.__config_manager.config.socket.ip = self.__ui.ip_le.text()
            self.__config_manager.config.socket.port = self.__ui.port_sp.value()
            self.__config_manager.config.socket.udp_read_timeout = self.__ui.read_timeout_sp.value()
            self.__config_manager.config.socket.bypass_other_modules_block = self.__ui.bypass_cb.isChecked()

            self.__config_manager.write()
        except Exception:
            _logger.warning("Failed to save camera settings", exc_info=True, stack_info=True)
