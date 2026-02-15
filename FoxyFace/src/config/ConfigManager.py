import logging
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Callable, Type

from src.config.AbstractConfig import MigrationManager
from src.config.ConfigUpdateListener import ConfigUpdateListener

_logger = logging.getLogger(__name__)


class ConfigManager[T]:
    def __init__(self, path: Path, config_cls: Type[T], migration_manager: MigrationManager[T] | None = None):
        self.__path: Path = path
        self.__config_cls: Type[T] = config_cls
        self.__migration_manager = migration_manager

        self.__thread_pool = ThreadPoolExecutor(max_workers=1, thread_name_prefix=f"{config_cls.__name__} Manager")
        self.__last_hash: int = 0

        self.config: T = self.__config_cls()

        self.__update_listeners: set[ConfigUpdateListener[T]] = set()

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
            _logger.warning(f"Failed to hard reset config {self.__path}", exc_info=True, stack_info=True)

    def import_file_or_crash(self, file: Path):
        future = self.__thread_pool.submit(self.__import_task, file)
        future.result()

    def export_file(self, file: Path):
        json_text = self.config.to_json(indent=2)

        file.write_text(json_text, encoding="utf-8")

    def close(self):
        self.__thread_pool.shutdown(wait=True, cancel_futures=True)
        self.__write_task()

    def create_update_listener(self, update_callback: Callable[["ConfigManager[T]"], None],
                               watched_elements: list[Callable[[T], Any]] | None = None,
                               call_on_create: bool = False) -> ConfigUpdateListener[T]:
        listener = ConfigUpdateListener(self, update_callback, call_on_create, watched_elements)

        self.__update_listeners.add(listener)

        return listener

    def unregister_update_listener(self, listener: ConfigUpdateListener[T]):
        try:
            self.__update_listeners.remove(listener)
        except Exception:
            pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __read_task(self):
        try:
            if self.__path.exists():
                json_text = self.__path.read_text(encoding="utf-8")

                config = self.__config_cls.from_json(json_text)

                if self.__migration_manager:
                    self.__migration_manager.try_migrate(config)

                self.config = config

                self.__last_hash = hash(json_text)
        except Exception:
            _logger.warning(f"Failed to load config {self.__path}", exc_info=True, stack_info=True)

        self.__write_task()

    def __import_task(self, path: Path):
        json_text = path.read_text(encoding="utf-8")

        config = self.__config_cls.from_json(json_text)

        if self.__migration_manager:
            self.__migration_manager.try_migrate(config)

        self.config = config

        self.__last_hash = hash(json_text)

        self.__write_task()

    def __write_task(self):
        try:
            self.__path.parent.mkdir(parents=True, exist_ok=True)
        except Exception:
            _logger.info("Failed to create config directory", exc_info=True, stack_info=True)

        try:
            json_text = self.config.to_json(indent=2, sort_keys=True)

            if hash(json_text) == self.__last_hash:
                _logger.info(f"Config {self.__path.name} did not change")
                return

            self.__path.write_text(json_text, encoding="utf-8")

            self.__last_hash = hash(json_text)

            count = 0
            for listener in self.__update_listeners:
                if listener.call_update():
                    count += 1

            _logger.info(f"Config {self.__path.name} saved, {count} listeners called")
        except Exception:
            _logger.warning("Failed to write config", exc_info=True, stack_info=True)

    def __hard_reset_task(self):
        try:
            self.__path.unlink()
        except Exception:
            _logger.warning("Failed to hard delete config", exc_info=True, stack_info=True)

        self.config = self.__config_cls()
        self.__read_task()
