from collections.abc import Callable
from pathlib import Path
from threading import Lock

from blendshape_router.plugin.endpoints.vrchat.AvatarInfo import AvatarInfo
from blendshape_router.plugin.endpoints.vrchat.connection.receive.ConnectionNode import ConnectionNode
from blendshape_router.util.ListenerManager import ListenerManager

from src.config.ConfigManager import ConfigManager
from src.config.schemas.avatar.AvatarConfig import AvatarConfig
from src.config.schemas.avatar.AvatarConfigMigrationManager import AvatarConfigMigrationManager


class VRChatAvatarConfigManager:
    def __init__(self, avatar_folder: Path):
        self.avatar_folder = avatar_folder

        self.__lock: Lock = Lock()
        self.__config_dict: dict[ConnectionNode, ConfigManager[AvatarConfig]] = {}
        self.__listener_manager: ListenerManager = ListenerManager()

    def get_config_or_load(self, connection: ConnectionNode, avatar_info: AvatarInfo):
        with self.__lock:
            config = self.__config_dict.get(connection)

            if config is not None:
                return config

            config_manager = ConfigManager[AvatarConfig](path=self.avatar_folder / f"{avatar_info.avatar_id}.json",
                                                         config_cls=AvatarConfig,
                                                         migration_manager=AvatarConfigMigrationManager())

            config_manager.load(wait=True)

            self.__config_dict[connection] = config_manager

            self.__listener_manager.notify(connection, config_manager, True)

            return config_manager

    def close_connection(self, connection: ConnectionNode):
        with self.__lock:
            config_manager = self.__config_dict.pop(connection, None)

            if config_manager is not None:
                config_manager.close()

                self.__listener_manager.notify(connection, config_manager, False)

    def subscribe_change(self, callback: Callable[[ConnectionNode, ConfigManager, bool], None]):
        self.__listener_manager.subscribe(callback)

    def unsubscribe_change(self, callback: Callable[[ConnectionNode, ConfigManager, bool], None]):
        self.__listener_manager.unsubscribe(callback)

    def close(self):
        for connection in frozenset(self.__config_dict.keys()):
            self.close_connection(connection)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
