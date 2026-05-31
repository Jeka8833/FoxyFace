import cv2
import numpy as np
from cv2.typing import MatLike

from src.stream.core.StreamReadOnly import StreamReadOnly
from src.stream.mediapipe.face.core.MediaPipeFrame import MediaPipeFrame
from src.stream.mediapipe.tongue.MediaPipeTongueModel import MPT_IMAGE_INPUT_SIZE_X, MPT_IMAGE_INPUT_SIZE_Y
from src.stream.mediapipe.tongue.image_processing.MediaPipeTongueProcessingOptions import \
    MediaPipeTongueProcessingOptions
from src.stream.postprocessing.frames.ImageFrame import ImageFrame


class MediaPipeTongueImageProcessing(StreamReadOnly[ImageFrame]):
    def __init__(self, stream: StreamReadOnly[MediaPipeFrame], options: MediaPipeTongueProcessingOptions):
        self.__stream: StreamReadOnly[MediaPipeFrame] = stream
        self.__options: MediaPipeTongueProcessingOptions = options

    def poll(self, timeout: float | None = None) -> ImageFrame:
        mediapipe_frame = self.__stream.poll(timeout)

        return ImageFrame(
            self.crop_and_align_face(
                mediapipe_frame.camera_frame.image,
                mediapipe_frame.face_landmarker_result.face_landmarks[0],
                target_size=(MPT_IMAGE_INPUT_SIZE_X, MPT_IMAGE_INPUT_SIZE_Y),
                paddings=(self.__options.padding_x, self.__options.padding_top, self.__options.padding_bottom),
            ),
            mediapipe_frame.camera_frame.timestamp_ns
        )

    @staticmethod
    def crop_and_align_face(image: MatLike, landmarks, target_size: tuple[int, int] = (256, 256),
                            paddings: tuple[int, int, int] = (30, 30, 30)):
        h, w, _ = image.shape

        lm33 = landmarks[33]
        lm263 = landmarks[263]
        left_eye_x, left_eye_y = lm33.x * w, lm33.y * h
        right_eye_x, right_eye_y = lm263.x * w, lm263.y * h

        angle = np.degrees(np.arctan2(right_eye_y - left_eye_y, right_eye_x - left_eye_x))
        eye_center = ((left_eye_x + right_eye_x) * 0.5, (left_eye_y + right_eye_y) * 0.5)

        m_rot = cv2.getRotationMatrix2D(eye_center, angle, scale=1.0)

        xs = np.array([lm.x for lm in landmarks], dtype=np.float64) * w
        ys = np.array([lm.y for lm in landmarks], dtype=np.float64) * h

        m00, m01, m02 = m_rot[0]
        m10, m11, m12 = m_rot[1]

        rotated_xs = xs * m00 + ys * m01 + m02
        rotated_ys = xs * m10 + ys * m11 + m12

        x_min, x_max = np.min(rotated_xs), np.max(rotated_xs)
        y_min, y_max = np.min(rotated_ys), np.max(rotated_ys)

        pad_x, pad_top, pad_bottom = paddings

        x_min -= pad_x
        y_min -= pad_top
        x_max += pad_x
        y_max += pad_bottom

        assert x_max - x_min >= 1.0 and y_max - y_min >= 1.0

        tw, th = target_size
        scale_x = tw / (x_max - x_min)
        scale_y = th / (y_max - y_min)

        m_final = np.array([
            [m00 * scale_x, m01 * scale_x, (m02 - x_min) * scale_x],
            [m10 * scale_y, m11 * scale_y, (m12 - y_min) * scale_y]
        ], dtype=np.float64)

        face_final = cv2.warpAffine(
            image,
            m_final,
            target_size,
            flags=cv2.INTER_CUBIC,
            borderMode=cv2.BORDER_CONSTANT,
            borderValue=(0, 0, 0)
        )

        return face_final
