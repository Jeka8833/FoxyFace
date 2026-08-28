from typing import Protocol


class StreamReadOnly[T](Protocol):
    def poll(self, timeout: float | None = None) -> T:
        ...
