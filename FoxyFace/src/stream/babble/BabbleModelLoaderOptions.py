from dataclasses import dataclass


@dataclass(slots=True)
class BabbleModelLoaderOptions:
    model_path : str = ""
    use_gpu: bool = True
    intra_op_num_threads: int = 1
    allow_spinning: bool = False