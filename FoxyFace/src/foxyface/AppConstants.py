import importlib
import sys
from pathlib import Path
from typing import Final

from packaging.version import Version


class AppConstants:
    VERSION: Final[Version] = Version("1.0.5.1")

    @staticmethod
    def get_application_root() -> Path:
        if getattr(sys, "frozen", False):
            if hasattr(sys, "_MEIPASS"):
                return Path(sys._MEIPASS).resolve()

            return Path(sys.executable).resolve().parent

        return Path(__file__).resolve().parent

    @staticmethod
    def get_baballonia_face_model_path() -> Path:
        model_filename = "faceModel.onnx"

        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            base_path = Path(sys._MEIPASS)

            pyinstaller_path = base_path / "Baballonia" / "src" / "Baballonia" / model_filename
            if pyinstaller_path.is_file():
                return Path(pyinstaller_path)

        try:
            resource_path = importlib.resources.files("foxyface.assets.baballonia") / model_filename

            if resource_path.is_file():
                return Path(resource_path)
        except ModuleNotFoundError:
            pass

        current_dir = Path(__file__).resolve()

        for parent in current_dir.parents:
            dev_path = parent / "Baballonia" / "src" / "Baballonia" / model_filename
            if dev_path.is_file():
                return Path(dev_path)

        raise FileNotFoundError(f"File {model_filename} not found")
