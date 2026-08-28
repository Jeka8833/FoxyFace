from dataclasses import dataclass


@dataclass(slots=True)
class MediaPipeTongueProcessingOptions:
    padding_x: int = 64
    padding_top: int = 64
    padding_bottom: int = 64
