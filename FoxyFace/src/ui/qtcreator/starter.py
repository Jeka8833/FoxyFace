# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_MainWindow import Ui_MainWindow
from ui_CameraSettings import Ui_CameraSettings
from ui_MediaPipeSettings import Ui_MediaPipeSettings
from ui_AutoCalibrationWindow import Ui_AutoCalibrationWindow
from ui_SenderSettings import Ui_SenderSettings

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        #self.ui = Ui_MainWindow()
        #self.ui = Ui_CameraSettings()
        #self.ui = Ui_MediaPipeSettings()
        #self.ui = Ui_AutoCalibrationWindow()
        self.ui = Ui_SenderSettings()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
