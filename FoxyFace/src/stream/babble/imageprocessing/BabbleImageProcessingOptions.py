import math
from dataclasses import dataclass


@dataclass(slots=True)
class BabbleImageProcessingOptions:
    max_head_rotation_x: float = 30 * (math.pi / 180)
    max_head_rotation_y: float = 30 * (math.pi / 180)
