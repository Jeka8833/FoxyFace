from dataclasses import dataclass


@dataclass(slots=True)
class MediaPipeTongueConfig:
    enabled: bool = True

    provider: str | None = None
    device_id: int = 0
    intra_op_num_threads: int = 1
    allow_spinning: bool = False

    padding_x: int = 64
    padding_top: int = 64
    padding_bottom: int = 64

    mincutoff: float = 1.0
    beta: float = 0.001
    dcutoff: float = 1.0
