import logging
from dataclasses import dataclass
from pathlib import Path

import numpy
from cv2.typing import MatLike
from onnxruntime import InferenceSession, SessionOptions, GraphOptimizationLevel

from AppConstants import AppConstants
from util import OnnxUtil

_logger = logging.getLogger(__name__)

MPT_IMAGE_INPUT_SIZE_X: int = 256
MPT_IMAGE_INPUT_SIZE_Y: int = 256


@dataclass(frozen=True, slots=True)
class MediaPipeTongueModel:
    __session: InferenceSession
    __input_name: str
    __output_names: list[str]
    input_size_x: int
    input_size_y: int

    def run(self, image: MatLike) -> float:
        frame = numpy.expand_dims(numpy.divide(image, 255, dtype=numpy.float32), axis=0)  # [1, H, W, 3]

        with OnnxUtil.global_lock:
            out = self.__session.run(self.__output_names, {self.__input_name: frame})

        return float(out[0][0][0])

    def __run_test_image(self):
        frame = numpy.zeros((MPT_IMAGE_INPUT_SIZE_Y, MPT_IMAGE_INPUT_SIZE_X, 3), dtype=numpy.uint8)

        self.run(frame)

    @staticmethod
    def load_model(provider_name: str | None, intra_op_num_threads: int, allow_spinning: bool,
                   device_id: int) -> MediaPipeTongueModel:
        opts = SessionOptions()
        opts.inter_op_num_threads = 1
        opts.intra_op_num_threads = intra_op_num_threads
        opts.graph_optimization_level = GraphOptimizationLevel.ORT_ENABLE_ALL
        opts.add_session_config_entry("session.intra_op.allow_spinning", "1" if allow_spinning else "0")
        opts.enable_mem_pattern = False

        provider = OnnxUtil.get_provider(provider_name, device_id)
        session = InferenceSession(MediaPipeTongueModel.get_base_model_path(), opts, providers=provider)

        first_input = session.get_inputs()[0]
        input_name = first_input.name
        input_size_x = first_input.shape[2]
        input_size_y = first_input.shape[3]

        output_names = [session.get_outputs()[0].name]

        model = MediaPipeTongueModel(session, input_name, output_names, input_size_x, input_size_y)

        model.__run_test_image()

        _logger.info(f"Media Pipe Tongue model has loaded with provider: {provider}, device id: {device_id}, "
                     f"intra_op_num_threads: {intra_op_num_threads}, allow_spinning: {allow_spinning}")

        return model

    @staticmethod
    def get_base_model_path() -> Path:
        return AppConstants.get_application_root() / "Assets" / "tongue_detector.onnx"
