import math

from src.stream.core.StreamReadOnly import StreamReadOnly
from src.stream.postprocessing.BlendShapesFrame import BlendShapesFrame
from src.stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum


class ValidateGeneralBlendShapes(StreamReadOnly[BlendShapesFrame[GeneralBlendShapeEnum]]):
    def __init__(self, stream: StreamReadOnly[BlendShapesFrame[GeneralBlendShapeEnum]]):
        self.__stream: StreamReadOnly[BlendShapesFrame[GeneralBlendShapeEnum]] = stream

    def poll(self, timeout: float | None = None) -> BlendShapesFrame[GeneralBlendShapeEnum]:
        frame = self.__stream.poll(timeout)

        blend_shapes = {k: min(k.value.max_value, max(k.value.min_value, v)) for k, v in frame.blend_shapes.items() if
                        isinstance(v, float) and math.isfinite(v)}

        return BlendShapesFrame(blend_shapes, frame.timestamp_ns)
