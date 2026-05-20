from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class BlendShapesFrame[T]:
    blend_shapes: dict[T, float]
    timestamp_ns: int
