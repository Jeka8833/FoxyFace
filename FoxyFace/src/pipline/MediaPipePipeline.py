import logging
from typing import Any, Callable

from scipy.spatial.transform import Rotation

from AppConstants import AppConstants
from src.config.ConfigManager import ConfigManager
from src.config.ConfigUpdateListener import ConfigUpdateListener
from src.config.schemas.Config import Config
from src.pipline.CameraPipeline import CameraPipeline
from src.stream.camera.CameraFrame import CameraFrame
from src.stream.camera.CameraProcessing import CameraProcessing
from src.stream.core.StreamWriteOnly import StreamWriteOnly
from src.stream.core.components.SingleBufferStream import SingleBufferStream
from src.stream.core.components.WriteCpsCounter import WriteCpsCounter
from src.stream.mediapipe.MediaPipeProcessingOptions import MediaPipeProcessingOptions
from src.stream.mediapipe.core.MediaPipeFrame import MediaPipeFrame
from src.stream.mediapipe.core.MediaPipePreview import MediaPipePreview
from src.stream.mediapipe.core.MediaPipeStream import MediaPipeStream
from src.stream.ui.BlendShapesFrameLatency import BlendShapesFrameLatency

_logger = logging.getLogger(__name__)


class MediaPipePipeline:
    def __init__(self, config_manager: ConfigManager, camera_pipeline: CameraPipeline):
        self.__config_manager = config_manager
        self.__camera_pipeline = camera_pipeline

        self.__buffer = SingleBufferStream[CameraFrame]()
        self.__camera_pipeline.register_stream(self.__buffer)
        processed_stream = CameraProcessing(self.__buffer, self.__camera_pipeline.get_processing_options())

        self.__stream: MediaPipeStream = MediaPipeStream(processed_stream, MediaPipePipeline.__read_media_pipe_model(),
                                                         min_face_detection_confidence=self.__config_manager.config.media_pipe.min_face_detection_confidence,
                                                         min_face_presence_confidence=self.__config_manager.config.media_pipe.min_face_presence_confidence,
                                                         min_tracking_confidence=self.__config_manager.config.media_pipe.min_tracking_confidence,
                                                         frame_lost_timeout=self.__config_manager.config.media_pipe.frame_lost_timeout,
                                                         try_use_gpu=self.__config_manager.config.media_pipe.try_use_gpu)

        self.__processing_options = MediaPipeProcessingOptions()
        self.__processing_options_listener: ConfigUpdateListener = self.__register_change_processing_options()
        self.__fps_limit_listener: ConfigUpdateListener = self.__register_change_fps_limit()

        self.__fps_counter = WriteCpsCounter()
        self.__stream.register_stream(self.__fps_counter)

        self.__latency_counter = BlendShapesFrameLatency()
        self.__stream.register_stream(self.__latency_counter)

        self.__preview_window: MediaPipePreview | None = None

    def register_stream(self, stream: StreamWriteOnly[MediaPipeFrame]) -> None:
        self.__stream.register_stream(stream)

    def unregister_stream(self, stream: StreamWriteOnly[MediaPipeFrame]) -> None:
        self.__stream.unregister_stream(stream)

    def trigger_view_preview(self):
        if self.__preview_window is None or self.__preview_window.is_closed():
            self.__preview_window = MediaPipePreview(self.__stream)
        else:
            self.__preview_window.close()

    def get_processing_options(self) -> MediaPipeProcessingOptions:
        return self.__processing_options

    def get_fps(self):
        return self.__fps_counter.get_cps()

    def get_latency(self):
        return self.__latency_counter.get_latency()

    def close(self):
        if self.__preview_window is not None:
            self.__preview_window.close()

        self.__camera_pipeline.unregister_stream(self.__buffer)

        self.__stream.unregister_stream(self.__fps_counter)
        self.__stream.unregister_stream(self.__latency_counter)

        self.__fps_limit_listener.unregister()
        self.__processing_options_listener.unregister()

        self.__stream.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __register_change_processing_options(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.media_pipe.head_rotation_transformation]

        return self.__config_manager.create_update_listener(self.__update_processing_options, watch_array, True)

    def __update_processing_options(self, config_manager: ConfigManager):
        try:
            matrix = config_manager.config.media_pipe.head_rotation_transformation

            # noinspection PyArgumentList
            Rotation.from_matrix(matrix)  # Crash if matrix is not valid

            self.__processing_options.initial_rotation = matrix
        except Exception:
            _logger.warning("Failed to update post processing options", exc_info=True, stack_info=True)

    def __register_change_fps_limit(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.media_pipe.enable_fps_limit,
                                                      lambda config: config.media_pipe.fps_limit]

        return self.__config_manager.create_update_listener(self.__update_fps_limit, watch_array, True)

    def __update_fps_limit(self, config_manager: ConfigManager):
        if config_manager.config.media_pipe.enable_fps_limit:
            self.__stream.set_fps_limit(config_manager.config.media_pipe.fps_limit)
        else:
            self.__stream.set_fps_limit(None)

    @staticmethod
    def __read_media_pipe_model() -> bytes:
        return (AppConstants.get_application_root() / 'Assets' / 'face_landmarker.task').read_bytes()
