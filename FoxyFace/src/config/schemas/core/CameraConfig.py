from dataclasses import dataclass, field

from src.stream.camera.info.CameraEntry import CameraEntry


@dataclass(slots=True)
class CameraConfig:
    camera_info: CameraEntry = field(default_factory=CameraEntry)
    width: int = 640
    height: int = 480
    mirror_x: bool = False
    mirror_y: bool = False
    rotate_ninety: bool = False
