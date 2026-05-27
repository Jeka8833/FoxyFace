import logging
from threading import Lock

from src.stream.core.StreamWriteOnly import StreamWriteOnly

_logger = logging.getLogger(__name__)


class WriteStreamSplitter[T](StreamWriteOnly[T]):
    def __init__(self):
        self._streams: set[StreamWriteOnly[T]] | None = set[StreamWriteOnly[T]]()
        self.__lock: Lock = Lock()

    def put(self, value: T) -> None:
        with self.__lock:
            if self._streams is None:
                raise InterruptedError()

            for stream in self._streams:
                try:
                    stream.put(value)
                except Exception:
                    _logger.warning("Failed to write to child stream", exc_info=True, stack_info=True)

    def register_stream(self, stream: StreamWriteOnly[T]) -> None:
        if self is stream:
            raise ValueError("Cannot register splitter from itself")

        with self.__lock:
            if self._streams is None:
                raise InterruptedError()

            self._streams.add(stream)

    def unregister_stream(self, stream: StreamWriteOnly[T]) -> None:
        if self is stream:
            raise ValueError("Cannot unregister splitter from itself")

        with self.__lock:
            if self._streams is not None:
                self._streams.discard(stream)

    def close(self) -> None:
        with self.__lock:
            if self._streams is None:
                return

            streams = self._streams
            self._streams = None

        for stream in streams:
            try:
                stream.close()
            except Exception:
                _logger.warning("Failed to close child stream", exc_info=True, stack_info=True)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()
