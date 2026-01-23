from blendshape_router.graph.Node import Node

from stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum


class FoxyFaceToVRChatMapper:
    @staticmethod
    def convert(key: GeneralBlendShapeEnum, value: float) -> tuple[Node, float]:
        pass