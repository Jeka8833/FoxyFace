from dataclasses import dataclass

from numpy import ndarray


@dataclass(slots=True)
class MediaPipeProcessingOptions:
    center_point_matrix: ndarray | None = None
