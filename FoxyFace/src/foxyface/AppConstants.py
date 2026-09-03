import logging
from importlib import resources, metadata
from importlib.resources.abc import Traversable
from pathlib import Path
from typing import Final

from packaging.version import Version

_logger = logging.getLogger(__name__)


class AppConstants:
    VERSION: Final[Version] = Version(metadata.version("foxyface"))

    @staticmethod
    def get_file_from_assets(file_name: str) -> Traversable:
        return resources.files("foxyface.assets").joinpath(file_name)

    @staticmethod
    def get_baballonia_face_model_path() -> Traversable | Path:
        try:
            return resources.files("foxyface.assets.baballonia").joinpath("faceModel.onnx")
        except ModuleNotFoundError:
            _logger.info("Baballonia model not found in assets, trying to load from project root")

            current_file_path = Path(__file__).resolve()
            project_root = current_file_path.parent.parent.parent

            return project_root / "Baballonia" / "src" / "Baballonia" / "faceModel.onnx"
