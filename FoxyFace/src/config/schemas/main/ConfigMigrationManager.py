import logging

from packaging.version import Version

from AppConstants import AppConstants
from src.config.AbstractConfig import MigrationManager
from config.schemas.main.Config import Config

_logger = logging.getLogger(__name__)


class MainConfigMigrationManager(MigrationManager[Config]):

    def try_migrate(self, config: Config) -> None:
        try:
            version = Version(config.file_version)

            if version < AppConstants.VERSION:
                config.file_version = str(AppConstants.VERSION)
                self.__migrate(config, version)
        except Exception:
            _logger.warning("Failed to migrate config", exc_info=True, stack_info=True)

    def __migrate(self, config: Config, version: Version):
        # if version < Version("1.0.0.0"):
        #    pass
        pass
