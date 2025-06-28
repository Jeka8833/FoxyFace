import logging
import subprocess
import webbrowser
from pathlib import Path
from threading import Thread
from typing import Any, Callable

from src.autorun.AutoRunOptions import AutoRunOptions
from src.autorun.RunStrategyEnum import RunStrategyEnum
from src.config.ConfigManager import ConfigManager
from src.config.ConfigUpdateListener import ConfigUpdateListener
from src.config.schemas.Config import Config

_logger = logging.getLogger(__name__)


class SteamAutoRun:
    __VRCHAT_STEAM_ID: int = 438100
    __VRCFACE_TRACKING_STEAM_ID: int = 3329480

    def __init__(self, config_manager: ConfigManager):
        self.__config_manager = config_manager

        self.__options: AutoRunOptions = AutoRunOptions()
        self.__options_listener: ConfigUpdateListener = self.__register_change_options()

        self.__vrchat_thread: Thread | None = None
        self.__vrcft_thread: Thread | None = None

        self.__last_error_message_vrchat: str | None = None
        self.__last_error_message_vrcft: str | None = None

    def run(self):
        self.__last_error_message_vrchat = None
        self.__last_error_message_vrcft = None

        try:
            if self.__options.vrchat_strategy == RunStrategyEnum.USING_STEAM:
                self.__vrchat_thread = SteamAutoRun.__create_thread_and_run(self.__vrchat_thread,
                                                                            SteamAutoRun.__run_steam_process,
                                                                            SteamAutoRun.__VRCHAT_STEAM_ID,
                                                                            self.__set_vrchat_error_message)
            elif self.__options.vrchat_strategy == RunStrategyEnum.USING_PATH:
                if self.__options.vrchat_path and not self.__options.vrchat_path.isspace():
                    path = Path(self.__options.vrchat_path).resolve(strict=True)

                    if path.is_file():
                        self.__vrchat_thread = SteamAutoRun.__create_thread_and_run(self.__vrchat_thread,
                                                                                    SteamAutoRun.__run_file_process,
                                                                                    path,
                                                                                    self.__set_vrchat_error_message)
                    else:
                        _logger.warning(f"Invalid file path: {path}")

                        self.__last_error_message_vrchat = "VRChat path is invalid"
                else:
                    _logger.warning("Process for VRChat failed, path is empty")

                    self.__last_error_message_vrchat = "VRChat path is empty"
        except Exception as e:
            _logger.warning("Failed to run VRChat process", exc_info=True, stack_info=True)

            self.__last_error_message_vrchat = str(e)

        try:
            if self.__options.vrcft_strategy == RunStrategyEnum.USING_STEAM:
                self.__vrcft_thread = SteamAutoRun.__create_thread_and_run(self.__vrcft_thread,
                                                                           SteamAutoRun.__run_steam_process,
                                                                           SteamAutoRun.__VRCFACE_TRACKING_STEAM_ID,
                                                                           self.__set_vrcft_error_message)
            elif self.__options.vrcft_strategy == RunStrategyEnum.USING_PATH:
                if self.__options.vrcft_path and not self.__options.vrcft_path.isspace():
                    path = Path(self.__options.vrcft_path).resolve(strict=True)

                    if path.is_file():
                        self.__vrcft_thread = SteamAutoRun.__create_thread_and_run(self.__vrcft_thread,
                                                                                   SteamAutoRun.__run_file_process,
                                                                                   path, self.__set_vrcft_error_message)
                    else:
                        _logger.warning(f"Invalid file path: {path}")

                        self.__last_error_message_vrcft = "VRCFT path is invalid"
                else:
                    _logger.warning("Process for VRCFT failed, path is empty")

                    self.__last_error_message_vrcft = "VRCFT path is empty"
        except Exception as e:
            _logger.warning("Failed to run VRCFT process", exc_info=True, stack_info=True)

            self.__last_error_message_vrcft = str(e)

    def get_error_message_vrchat(self) -> str | None:
        return self.__last_error_message_vrchat

    def get_error_message_vrcft(self) -> str | None:
        return self.__last_error_message_vrcft

    def close(self):
        self.__options_listener.unregister()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __register_change_options(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.auto_run]

        return self.__config_manager.create_update_listener(self.__update_options, watch_array, True)

    def __update_options(self, config_manager: ConfigManager):
        self.__options.vrchat_strategy = config_manager.config.auto_run.vrchat_strategy
        self.__options.vrchat_path = config_manager.config.auto_run.vrchat_path

        self.__options.vrcft_strategy = config_manager.config.auto_run.vrcft_strategy
        self.__options.vrcft_path = config_manager.config.auto_run.vrcft_path

    def __set_vrchat_error_message(self, error_message: str):
        self.__last_error_message_vrchat = error_message

    def __set_vrcft_error_message(self, error_message: str):
        self.__last_error_message_vrcft = error_message

    @staticmethod
    def __create_thread_and_run(previous_thread: Thread | None,
                                method: Callable[[int | Path, Callable[[str], None]], None], arg: int | Path,
                                error_callback: Callable[[str], None]) -> Thread:
        if previous_thread is not None and previous_thread.is_alive():
            return previous_thread

        thread = Thread(target=method, args=(arg, error_callback), daemon=True, name="Auto Run Application Thread")
        thread.start()

        return thread

    @staticmethod
    def __run_steam_process(steam_id: int, error_callback: Callable[[str], None]) -> None:
        try:
            webbrowser.open(f"steam://rungameid/{steam_id}")
        except Exception as e:
            _logger.warning(f"Failed to run {steam_id} process", exc_info=True, stack_info=True)

            error_callback(str(e))

    @staticmethod
    def __run_file_process(path: Path, error_callback: Callable[[str], None]) -> None:
        try:
            subprocess.Popen(path)
        except Exception as e:
            _logger.warning(f"Failed to run process: {path}", exc_info=True, stack_info=True)

            error_callback(str(e))
