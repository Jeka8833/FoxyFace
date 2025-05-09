from dataclasses import dataclass


@dataclass(slots=True)
class VrcftInterfaceOptions:
    udp_read_timeout_ms: int = 5_000
    bypass_other_modules_block: bool = False

    def to_packet_format_dict(self) -> dict[str, int | bool]:
        return {"UdpReadTimeoutMs": self.udp_read_timeout_ms,
                "BypassOtherModulesBlock": self.bypass_other_modules_block}
