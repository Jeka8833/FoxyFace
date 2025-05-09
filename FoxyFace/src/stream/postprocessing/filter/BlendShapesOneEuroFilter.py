from typing import Any

from OneEuroFilter import OneEuroFilter

from src.stream.core.StreamWriteOnly import StreamWriteOnly
from src.stream.postprocessing.BlendShapesFrame import BlendShapesFrame
from src.stream.postprocessing.filter.BlendShapesOneEuroFilterOptions import BlendShapesOneEuroFilterOptions


class BlendShapesOneEuroFilter[T](StreamWriteOnly[BlendShapesFrame[T]]):
    def __init__(self, stream: StreamWriteOnly[BlendShapesFrame[T]], options: BlendShapesOneEuroFilterOptions):
        self.__stream = stream
        self.__options = options

        self.__filter_map: dict[Any, OneEuroFilter] = {}

    def put(self, value: BlendShapesFrame[T]) -> bool:
        blend_shapes = {}
        for k, v in value.blend_shapes.items():
            one_euro_filter = self.__filter_map.setdefault(k, OneEuroFilter(30, self.__options.mincutoff,
                                                                            self.__options.beta,
                                                                            self.__options.dcutoff))

            blend_shapes[k] = one_euro_filter.filter(v, value.timestamp_ns / 1_000_000_000)

        return self.__stream.put(BlendShapesFrame(blend_shapes, value.timestamp_ns))

    def recreate(self):
        self.__filter_map.clear()

    def close(self) -> None:
        self.__stream.close()
