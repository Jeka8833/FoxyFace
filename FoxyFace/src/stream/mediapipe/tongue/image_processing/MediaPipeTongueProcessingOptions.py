from dataclasses import dataclass


@dataclass(slots=True)
class MediaPipeTongueProcessingOptions:
    padding_x: int = 30
    padding_y: int = 30
