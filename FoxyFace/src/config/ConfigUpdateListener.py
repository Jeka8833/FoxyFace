import copy
import logging
from typing import Any, Callable, Generic, TYPE_CHECKING

from src.config.AbstractConfig import T

if TYPE_CHECKING:
    from src.config.ConfigManager import ConfigManager

_logger = logging.getLogger(__name__)


class ConfigUpdateListener(Generic[T]):
    def __init__(self, config_manager: "ConfigManager[T]",
                 update_callback: Callable[["ConfigManager[T]"], None],
                 call_on_create: bool = False,
                 watched_elements: list[Callable[[T], Any]] | None = None):
        self.__config_manager = config_manager
        self.__update_callback = update_callback
        self.__watched_elements = watched_elements

        self.__previous_values: list[Any] = [None] * (len(watched_elements) if watched_elements is not None else 0)
        self.__update_previous_values()

        if call_on_create:
            try:
                self.__update_callback(self.__config_manager)
            except Exception:
                _logger.warning("Failed to call update", exc_info=True, stack_info=True)

    def __update_previous_values(self):
        if self.__watched_elements is None:
            return

        current_config = self.__config_manager.config
        for i, watcher in enumerate(self.__watched_elements):
            self.__previous_values[i] = copy.deepcopy(watcher(current_config))

    def call_update(self) -> bool:
        try:
            if self.__watched_elements is None:
                self.__update_callback(self.__config_manager)
                return True

            current_config = self.__config_manager.config

            for i, watcher in enumerate(self.__watched_elements):
                new_val = watcher(current_config)
                if new_val != self.__previous_values[i]:
                    self.__update_callback(self.__config_manager)
                    self.__update_previous_values()
                    return True

        except Exception:
            _logger.warning("Failed to call update", exc_info=True, stack_info=True)

        return False

    def unregister(self):
        self.__config_manager.unregister_update_listener(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.unregister()
