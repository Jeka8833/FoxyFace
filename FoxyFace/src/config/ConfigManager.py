import logging
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Callable

from src.config.ConfigMigrationManager import ConfigMigrationManager
from src.config.ConfigUpdateListener import ConfigUpdateListener
from src.config.schemas.Config import Config

_logger = logging.getLogger(__name__)


class ConfigManager:
    def __init__(self, path: Path):
        self.__path: Path = path

        self.__thread_pool = ThreadPoolExecutor(max_workers=1, thread_name_prefix="Config Manager")
        self.__last_hash: int = 0

        self.__migration_manager: ConfigMigrationManager = ConfigMigrationManager()

        self.config: Config = Config()

        self.__update_listeners: set[ConfigUpdateListener] = set[ConfigUpdateListener]()

    def load(self, wait: bool = False):
        try:
            future = self.__thread_pool.submit(self.__read_task)

            if wait:
                future.result()
        except Exception:
            pass

    def write(self, wait: bool = False):
        try:
            future = self.__thread_pool.submit(self.__write_task)

            if wait:
                future.result()
        except Exception:
            pass

    def hard_reset(self, wait: bool = False):
        try:
            future = self.__thread_pool.submit(self.__hard_reset_task)

            if wait:
                future.result()
        except Exception:
            pass

    def close(self):
        self.__thread_pool.shutdown(wait=True, cancel_futures=True)
        self.__write_task()

    def create_update_listener(self, update_callback: Callable[["ConfigManager"], None],
                               watched_elements: list[Callable[[Config], Any]] = None,
                               call_on_create: bool = False) -> ConfigUpdateListener:
        listener = ConfigUpdateListener(self, update_callback, call_on_create, watched_elements)

        self.__update_listeners.add(listener)

        return listener

    def unregister_update_listener(self, listener: ConfigUpdateListener):
        try:
            self.__update_listeners.remove(listener)
        except Exception:
            pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __read_task(self):
        for listener in self.__update_listeners:
            listener.call_update()

        try:
            if self.__path.exists():
                json_text = self.__path.read_text(encoding="utf-8")

                config = Config.from_json(json_text)

                self.__migration_manager.try_migrate(config)

                self.config = config

                self.__last_hash = hash(json_text)
        except Exception:
            _logger.warning("Failed to load config", exc_info=True, stack_info=True)

        self.__write_task()

    def __write_task(self):
        try:
            self.__path.parent.mkdir(parents=True, exist_ok=True)
        except Exception:
            _logger.info("Failed to create config directory", exc_info=True, stack_info=True)

        try:
            json_text = self.config.to_json(indent=2)

            if hash(json_text) == self.__last_hash:
                _logger.info("Config did not change")
                return

            self.__path.write_text(json_text, encoding="utf-8")

            self.__last_hash = hash(json_text)

            count = 0
            for listener in self.__update_listeners:
                if listener.call_update():
                    count += 1

            _logger.info(f"Config saved, {count} listeners called")
        except Exception:
            _logger.warning("Failed to write config", exc_info=True, stack_info=True)

    def __hard_reset_task(self):
        try:
            self.__path.unlink()
        except Exception:
            _logger.warning("Failed to hard delete config", exc_info=True, stack_info=True)

        self.config = Config()
        self.__read_task()
