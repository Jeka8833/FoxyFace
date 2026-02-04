from dataclasses import dataclass

from src.config.ConfigManager import ConfigManager
from src.config.schemas.avatar.AvatarConfig import AvatarConfig


@dataclass(slots=True)
class FindInstanceItem:
    retry_count: int
    config: ConfigManager[AvatarConfig]
