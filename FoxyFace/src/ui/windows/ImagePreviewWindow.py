from PySide6.QtCore import Signal
from PySide6.QtWidgets import QHBoxLayout, QLabel, QSizePolicy, QWidget

from src.ui import UiImageUtil
from src.ui.FoxyWindow import FoxyWindow


class ImagePreviewWindow(FoxyWindow):
    image_event = Signal(object)
    noimage_event = Signal()

    def __init__(self, title: str = "Image Preview Window", width: int = 640, height: int = 480):
        super().__init__()

        self.resize(width, height)
        self.setWindowTitle(title)

        central_widget = QWidget(self)

        horizontal_layout = QHBoxLayout(central_widget)
        horizontal_layout.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel()
        self.label.setScaledContents(True)
        self.label.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored))
        self.__no_image()

        horizontal_layout.addWidget(self.label)

        self.setCentralWidget(central_widget)

        self.image_event.connect(self.label.setPixmap)
        self.noimage_event.connect(self.__no_image)

        self.show()

    def __no_image(self):
        no_image = UiImageUtil.get_no_image_icon()

        if no_image is not None:
            self.label.setPixmap(no_image)

    def closeEvent(self, event, /):
        super().closeEvent(event)

        self.image_event.disconnect(self.label.setPixmap)
        self.noimage_event.disconnect(self.__no_image)
