from dataclasses import dataclass

from scipy.spatial.transform import Rotation


@dataclass(frozen=True, slots=True)
class BlendShapesFrame[T]:
    blend_shapes: dict[T, float | Rotation]
    timestamp_ns: int
