from src.config.ConfigManager import ConfigManager
from src.ui.FoxyWindow import FoxyWindow
from src.ui.qtcreator.ui_AvatarCalibration import Ui_AvatarCalibration


class AvatarCalibrationWindow(FoxyWindow):

    def __init__(self, config_manager: ConfigManager):
        super().__init__()

        self.__config_manager = config_manager

        self.__ui = Ui_AvatarCalibration()
        self.__ui.setupUi(self)

        self.show()

    def closeEvent(self, event, /):
        super().closeEvent(event)
