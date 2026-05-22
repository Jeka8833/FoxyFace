from dataclasses import dataclass


@dataclass(slots=True)
class MediaPipeTongueProcessingOptions:
    padding_x: int = 49
    padding_y: int = 43
