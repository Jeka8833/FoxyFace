import logging
from threading import RLock

from src.stream.core.StreamWriteOnly import StreamWriteOnly

_logger = logging.getLogger(__name__)


class WriteStreamSplitter[T](StreamWriteOnly[T]):
    def __init__(self):
        self.__streams: set[StreamWriteOnly[T]] | None = set[StreamWriteOnly[T]]()
        self.__lock: RLock = RLock()

    def put(self, value: T) -> bool:
        not_closed = False

        with self.__lock:
            if self.__streams is None:
                raise InterruptedError()

            for stream in self.__streams.copy():
                if not stream.put(value):
                    self.unregister_stream(stream)
                else:
                    not_closed = True

        return not_closed

    def register_stream(self, stream: StreamWriteOnly[T]) -> None:
        if self is stream:
            raise ValueError("Cannot register splitter from itself")

        with self.__lock:
            if self.__streams is None:
                raise InterruptedError()

            self.__streams.add(stream)

    def unregister_stream(self, stream: StreamWriteOnly[T]) -> None:
        if self is stream:
            raise ValueError("Cannot unregister splitter from itself")

        with self.__lock:
            if self.__streams is not None:
                try:
                    self.__streams.remove(stream)
                except KeyError:
                    pass

    def close(self) -> None:
        with self.__lock:
            streams = self.__streams
            self.__streams = None

        if streams is not None:
            for stream in streams:
                try:
                    stream.close()
                except Exception:
                    _logger.warning("Failed to close child stream", exc_info=True, stack_info=True)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()
