from src.config.ConfigManager import ConfigManager
from src.pipline.MediaPipePipeline import MediaPipePipeline
from src.pipline.ProcessingPipeline import ProcessingPipeline
from src.pipline.calibration.AutoCalibration import AutoCalibration
from src.stream.core.components.SingleBufferStream import SingleBufferStream
from src.stream.mediapipe.core.MediaPipeFrame import MediaPipeFrame


class AutoCalibrationEndpoint:
    def __init__(self, config_manager: ConfigManager, media_pipe_pipeline: MediaPipePipeline,
                 processing_pipeline: ProcessingPipeline):
        self.__config_manager: ConfigManager = config_manager
        self.__media_pipe_pipeline: MediaPipePipeline = media_pipe_pipeline
        self.__processing_pipeline: ProcessingPipeline = processing_pipeline

        self.__buffer = SingleBufferStream[MediaPipeFrame]()
        self.__media_pipe_pipeline.register_stream(self.__buffer)

        self.auto_calibration = AutoCalibration(self.__config_manager,
                                                self.__processing_pipeline.get_auto_calibration_stream(), self.__buffer)

    def close(self):
        self.__buffer.close()
        self.auto_calibration.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
