import math
from typing import Any, Callable

from src.config.ConfigManager import ConfigManager
from src.config.ConfigUpdateListener import ConfigUpdateListener
from src.config.schemas.Config import Config
from src.pipline.MediaPipePipeline import MediaPipePipeline
from src.stream.babble.BabbleBlendShapeEnum import BabbleBlendShapeEnum
from src.stream.babble.BabbleModelLoader import BabbleModelLoader
from src.stream.babble.BabbleStream import BabbleStream
from src.stream.babble.imageprocessing.BabbleImageProcessing import BabbleImageProcessing
from src.stream.babble.imageprocessing.BabbleImageProcessingOptions import BabbleImageProcessingOptions
from src.stream.babble.imageprocessing.BabblePreview import BabblePreview
from src.stream.core.StreamWriteOnly import StreamWriteOnly
from src.stream.core.components.SingleBufferStream import SingleBufferStream
from src.stream.core.components.WriteCpsCounter import WriteCpsCounter
from src.stream.mediapipe.core.MediaPipeFrame import MediaPipeFrame
from src.stream.postprocessing.BlendShapesFrame import BlendShapesFrame
from src.stream.postprocessing.filter.BlendShapesOneEuroFilterOptions import BlendShapesOneEuroFilterOptions
from src.stream.ui.BlendShapesFrameLatency import BlendShapesFrameLatency


class BabblePipeline:
    def __init__(self, config_manager: ConfigManager, media_pipe_pipeline: MediaPipePipeline):
        self.__config_manager: ConfigManager = config_manager
        self.__media_pipe_pipeline: MediaPipePipeline = media_pipe_pipeline

        self.__processing_options = BabbleImageProcessingOptions()
        self.__processing_options_listener: ConfigUpdateListener = self.__register_change_processing_options()

        self.__buffer = SingleBufferStream[MediaPipeFrame]()
        self.__media_pipe_pipeline.register_stream(self.__buffer)

        self.__enabled_listener: ConfigUpdateListener = self.__register_change_enabled()

        self.__babble_loader = BabbleModelLoader()
        self.__babble_loader_options_listener: ConfigUpdateListener = self.__register_change_babble_loader_options()

        processed_stream = BabbleImageProcessing(self.__buffer, self.__processing_options, self.__babble_loader)
        self.__stream = BabbleStream(processed_stream, 1.0, self.__babble_loader)

        self.__filter_processing_options = BlendShapesOneEuroFilterOptions()
        self.__filter_processing_options_listener: ConfigUpdateListener = self.__register_change_filter_processing_options()

        self.__fps_counter = WriteCpsCounter()
        self.__stream.register_stream(self.__fps_counter)

        self.__latency_counter = BlendShapesFrameLatency()
        self.__stream.register_stream(self.__latency_counter)

        self.__preview_window: BabblePreview | None = None

    def register_stream(self, stream: StreamWriteOnly[BlendShapesFrame[BabbleBlendShapeEnum]]) -> None:
        self.__stream.register_stream(stream)

    def unregister_stream(self, stream: StreamWriteOnly[BlendShapesFrame[BabbleBlendShapeEnum]]) -> None:
        self.__stream.unregister_stream(stream)

    def trigger_view_preview(self):
        if self.__preview_window is None or self.__preview_window.is_closed():
            self.__preview_window = BabblePreview(self.__media_pipe_pipeline, self.__processing_options,
                                                  self.__babble_loader)
        else:
            self.__preview_window.close()

    def get_filter_processing_options(self) -> BlendShapesOneEuroFilterOptions:
        return self.__filter_processing_options

    def get_fps(self):
        return self.__fps_counter.get_cps()

    def get_latency(self):
        return self.__latency_counter.get_latency()

    def get_model_loader(self) -> BabbleModelLoader:
        return self.__babble_loader

    def close(self):
        if self.__preview_window is not None:
            self.__preview_window.close()

        self.__enabled_listener.unregister()
        self.__media_pipe_pipeline.unregister_stream(self.__buffer)

        self.__stream.unregister_stream(self.__fps_counter)
        self.__stream.unregister_stream(self.__latency_counter)

        self.__processing_options_listener.unregister()
        self.__babble_loader_options_listener.unregister()
        self.__filter_processing_options_listener.unregister()

        self.__stream.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __register_change_processing_options(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.babble.max_head_rotation_x,
                                                      lambda config: config.babble.max_head_rotation_y]

        return self.__config_manager.create_update_listener(self.__update_processing_options, watch_array, True)

    def __update_processing_options(self, config_manager: ConfigManager):
        self.__processing_options.max_head_rotation_x = math.radians(config_manager.config.babble.max_head_rotation_x)
        self.__processing_options.max_head_rotation_y = math.radians(config_manager.config.babble.max_head_rotation_y)

    def __register_change_filter_processing_options(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.babble.mincutoff,
                                                      lambda config: config.babble.beta,
                                                      lambda config: config.babble.dcutoff]

        return self.__config_manager.create_update_listener(self.__update_filter_processing_options, watch_array, True)

    def __update_filter_processing_options(self, config_manager: ConfigManager):
        self.__filter_processing_options.mincutoff = config_manager.config.babble.mincutoff
        self.__filter_processing_options.beta = config_manager.config.babble.beta
        self.__filter_processing_options.dcutoff = config_manager.config.babble.dcutoff

    def __register_change_enabled(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.babble.enabled]

        return self.__config_manager.create_update_listener(self.__update_enabled, watch_array, True)

    def __update_enabled(self, config_manager: ConfigManager):
        if config_manager.config.babble.enabled:
            self.__media_pipe_pipeline.register_stream(self.__buffer)
        else:
            self.__media_pipe_pipeline.unregister_stream(self.__buffer)

    def __register_change_babble_loader_options(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.babble.model_path,
                                                      lambda config: config.babble.try_use_gpu,
                                                      lambda config: config.babble.intra_op_num_threads,
                                                      lambda config: config.babble.allow_spinning]

        return self.__config_manager.create_update_listener(self.__update_babble_loader_options, watch_array, True)

    def __update_babble_loader_options(self, config_manager: ConfigManager):
        self.__babble_loader.start_new_session(config_manager.config.babble.model_path,
                                               config_manager.config.babble.try_use_gpu,
                                               config_manager.config.babble.intra_op_num_threads,
                                               config_manager.config.babble.allow_spinning)
