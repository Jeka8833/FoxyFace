import logging
from collections.abc import Callable

from PySide6.QtCore import QTimer, Qt, Signal

from src.config.ConfigManager import ConfigManager
from src.pipline.senders.SenderRouterPipeline import SenderRouterPipeline
from src.stream.senders.AvatarEndpoint import AvatarEndpoint
from src.ui.FoxyWindow import FoxyWindow
from src.ui.qtcreator.ui_AvatarCalibration import Ui_AvatarCalibration
from src.ui.widgets.AvatarCalibrationWidget import AvatarCalibrationWidget

_logger = logging.getLogger(__name__)


class AvatarCalibrationWindow(FoxyWindow):
    no_connection_description_signal = Signal(str)

    def __init__(self, config_manager: ConfigManager, open_connection_setting: Callable[[], None],
                 sender_manager: SenderRouterPipeline):
        super().__init__()

        self.__config_manager = config_manager
        self.__open_connection_setting_callback = open_connection_setting
        self.__sender_manager = sender_manager

        self.__ui = Ui_AvatarCalibration()
        self.__ui.setupUi(self)

        self.__register_events()
        self.__register_signals()

        self.__timer: QTimer = QTimer(self, interval=2000, timerType=Qt.TimerType.VeryCoarseTimer)
        self.__timer.timeout.connect(self.__update_thread)
        self.__timer.start()
        self.__update_thread()

        self.show()

    def closeEvent(self, event, /):
        super().closeEvent(event)

        self.__unregister_signals()

        self.__timer.stop()

    def __update_thread(self):
        endpoints: set[AvatarEndpoint] = self.__sender_manager.get_endpoints()
        if endpoints:
            has_endpoints: set[AvatarEndpoint] = set()

            for index in reversed(range(self.__ui.endpoint_list_tab.count())):
                try:
                    widget = self.__ui.endpoint_list_tab.widget(index)
                    if not isinstance(widget, AvatarCalibrationWidget):
                        self.__ui.endpoint_list_tab.removeTab(index)

                    if widget.avatar_endpoint not in endpoints:
                        self.__ui.endpoint_list_tab.removeTab(index)
                    else:
                        for endpoint in endpoints:
                            if endpoint is widget.avatar_endpoint:
                                widget.update_endpoint(endpoint)
                                break

                        has_endpoints.add(widget.avatar_endpoint)
                except Exception:
                    _logger.warning("Failed to remove tab", exc_info=True, stack_info=True)

            need_to_add_endpoints = endpoints - has_endpoints
            for endpoint in need_to_add_endpoints:
                self.__ui.endpoint_list_tab.addTab(AvatarCalibrationWidget(endpoint), endpoint.endpoint_name)

            self.__ui.page_selector_sw.setCurrentIndex(0)
        else:
            self.__ui.page_selector_sw.setCurrentIndex(1)

    def __register_signals(self):
        self.no_connection_description_signal.connect(self.__ui.no_connection_description_lb.setText)

    def __unregister_signals(self):
        self.no_connection_description_signal.disconnect(self.__ui.no_connection_description_lb.setText)

    def __register_events(self):
        self.__ui.open_connection_settings_btn.clicked.connect(self.__open_connection_setting_callback)

    def __open_sender_settings(self):
        self.__open_connection_setting_callback()
