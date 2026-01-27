from collections.abc import Callable
from pathlib import Path

from blendshape_router.plugin.endpoints.vrchat.AvatarInfo import AvatarInfo
from blendshape_router.util.ListenerManager import ListenerManager

from config.ConfigManager import ConfigManager
from config.schemas.avatar.AvatarConfig import AvatarConfig
from config.schemas.avatar.AvatarConfigMigrationManager import AvatarConfigMigrationManager


class VRChatAvatarConfigManager:
    def __init__(self, avatar_folder: Path):
        self.avatar_folder = avatar_folder

        self.__config_dict: dict[str, ConfigManager[AvatarConfig]] = {}
        self.__listener_manager: ListenerManager = ListenerManager()

    def avatar_change(self, avatar: str, avatar_info: AvatarInfo):
        comfig_manager = ConfigManager[AvatarConfig](path=self.avatar_folder / f"{avatar_info.avatar_id}.json",
                                                     config_cls=AvatarConfig,
                                                     migration_manager=AvatarConfigMigrationManager())

        comfig_manager.load(wait=True)

        self.__config_dict[avatar] = comfig_manager

        self.__listener_manager.notify()

    def close_connection(self, avatar: str):
        config_manager = self.__config_dict.pop(avatar, None)

        if config_manager is not None:
            config_manager.close()

        self.__listener_manager.notify()

    @property
    def configs(self) -> dict[str, ConfigManager[AvatarConfig]]:
        return self.__config_dict

    def subscribe_change(self, callback: Callable[[], None]):
        self.__listener_manager.subscribe(callback)

    def unsubscribe_change(self, callback: Callable[[], None]):
        self.__listener_manager.unsubscribe(callback)

    def close(self):
        for config_manager in self.__config_dict.values():
            config_manager.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
