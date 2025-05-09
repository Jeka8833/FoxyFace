from dataclasses import dataclass, field


@dataclass(slots=True)
class MediaPipeConfig:
    center_point_matrix: list[list[float]] = field(default_factory=list)

    try_use_gpu: bool = True
    min_face_detection_confidence: float = 0.5
    min_face_presence_confidence: float = 0.5
    min_tracking_confidence: float = 0.5
    frame_lost_timeout: float = 1.0
