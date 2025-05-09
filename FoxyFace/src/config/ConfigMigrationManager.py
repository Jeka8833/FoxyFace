import logging

from packaging.version import Version

from AppConstants import AppConstants
from src.config.schemas.Config import Config

_logger = logging.getLogger(__name__)


class ConfigMigrationManager:
    @staticmethod
    def try_migrate(config: Config):
        try:
            version = Version(config.file_version)

            if version < AppConstants.VERSION:
                config.file_version = str(AppConstants.VERSION)

                ConfigMigrationManager.__migrate(config, version)
        except Exception:
            _logger.warning("Failed to migrate config", exc_info=True, stack_info=True)

    @staticmethod
    def __migrate(config: Config, version: Version):
        # if version < Version("1.0.0.0"):
        #    pass
        pass
