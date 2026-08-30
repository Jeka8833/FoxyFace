import ctypes
import logging
from functools import cache

from PySide6.QtCore import QByteArray
from PySide6.QtGui import QPixmap

from foxyface.AppConstants import AppConstants

__logger = logging.getLogger(__name__)


def allow_change_windows_icon():
    try:
        myappid = u'com.Jeka8833.FoxyFace'

        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except Exception:
        __logger.info("Failed to set app id, app is not Windows")


@cache
def get_window_icon() -> QPixmap | None:
    return __load_image("icon.png")


@cache
def get_no_image_icon() -> QPixmap | None:
    return __load_image("no-image.png")


@cache
def get_warning_icon() -> QPixmap | None:
    return __load_image("warning.png")


def __load_image(path: str) -> QPixmap | None:
    try:
        pixmap = QPixmap()
        pixmap.loadFromData(QByteArray(AppConstants.get_file_from_assets(path).read_bytes()))

        return pixmap
    except Exception:
        __logger.warning(f"Failed to load image {path}", exc_info=True, stack_info=True)

        return None
