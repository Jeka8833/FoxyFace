import logging
from collections.abc import Iterable
from pathlib import Path

import msgspec
from blendshape_router.graph.Node import Node
from blendshape_router.solver.graph.SolverNode import SolverNode
from blendshape_router.solver.model.loader.ModelLoader import ModelLoader

from stream.senders.config.AvatarConfig import AvatarConfig

_logger = logging.getLogger(__name__)


class AvatarConfigLoader:

    def __init__(self, file: Path, model: ModelLoader, output_nodes: Iterable[Node]):
        self.__config: AvatarConfig = msgspec.json.decode(file.read_text("utf-8"), type=AvatarConfig)
        self.__solver_nodes: dict[str, SolverNode] = {key.id: key for key in model.get_blendshapes().keys()}
        self.__global_output_nodes: dict[str, Node] = {key.id: key for key in output_nodes}

    def get_disable_solver_input_nodes(self) -> set[SolverNode]:
        out: set[SolverNode] = set[SolverNode]()

        for node_name in self.__config.disable_solver_input_nodes:
            try:
                out.add(self.__solver_nodes[node_name])
            except Exception:
                _logger.warning(f"Failed to find solver node {node_name} for disabled solver input")

        return out

    def get_disable_solver_output_nodes(self) -> set[SolverNode]:
        out: set[SolverNode] = set[SolverNode]()

        for node_name in self.__config.disable_solver_output_nodes:
            try:
                out.add(self.__solver_nodes[node_name])
            except Exception:
                _logger.warning(f"Failed to find solver node {node_name} for disabled solver output")

        return out

    def get_disable_global_output_nodes(self) -> set[Node]:
        out: set[Node] = set[Node]()

        for node_name in self.__config.disable_global_output_nodes:
            try:
                out.add(self.__global_output_nodes[node_name])
            except Exception:
                _logger.warning(f"Failed to find global output node {node_name} for disabled global output")

        return out
