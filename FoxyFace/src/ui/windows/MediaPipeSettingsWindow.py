import logging
import platform

from src.config.ConfigManager import ConfigManager
from src.ui.FoxyWindow import FoxyWindow
from src.ui.qtcreator.ui_mediapipesettings import Ui_MediaPipeSettings

_logger = logging.getLogger(__name__)


class MediaPipeSettingsWindow(FoxyWindow):
    def __init__(self, config_manager: ConfigManager):
        super().__init__()

        self.__config_manager = config_manager

        self.__ui = Ui_MediaPipeSettings()
        self.__ui.setupUi(self)

        self.__ui.save_btn.clicked.connect(self.__save)

        self.__set_default_values()

        self.show()

    def __set_default_values(self):
        if not (platform.system() in ['Linux', 'Darwin']):
            self.__ui.try_gpu_cb.hide()

        self.__ui.try_gpu_cb.setChecked(self.__config_manager.config.media_pipe.try_use_gpu)
        self.__ui.mtc_sp.setValue(self.__config_manager.config.media_pipe.min_tracking_confidence)
        self.__ui.mfdc_sp.setValue(self.__config_manager.config.media_pipe.min_face_detection_confidence)
        self.__ui.mfpc_sp.setValue(self.__config_manager.config.media_pipe.min_face_presence_confidence)



    def __save(self):
        try:
            self.__config_manager.config.media_pipe.try_use_gpu = self.__ui.try_gpu_cb.isChecked()
            self.__config_manager.config.media_pipe.min_tracking_confidence = self.__ui.mtc_sp.value()
            self.__config_manager.config.media_pipe.min_face_detection_confidence = self.__ui.mfdc_sp.value()
            self.__config_manager.config.media_pipe.min_face_presence_confidence = self.__ui.mfpc_sp.value()

            self.__config_manager.write()
        except Exception:
            _logger.warning("Failed to save camera settings", exc_info=True, stack_info=True)
