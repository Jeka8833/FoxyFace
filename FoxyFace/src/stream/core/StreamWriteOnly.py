from typing import Protocol


class StreamWriteOnly[T](Protocol):
    def put(self, value: T) -> bool:
        ...

    def close(self) -> None:
        ...
