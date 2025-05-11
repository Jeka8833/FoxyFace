import time

from PySide6.QtCore import Signal
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QHBoxLayout, QLabel, QSizePolicy, QWidget

from src.ui import UiImageUtil
from src.ui.FoxyWindow import FoxyWindow


class ImagePreviewWindow(FoxyWindow):
    set_image_event = Signal(object)

    __TITLE_UPDATE_INTERVAL_NS = 1_000_000_000  # 1 second

    def __init__(self, title: str = "Image Preview Window", width: int = 640, height: int = 480):
        super().__init__()

        self.__title = title
        self.__last_title_update: int = time.perf_counter_ns()

        self.setWindowTitle(title)
        self.resize(width, height)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        horizontal_layout = QHBoxLayout(central_widget)
        horizontal_layout.setContentsMargins(0, 0, 0, 0)

        self.__image_label = QLabel(scaledContents=True)
        self.__image_label.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored))
        horizontal_layout.addWidget(self.__image_label)

        self.set_image_event.connect(self.__set_image)
        self.__set_image(None)

        self.show()

    def __set_image(self, image: QImage | None) -> None:
        if image is None:
            no_image = UiImageUtil.get_no_image_icon() or QPixmap()

            self.__image_label.setPixmap(no_image)
            self.setWindowTitle(self.__title)
        else:
            self.__image_label.setPixmap(QPixmap.fromImage(image))

            current_time_ns = time.perf_counter_ns()
            if current_time_ns - self.__last_title_update > ImagePreviewWindow.__TITLE_UPDATE_INTERVAL_NS:
                self.__last_title_update = current_time_ns

                self.setWindowTitle(f"{self.__title} > Size: {image.width()}x{image.height()}")

    def closeEvent(self, event, /) -> None:
        super().closeEvent(event)

        try:
            self.set_image_event.disconnect(self.__set_image)
        except Exception:
            pass
