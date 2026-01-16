from dataclasses import dataclass


@dataclass(slots=True)
class BabbleConfig:
    enabled: bool = True

    model_path: str = ""

    try_use_gpu: bool = True
    device_id: int = 0
    intra_op_num_threads: int = 1
    allow_spinning: bool = False

    max_head_rotation_x: float = 30
    max_head_rotation_y: float = 50

    mincutoff: float = 0.9
    beta: float = 0.9
    dcutoff: float = 1.0
