import logging
from typing import Any, Callable

from src.config.ConfigManager import ConfigManager
from src.config.ConfigUpdateListener import ConfigUpdateListener
from src.config.schemas.Config import Config
from src.pipline.MediaPipePipeline import MediaPipePipeline
from src.stream.core.StreamWriteOnly import StreamWriteOnly
from src.stream.core.components.SingleBufferStream import SingleBufferStream
from src.stream.mediapipe.face.core.MediaPipeFrame import MediaPipeFrame
from src.stream.mediapipe.tongue.MediaPipeTongueBlendShapeEnum import MediaPipeTongueBlendShapeEnum
from src.stream.mediapipe.tongue.MediaPipeTongueModel import MediaPipeTongueModel
from src.stream.mediapipe.tongue.MediaPipeTongueStream import MediaPipeTongueStream
from src.stream.mediapipe.tongue.image_processing.MediaPipeTongueImageProcessing import MediaPipeTongueImageProcessing
from src.stream.mediapipe.tongue.image_processing.MediaPipeTonguePreview import MediaPipeTonguePreview
from src.stream.mediapipe.tongue.image_processing.MediaPipeTongueProcessingOptions import \
    MediaPipeTongueProcessingOptions
from src.stream.postprocessing.filter.BlendShapesOneEuroFilter import BlendShapesOneEuroFilter
from src.stream.postprocessing.filter.BlendShapesOneEuroFilterOptions import BlendShapesOneEuroFilterOptions
from src.stream.postprocessing.frames.BlendShapesFrame import BlendShapesFrame

_logger = logging.getLogger(__name__)


class MediaPipeTonguePipeline:
    def __init__(self, config_manager: ConfigManager, media_pipe_pipeline: MediaPipePipeline):
        self.__config_manager: ConfigManager = config_manager
        self.__media_pipe_pipeline: MediaPipePipeline = media_pipe_pipeline

        self.__processing_options = MediaPipeTongueProcessingOptions()
        self.__processing_options_listener: ConfigUpdateListener = self.__register_change_processing_options()

        self.__buffer = SingleBufferStream[MediaPipeFrame]()
        self.__media_pipe_pipeline.register_stream(self.__buffer)

        self.__enabled_listener: ConfigUpdateListener = self.__register_change_enabled()

        self.__babble_loader_options_listener: ConfigUpdateListener = self.__register_change_model_options()

        processed_stream = MediaPipeTongueImageProcessing(self.__buffer, self.__processing_options)
        self.__stream = MediaPipeTongueStream(processed_stream, 1.0)

        self.__filter_processing_options = BlendShapesOneEuroFilterOptions()
        self.__filter_processing_options_listener: ConfigUpdateListener = self.__register_change_filter_processing_options()

        self.__babble_stream = BlendShapesOneEuroFilter[MediaPipeTongueBlendShapeEnum](self.__filter_processing_options)
        self.__stream.register_stream(self.__babble_stream)

        self.__preview_window: MediaPipeTonguePreview | None = None

    def register_stream(self, stream: StreamWriteOnly[BlendShapesFrame[MediaPipeTongueBlendShapeEnum]]) -> None:
        self.__babble_stream.register_stream(stream)

    def unregister_stream(self, stream: StreamWriteOnly[BlendShapesFrame[MediaPipeTongueBlendShapeEnum]]) -> None:
        self.__babble_stream.unregister_stream(stream)

    def trigger_view_preview(self):
        if self.__preview_window is None or self.__preview_window.is_closed():
            self.__preview_window = MediaPipeTonguePreview(self.__media_pipe_pipeline, self.__processing_options)
        else:
            self.__preview_window.close()

    def get_filter_processing_options(self) -> BlendShapesOneEuroFilterOptions:
        return self.__filter_processing_options

    def close(self):
        if self.__preview_window is not None:
            self.__preview_window.close()

        self.__enabled_listener.unregister()
        self.__media_pipe_pipeline.unregister_stream(self.__buffer)
        self.__stream.unregister_stream(self.__babble_stream)

        self.__processing_options_listener.unregister()
        self.__babble_loader_options_listener.unregister()
        self.__filter_processing_options_listener.unregister()

        self.__stream.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __register_change_processing_options(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.media_pipe_tongue.padding_x,
                                                      lambda config: config.media_pipe_tongue.padding_y]

        return self.__config_manager.create_update_listener(self.__update_processing_options, watch_array, True)

    def __update_processing_options(self, config_manager: ConfigManager):
        self.__processing_options.padding_x = config_manager.config.media_pipe_tongue.padding_x
        self.__processing_options.padding_y = config_manager.config.media_pipe_tongue.padding_y

    def __register_change_filter_processing_options(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.media_pipe_tongue.mincutoff,
                                                      lambda config: config.media_pipe_tongue.beta,
                                                      lambda config: config.media_pipe_tongue.dcutoff]

        return self.__config_manager.create_update_listener(self.__update_filter_processing_options, watch_array, True)

    def __update_filter_processing_options(self, config_manager: ConfigManager):
        self.__filter_processing_options.mincutoff = config_manager.config.media_pipe_tongue.mincutoff
        self.__filter_processing_options.beta = config_manager.config.media_pipe_tongue.beta
        self.__filter_processing_options.dcutoff = config_manager.config.media_pipe_tongue.dcutoff

        self.__babble_stream.recreate()

    def __register_change_enabled(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.media_pipe_tongue.enabled]

        return self.__config_manager.create_update_listener(self.__update_enabled, watch_array, True)

    def __update_enabled(self, config_manager: ConfigManager):
        if config_manager.config.media_pipe_tongue.enabled:
            self.__media_pipe_pipeline.register_stream(self.__buffer)
        else:
            self.__media_pipe_pipeline.unregister_stream(self.__buffer)

    def __register_change_model_options(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.media_pipe_tongue.try_use_gpu,
                                                      lambda config: config.media_pipe_tongue.intra_op_num_threads,
                                                      lambda config: config.media_pipe_tongue.allow_spinning,
                                                      lambda config: config.media_pipe_tongue.device_id]

        return self.__config_manager.create_update_listener(self.__update_model_options, watch_array, True)

    def __update_model_options(self, config_manager: ConfigManager):
        try:
            model = MediaPipeTongueModel.load_model(
                config_manager.config.media_pipe_tongue.try_use_gpu,
                config_manager.config.media_pipe_tongue.intra_op_num_threads,
                config_manager.config.media_pipe_tongue.allow_spinning,
                config_manager.config.media_pipe_tongue.device_id
            )

            self.__stream.model = model
        except Exception:
            _logger.warning("Failed to load model", exc_info=True, stack_info=True)
