from typing import Protocol

from blendshape_router.preset.ARKitParameter import ARKitParameter
from blendshape_router.preset.BaseParameter import BaseParameter

from src.stream.core.StreamWriteOnly import StreamWriteOnly
from src.stream.postprocessing.BlendShapesFrame import BlendShapesFrame
from src.stream.senders.AvatarEndpoint import AvatarEndpoint


class SenderInterface(StreamWriteOnly[BlendShapesFrame[BaseParameter | ARKitParameter]], Protocol):
    def get_endpoints(self) -> frozenset[AvatarEndpoint]:
        ...
