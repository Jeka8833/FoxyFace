from dataclasses import dataclass, field


@dataclass(slots=True)
class AvatarConfig:
    disable_solver_input_nodes: list[str] = field(default_factory=list)
    disable_solver_output_nodes: list[str] = field(default_factory=list)
    disable_global_output_nodes: list[str] = field(default_factory=list)
