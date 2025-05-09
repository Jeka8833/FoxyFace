import logging
from threading import Event

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow

from src.ui import UiImageUtil

_logger = logging.getLogger(__name__)


class FoxyWindow(QMainWindow):
    close_event = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.is_closed: Event = Event()

        self.close_event.connect(self.close)

        icon = UiImageUtil.get_window_icon()
        if icon is not None:
            self.setWindowIcon(icon)

    def closeEvent(self, event, /):
        self.is_closed.set()

        try:
            self.close_event.disconnect(self.close)
        except Exception:
            _logger.warning("Failed to disconnect close event", exc_info=True, stack_info=True)

        super().closeEvent(event)
