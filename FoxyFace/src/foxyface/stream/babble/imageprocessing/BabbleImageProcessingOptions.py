import math
from dataclasses import dataclass


@dataclass(slots=True)
class BabbleImageProcessingOptions:
    max_head_rotation_x: float = math.radians(30.0)
    max_head_rotation_y: float = math.radians(50.0)
