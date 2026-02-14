from collections.abc import Iterable
from typing import Protocol

from blendshape_router.facades.foxyface.FoxyFace import FoxyFace
from blendshape_router.facades.ifacialmocap.IFacialMocap import IFacialMocap
from blendshape_router.facades.meowface.MeowFace import MeowFace
from blendshape_router.facades.vrchat.VRChatInstance import VRChatInstance
from blendshape_router.preset.ARKitParameter import ARKitParameter
from blendshape_router.preset.BaseParameter import BaseParameter
from blendshape_router.router.EndpointEncoderInterface import EndpointEncoderInterface
from blendshape_router.solver.graph.SolverNode import SolverNode

from src.stream.core.StreamWriteOnly import StreamWriteOnly
from src.stream.postprocessing.BlendShapesFrame import BlendShapesFrame


class SenderInterface(StreamWriteOnly[BlendShapesFrame[BaseParameter | ARKitParameter]], Protocol):
    def get_endpoints(self) -> frozenset[EndpointEncoderInterface]:
        ...

    def get_solver_inputs(self) -> Iterable[SolverNode]:
        ...

    def get_solver_outputs(self) -> Iterable[SolverNode]:
        ...

    def get_instances(self) -> list[VRChatInstance | IFacialMocap | FoxyFace | MeowFace]:
        ...
