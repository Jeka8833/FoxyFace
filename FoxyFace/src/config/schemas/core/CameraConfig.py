from dataclasses import dataclass


@dataclass
class CameraConfig:
    width: int = 640
    height: int = 480
    camera_id: int = 0
    mirror_x: bool = False
    mirror_y: bool = False
    rotate_ninety: bool = False
