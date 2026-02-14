from dataclasses import dataclass

from blendshape_router.router.EndpointEncoderInterface import EndpointEncoderInterface
from blendshape_router.solver.graph.SolverNode import SolverNode

from src.config.ConfigManager import ConfigManager
from src.config.schemas.avatar.AvatarConfig import AvatarConfig


@dataclass(frozen=True, slots=True)
class AvatarEndpoint:
    endpoint_name: str

    config_manager: ConfigManager[AvatarConfig]

    endpoints: frozenset[EndpointEncoderInterface]
    solver_inputs: frozenset[SolverNode]
    solver_outputs: frozenset[SolverNode]
