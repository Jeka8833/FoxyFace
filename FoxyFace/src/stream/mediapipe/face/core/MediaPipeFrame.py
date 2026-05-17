from dataclasses import dataclass

from mediapipe.tasks.python.vision.face_landmarker import FaceLandmarkerResult

from src.stream.camera.CameraFrame import CameraFrame


@dataclass(frozen=True, slots=True)
class MediaPipeFrame:
    camera_frame: CameraFrame
    face_landmarker_result: FaceLandmarkerResult
