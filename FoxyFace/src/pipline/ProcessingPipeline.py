from typing import Any, Callable

from src.config.ConfigManager import ConfigManager
from src.config.ConfigUpdateListener import ConfigUpdateListener
from src.config.schemas.Config import Config
from src.pipline.BabblePipeline import BabblePipeline
from src.pipline.MediaPipePipeline import MediaPipePipeline
from src.pipline.MediaPipeTonguePipeline import MediaPipeTonguePipeline
from src.stream.core.StreamReadOnly import StreamReadOnly
from src.stream.core.components.BlendshapeMigrationBufferStream import BlendshapeMigrationBufferStream
from src.stream.core.components.SingleReadStreamSplitter import SingleReadStreamSplitter
from src.stream.core.components.WriteCpsCounter import WriteCpsCounter
from src.stream.mediapipe.face.MediaPipeProcessing import MediaPipeProcessing
from src.stream.mediapipe.tongue.MediaPipeTongueProcess import Status
from src.stream.postprocessing.BlendShapeTimedBuffer import BlendShapeTimedBuffer
from src.stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum
from src.stream.postprocessing.ValidateGeneralBlendShapes import ValidateGeneralBlendShapes
from src.stream.postprocessing.calibration.CalibrateProcessing import CalibrateProcessing
from src.stream.postprocessing.calibration.CalibrateProcessingOptions import CalibrateProcessingOptions
from src.stream.postprocessing.frames.BlendShapesFrame import BlendShapesFrame
from src.stream.postprocessing.mixer.MixerFilterStream import MixerFilterStream
from src.stream.postprocessing.mixer.MixerRoute import MixerRoute
from src.stream.ui.BlendShapesFrameLatency import BlendShapesFrameLatency


class ProcessingPipeline:
    def __init__(self, config_manager: ConfigManager, media_pipe_pipeline: MediaPipePipeline,
                 media_pipe_tongue_pipeline: MediaPipeTonguePipeline, babble_pipeline: BabblePipeline):
        self.__config_manager = config_manager
        self.__media_pipe_pipeline = media_pipe_pipeline
        self.__media_pipe_tongue_pipeline = media_pipe_tongue_pipeline
        self.__babble_pipeline = babble_pipeline

        self.__buffer = BlendshapeMigrationBufferStream()

        # ==== MediaPipe Block ====
        self.__media_pipe_fps_counter = WriteCpsCounter()
        self.__media_pipe_latency_counter = BlendShapesFrameLatency()
        self.__media_pipe_stream = MediaPipeProcessing(self.__media_pipe_pipeline.get_processing_options())

        self.__media_pipe_pipeline.register_stream(self.__media_pipe_stream)
        self.__media_pipe_stream.register_stream(self.__buffer)
        self.__media_pipe_stream.register_stream(self.__media_pipe_fps_counter)
        self.__media_pipe_stream.register_stream(self.__media_pipe_latency_counter)

        # ==== MediaPipeTongue Block ====
        self.__media_pipe_tongue_fps_counter = WriteCpsCounter()
        self.__media_pipe_tongue_latency_counter = BlendShapesFrameLatency()

        self.__media_pipe_tongue_pipeline.register_stream(self.__buffer)
        self.__media_pipe_tongue_pipeline.register_stream(self.__media_pipe_tongue_fps_counter)
        self.__media_pipe_tongue_pipeline.register_stream(self.__media_pipe_tongue_latency_counter)

        # ==== Babble Block ====
        self.__babble_fps_counter = WriteCpsCounter()
        self.__babble_latency_counter = BlendShapesFrameLatency()

        self.__babble_pipeline.register_stream(self.__buffer)
        self.__babble_pipeline.register_stream(self.__babble_fps_counter)
        self.__babble_pipeline.register_stream(self.__babble_latency_counter)

        # ==== Other Staff Block ====
        self.__mixer = MixerFilterStream(self.__buffer)
        self.__mixer_options_listener: ConfigUpdateListener = self.__register_change_mixer_options()

        self.__calibration_options = CalibrateProcessingOptions()
        self.__calibration_options_listener: ConfigUpdateListener = self.__register_change_calibration_options()

        self.__stream_without_calibration_first = SingleReadStreamSplitter(
            self.__mixer
        )

        self.__stream_without_calibration_second = SingleReadStreamSplitter(self.__stream_without_calibration_first)
        self.__stream_without_calibration_cached = BlendShapeTimedBuffer(
            self.__stream_without_calibration_second.get_slave_stream(),
            ttl=1.0
        )

        processing_line = CalibrateProcessing(self.__stream_without_calibration_second, self.__calibration_options)
        processing_line = ValidateGeneralBlendShapes(processing_line)
        processing_line = BlendShapeTimedBuffer(processing_line, ttl=1.0)
        self.__stream_output = SingleReadStreamSplitter(processing_line)

    @property
    def ui_stream_input(self) -> StreamReadOnly[BlendShapesFrame[GeneralBlendShapeEnum]]:
        return self.__stream_without_calibration_cached

    @property
    def stream_without_calibration(self) -> StreamReadOnly[BlendShapesFrame[GeneralBlendShapeEnum]]:
        return self.__stream_without_calibration_first.get_slave_stream()

    @property
    def stream_output(self) -> StreamReadOnly[BlendShapesFrame[GeneralBlendShapeEnum]]:
        return self.__stream_output

    @property
    def ui_stream_output(self) -> StreamReadOnly[BlendShapesFrame[GeneralBlendShapeEnum]]:
        return self.__stream_output.get_slave_stream()

    @property
    def media_pipe_fps(self) -> float:
        return self.__media_pipe_fps_counter.get_cps()

    @property
    def media_pipe_latency(self) -> float:
        return self.__media_pipe_latency_counter.get_latency()

    @property
    def media_pipe_tongue_fps(self) -> float:
        return self.__media_pipe_tongue_fps_counter.get_cps()

    @property
    def media_pipe_tongue_latency(self) -> float:
        return self.__media_pipe_tongue_latency_counter.get_latency()

    @property
    def babble_fps(self) -> float:
        return self.__babble_fps_counter.get_cps()

    @property
    def babble_latency(self) -> float:
        return self.__babble_latency_counter.get_latency()

    @property
    def mixer(self) -> MixerFilterStream:
        return self.__mixer

    def close(self):
        self.__buffer.close()

        self.__media_pipe_pipeline.unregister_stream(self.__media_pipe_stream)
        self.__media_pipe_stream.unregister_stream(self.__buffer)
        self.__media_pipe_stream.unregister_stream(self.__media_pipe_fps_counter)
        self.__media_pipe_stream.unregister_stream(self.__media_pipe_latency_counter)

        self.__media_pipe_tongue_pipeline.unregister_stream(self.__buffer)
        self.__media_pipe_tongue_pipeline.unregister_stream(self.__media_pipe_tongue_fps_counter)
        self.__media_pipe_tongue_pipeline.unregister_stream(self.__media_pipe_tongue_latency_counter)

        self.__babble_pipeline.unregister_stream(self.__buffer)
        self.__babble_pipeline.unregister_stream(self.__babble_fps_counter)
        self.__babble_pipeline.unregister_stream(self.__babble_latency_counter)

        self.__mixer_options_listener.unregister()
        self.__calibration_options_listener.unregister()

        self.__media_pipe_stream.close()
        self.__stream_without_calibration_first.close()
        self.__stream_without_calibration_second.close()
        self.__stream_output.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __register_change_mixer_options(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [
            lambda config: config.processing.source,
            lambda config: config.media_pipe_tongue.enabled,
            lambda config: config.media_pipe_tongue.device_id,
            lambda config: config.media_pipe_tongue.provider,
            lambda config: config.babble.enabled,
            lambda config: config.babble.device_id,
            lambda config: config.babble.model_path,
            lambda config: config.babble.provider,
        ]

        return self.__config_manager.create_update_listener(self.__update_mixer_options, watch_array, True)

    def __update_mixer_options(self, config_manager: ConfigManager):
        custom_route = {key.to_original(): value for key, value in
                        config_manager.config.processing.source.items()}

        disabled_routes_dict = {
            MixerRoute.MEDIA_PIPE_TONGUE: config_manager.config.media_pipe_tongue.enabled
                                          and self.__media_pipe_tongue_pipeline.process_status is not Status.CRASHED,
            MixerRoute.BABBLE: config_manager.config.babble.enabled
                               and self.__babble_pipeline.get_model_loader().model,
        }

        disabled_routes = {key for key, value in disabled_routes_dict.items() if not value}

        self.mixer.update_routes(custom_route, disabled_routes)

    def __register_change_calibration_options(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [
            lambda config: config.processing.calibration
        ]

        return self.__config_manager.create_update_listener(self.__update_calibration_options, watch_array, True)

    def __update_calibration_options(self, config_manager: ConfigManager):
        self.__calibration_options.blend_shape_options = {key.to_original(): value for key, value in
                                                          config_manager.config.processing.calibration.items()}
