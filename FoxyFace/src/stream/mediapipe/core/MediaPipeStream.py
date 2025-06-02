import logging
import time
from threading import Condition, Event, Lock, Thread

import mediapipe
from mediapipe.tasks.python import BaseOptions
from mediapipe.tasks.python.vision.core.vision_task_running_mode import VisionTaskRunningMode
from mediapipe.tasks.python.vision.face_landmarker import FaceLandmarker, FaceLandmarkerOptions, FaceLandmarkerResult

from src.stream.camera.CameraFrame import CameraFrame
from src.stream.core.StreamReadOnly import StreamReadOnly
from src.stream.core.StreamWriteOnly import StreamWriteOnly
from src.stream.core.components.WriteStreamSplitter import WriteStreamSplitter
from src.stream.mediapipe.core.MediaPipeFrame import MediaPipeFrame

_logger = logging.getLogger(__name__)


class MediaPipeStream:
    """
    Unstable when recreated, try to avoid any reinitialization
    """

    def __init__(self, image_stream: StreamReadOnly[CameraFrame], model_asset_data: bytes,
                 frame_timeout: float | None = 1.0, min_face_detection_confidence: float = 0.5,
                 min_face_presence_confidence: float = 0.5, min_tracking_confidence: float = 0.5,
                 frame_lost_timeout: float = 1.0, try_use_gpu: bool = True):
        self.__image_stream: StreamReadOnly[CameraFrame] = image_stream
        self.__frame_timeout: float | None = frame_timeout
        self.__frame_lost_timeout: float = frame_lost_timeout

        self.__landmarker = self.__create_landmarker(model_asset_data, min_face_detection_confidence,
                                                     min_face_presence_confidence, min_tracking_confidence, try_use_gpu)

        self.__close_event = Event()
        self.__condition_lock = Condition(Lock())
        self.__callback_lock = Lock()

        self.__last_frame: CameraFrame | None = None
        self.__last_packet_time_ms: int = time.perf_counter_ns() // 1_000_000
        self.__last_callback_time_ms: int = time.perf_counter_ns() // 1_000_000

        self.__stream_root = WriteStreamSplitter[MediaPipeFrame]()

        self.__fps_limiter_time: int = time.perf_counter_ns()
        self.__fps_limit_ns: int | None = None

        self.__thread = Thread(target=self.__loop, daemon=True, name="MediaPipe Thread")
        self.__thread.start()

    def register_stream(self, stream: StreamWriteOnly[MediaPipeFrame]) -> None:
        self.__stream_root.register_stream(stream)

    def unregister_stream(self, stream: StreamWriteOnly[MediaPipeFrame]) -> None:
        self.__stream_root.unregister_stream(stream)

    def set_fps_limit(self, fps_limit: int | None):
        if fps_limit is None:
            self.__fps_limit_ns = None
        else:
            if fps_limit <= 0:
                raise ValueError("fps_limit must be positive")

            self.__fps_limit_ns = 1_000_000_000 // fps_limit

    def close(self):
        self.__close_event.set()
        self.__stream_root.close()

        with self.__condition_lock:
            self.__condition_lock.notify_all()

        try:
            self.__thread.join(self.__frame_timeout * 2.0)
        except Exception:
            _logger.warning("Failed to join MediaPipe thread", exc_info=True, stack_info=True)

        self.__landmarker.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __loop(self):
        while not self.__close_event.is_set():
            try:
                self.__last_frame = self.__image_stream.poll(self.__frame_timeout)
                packet_time_ms = self.__last_frame.timestamp_ns // 1_000_000

                if self.__last_packet_time_ms - packet_time_ms >= 0:
                    continue  # System lag

                mp_image = mediapipe.Image(image_format=mediapipe.ImageFormat.SRGB, data=self.__last_frame.frame)

                self.__landmarker.detect_async(mp_image, packet_time_ms)

                with self.__condition_lock:  # not ideal back-pressure, we can load more to achieve more FPS, but latency will increase
                    self.__condition_lock.wait(self.__frame_lost_timeout)

                fps_limit = self.__fps_limit_ns
                if fps_limit is not None:
                    target_frame_completion_time_ns = self.__fps_limiter_time + fps_limit
                    current_actual_time_ns = time.perf_counter_ns()
                    sleep_duration_ns = target_frame_completion_time_ns - current_actual_time_ns
                    if sleep_duration_ns > 0:
                        self.__close_event.wait(sleep_duration_ns / 1_000_000_000)
                        self.__fps_limiter_time = target_frame_completion_time_ns
                    else:
                        self.__fps_limiter_time = current_actual_time_ns

                self.__last_packet_time_ms = packet_time_ms
            except TimeoutError:
                continue
            except InterruptedError:
                return
            except Exception:
                _logger.warning("Exception in MediaPipe loop", exc_info=True, stack_info=True)

                self.__close_event.wait(0.001)

    def __async_result(self, result: FaceLandmarkerResult, image, timestamp_ms):
        last_packet = self.__last_frame

        with self.__condition_lock:
            self.__condition_lock.notify()

        if result.face_blendshapes and result.facial_transformation_matrixes and result.face_landmarks:
            try:
                with self.__callback_lock:
                    if self.__last_callback_time_ms - timestamp_ms > 0:
                        return

                    self.__last_callback_time_ms = timestamp_ms

                    self.__stream_root.put(MediaPipeFrame(last_packet, result))
            except InterruptedError:
                return
            except Exception:
                _logger.warning("Exception in MediaPipe callback", exc_info=True, stack_info=True)

    def __create_landmarker(self, model_asset_data: bytes, min_face_detection_confidence: float,
                            min_face_presence_confidence: float, min_tracking_confidence: float,
                            try_use_gpu: bool = True) -> FaceLandmarker:
        if min_face_detection_confidence < 0.0 or min_face_detection_confidence > 1.0:
            raise ValueError("min_face_detection_confidence must be in range [0.0, 1.0]")

        if min_face_presence_confidence < 0.0 or min_face_presence_confidence > 1.0:
            raise ValueError("min_face_presence_confidence must be in range [0.0, 1.0]")

        if min_tracking_confidence < 0.0 or min_tracking_confidence > 1.0:
            raise ValueError("min_tracking_confidence must be in range [0.0, 1.0]")

        try:  # Ubuntu
            if not try_use_gpu:
                raise Exception

            return FaceLandmarker.create_from_options(FaceLandmarkerOptions(
                base_options=BaseOptions(model_asset_buffer=model_asset_data, delegate=BaseOptions.Delegate.GPU),
                running_mode=VisionTaskRunningMode.LIVE_STREAM, num_faces=1,
                min_face_detection_confidence=min_face_detection_confidence,
                min_face_presence_confidence=min_face_presence_confidence,
                min_tracking_confidence=min_tracking_confidence, output_face_blendshapes=True,
                output_facial_transformation_matrixes=True, result_callback=self.__async_result))
        except Exception:
            return FaceLandmarker.create_from_options(
                FaceLandmarkerOptions(base_options=BaseOptions(model_asset_buffer=model_asset_data),
                                      running_mode=VisionTaskRunningMode.LIVE_STREAM, num_faces=1,
                                      min_face_detection_confidence=min_face_detection_confidence,
                                      min_face_presence_confidence=min_face_presence_confidence,
                                      min_tracking_confidence=min_tracking_confidence, output_face_blendshapes=True,
                                      output_facial_transformation_matrixes=True, result_callback=self.__async_result))
