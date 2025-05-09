import dataclasses
import logging
from concurrent.futures import Future, ThreadPoolExecutor
from pathlib import Path

from cv2.typing import MatLike
from onnxruntime import GraphOptimizationLevel, InferenceSession, SessionOptions

from AppConstants import AppConstants
from src.stream.babble.BabbleBlendShapeEnum import BabbleBlendShapeEnum
from src.stream.babble.BabbleModel import BabbleModel
from src.stream.babble.BabbleModelLoaderOptions import BabbleModelLoaderOptions

_logger = logging.getLogger(__name__)


class BabbleModelLoader:
    def __init__(self, options: BabbleModelLoaderOptions):
        self.__options: BabbleModelLoaderOptions = options

        self.model: BabbleModel | None = None

        self.__thread_pool: ThreadPoolExecutor = ThreadPoolExecutor(max_workers=1, thread_name_prefix="Babble Reloader")
        self.recreate()

    def recreate(self) -> Future[bool]:
        return self.__thread_pool.submit(self.__create_session)

    def process_gray_image(self, image: MatLike) -> dict[BabbleBlendShapeEnum, float] | None:
        if self.model is None:
            return None

        return self.model.process_gray_image(image)

    def close(self):
        self.__thread_pool.shutdown(wait=True, cancel_futures=True)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __create_session(self) -> bool:
        try:
            options = dataclasses.replace(self.__options)

            opts = SessionOptions()
            opts.inter_op_num_threads = 1
            opts.intra_op_num_threads = options.intra_op_num_threads
            opts.graph_optimization_level = GraphOptimizationLevel.ORT_ENABLE_ALL
            opts.add_session_config_entry("session.intra_op.allow_spinning", "1" if options.allow_spinning else "0")
            opts.enable_mem_pattern = False

            if options.use_gpu:
                provider = ["DmlExecutionProvider", "CUDAExecutionProvider", "CPUExecutionProvider"]
            else:
                provider = ["CPUExecutionProvider"]

            if not options.model_path or options.model_path.isspace():
                model_path = BabbleModelLoader.get_base_model_path()
            else:
                model_path = Path(options.model_path).resolve(strict=True)

            session = InferenceSession(model_path, opts, providers=provider)

            first_input = session.get_inputs()[0]
            input_name = first_input.name
            input_size_x = first_input.shape[2]
            input_size_y = first_input.shape[3]

            output_names = [session.get_outputs()[0].name]

            is_default_model = BabbleModelLoader.get_base_model_path().samefile(model_path)

            model = BabbleModel(session, input_name, output_names, is_default_model, input_size_x, input_size_y)
            if model.is_loaded_successfully():
                self.model = model

                _logger.info("Babble model reloaded")
                return True
        except Exception:
            _logger.warning("Failed to create session", exc_info=True, stack_info=True)

        self.model = None

        return False

    @staticmethod
    def get_base_model_path() -> Path:
        return AppConstants.get_application_root() / "Baballonia" / "src" / "Baballonia" / "faceModel.onnx"
