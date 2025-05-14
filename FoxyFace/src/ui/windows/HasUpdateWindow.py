import webbrowser

from packaging.version import Version

from AppConstants import AppConstants
from src.config.ConfigManager import ConfigManager
from src.ui.FoxyWindow import FoxyWindow
from src.ui.qtcreator.ui_HasUpdateWindow import Ui_HasUpdateWindow


class HasUpdateWindow(FoxyWindow):
    def __init__(self, config_manager: ConfigManager, new_version: Version):
        super().__init__()

        self.__config_manager = config_manager

        self.__ui = Ui_HasUpdateWindow()
        self.__ui.setupUi(self)

        self.__ui.open_btn.clicked.connect(self.__open_browser)
        self.__ui.ignore_update_btn.clicked.connect(self.__ignore_update)

        self.__ui.version_lb.setText(f"FoxyFace update: {str(AppConstants.VERSION)} -> {str(new_version)}")

        self.show()

    @staticmethod
    def __open_browser():
        webbrowser.open('https://github.com/Jeka8833/FoxyFace')

    def __ignore_update(self):
        self.__config_manager.config.gui.auto_updater_version_skip = str(AppConstants.VERSION)
        self.__config_manager.write()
