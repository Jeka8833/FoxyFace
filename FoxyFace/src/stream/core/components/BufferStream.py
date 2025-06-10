from collections import deque
from threading import Condition, Lock

from src.stream.core.StreamReadOnly import StreamReadOnly
from src.stream.core.StreamWriteOnly import StreamWriteOnly


class BufferStream[T](StreamReadOnly[T], StreamWriteOnly[T]):
    def __init__(self, max_len: int | None = None):
        self.__values: deque[T] = deque(maxlen=max_len)
        self.__closed: bool = False
        self.__condition: Condition = Condition(Lock())

    def put(self, value: T) -> bool:
        if self.__closed:
            return False

        with self.__condition:
            self.__values.append(value)
            self.__condition.notify()

        return True

    def poll(self, timeout: float | None = None) -> T:
        if timeout is not None and timeout <= 0.0:
            raise TimeoutError()

        with self.__condition:
            while not self.__values and not self.__closed:
                if not self.__condition.wait(timeout):
                    raise TimeoutError()

            if self.__closed:
                raise InterruptedError()

            return self.__values.popleft()

    def flush(self, timeout: float | None = None) -> list[T]:
        with self.__condition:
            while not self.__values and not self.__closed:
                if not self.__condition.wait(timeout):
                    raise TimeoutError()

            if self.__closed:
                raise InterruptedError()

            values = list(self.__values)
            self.__values.clear()
        return values

    def close(self) -> None:
        self.__closed = True

        with self.__condition:
            self.__values.clear()
            self.__condition.notify_all()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()
