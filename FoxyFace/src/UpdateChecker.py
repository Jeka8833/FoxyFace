import logging
import os
import sys
from concurrent.futures import Future, ThreadPoolExecutor

import requests
from packaging.version import Version

from AppConstants import AppConstants
from src.config.ConfigManager import ConfigManager
from src.ui.windows.HasUpdateWindow import HasUpdateWindow
from src.ui.windows.MainWindow import MainWindow

_logger = logging.getLogger(__name__)


class UpdateChecker:
    __VERSION_FILE_URL = "https://raw.githubusercontent.com/Jeka8833/FoxyFace/refs/heads/main/FoxyFace/current_release.json"
    __HEADERS = {"User-Agent": f"FoxyFace-{str(AppConstants.VERSION)}"}

    def __init__(self, config_manager: ConfigManager, main_window : MainWindow):
        self.__config_manager = config_manager
        self.__main_window = main_window

        if sys.platform == 'darwin':
            os.environ["no_proxy"] = "*"

        self.__thread_pool: ThreadPoolExecutor = ThreadPoolExecutor(max_workers=1, thread_name_prefix="Update Checker")

        self.__update_window: HasUpdateWindow | None = None

    def startup_check(self) -> None:
        if str(AppConstants.VERSION) != self.__config_manager.config.gui.auto_updater_version_skip:
            self.manual_check()
        else:
            _logger.info("Skipping update check")

    def manual_check(self) -> Future[bool]:
        return self.__thread_pool.submit(self.__update_check)

    def close(self) -> None:
        self.__thread_pool.shutdown(cancel_futures=True)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __update_check(self) -> bool:
        try:
            # Used requests library because of automatic GZIP, easy to update library and other stuff
            request_result = requests.get(UpdateChecker.__VERSION_FILE_URL, headers=UpdateChecker.__HEADERS)

            json_content = request_result.json()

            founded_version = Version(json_content['version'])

            if AppConstants.VERSION < founded_version:
                _logger.info(f"New version of FoxyFace is available: {founded_version}")

                self.__main_window.has_update_signal.emit(founded_version)
            return True
        except Exception:
            _logger.warning("Failed to check for updates", exc_info=True, stack_info=True)

        return False
