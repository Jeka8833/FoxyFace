from typing import Any, Callable

from src.config.ConfigManager import ConfigManager
from src.config.ConfigUpdateListener import ConfigUpdateListener
from src.config.schemas.Config import Config
from src.pipline.BabblePipeline import BabblePipeline
from src.pipline.MediaPipePipeline import MediaPipePipeline
from src.stream.babble.BabbleBlendShapeEnum import BabbleBlendShapeEnum
from src.stream.core.StreamReadOnly import StreamReadOnly
from src.stream.core.components.BufferStream import BufferStream
from src.stream.core.components.SingleReadStreamSplitter import SingleReadStreamSplitter
from src.stream.mediapipe.MediaPipeBlendShapeEnum import MediaPipeBlendShapeEnum
from src.stream.mediapipe.MediaPipeProcessing import MediaPipeProcessing
from src.stream.postprocessing.BlendShapeTimedBuffer import BlendShapeTimedBuffer
from src.stream.postprocessing.BlendShapesFrame import BlendShapesFrame
from src.stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum
from src.stream.postprocessing.ValidateGeneralBlendShapes import ValidateGeneralBlendShapes
from src.stream.postprocessing.calibration.CalibrateProcessing import CalibrateProcessing
from src.stream.postprocessing.calibration.CalibrateProcessingOptions import CalibrateProcessingOptions
from src.stream.postprocessing.filter.BlendShapesOneEuroFilter import BlendShapesOneEuroFilter
from src.stream.postprocessing.mixer.MixerProcessing import MixerProcessing
from src.stream.postprocessing.mixer.MixerProcessingOptions import MixerProcessingOptions


class ProcessingPipeline:
    def __init__(self, config_manager: ConfigManager, media_pipe_pipeline: MediaPipePipeline,
                 babble_pipeline: BabblePipeline):
        self.__config_manager = config_manager
        self.__media_pipe_pipeline = media_pipe_pipeline
        self.__babble_pipeline = babble_pipeline

        self.__buffer = BufferStream[BlendShapesFrame[MediaPipeBlendShapeEnum | BabbleBlendShapeEnum]](16)

        self.__media_pipe_stream = MediaPipeProcessing(self.__buffer,
                                                       self.__media_pipe_pipeline.get_processing_options())
        self.__media_pipe_pipeline.register_stream(self.__media_pipe_stream)

        self.__babble_stream = BlendShapesOneEuroFilter[BabbleBlendShapeEnum](self.__buffer,
                                                                              self.__babble_pipeline.get_filter_processing_options())
        self.__babble_pipeline.register_stream(self.__babble_stream)

        self.__restart_filter_listener: ConfigUpdateListener = self.__register_restart_filter()

        self.__mixer_options = MixerProcessingOptions()
        self.__mixer_options_listener: ConfigUpdateListener = self.__register_change_mixer_options()

        self.__calibration_options = CalibrateProcessingOptions()
        self.__calibration_options_listener: ConfigUpdateListener = self.__register_change_calibration_options()

        self.__stream_without_calibration_first = SingleReadStreamSplitter(
            MixerProcessing(self.__buffer, self.__mixer_options))

        stream_without_calibration_second = SingleReadStreamSplitter(self.__stream_without_calibration_first)
        self.__stream_without_calibration_cached = BlendShapeTimedBuffer(
            stream_without_calibration_second.get_slave_stream(), ttl=1.0)

        processing_line = CalibrateProcessing(stream_without_calibration_second, self.__calibration_options)
        processing_line = ValidateGeneralBlendShapes(processing_line)
        processing_line = BlendShapeTimedBuffer(processing_line, ttl=1.0)
        self.__stream_with_calibration = SingleReadStreamSplitter(processing_line)

    def get_auto_calibration_stream(self) -> StreamReadOnly[BlendShapesFrame[GeneralBlendShapeEnum]]:
        return self.__stream_without_calibration_first.get_slave_stream()

    def get_udp_stream(self) -> StreamReadOnly[BlendShapesFrame[GeneralBlendShapeEnum]]:
        return self.__stream_with_calibration

    def get_ui_stream_input(self) -> StreamReadOnly[BlendShapesFrame[GeneralBlendShapeEnum]]:
        return self.__stream_without_calibration_cached

    def get_ui_stream_output(self) -> StreamReadOnly[BlendShapesFrame[GeneralBlendShapeEnum]]:
        return self.__stream_with_calibration.get_slave_stream()

    def close(self):
        self.__buffer.close()

        self.__media_pipe_pipeline.unregister_stream(self.__media_pipe_stream)
        self.__babble_pipeline.unregister_stream(self.__babble_stream)

        self.__restart_filter_listener.unregister()
        self.__mixer_options_listener.unregister()
        self.__calibration_options_listener.unregister()

        self.__stream_without_calibration_first.close()
        self.__stream_with_calibration.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __register_restart_filter(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.babble.mincutoff,
                                                      lambda config: config.babble.beta,
                                                      lambda config: config.babble.dcutoff]

        return self.__config_manager.create_update_listener(self.__update_filter, watch_array, False)

    # noinspection PyUnusedLocal
    def __update_filter(self, config_manager: ConfigManager):
        self.__babble_stream.recreate()

    def __register_change_mixer_options(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.processing.source]

        return self.__config_manager.create_update_listener(self.__update_mixer_options, watch_array, True)

    def __update_mixer_options(self, config_manager: ConfigManager):
        self.__mixer_options.enable = {key.to_original(): value.to_original() for key, value in
                                       config_manager.config.processing.source.items()}

    def __register_change_calibration_options(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.processing.calibration]

        return self.__config_manager.create_update_listener(self.__update_calibration_options, watch_array, True)

    def __update_calibration_options(self, config_manager: ConfigManager):
        self.__calibration_options.blend_shape_options = {key.to_original(): value for key, value in
                                                          config_manager.config.processing.calibration.items()}
