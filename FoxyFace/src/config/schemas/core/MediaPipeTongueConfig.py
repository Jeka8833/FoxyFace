from dataclasses import dataclass


@dataclass(slots=True)
class MediaPipeTongueConfig:
    enabled: bool = True

    try_use_gpu: bool = True
    device_id: int = 0
    intra_op_num_threads: int = 1
    allow_spinning: bool = False

    padding_x: int = 49
    padding_y: int = 43

    mincutoff: float = 0.9
    beta: float = 0.9
    dcutoff: float = 1.0
