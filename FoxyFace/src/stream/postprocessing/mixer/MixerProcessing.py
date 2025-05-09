from typing import Any

from src.stream.core.StreamReadOnly import StreamReadOnly
from src.stream.core.components.BufferStream import BufferStream
from src.stream.postprocessing.BlendShapesFrame import BlendShapesFrame
from src.stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum
from src.stream.postprocessing.mixer.MixSelectEnum import MixSelectEnum
from src.stream.postprocessing.mixer.MixerProcessingOptions import MixerProcessingOptions


class MixerProcessing(StreamReadOnly[BlendShapesFrame[GeneralBlendShapeEnum]]):
    def __init__(self, stream: BufferStream[BlendShapesFrame[Any]], options: MixerProcessingOptions):
        self.__stream: BufferStream[BlendShapesFrame[Any]] = stream
        self.__options: MixerProcessingOptions = options

    def poll(self, timeout: float | None = None) -> BlendShapesFrame[GeneralBlendShapeEnum]:
        output = {}

        enabled = self.__options.get_enabled()

        frame = self.__stream.flush(timeout)

        last_timestamp = frame[-1].timestamp_ns
        for packet in frame:
            for enumEntry in GeneralBlendShapeEnum:
                enable_state = enabled.get(enumEntry)
                if enable_state is None:
                    value = packet.blend_shapes.get(enumEntry.value.same_as[0])
                    if value is not None:
                        output[enumEntry] = value
                        last_timestamp = packet.timestamp_ns
                elif enable_state == MixSelectEnum.Disabled:
                    continue
                else:
                    for same_as in enumEntry.value.same_as:
                        if isinstance(same_as, enable_state.value):
                            value = packet.blend_shapes.get(same_as)
                            if value is not None:
                                output[enumEntry] = value
                                last_timestamp = packet.timestamp_ns
                            break

        return BlendShapesFrame(output, last_timestamp)
