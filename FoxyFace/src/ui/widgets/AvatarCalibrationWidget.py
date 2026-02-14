from PySide6.QtWidgets import QWidget
from blendshape_router.router.EndpointEncoderInterface import EndpointEncoderInterface

from src.ui.qtcreator.ui_AvatarCalibrationWidget import Ui_AvatarCalibrationWidget


class AvatarCalibrationWidget(QWidget):

    def __init__(self, endpoints: list[EndpointEncoderInterface], solver):
        super().__init__()

        self.__ui = Ui_AvatarCalibrationWidget()
        self.__ui.setupUi(self)

    def closeEvent(self, event, /):
        super().closeEvent(event)
