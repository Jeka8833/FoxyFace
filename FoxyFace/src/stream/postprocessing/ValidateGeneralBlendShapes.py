from scipy.spatial.transform import Rotation

from src.stream.core.StreamReadOnly import StreamReadOnly
from src.stream.postprocessing.BlendShapesFrame import BlendShapesFrame
from src.stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum


class ValidateGeneralBlendShapes(StreamReadOnly[BlendShapesFrame[GeneralBlendShapeEnum]]):
    def __init__(self, stream: StreamReadOnly[BlendShapesFrame[GeneralBlendShapeEnum]]):
        self.__stream: StreamReadOnly[BlendShapesFrame[GeneralBlendShapeEnum]] = stream

    def poll(self, timeout: float | None = None) -> BlendShapesFrame[GeneralBlendShapeEnum]:
        frame = self.__stream.poll(timeout)

        new_blend_shapes = {}

        for key, value in frame.blend_shapes.items():
            if isinstance(value, float):
                new_blend_shapes[key] = min(key.value.max_value, max(key.value.min_value, value))
            elif isinstance(value, Rotation):
                new_blend_shapes[key] = value
            else:
                assert False, f"Unsupported value type: {type(value)} for key: {key}, value: {value}"

        return BlendShapesFrame(new_blend_shapes, frame.timestamp_ns)
