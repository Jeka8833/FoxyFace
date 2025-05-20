from src.stream.core.StreamReadOnly import StreamReadOnly
from src.stream.core.components.SingleBufferStream import SingleBufferStream


class SingleReadStreamSplitter[T](StreamReadOnly[T]):
    def __init__(self, stream: StreamReadOnly[T]):
        self.__stream: StreamReadOnly[T] = stream
        self.__single_buffer_stream: SingleBufferStream[T] = SingleBufferStream[T]()

    def get_slave_stream(self) -> StreamReadOnly[T]:
        return self.__single_buffer_stream

    def poll(self, timeout: float | None = None) -> T:
        if timeout is not None and timeout <= 0.0:
            raise TimeoutError()

        value = self.__stream.poll(timeout)
        self.__single_buffer_stream.put(value)

        return value

    def close(self):
        self.__single_buffer_stream.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
