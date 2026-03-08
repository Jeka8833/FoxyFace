from dataclasses import dataclass


@dataclass(slots=True)
class CameraConfig:
    width: int = 640
    height: int = 480
    camera_id: int = 0
    camera_name: str = ""  # Preferred: use camera name instead of ID
    mirror_x: bool = False
    mirror_y: bool = False
    rotate_ninety: bool = False
