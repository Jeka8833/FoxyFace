import logging
import math

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

        shapes = {MediaPipeBlendShapeEnum.HeadX: bottom_point.x, MediaPipeBlendShapeEnum.HeadY: 1.0 - bottom_point.y,
                  MediaPipeBlendShapeEnum.HeadZ: transformation_matrix[2, 3], MediaPipeBlendShapeEnum.EyeXLeft: 0.0,
                  MediaPipeBlendShapeEnum.EyeXRight: 0.0, MediaPipeBlendShapeEnum.EyeYLeft: 0.0,
                  MediaPipeBlendShapeEnum.EyeYRight: 0.0}

        rotation = self.__transformed_normalized_euler_zxy_rotation(transformation_matrix)

        if rotation is not None:
            shapes[MediaPipeBlendShapeEnum.HeadPitch] = rotation[1]
            shapes[MediaPipeBlendShapeEnum.HeadYaw] = rotation[2]
            shapes[MediaPipeBlendShapeEnum.HeadRoll] = rotation[0]

        for shape in value.face_landmarker_result.face_blendshapes[0]:
            # noinspection PyUnreachableCode
            match shape.category_name:
                case "_neutral":
                    pass
                case "eyeLookInLeft":
                    shapes[MediaPipeBlendShapeEnum.EyeXRight] += shape.score
                case "eyeLookOutLeft":
                    shapes[MediaPipeBlendShapeEnum.EyeXRight] -= shape.score
                case "eyeLookInRight":
                    shapes[MediaPipeBlendShapeEnum.EyeXLeft] -= shape.score
                case "eyeLookOutRight":
                    shapes[MediaPipeBlendShapeEnum.EyeXLeft] += shape.score
                case "eyeLookDownLeft":
                    shapes[MediaPipeBlendShapeEnum.EyeYLeft] -= shape.score
                case "eyeLookUpLeft":
                    shapes[MediaPipeBlendShapeEnum.EyeYLeft] += shape.score
                case "eyeLookDownRight":
                    shapes[MediaPipeBlendShapeEnum.EyeYRight] -= shape.score
                case "eyeLookUpRight":
                    shapes[MediaPipeBlendShapeEnum.EyeYRight] += shape.score
                case _:
                    shapes[MediaPipeBlendShapeEnum(shape.category_name)] = shape.score

        new_value = BlendShapesFrame(shapes, value.camera_frame.timestamp_ns)

        return self.__stream.put(new_value)

    def close(self) -> None:
        self.__stream.close()

    # https://docs.unity3d.com/ScriptReference/Quaternion-eulerAngles.html
    # Scipy coordinates order doesn't match Unity!
    def __transformed_normalized_euler_zxy_rotation(self, rotation_matrix: ndarray) -> list[float] | None:
        # noinspection PyBroadException
        try:
            mirror_matrix = numpy.diag([-1, 1, 1])

            transformed_rotation = mirror_matrix @ (
                    rotation_matrix[0:3, 0:3] @ self.__options.initial_rotation) @ mirror_matrix

            # noinspection PyArgumentList
            return Rotation.from_matrix(transformed_rotation).as_euler('zxy', degrees=False) / (math.pi / 2.0)
        except Exception:
            _logger.warning("Rotation matrix", exc_info=True, stack_info=True)

            return None
