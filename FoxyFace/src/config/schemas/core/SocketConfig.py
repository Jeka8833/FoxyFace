from dataclasses import dataclass


@dataclass
class SocketConfig:
    ip: str = "localhost"
    port: int = 54321
    auto_connect: bool = True
    udp_read_timeout: int = 2_500
    bypass_other_modules_block: bool = False
