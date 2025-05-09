from src.stream.core.StreamWriteOnly import StreamWriteOnly


class WriteStreamSplitter[T](StreamWriteOnly[T]):
    def __init__(self):
        self.__streams: set[StreamWriteOnly[T]] | None = set[StreamWriteOnly[T]]()

    def put(self, value: T) -> bool:
        streams = self.__streams

        if streams is None:
            raise InterruptedError()

        not_closed = False

        for stream in streams:
            if not stream.put(value):
                self.unregister_stream(stream)
            else:
                not_closed = True

        return not_closed

    def register_stream(self, stream: StreamWriteOnly[T]) -> None:
        if self is stream:
            raise ValueError()

        streams = self.__streams

        if streams is None:
            raise InterruptedError()

        streams.add(stream)

    def unregister_stream(self, stream: StreamWriteOnly[T]) -> None:
        if self is stream:
            raise ValueError()

        streams = self.__streams

        if streams is not None:
            try:
                streams.remove(stream)
            except KeyError:
                pass

    def close(self) -> None:
        streams = self.__streams
        self.__streams = None

        if streams is not None:
            for stream in streams:
                stream.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()
