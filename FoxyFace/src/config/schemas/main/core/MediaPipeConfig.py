from dataclasses import dataclass, field


@dataclass(slots=True)
class MediaPipeConfig:
    head_rotation_transformation: list[list[float]] = field(
        default_factory=lambda: [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])

    enable_fps_limit: bool = False
    fps_limit: int = 25

    try_use_gpu: bool = True
    min_face_detection_confidence: float = 0.5
    min_face_presence_confidence: float = 0.5
    min_tracking_confidence: float = 0.5
    frame_lost_timeout: float = 1.0
