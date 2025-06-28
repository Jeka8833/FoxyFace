import logging
from typing import Any, Callable

from PySide6.QtCore import QTimer, Qt, Signal
from PySide6.QtWidgets import QComboBox, QFileDialog

from src.autorun.RunStrategyEnum import RunStrategyEnum
from src.autorun.SteamAutoRun import SteamAutoRun
from src.config.ConfigManager import ConfigManager
from src.config.ConfigUpdateListener import ConfigUpdateListener
from src.config.schemas.Config import Config
from src.ui.FoxyWindow import FoxyWindow
from src.ui.qtcreator.ui_VrcftSettings import Ui_VrcftSettings

_logger = logging.getLogger(__name__)


class VrcftSettingsWindow(FoxyWindow):
    __update_ip_signal: Signal = Signal()

    def __init__(self, config_manager: ConfigManager, steam_auto_run: SteamAutoRun):
        super().__init__()

        self.__config_manager = config_manager
        self.__steam_auto_run = steam_auto_run

        self.__ui = Ui_VrcftSettings()
        self.__ui.setupUi(self)

        self.__update_ip_signal.connect(self.__update_ip)
        self.__ui.save_btn.clicked.connect(self.__save)
        self.__ui.force_run_btn.clicked.connect(self.__force_auto_run)

        self.__ui.run_vrchat_strategy_cb.currentIndexChanged.connect(self.__auto_run_changed)
        self.__ui.run_vrcft_strategy_cb.currentIndexChanged.connect(self.__auto_run_changed)
        self.__ui.vrchat_file_path_le.textChanged.connect(self.__auto_run_changed)
        self.__ui.vrcft_file_path_le.textChanged.connect(self.__auto_run_changed)

        self.__ui.vrchat_file_path_select_btn.clicked.connect(self.__change_vrchat_path)
        self.__ui.vrcft_file_path_select_btn.clicked.connect(self.__change_vrcft_path)

        self.__timer: QTimer = QTimer(self, interval=1000, timerType=Qt.TimerType.VeryCoarseTimer)
        self.__timer.timeout.connect(self.__update_thread)
        self.__timer.start()

        self.__ip_change_listener = self.__register_ip_change()

        self.__set_default_values()

        self.show()

    def closeEvent(self, event, /):
        super().closeEvent(event)

        self.__ip_change_listener.unregister()

        self.__timer.stop()

        self.__update_ip_signal.disconnect(self.__update_ip)
        self.__ui.save_btn.clicked.disconnect(self.__save)
        self.__ui.force_run_btn.clicked.disconnect(self.__force_auto_run)

        self.__ui.run_vrchat_strategy_cb.currentIndexChanged.disconnect(self.__auto_run_changed)
        self.__ui.run_vrcft_strategy_cb.currentIndexChanged.disconnect(self.__auto_run_changed)
        self.__ui.vrchat_file_path_le.textChanged.disconnect(self.__auto_run_changed)
        self.__ui.vrcft_file_path_le.textChanged.disconnect(self.__auto_run_changed)

        self.__ui.vrchat_file_path_select_btn.clicked.disconnect(self.__change_vrchat_path)
        self.__ui.vrcft_file_path_select_btn.clicked.disconnect(self.__change_vrcft_path)

    def __set_default_values(self):
        self.__ui.auto_connect_cb.setChecked(self.__config_manager.config.socket.auto_connect)
        self.__ui.read_timeout_sp.setValue(self.__config_manager.config.socket.udp_read_timeout)
        self.__ui.bypass_cb.setChecked(self.__config_manager.config.socket.bypass_other_modules_block)

        self.__ui.vrchat_file_path_le.setText(self.__config_manager.config.auto_run.vrchat_path)
        self.__ui.vrcft_file_path_le.setText(self.__config_manager.config.auto_run.vrcft_path)

        self.__ui.run_vrchat_strategy_cb.setCurrentIndex(
            self.__get_run_strategy_index(self.__config_manager.config.auto_run.vrchat_strategy))
        self.__ui.run_vrcft_strategy_cb.setCurrentIndex(
            self.__get_run_strategy_index(self.__config_manager.config.auto_run.vrcft_strategy))

        self.__auto_run_changed()
        self.__update_on_apply()
        self.__update_thread()

    def __save(self):
        try:
            self.__config_manager.config.socket.auto_connect = self.__ui.auto_connect_cb.isChecked()
            self.__config_manager.config.socket.ip = self.__ui.ip_le.text()
            self.__config_manager.config.socket.port = self.__ui.port_sp.value()
            self.__config_manager.config.socket.udp_read_timeout = self.__ui.read_timeout_sp.value()
            self.__config_manager.config.socket.bypass_other_modules_block = self.__ui.bypass_cb.isChecked()

            self.__config_manager.config.auto_run.vrchat_path = self.__ui.vrchat_file_path_le.text()
            self.__config_manager.config.auto_run.vrcft_path = self.__ui.vrcft_file_path_le.text()
            self.__config_manager.config.auto_run.vrchat_strategy = self.__get_run_strategy(
                self.__ui.run_vrchat_strategy_cb)
            self.__config_manager.config.auto_run.vrcft_strategy = self.__get_run_strategy(
                self.__ui.run_vrcft_strategy_cb)

            self.__config_manager.write()

            self.__update_on_apply()
        except Exception:
            _logger.warning("Failed to save camera settings", exc_info=True, stack_info=True)

    def __update_thread(self):
        if self.__steam_auto_run.get_error_message_vrchat() is not None:
            self.__ui.vrchat_auto_run_error_lb.setText(f"Error: {self.__steam_auto_run.get_error_message_vrchat()}")
            self.__ui.vrchat_auto_run_error_lb.show()
        else:
            self.__ui.vrchat_auto_run_error_lb.hide()

        if self.__steam_auto_run.get_error_message_vrcft() is not None:
            self.__ui.vrcft_auto_run_error_lb.setText(f"Error: {self.__steam_auto_run.get_error_message_vrcft()}")
            self.__ui.vrcft_auto_run_error_lb.show()
        else:
            self.__ui.vrcft_auto_run_error_lb.hide()

    def __force_auto_run(self):
        self.__steam_auto_run.run()

    def __change_vrchat_path(self):
        filename, window_filter = QFileDialog.getOpenFileName(parent=self, caption='Open VRChat Application', dir='.',
                                                              filter='*')

        if filename:
            self.__ui.vrchat_file_path_le.setText(filename)

    def __change_vrcft_path(self):
        filename, window_filter = QFileDialog.getOpenFileName(parent=self, caption='Open VRCFT Application', dir='.',
                                                              filter='*')

        if filename:
            self.__ui.vrcft_file_path_le.setText(filename)

    def __auto_run_changed(self):
        vrchat_strategy = self.__get_run_strategy(self.__ui.run_vrchat_strategy_cb)
        vrcft_strategy = self.__get_run_strategy(self.__ui.run_vrcft_strategy_cb)

        self.__ui.vrchat_file_path_widget.setVisible(vrchat_strategy == RunStrategyEnum.USING_PATH)
        self.__ui.vrcft_file_path_widget.setVisible(vrcft_strategy == RunStrategyEnum.USING_PATH)

        vrchat_selected_path = self.__ui.vrchat_file_path_le.text()
        vrcft_selected_path = self.__ui.vrcft_file_path_le.text()

        self.__ui.vrchat_file_path_reset_widget.setVisible(bool(vrchat_selected_path))
        self.__ui.vrcft_file_path_reset_widget.setVisible(bool(vrcft_selected_path))

    def __update_on_apply(self):
        vrchat_strategy = self.__get_run_strategy(self.__ui.run_vrchat_strategy_cb)
        vrcft_strategy = self.__get_run_strategy(self.__ui.run_vrcft_strategy_cb)

        self.__ui.force_run_btn.setVisible(
            vrchat_strategy != RunStrategyEnum.DISABLED or vrcft_strategy != RunStrategyEnum.DISABLED)

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

    @staticmethod
    def __get_run_strategy(combobox: QComboBox) -> RunStrategyEnum:
        for item in RunStrategyEnum:
            if VrcftSettingsWindow.__get_run_strategy_index(item) == combobox.currentIndex():
                return item

        raise ValueError("Invalid run strategy index")

    @staticmethod
    def __get_run_strategy_index(run_strategy: RunStrategyEnum) -> int:
        if run_strategy == RunStrategyEnum.USING_STEAM:
            return 1
        elif run_strategy == RunStrategyEnum.USING_PATH:
            return 2
        else:
            return 0
