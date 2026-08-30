import logging
from importlib import resources
from pathlib import Path

from cv2.typing import MatLike
from onnxruntime import GraphOptimizationLevel, InferenceSession, SessionOptions

from foxyface.AppConstants import AppConstants
from foxyface.stream.babble.BabbleBlendshapeEnum import BabbleBlendshapeEnum
from foxyface.stream.babble.BabbleModel import BabbleModel
from foxyface.util import OnnxUtil

_logger = logging.getLogger(__name__)


class BabbleModelLoader:
    def __init__(self):
        self.model: BabbleModel | None = None

    def start_new_session(self, model_path: str, provider_name: str | None, intra_op_num_threads: int,
                          allow_spinning: bool, device_id: int):
        self.model = None

        opts = SessionOptions()
        opts.inter_op_num_threads = 1
        opts.intra_op_num_threads = intra_op_num_threads
        opts.graph_optimization_level = GraphOptimizationLevel.ORT_ENABLE_ALL
        opts.add_session_config_entry("session.intra_op.allow_spinning", "1" if allow_spinning else "0")
        opts.enable_mem_pattern = False

        is_default_model = not model_path or model_path.isspace()

        if is_default_model:
            with resources.as_file(AppConstants.get_baballonia_face_model_path()) as default_model_path:
                path = default_model_path
                provider = OnnxUtil.get_provider(provider_name, device_id)
                session = InferenceSession(path, opts, providers=provider)
        else:
            path = Path(model_path).resolve(strict=True)
            provider = OnnxUtil.get_provider(provider_name, device_id)
            session = InferenceSession(path, opts, providers=provider)

        first_input = session.get_inputs()[0]
        input_name = first_input.name
        input_size_x = first_input.shape[2]
        input_size_y = first_input.shape[3]

        output_names = [session.get_outputs()[0].name]

        model = BabbleModel(session, input_name, output_names, is_default_model, input_size_x, input_size_y)
        if model.is_loaded_successfully():
            self.model = model

            _logger.info(
                f"Babble model has loaded with provider: {provider}, "
                f"intra_op_num_threads: {intra_op_num_threads}, allow_spinning: {allow_spinning}")

    def process_gray_image(self, image: MatLike) -> dict[BabbleBlendshapeEnum, float] | None:
        if self.model is None:
            return None

        return self.model.process_gray_image(image)
