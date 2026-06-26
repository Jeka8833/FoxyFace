import json
import logging

from PySide6.QtCore import QTimer, Qt
from PySide6.QtWebEngineWidgets import QWebEngineView
from blendshape_router.graph.Node import Node
from blendshape_router.graph.util.FunctionEval import FunctionEval
from blendshape_router.preset.ARKitParameter import ARKitParameter
from blendshape_router.preset.BaseParameter import BaseParameter
from blendshape_router.router.GraphContainer import GraphContainer
from blendshape_router.solver.graph.SolverNode import SolverNode
from scipy.spatial.transform import Rotation

from AppConstants import AppConstants
from src.stream.senders.AvatarEndpoint import AvatarEndpoint
from src.ui.FoxyWindow import FoxyWindow

_logger = logging.getLogger(__name__)


class GraphPreviewWindow(FoxyWindow):
    def __init__(self, endpoint: AvatarEndpoint, title: str = "Graph Preview Window", width: int = 640,
                 height: int = 480):
        super().__init__()

        self.__endpoint = endpoint

        self.setWindowTitle(title)
        self.resize(width, height)

        html = (AppConstants.get_application_root() / "Assets" / "GraphPreview.html").read_text(encoding="utf-8")

        self.__web_view = QWebEngineView()
        self.__web_view.setHtml(html)
        self.setCentralWidget(self.__web_view)

        self.__timer: QTimer = QTimer(self, interval=1000, timerType=Qt.TimerType.VeryCoarseTimer)
        self.__timer.timeout.connect(self.__update_thread)
        self.__timer.start()

        self.show()

    def __update_thread(self):
        try:
            graph = self.__graph_to_json(self.__endpoint.graphs(),
                                         self.__endpoint.solver_inputs, self.__endpoint.solver_outputs)

            _logger.info(f"Show the graph: {graph}")

            self.__web_view.page().runJavaScript(f"updateGraph('{graph}')")
        except Exception:
            _logger.warning("Failed to update thread", exc_info=True, stack_info=True)

    def closeEvent(self, event, /) -> None:
        super().closeEvent(event)

        self.__timer.stop()

    @staticmethod
    def __graph_to_json(graphs: dict[str, GraphContainer],
                        solver_inputs: frozenset[SolverNode], solver_outputs: frozenset[Node]):
        out = {}

        for graph_name, graph_container in graphs.items():
            out_for_graph = {}

            for encoder, value in graph_container.harvest_endpoints().items():
                if isinstance(value, dict):
                    for key, val in value.items():
                        name = encoder.id_str() if encoder.id_str() == key else f"{encoder.id_str()}:{key}"

                        out_for_graph[name] = {
                            "value": GraphPreviewWindow.__normalize_value(val),
                            "next_nodes": [next_node.id for next_node in encoder.get_used_nodes()],
                            "type": "Output"
                        }
                else:
                    out_for_graph[encoder.id_str()] = {
                        "value": GraphPreviewWindow.__normalize_value(value),
                        "next_nodes": [next_node.id for next_node in encoder.get_used_nodes()],
                        "type": "Output"
                    }

            for node, function in graph_container.graph.items():
                node_type = "Compute"
                if node in solver_inputs and graph_name == "main":
                    node_type = "Solver Input"
                elif node in solver_outputs and graph_name == "solver":
                    node_type = "Solver Aggregator"
                elif isinstance(node, (BaseParameter | ARKitParameter)):
                    node_type = "Face Input"
                elif isinstance(node, SolverNode):
                    node_type = "Solver Output"

                value = FunctionEval.eval_node(graph_container.graph, node)

                out_for_graph[node.id] = {
                    "min": node.min_value,
                    "max": node.max_value,
                    "default": GraphPreviewWindow.__normalize_value(node.default_value),
                    "value": GraphPreviewWindow.__normalize_value(value),
                    "next_nodes": [next_node.id for next_node in function.get_used_nodes()],
                    "type": node_type
                }

            out[graph_name] = out_for_graph

        return json.dumps(out)

    @staticmethod
    def __normalize_value(value: float | Rotation) -> float | list[float]:
        if isinstance(value, Rotation):
            return value.as_matrix().tolist()

        return value
