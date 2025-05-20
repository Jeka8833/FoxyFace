import time
from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor
from statistics import median
from threading import Event

from src.config.ConfigManager import ConfigManager
from src.config.schemas.core.enums.GeneralBlendShapeEnumConfig import GeneralBlendShapeEnumConfig
from src.stream.core.StreamReadOnly import StreamReadOnly
from src.stream.mediapipe.core.MediaPipeFrame import MediaPipeFrame
from src.stream.postprocessing.BlendShapesFrame import BlendShapesFrame
from src.stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum
from src.stream.postprocessing.calibration.BlendShapeOption import BlendShapeOption


class AutoCalibration:
    def __init__(self, config_manager: ConfigManager,
                 general_blend_shapes_stream: StreamReadOnly[BlendShapesFrame[GeneralBlendShapeEnum]],
                 media_pipe_stream: StreamReadOnly[MediaPipeFrame]):
        self.__config_manager: ConfigManager = config_manager
        self.__general_blend_shapes_stream: StreamReadOnly[
            BlendShapesFrame[GeneralBlendShapeEnum]] = general_blend_shapes_stream
        self.__media_pipe_stream: StreamReadOnly[MediaPipeFrame] = media_pipe_stream

        self.__thread_pool = ThreadPoolExecutor(max_workers=1)

    def neutral_pose_async(self, calibration_list: list[GeneralBlendShapeEnum], calibrate_rotation: bool,
                           average_time: float = 1.0) -> Future[bool]:
        return self.__thread_pool.submit(self.__neutral_pose, calibration_list, calibrate_rotation, average_time)

    def max_pose_async(self, calibration_list: list[GeneralBlendShapeEnum], cancel_event: Event,
                       timeout: float = 1.0) -> Future[bool]:
        return self.__thread_pool.submit(self.__max_pose, calibration_list, cancel_event, timeout)

    def close(self):
        self.__thread_pool.shutdown(cancel_futures=True, wait=True)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __neutral_pose(self, calibration_list: list[GeneralBlendShapeEnum], calibrate_rotation: bool,
                       average_time: float) -> bool:
        start_time = time.perf_counter_ns()

        record_list: dict[GeneralBlendShapeEnum, list[float]] = {}
        try:
            self.__general_blend_shapes_stream.poll(average_time)  # Drop first frame

            while True:
                frame = self.__general_blend_shapes_stream.poll(
                    average_time - (time.perf_counter_ns() - start_time) / 1_000_000_000)

                for key, value in frame.blend_shapes.items():
                    if not key.value.disable_calibration and key in calibration_list:
                        record_list.setdefault(key, []).append(value)
        except TimeoutError:
            pass
        except InterruptedError:
            return False

        if calibrate_rotation:
            try:
                self.__media_pipe_stream.poll(average_time)  # Drop first frame

                transformation_matrix = \
                    self.__media_pipe_stream.poll(average_time).face_landmarker_result.facial_transformation_matrixes[0]

                self.__config_manager.config.media_pipe.head_rotation_transformation = transformation_matrix[0:3,
                                                                                       0:3].transpose().tolist()
            except TimeoutError:
                return False
            except InterruptedError:
                return False
        elif not record_list:
            return False

        for key, value in record_list.items():
            option = self.__config_manager.config.processing.calibration.setdefault(
                GeneralBlendShapeEnumConfig.from_original(key), BlendShapeOption())
            option.neutral_pose = median(value)  # 50% cumulative probability

        self.__config_manager.write()

        return True

    def __max_pose(self, calibration_list: list[GeneralBlendShapeEnum], cancel_event: Event,
                   timeout: float = 1.0) -> bool:
        record_list: dict[GeneralBlendShapeEnum, list[float]] = {}
        try:
            self.__general_blend_shapes_stream.poll(timeout)  # Drop first frame

            while not cancel_event.is_set():
                frame = self.__general_blend_shapes_stream.poll(timeout)

                for key, value in frame.blend_shapes.items():
                    if key in calibration_list:
                        record_list.setdefault(key, []).append(value)
        except TimeoutError:
            return False
        except InterruptedError:
            return False

        for key, value in record_list.items():
            option = self.__config_manager.config.processing.calibration.setdefault(
                GeneralBlendShapeEnumConfig.from_original(key), BlendShapeOption())

            option.max_pose_negative = min(value)
            option.max_pose_positive = max(value)

        self.__config_manager.write()

        return True
