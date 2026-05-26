import time

import cv2
import numpy
import numpy as np
from cv2.typing import MatLike
from scipy.spatial.transform import Rotation

from src.stream.babble.BabbleModelLoader import BabbleModelLoader
from src.stream.babble.imageprocessing.BabbleImageProcessingOptions import BabbleImageProcessingOptions
from src.stream.core.StreamReadOnly import StreamReadOnly
from src.stream.mediapipe.face.core.MediaPipeFrame import MediaPipeFrame
from src.stream.postprocessing.frames.ImageFrame import ImageFrame


class BabbleImageProcessing(StreamReadOnly[ImageFrame]):
    def __init__(self, stream: StreamReadOnly[MediaPipeFrame], options: BabbleImageProcessingOptions,
                 model_loader: BabbleModelLoader):
        self.__stream: StreamReadOnly[MediaPipeFrame] = stream
        self.__options: BabbleImageProcessingOptions = options
        self.__model_loader: BabbleModelLoader = model_loader

    def poll(self, timeout: float | None = None) -> ImageFrame:
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

        img_gray = cv2.cvtColor(mediapipe_frame.camera_frame.image, cv2.COLOR_RGB2GRAY)

        # landmarks = mediapipe_frame.face_landmarker_result.face_landmarks[0]
        #
        # # Получаем параметры модели
        # target_size = (model.input_size_x, model.input_size_y)
        #
        # # Вызываем нашу математически правильную функцию
        # img_gray_cropped = BabbleImageProcessing.crop_and_align_face_full_new(
        #     image=img_gray,
        #     landmarks=landmarks,
        #     target_size=target_size,
        #     paddings=(5, 22, 9)  # Настройте отступы по вкусу (X, Top, Bottom)
        # )
        #
        # return ImageFrame(img_gray_cropped, mediapipe_frame.camera_frame.timestamp_ns)

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

        return ImageFrame(img_gray, mediapipe_frame.camera_frame.timestamp_ns)

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
        if denominator < 0.0000001:
            return point_c, point_c

        signed_numerator = delta_y_ab * point_c[0] - delta_x_ab * point_c[1] + point_b[0] * point_a[1] - point_b[1] * \
                           point_a[0]

        value = (scale_point_c * signed_numerator) / denominator

        side_vector = (delta_y_ab * value, -delta_x_ab * value)

        point_d = (point_a[0] + side_vector[0], point_a[1] + side_vector[1])
        point_e = (point_b[0] + side_vector[0], point_b[1] + side_vector[1])

        return point_d, point_e

    @staticmethod
    def crop_and_align_face_full_new(image: MatLike, landmarks, target_size: tuple[int, int] = (256, 256),
                                     paddings: tuple[int, int, int] = (30, 30, 30)):
        h, w = image.shape[:2]

        lm33, lm263 = landmarks[33], landmarks[263]
        lx, ly = lm33.x * w, lm33.y * h
        rx, ry = lm263.x * w, lm263.y * h

        angle = np.degrees(np.arctan2(ry - ly, rx - lx))
        eye_center = ((lx + rx) * 0.5, (ly + ry) * 0.5)

        m_rot = cv2.getRotationMatrix2D(eye_center, angle, scale=1.0)

        all_pts = np.array([[lm.x * w, lm.y * h] for lm in landmarks])

        rotated_pts = cv2.transform(all_pts.reshape(1, -1, 2), m_rot)[0]

        x_min = np.min(rotated_pts[:, 0])
        x_max = np.max(rotated_pts[:, 0])
        y_max = np.max(rotated_pts[:, 1])
        y_min = eye_center[1]

        pad_x, pad_top, pad_bottom = paddings

        x_min -= pad_x
        x_max += pad_x
        y_min -= pad_top
        y_max += pad_bottom

        tw, th = target_size

        bbox_w = max(x_max - x_min, 1e-5)
        bbox_h = max(y_max - y_min, 1e-5)

        scale_x = tw / bbox_w
        scale_y = th / bbox_h

        m_crop = np.array([
            [scale_x, 0, -x_min * scale_x],
            [0, scale_y, -y_min * scale_y],
            [0, 0, 1]
        ], dtype=np.float64)

        m_rot_3x3 = np.vstack([m_rot, [0, 0, 1]])

        m_final = (m_crop @ m_rot_3x3)[:2, :]

        final_pts = cv2.transform(all_pts.reshape(1, -1, 2), m_final)[0].astype(np.int32)

        hull = cv2.convexHull(final_pts)

        mask = np.zeros((th, tw), dtype=np.uint8)
        cv2.fillConvexPoly(mask, hull, 255)

        face_final = cv2.warpAffine(
            image,
            m_final,
            target_size,
            flags=cv2.INTER_CUBIC,
            borderMode=cv2.BORDER_CONSTANT,
            borderValue=(0, 0, 0)
        )
        # face_final[mask == 0] = 2

        return face_final