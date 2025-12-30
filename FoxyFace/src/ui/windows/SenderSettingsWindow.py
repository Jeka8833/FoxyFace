import logging

from config.ConfigManager import ConfigManager
from ui.FoxyWindow import FoxyWindow
from ui.qtcreator.ui_SenderSettings import Ui_SenderSettings

_logger = logging.getLogger(__name__)


class SenderSettingsWindow(FoxyWindow):

    def __init__(self, config_manager: ConfigManager):
        super().__init__()

        self.__config_manager = config_manager

        self.__ui = Ui_SenderSettings()
        self.__ui.setupUi(self)

        self.__ui.save_btn.clicked.connect(self.__save)

        self.__set_default_values()

        self.show()

    def __set_default_values(self):
        pass

    def __save(self):
        try:


            self.__config_manager.write()
        except Exception:
            _logger.exception("Failed to save config")