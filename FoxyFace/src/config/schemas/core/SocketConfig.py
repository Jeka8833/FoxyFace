from dataclasses import dataclass


@dataclass
class SocketConfig:
    ip: str = "localhost"
    port: int = 54321
    udp_read_timeout: int = 5_000
    bypass_other_modules_block: bool = False