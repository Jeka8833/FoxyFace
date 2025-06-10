from threading import Condition, Lock

from src.stream.core.StreamReadOnly import StreamReadOnly
from src.stream.core.StreamWriteOnly import StreamWriteOnly


class SingleBufferStream[T](StreamReadOnly[T], StreamWriteOnly[T]):
    def __init__(self):
        self.__value: T | None = None
        self.__closed: bool = False
        self.__condition: Condition = Condition(Lock())

    def put(self, value: T) -> bool:
        if self.__closed:
            return False

        with self.__condition:
            self.__value = value
            self.__condition.notify()

        return True

    def poll(self, timeout: float | None = None) -> T:
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
