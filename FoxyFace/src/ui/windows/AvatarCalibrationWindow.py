from collections.abc import Callable

from PySide6.QtCore import QTimer, Qt, Signal

from src.config.ConfigManager import ConfigManager
from src.config.schemas.avatar.AvatarConfig import AvatarConfig
from src.pipline.senders.SenderRouterPipeline import SenderRouterPipeline
from src.stream.senders.vrchat.VRchatAvatarConfigManager import VRChatAvatarConfigManager
from src.ui.FoxyWindow import FoxyWindow
from src.ui.qtcreator.ui_AvatarCalibration import Ui_AvatarCalibration


class AvatarCalibrationWindow(FoxyWindow):
    no_connection_description_signal = Signal(str)

    def __init__(self, config_manager: ConfigManager, open_connection_setting: Callable[[], None],
                 sender_manager: SenderRouterPipeline,
                 vrchat_config_manager: VRChatAvatarConfigManager,
                 ifacialmocap_config_manager: ConfigManager[AvatarConfig],
                 foxyface_config_manager: ConfigManager[AvatarConfig],
                 meowface_config_manager: ConfigManager[AvatarConfig]):
        super().__init__()

        self.__config_manager = config_manager
        self.__open_connection_setting_callback = open_connection_setting
        self.__sender_manager = sender_manager
        self.__vrchat_config_manager = vrchat_config_manager
        self.__ifacialmocap_config_manager = ifacialmocap_config_manager
        self.__foxyface_config_manager = foxyface_config_manager
        self.__meowface_config_manager = meowface_config_manager

        self.__ui = Ui_AvatarCalibration()
        self.__ui.setupUi(self)

        self.__register_events()
        self.__register_signals()

        self.__timer: QTimer = QTimer(self, interval=2000, timerType=Qt.TimerType.VeryCoarseTimer)
        self.__timer.timeout.connect(self.__update_thread)
        self.__timer.start()

        self.show()

    def closeEvent(self, event, /):
        super().closeEvent(event)

        self.__unregister_signals()

        self.__timer.stop()

    def __update_thread(self):
        pass

    def __register_signals(self):
        self.no_connection_description_signal.connect(self.__ui.no_connection_description_lb.setText)

    def __unregister_signals(self):
        self.no_connection_description_signal.disconnect(self.__ui.no_connection_description_lb.setText)

    def __register_events(self):
        self.__ui.open_connection_settings_btn.clicked.connect(self.__open_connection_setting_callback)

    def __open_sender_settings(self):
        self.__open_connection_setting_callback()