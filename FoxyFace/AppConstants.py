import sys
from pathlib import Path
from typing import Final

from packaging.version import Version


class AppConstants:
    VERSION: Final[Version] = Version("1.0.4.0")

    @staticmethod
    def get_application_root() -> Path:
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            # noinspection PyProtectedMember
            return Path(sys._MEIPASS).resolve(strict=True)
        else:
            return Path.cwd()
