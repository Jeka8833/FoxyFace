import math
import time

import cv2
import numpy
from scipy.spatial.transform import Rotation

from src.stream.babble.BabbleModelLoader import BabbleModelLoader
from src.stream.babble.imageprocessing.BabbleImageFrame import BabbleImageFrame
from src.stream.babble.imageprocessing.BabbleImageProcessingOptions import BabbleImageProcessingOptions
from src.stream.core.StreamReadOnly import StreamReadOnly
from src.stream.mediapipe.core.MediaPipeFrame import MediaPipeFrame


class BabbleImageProcessing(StreamReadOnly[BabbleImageFrame]):
    def __init__(self, stream: StreamReadOnly[MediaPipeFrame], options: BabbleImageProcessingOptions,
                 model_loader: BabbleModelLoader):
        self.__stream: StreamReadOnly[MediaPipeFrame] = stream
        self.__options: BabbleImageProcessingOptions = options
        self.__model_loader: BabbleModelLoader = model_loader

    def poll(self, timeout: float | None = None) -> BabbleImageFrame:
        start_time = time.perf_counter_ns()

        while True:
            if timeout is None or timeout < 0.0:
                mediapipe_frame = self.__stream.poll(timeout)
            else:
                mediapipe_frame = self.__stream.poll(timeout - (time.perf_counter_ns() - start_time) / 1_000_000_000)

            if self.__validate_rotation(mediapipe_frame):
                model = self.__model_loader.model
                if model is not None:
                    break

        img_gray = cv2.cvtColor(mediapipe_frame.camera_frame.frame, cv2.COLOR_RGB2GRAY)
        height, width = img_gray.shape[:2]

        # Center Top
        point_5 = mediapipe_frame.face_landmarker_result.face_landmarks[0][4]  # 195 or 5 or 4
        point_5_x = point_5.x * width
        point_5_y = point_5.y * height

        # Left
        point_234 = mediapipe_frame.face_landmarker_result.face_landmarks[0][234]  # 234 or 93
        point_234_x = point_234.x * width
        point_234_y = point_234.y * height

        # Right
        point_454 = mediapipe_frame.face_landmarker_result.face_landmarks[0][454]  # 454 or 323
        point_454_x = point_454.x * width
        point_454_y = point_454.y * height

        # Center Bottom
        point_152 = mediapipe_frame.face_landmarker_result.face_landmarks[0][152]
        point_152_x = point_152.x * width
        point_152_y = point_152.y * height

        point_a, point_b = BabbleImageProcessing.__calculate_rectangle_points((point_234_x, point_234_y),
                                                                              (point_454_x, point_454_y),
                                                                              (point_5_x, point_5_y), 1.0)

        point_d, point_e = BabbleImageProcessing.__calculate_rectangle_points(point_a, point_b,
                                                                              (point_152_x, point_152_y), 1.0)

        pts1 = numpy.float32(
            [[point_a[0], point_a[1]], [point_b[0], point_b[1]], [point_d[0], point_d[1]], [point_e[0], point_e[1]]])
        pts2 = numpy.float32(
            [[0, 0], [model.input_size_x, 0], [0, model.input_size_y], [model.input_size_x, model.input_size_y]])

        matrix = cv2.getPerspectiveTransform(pts1, pts2)

        img_gray = cv2.warpPerspective(img_gray, matrix, (model.input_size_x, model.input_size_y))

        return BabbleImageFrame(img_gray, mediapipe_frame.camera_frame.timestamp_ns)

    def __validate_rotation(self, frame: MediaPipeFrame):
        rotation_matrix = frame.face_landmarker_result.facial_transformation_matrixes[0][0:3, 0:3]

        # noinspection PyArgumentList
        euler = Rotation.from_matrix(rotation_matrix).as_euler('zyx', degrees=False)

        return abs(euler[1]) <= self.__options.max_head_rotation_x and abs(
            euler[2]) <= self.__options.max_head_rotation_y

    # A-----B
    # |     |
    # |     |
    # D--C--E
    # https://stackoverflow.com/questions/56440433/how-to-get-the-4-coordinates-of-a-rectangle-from-3-coordinates
    @staticmethod
    def __calculate_rectangle_points(point_a: tuple[float, float], point_b: tuple[float, float],
                                     point_c: tuple[float, float], scale_point_c: float = 1.0) -> tuple[
        tuple[float, float], tuple[float, float]]:
        delta_x_ab = point_b[0] - point_a[0]
        delta_y_ab = point_b[1] - point_a[1]

        denominator = (delta_x_ab ** 2) + (delta_y_ab ** 2)
        if math.fabs(denominator) == 0.0:
            return point_c, point_c

        signed_numerator = delta_y_ab * point_c[0] - delta_x_ab * point_c[1] + point_b[0] * point_a[1] - point_b[1] * \
                           point_a[0]

        value = (scale_point_c * signed_numerator) / denominator

        side_vector = (delta_y_ab * value, -delta_x_ab * value)

        point_d = (point_a[0] + side_vector[0], point_a[1] + side_vector[1])
        point_e = (point_b[0] + side_vector[0], point_b[1] + side_vector[1])

        return point_d, point_e
