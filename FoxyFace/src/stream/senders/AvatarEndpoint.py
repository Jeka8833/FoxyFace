from collections.abc import Callable
from dataclasses import dataclass, field

from blendshape_router.graph.Node import Node
from blendshape_router.router.EndpointEncoderInterface import EndpointEncoderInterface
from blendshape_router.solver.graph.SolverNode import SolverNode

from src.config.ConfigManager import ConfigManager
from src.config.schemas.avatar.AvatarConfig import AvatarConfig


@dataclass(frozen=True, slots=True)
class AvatarEndpoint:
    endpoint_name: str

    config_manager: ConfigManager[AvatarConfig] = field(hash=False, compare=False)

    endpoints: frozenset[EndpointEncoderInterface]
    solver_inputs: frozenset[SolverNode]
    solver_outputs: frozenset[Node]

    test_endpoint_callable: Callable[[EndpointEncoderInterface], None] = field(hash=False, compare=False)
    stop_all_test_endpoint_callable: Callable[[], None] = field(hash=False, compare=False)
