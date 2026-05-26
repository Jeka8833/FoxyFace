import logging
from pathlib import Path

import onnxruntime
from cv2.typing import MatLike
from onnxruntime import GraphOptimizationLevel, InferenceSession, SessionOptions

from AppConstants import AppConstants
from src.stream.babble.BabbleBlendShapeEnum import BabbleBlendShapeEnum
from src.stream.babble.BabbleModel import BabbleModel
from src.util.PathUtil import PathUtil
from util import OnnxUtil

_logger = logging.getLogger(__name__)


class BabbleModelLoader:
    def __init__(self):
        self.model: BabbleModel | None = None

    def start_new_session(self, model_path: str, provider_name: str, intra_op_num_threads: int, allow_spinning: bool,
                          device_id: int):
        self.model = None

        opts = SessionOptions()
        opts.inter_op_num_threads = 1
        opts.intra_op_num_threads = intra_op_num_threads
        opts.graph_optimization_level = GraphOptimizationLevel.ORT_ENABLE_ALL
        opts.add_session_config_entry("session.intra_op.allow_spinning", "1" if allow_spinning else "0")
        opts.enable_mem_pattern = False

        path = PathUtil.to_path_or_default(model_path, BabbleModelLoader.get_base_model_path(), strict=True)

        session = InferenceSession(path, opts, providers=OnnxUtil.get_provider(provider_name, device_id))

        first_input = session.get_inputs()[0]
        input_name = first_input.name
        input_size_x = first_input.shape[2]
        input_size_y = first_input.shape[3]

        output_names = [session.get_outputs()[0].name]

        is_default_model = BabbleModelLoader.get_base_model_path().samefile(path)

        model = BabbleModel(session, input_name, output_names, is_default_model, input_size_x, input_size_y)
        if model.is_loaded_successfully():
            self.model = model

            _logger.info("Babble started")

    def process_gray_image(self, image: MatLike) -> dict[BabbleBlendShapeEnum, float] | None:
        if self.model is None:
            return None

        return self.model.process_gray_image(image)

    @staticmethod
    def get_base_model_path() -> Path:
        return AppConstants.get_application_root() / "Baballonia" / "src" / "Baballonia" / "faceModel.onnx"
