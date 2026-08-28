from typing import Protocol


class StreamWriteOnly[T](Protocol):
    def put(self, value: T) -> None:
        ...

    def close(self) -> None:
        ...
