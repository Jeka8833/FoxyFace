import logging
from dataclasses import dataclass
from pathlib import Path

import numpy
import onnxruntime
from cv2.typing import MatLike
from onnxruntime import InferenceSession, SessionOptions, GraphOptimizationLevel

from AppConstants import AppConstants
from src.stream import ONNX_LOCK

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

        with ONNX_LOCK:
            out = self.__session.run(self.__output_names, {self.__input_name: frame})

        return float(out[0][0][0])

    def __run_test_image(self):
        frame = numpy.zeros((MPT_IMAGE_INPUT_SIZE_Y, MPT_IMAGE_INPUT_SIZE_X, 3), dtype=numpy.uint8)

        self.run(frame)

    @staticmethod
    def load_model(use_gpu: bool, intra_op_num_threads: int, allow_spinning: bool,
                   device_id: int) -> MediaPipeTongueModel:
        device_id_param = {"device_id": str(device_id)}

        opts = SessionOptions()
        opts.inter_op_num_threads = 1
        opts.intra_op_num_threads = intra_op_num_threads
        opts.graph_optimization_level = GraphOptimizationLevel.ORT_ENABLE_ALL
        opts.add_session_config_entry("session.intra_op.allow_spinning", "1" if allow_spinning else "0")
        opts.enable_mem_pattern = False

        if use_gpu:
            provider = [("DmlExecutionProvider", device_id_param), ("CUDAExecutionProvider", device_id_param),
                        ("ROCMExecutionProvider", device_id_param), "CoreMLExecutionProvider",
                        "CPUExecutionProvider"]
        else:
            provider = ["CPUExecutionProvider"]

        available_providers = onnxruntime.get_available_providers()

        _logger.info(f"All providers: {available_providers}")

        final_providers = []
        for p in provider:
            name = p[0] if isinstance(p, tuple) else p
            if name in available_providers:
                final_providers.append(p)

        _logger.info(f"Using providers: {final_providers}")

        session = InferenceSession(MediaPipeTongueModel.get_base_model_path(), opts, providers=final_providers)

        first_input = session.get_inputs()[0]
        input_name = first_input.name
        input_size_x = first_input.shape[2]
        input_size_y = first_input.shape[3]

        output_names = [session.get_outputs()[0].name]

        model = MediaPipeTongueModel(session, input_name, output_names, input_size_x, input_size_y)

        model.__run_test_image()

        _logger.info("MediaPipe Tongue Model loaded successfully")

        return model

    @staticmethod
    def get_base_model_path() -> Path:
        return AppConstants.get_application_root() / "Assets" / "tongue_detector.onnx"
