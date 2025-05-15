import logging
from typing import Any, Callable

from PySide6.QtCore import Signal

from src.config.ConfigManager import ConfigManager
from src.config.ConfigUpdateListener import ConfigUpdateListener
from src.config.schemas.Config import Config
from src.ui.FoxyWindow import FoxyWindow
from src.ui.qtcreator.ui_VrcftSettings import Ui_VrcftSettings

_logger = logging.getLogger(__name__)


class VrcftSettingsWindow(FoxyWindow):
    __update_ip_signal: Signal = Signal()

    def __init__(self, config_manager: ConfigManager):
        super().__init__()

        self.__config_manager = config_manager

        self.__ui = Ui_VrcftSettings()
        self.__ui.setupUi(self)

        self.__update_ip_signal.connect(self.__update_ip)
        self.__ui.save_btn.clicked.connect(self.__save)

        self.__ip_change_listener = self.__register_ip_change()

        self.__set_default_values()

        self.show()

    def closeEvent(self, event, /):
        super().closeEvent(event)

        self.__ip_change_listener.unregister()

        self.__update_ip_signal.disconnect(self.__update_ip)

    def __set_default_values(self):
        self.__ui.auto_connect_cb.setChecked(self.__config_manager.config.socket.auto_connect)
        self.__ui.read_timeout_sp.setValue(self.__config_manager.config.socket.udp_read_timeout)
        self.__ui.bypass_cb.setChecked(self.__config_manager.config.socket.bypass_other_modules_block)

    def __save(self):
        try:
            self.__config_manager.config.socket.auto_connect = self.__ui.auto_connect_cb.isChecked()
            self.__config_manager.config.socket.ip = self.__ui.ip_le.text()
            self.__config_manager.config.socket.port = self.__ui.port_sp.value()
            self.__config_manager.config.socket.udp_read_timeout = self.__ui.read_timeout_sp.value()
            self.__config_manager.config.socket.bypass_other_modules_block = self.__ui.bypass_cb.isChecked()

            self.__config_manager.write()
        except Exception:
            _logger.warning("Failed to save camera settings", exc_info=True, stack_info=True)

    def __update_ip(self):
        self.__ui.ip_le.setText(self.__config_manager.config.socket.ip)
        self.__ui.port_sp.setValue(self.__config_manager.config.socket.port)

    def __register_ip_change(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.socket.ip,
                                                      lambda config: config.socket.port]

        return self.__config_manager.create_update_listener(self.__update_ip_change, watch_array, True)

    # noinspection PyUnusedLocal
    def __update_ip_change(self, config_manager: ConfigManager):
        self.__update_ip_signal.emit()
