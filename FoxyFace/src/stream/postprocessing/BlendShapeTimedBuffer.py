import time

from src.stream.core.StreamReadOnly import StreamReadOnly
from src.stream.postprocessing.BlendShapesFrame import BlendShapesFrame
from src.stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum


class BlendShapeTimedBuffer(StreamReadOnly[BlendShapesFrame[GeneralBlendShapeEnum]]):
    def __init__(self, stream: StreamReadOnly[BlendShapesFrame[GeneralBlendShapeEnum]], ttl: float = 1.0):
        """
        Initializes the buffer.

        Args:
            stream: The underlying stream of BlendShapesFrame objects.
            ttl: The time-to-live in seconds. Blend shape values older than this
                 (based on their source frame's timestamp) will be dropped.
        """
        if ttl < 0.0:
            raise ValueError("ttl cannot be negative")

        self.__stream: StreamReadOnly[BlendShapesFrame[GeneralBlendShapeEnum]] = stream
        self.__ttl_nanos: int = int(ttl * 1_000_000_000)

        self.__cache: dict[GeneralBlendShapeEnum, tuple[float, int]] = dict[GeneralBlendShapeEnum, tuple[float, int]]()

    def poll(self, timeout: float | None = None) -> BlendShapesFrame[GeneralBlendShapeEnum]:
        frame = self.__stream.poll(timeout=timeout)

        for key, value in frame.blend_shapes.items():
            self.__cache[key] = (value, frame.timestamp_ns)

        new_cache: dict[GeneralBlendShapeEnum, tuple[float, int]] = dict[GeneralBlendShapeEnum, tuple[float, int]]()
        new_blendshape: dict[GeneralBlendShapeEnum, float] = dict[GeneralBlendShapeEnum, float]()

        for key, value in self.__cache.items():
            if time.perf_counter_ns() - value[1] <= self.__ttl_nanos:
                new_cache[key] = value
                new_blendshape[key] = value[0]

        self.__cache = new_cache

        return BlendShapesFrame(new_blendshape, frame.timestamp_ns)
