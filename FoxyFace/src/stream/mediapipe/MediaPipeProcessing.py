import logging

import numpy
from numpy import ndarray
from scipy.spatial.transform import Rotation

from src.stream.core.StreamWriteOnly import StreamWriteOnly
from src.stream.mediapipe.MediaPipeBlendShapeEnum import MediaPipeBlendShapeEnum
from src.stream.mediapipe.MediaPipeProcessingOptions import MediaPipeProcessingOptions
from src.stream.mediapipe.core.MediaPipeFrame import MediaPipeFrame
from src.stream.postprocessing.BlendShapesFrame import BlendShapesFrame

_logger = logging.getLogger(__name__)


class MediaPipeProcessing(StreamWriteOnly[MediaPipeFrame]):
    def __init__(self, stream: StreamWriteOnly[BlendShapesFrame[MediaPipeBlendShapeEnum]],
                 options: MediaPipeProcessingOptions):
        self.__stream: StreamWriteOnly[BlendShapesFrame[MediaPipeBlendShapeEnum]] = stream
        self.__options: MediaPipeProcessingOptions = options

    def put(self, value: MediaPipeFrame) -> bool:
        bottom_point = value.face_landmarker_result.face_landmarks[0][152]
        transformation_matrix = value.face_landmarker_result.facial_transformation_matrixes[0]

        output_shapes: dict[MediaPipeBlendShapeEnum, float | Rotation] = {
            MediaPipeBlendShapeEnum.HeadX: float(bottom_point.x),
            MediaPipeBlendShapeEnum.HeadY: float(1.0 - bottom_point.y),
            MediaPipeBlendShapeEnum.HeadZ: float(transformation_matrix[2, 3]),
        }

        rotation = self.__calibrate_rotation(transformation_matrix)

        if rotation is not None:
            output_shapes[MediaPipeBlendShapeEnum.HeadRotation] = rotation

        for shape in value.face_landmarker_result.face_blendshapes[0]:
            if shape.category_name == "_neutral":
                continue

            output_shapes[MediaPipeBlendShapeEnum(shape.category_name)] = shape.score

        result_shapes = BlendShapesFrame(output_shapes, value.camera_frame.timestamp_ns)

        return self.__stream.put(result_shapes)

    def close(self) -> None:
        self.__stream.close()

    def __calibrate_rotation(self, rotation_matrix: ndarray) -> Rotation | None:
        try:
            mirror_matrix = numpy.diag([-1, 1, 1])

            transformed_rotation = mirror_matrix @ (
                    rotation_matrix[0:3, 0:3] @ self.__options.initial_rotation) @ mirror_matrix

            return Rotation.from_matrix(transformed_rotation)
        except Exception:
            _logger.warning("Rotation matrix", exc_info=True, stack_info=True)

            return None
