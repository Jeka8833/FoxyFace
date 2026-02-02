from dataclasses import dataclass

from config.ConfigManager import ConfigManager
from config.schemas.avatar.AvatarConfig import AvatarConfig


@dataclass(slots=True)
class FindInstanceItem:
    retry_count: int
    config: ConfigManager[AvatarConfig]