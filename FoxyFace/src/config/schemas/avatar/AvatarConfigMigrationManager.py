import logging

from packaging.version import Version

from AppConstants import AppConstants
from src.config.AbstractConfig import MigrationManager
from src.config.schemas.avatar.AvatarConfig import AvatarConfig

_logger = logging.getLogger(__name__)


class AvatarConfigMigrationManager(MigrationManager[AvatarConfig]):

    def try_migrate(self, config: AvatarConfig) -> None:
        try:
            version = Version(config.file_version)

            if version < AppConstants.VERSION:
                config.file_version = str(AppConstants.VERSION)
                self.__migrate(config, version)
        except Exception:
            _logger.warning("Failed to migrate avatar config", exc_info=True, stack_info=True)

    def __migrate(self, config: AvatarConfig, version: Version):
        # if version < Version("1.0.0.0"):
        #    pass
        pass
