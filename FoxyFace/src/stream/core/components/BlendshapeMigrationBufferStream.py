from enum import Enum
from threading import Condition, Lock

from src.stream.core.StreamReadOnly import StreamReadOnly
from src.stream.core.StreamWriteOnly import StreamWriteOnly
from src.stream.postprocessing.frames.BlendShapesFrame import BlendShapesFrame


class BlendshapeMigrationBufferStream(StreamReadOnly[BlendShapesFrame[Enum]], StreamWriteOnly[BlendShapesFrame[Enum]]):
    def __init__(self):
        self.__value: BlendShapesFrame[Enum] | None = None
        self.__closed: bool = False
        self.__condition: Condition = Condition(Lock())

    def put(self, value: BlendShapesFrame[Enum]) -> None:
        with self.__condition:
            if self.__closed:
                return

            if self.__value is not None:
                new_dict = self.__value.blend_shapes | value.blend_shapes
                self.__value = BlendShapesFrame(new_dict, value.timestamp_ns)
            else:
                self.__value = value

            self.__condition.notify()

    def poll(self, timeout: float | None = None) -> BlendShapesFrame[Enum]:
        if timeout is not None and timeout <= 0.0:
            raise TimeoutError()

        with self.__condition:
            while self.__value is None and not self.__closed:
                if not self.__condition.wait(timeout):
                    raise TimeoutError()

            if self.__closed:
                raise InterruptedError()

            value = self.__value
            self.__value = None

        return value

    def close(self) -> None:
        self.__closed = True

        with self.__condition:
            self.__value = None
            self.__condition.notify_all()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()
