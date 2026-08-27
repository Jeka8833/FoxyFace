import logging
import math

import numpy
from numpy import ndarray
from scipy.spatial.transform import Rotation

from src.stream.core.StreamWriteOnly import StreamWriteOnly
from src.stream.core.components.WriteStreamSplitter import WriteStreamSplitter
from src.stream.mediapipe.face.MediaPipeBlendshapeEnum import MediaPipeBlendshapeEnum
from src.stream.mediapipe.face.MediaPipeProcessingOptions import MediaPipeProcessingOptions
from src.stream.mediapipe.face.core.MediaPipeFrame import MediaPipeFrame
from src.stream.postprocessing.frames.BlendShapesFrame import BlendShapesFrame

_logger = logging.getLogger(__name__)


class MediaPipeProcessing(StreamWriteOnly[MediaPipeFrame]):
    def __init__(self, options: MediaPipeProcessingOptions):
        self.__options: MediaPipeProcessingOptions = options

        self.__stream_root = WriteStreamSplitter[BlendShapesFrame[MediaPipeBlendshapeEnum]]()

    def put(self, value: MediaPipeFrame) -> None:
        bottom_point = value.face_landmarker_result.face_landmarks[0][152]
        transformation_matrix = value.face_landmarker_result.facial_transformation_matrixes[0]

        shapes = {
            MediaPipeBlendshapeEnum.HeadX: float(bottom_point.x),
            MediaPipeBlendshapeEnum.HeadY: float(1.0 - bottom_point.y),
            MediaPipeBlendshapeEnum.HeadZ: float(transformation_matrix[2, 3]),
            MediaPipeBlendshapeEnum.EyeXLeft: 0.0,
            MediaPipeBlendshapeEnum.EyeXRight: 0.0,
            MediaPipeBlendshapeEnum.EyeYLeft: 0.0,
            MediaPipeBlendshapeEnum.EyeYRight: 0.0
        }

        rotation = self.__transformed_normalized_euler_zxy_rotation(transformation_matrix)

        if rotation is not None:
            shapes[MediaPipeBlendshapeEnum.HeadPitch] = rotation[1]
            shapes[MediaPipeBlendshapeEnum.HeadYaw] = rotation[2]
            shapes[MediaPipeBlendshapeEnum.HeadRoll] = rotation[0]

        for shape in value.face_landmarker_result.face_blendshapes[0]:
            # noinspection PyUnreachableCode
            match shape.category_name:
                case "_neutral":
                    pass
                case "eyeLookInLeft":
                    shapes[MediaPipeBlendshapeEnum.EyeXRight] += shape.score
                case "eyeLookOutLeft":
                    shapes[MediaPipeBlendshapeEnum.EyeXRight] -= shape.score
                case "eyeLookInRight":
                    shapes[MediaPipeBlendshapeEnum.EyeXLeft] -= shape.score
                case "eyeLookOutRight":
                    shapes[MediaPipeBlendshapeEnum.EyeXLeft] += shape.score
                case "eyeLookDownLeft":
                    shapes[MediaPipeBlendshapeEnum.EyeYLeft] -= shape.score
                case "eyeLookUpLeft":
                    shapes[MediaPipeBlendshapeEnum.EyeYLeft] += shape.score
                case "eyeLookDownRight":
                    shapes[MediaPipeBlendshapeEnum.EyeYRight] -= shape.score
                case "eyeLookUpRight":
                    shapes[MediaPipeBlendshapeEnum.EyeYRight] += shape.score
                case _:
                    shapes[MediaPipeBlendshapeEnum(shape.category_name)] = shape.score

        new_value = BlendShapesFrame(shapes, value.camera_frame.timestamp_ns)

        self.__stream_root.put(new_value)

    def register_stream(self, stream: StreamWriteOnly[BlendShapesFrame[MediaPipeBlendshapeEnum]]) -> None:
        self.__stream_root.register_stream(stream)

    def unregister_stream(self, stream: StreamWriteOnly[BlendShapesFrame[MediaPipeBlendshapeEnum]]) -> None:
        self.__stream_root.unregister_stream(stream)

    def close(self) -> None:
        self.__stream_root.close()

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
