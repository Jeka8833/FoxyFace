from dataclasses import dataclass

from src.config.schemas.core.enums.TrackingModeEnum import TrackingModeEnum


@dataclass(slots=True)
class SocketConfig:
    ip: str = "localhost"
    port: int = 25747
    auto_connect: bool = True
    udp_read_timeout: int = 2_500
    bypass_other_modules_block: bool = False
    tracking_mode: TrackingModeEnum = TrackingModeEnum.BOTH
