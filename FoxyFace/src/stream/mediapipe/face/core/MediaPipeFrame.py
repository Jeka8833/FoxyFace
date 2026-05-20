from dataclasses import dataclass

from mediapipe.tasks.python.vision.face_landmarker import FaceLandmarkerResult

from src.stream.postprocessing.frames.ImageFrame import ImageFrame


@dataclass(frozen=True, slots=True)
class MediaPipeFrame:
    camera_frame: ImageFrame
    face_landmarker_result: FaceLandmarkerResult
