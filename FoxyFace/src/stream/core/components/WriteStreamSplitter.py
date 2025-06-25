import logging
from threading import Lock

from src.stream.core.StreamWriteOnly import StreamWriteOnly

_logger = logging.getLogger(__name__)


class WriteStreamSplitter[T](StreamWriteOnly[T]):
    """
    A thread-safe component that splits its input to multiple output streams.

    This class receives values via its `put` method and forwards them to all
    registered child streams. It automatically handles the lifecycle of child
    streams, removing them if they are closed.
    """

    def __init__(self):
        self.__streams: set[StreamWriteOnly[T]] | None = set[StreamWriteOnly[T]]()
        self.__lock: Lock = Lock()

    def put(self, value: T) -> bool:
        """
        Puts a value into all registered streams.

        Removes any stream that is closed.

        Raises:
            InterruptedError if the splitter is closed.

        Returns:
            True if the value was successfully sent to at least one stream,
            False otherwise.
        """

        streams_to_remove: set[StreamWriteOnly[T]] = set[StreamWriteOnly[T]]()
        not_closed = False

        with self.__lock:
            if self.__streams is None:
                raise InterruptedError()

            for stream in self.__streams:
                try:
                    if stream.put(value):
                        not_closed = True
                    else:
                        streams_to_remove.add(stream)
                except Exception:
                    _logger.warning("Failed to write to child stream", exc_info=True, stack_info=True)

            self.__streams.difference_update(streams_to_remove)

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
                self.__streams.discard(stream)

    def close(self) -> None:
        with self.__lock:
            if self.__streams is None:
                return

            streams = self.__streams
            self.__streams = None

        for stream in streams:
            try:
                stream.close()
            except Exception:
                _logger.warning("Failed to close child stream", exc_info=True, stack_info=True)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()
