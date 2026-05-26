from dataclasses import dataclass


@dataclass(slots=True)
class MediaPipeTongueProcessingOptions:
    padding_x: int = 49
    padding_top: int = 43
    padding_bottom: int = 43