from dataclasses import dataclass


@dataclass(slots=True)
class BlendShapeOption:
    neutral_pose: float = 0.0
    max_pose_negative: float = -1.0
    max_pose_positive: float = 1.0
