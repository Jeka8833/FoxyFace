from dataclasses import dataclass


@dataclass(slots=True)
class CameraProcessingOption:
    mirror_x: bool = False
    mirror_y: bool = False
    rotate_ninety: bool = False
