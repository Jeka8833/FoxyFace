from dataclasses import dataclass, field


@dataclass(slots=True)
class MediaPipeProcessingOptions:
    initial_rotation: list[list[float]] = field(
        default_factory=lambda: [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
