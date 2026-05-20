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
            self.crop_and_align_face_full_new(
                mediapipe_frame.camera_frame.image,
                mediapipe_frame.face_landmarker_result.face_landmarks[0],
                target_size=(MPT_IMAGE_INPUT_SIZE_X, MPT_IMAGE_INPUT_SIZE_Y),
                paddings=(self.__options.padding_x, self.__options.padding_y),
            ),
            mediapipe_frame.camera_frame.timestamp_ns
        )

    @staticmethod
    def crop_and_align_face_full_new(image: MatLike, landmarks, target_size: tuple[int, int] = (256, 256),
                                     paddings: tuple[int, int] = (30, 30)):
        h, w, _ = image.shape

        left_eye = np.array([landmarks[33].x * w, landmarks[33].y * h])
        right_eye = np.array([landmarks[263].x * w, landmarks[263].y * h])

        d_y = right_eye[1] - left_eye[1]
        d_x = right_eye[0] - left_eye[0]
        angle = np.degrees(np.arctan2(d_y, d_x))
        eye_center = ((left_eye[0] + right_eye[0]) / 2.0, (left_eye[1] + right_eye[1]) / 2.0)

        m_rot = cv2.getRotationMatrix2D(eye_center, angle, scale=1.0)

        all_pts = np.array([[lm.x * w, lm.y * h] for lm in landmarks])
        ones = np.ones(shape=(len(all_pts), 1))
        points_ones = np.concatenate((all_pts, ones), axis=1)
        rotated_pts = m_rot.dot(points_ones.T).T

        x_min, y_min = np.min(rotated_pts, axis=0)
        x_max, y_max = np.max(rotated_pts, axis=0)

        pad_x, pad_y = paddings

        x_min -= pad_x
        y_min -= pad_y
        x_max += pad_x
        y_max += pad_y

        bbox_rotated_pts = np.array([
            [x_min, y_min],
            [x_max, y_min],
            [x_min, y_max]
        ], dtype=np.float32)

        m_inv = cv2.invertAffineTransform(m_rot)
        bbox_rotated_ones = np.concatenate((bbox_rotated_pts, np.ones((3, 1))), axis=1)
        src_pts = m_inv.dot(bbox_rotated_ones.T).T.astype(np.float32)

        tw, th = target_size
        dst_pts = np.array([
            [0, 0],
            [tw, 0],
            [0, th]
        ], dtype=np.float32)

        m_final = cv2.getAffineTransform(src_pts, dst_pts)

        face_final = cv2.warpAffine(
            image,
            m_final,
            target_size,
            flags=cv2.INTER_CUBIC,
            borderMode=cv2.BORDER_CONSTANT,
            borderValue=(0, 0, 0)
        )

        return face_final
