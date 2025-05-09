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
    def __init__(self, stream: StreamWriteOnly[BlendShapesFrame[MediaPipeBlendShapeEnum]], options: MediaPipeProcessingOptions):
        self.__stream: StreamWriteOnly[BlendShapesFrame[MediaPipeBlendShapeEnum]] = stream
        self.__options: MediaPipeProcessingOptions = options

    def put(self, value: MediaPipeFrame) -> bool:
        bottom_point = value.face_landmarker_result.face_landmarks[0][152]

        shapes = {MediaPipeBlendShapeEnum.HeadX: bottom_point.x, MediaPipeBlendShapeEnum.HeadY: 1.0 - bottom_point.y,
                  MediaPipeBlendShapeEnum.HeadZ: value.face_landmarker_result.facial_transformation_matrixes[0][2, 3],
                  MediaPipeBlendShapeEnum.EyeXLeft: 0.0, MediaPipeBlendShapeEnum.EyeXRight: 0.0,
                  MediaPipeBlendShapeEnum.EyeYLeft: 0.0, MediaPipeBlendShapeEnum.EyeYRight: 0.0}

        rotation = self.__rotation_matrix_to_euler_zxy(value.face_landmarker_result.facial_transformation_matrixes[0])
        if rotation is not None:
            shapes[MediaPipeBlendShapeEnum.HeadPitch] = rotation[1] / (math.pi / 2.0)
            shapes[MediaPipeBlendShapeEnum.HeadYaw] = rotation[2] / (math.pi / 2.0)
            shapes[MediaPipeBlendShapeEnum.HeadRoll] = rotation[0] / (math.pi / 2.0)

        for shape in value.face_landmarker_result.face_blendshapes[0]:
            match shape.category_name:
                case "_neutral":
                    pass
                case "eyeLookInLeft":
                    shapes[MediaPipeBlendShapeEnum.EyeXRight] += shape.score
                case "eyeLookOutLeft":
                    shapes[MediaPipeBlendShapeEnum.EyeXRight] -= shape.score
                case "eyeLookInRight":
                    shapes[MediaPipeBlendShapeEnum.EyeXLeft] += shape.score
                case "eyeLookOutRight":
                    shapes[MediaPipeBlendShapeEnum.EyeXLeft] -= shape.score
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

    def __rotation_matrix_to_euler_zxy(self, rotation_matrix: ndarray):
        try:
            if self.__options.center_point_matrix is None:
                centered_matrix = rotation_matrix[0:3, 0:3]
            else:
                centered_matrix = numpy.dot(self.__options.center_point_matrix, rotation_matrix[0:3, 0:3])

            # https://docs.unity3d.com/ScriptReference/Quaternion-eulerAngles.html
            # Method has slight error compared with Wolfram Mathematica, and it doesn't look like a rounding error.
            # Scipy coordinates doesn't match Unity!
            return Rotation.from_matrix(centered_matrix).as_euler('zxy', degrees=False)
        except Exception:
            _logger.warning("Rotation matrix", exc_info=True, stack_info=True)

            return None
