import ctypes
import logging
from functools import cache

from PySide6.QtGui import QPixmap

from AppConstants import AppConstants

__logger = logging.getLogger(__name__)


def allow_change_windows_icon():
    try:
        myappid = u'com.Jeka8833.FoxyFace'

        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except Exception:
        __logger.info("Failed to set app id, app is not Windows")


@cache
def get_window_icon() -> QPixmap | None:
    try:
        return QPixmap(AppConstants.get_application_root() / 'Assets' / 'icon.png')
    except Exception:
        __logger.warning("Failed to load get_window_icon", exc_info=True, stack_info=True)

        return None


@cache
def get_no_image_icon() -> QPixmap | None:
    try:
        return QPixmap(AppConstants.get_application_root() / 'Assets' / 'no-image.jpg')
    except Exception:
        __logger.warning("Failed to load get_no_image_qpixmap", exc_info=True, stack_info=True)

        return None

@cache
def get_warning_icon() -> QPixmap | None:
    try:
        return QPixmap(AppConstants.get_application_root() / 'Assets' / 'warning.png')
    except Exception:
        __logger.warning("Failed to load get_warning_icon", exc_info=True, stack_info=True)

        return None