from dataclasses import dataclass

from src.config.schemas.core.enums.TrackingModeEnum import TrackingModeEnum


@dataclass(slots=True)
class VrcftInterfaceOptions:
    udp_read_timeout_ms: int = 5_000
    bypass_other_modules_block: bool = False
    tracking_mode: TrackingModeEnum = TrackingModeEnum.BOTH

    def to_packet_format_dict(self) -> dict[str, int | bool | str]:
        return {"UdpReadTimeoutMs": self.udp_read_timeout_ms,
                "BypassOtherModulesBlock": self.bypass_other_modules_block,
                "TrackingMode": self.tracking_mode.value}
