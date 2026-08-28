from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class CameraBackend:
    name: str
    index: int
    input_type: frozenset[type[str | int]]
