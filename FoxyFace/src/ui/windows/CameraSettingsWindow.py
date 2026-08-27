import logging

from src.config.ConfigManager import ConfigManager
from src.pipline.CameraPipeline import CameraPipeline
from src.stream.camera.info.CameraBackend import CameraBackend
from src.stream.camera.info.CameraEntry import CameraEntry
from src.stream.camera.info.CameraList import CameraList
from src.ui.FoxyWindow import FoxyWindow
from src.ui.qtcreator.ui_camerasettings import Ui_CameraSettings

_logger = logging.getLogger(__name__)


class CameraSettingsWindow(FoxyWindow):
    def __init__(self, config_manager: ConfigManager, camera_pipeline: CameraPipeline):
        super().__init__()

        self.__config_manager = config_manager
        self.__camera_pipeline = camera_pipeline
        self.__camera_list: CameraList = camera_pipeline.get_camera_list

        self.__ui = Ui_CameraSettings()
        self.__ui.setupUi(self)

        self.__init_camera_lists()

        self.__ui.apply_and_save_btn.clicked.connect(self.__save)
        self.__ui.camera_restart_btn.clicked.connect(self.__camera_restart)
        self.__ui.manual_backend_cb.currentIndexChanged.connect(self.__update_manual_input_visibility)
        self.__ui.manual_mode_cb.toggled.connect(self.__on_manual_mode_toggled)
        self.__ui.height_sp.installEventFilter(self)
        self.__ui.width_sp.installEventFilter(self)

        self.__set_default_values()

        self.show()

    def eventFilter(self, watched, event, /):
        if watched == self.__ui.width_sp and event.type() == event.Type.FocusOut:
            if self.__ui.width_sp.value() % 2 != 0:
                self.__ui.width_sp.setValue(self.__ui.width_sp.value() + 1)
        elif watched == self.__ui.height_sp and event.type() == event.Type.FocusOut:
            if self.__ui.height_sp.value() % 2 != 0:
                self.__ui.height_sp.setValue(self.__ui.height_sp.value() + 1)

        return super().eventFilter(watched, event)

    def __init_camera_lists(self):
        self.__ui.manual_backend_cb.clear()
        self.__ui.available_cameras_cb.clear()

        for backend in sorted(self.__camera_list.backends.values(), key=lambda b: b.name):
            self.__ui.manual_backend_cb.addItem(backend.name, backend)

        for camera in self.__camera_list.get_all_cameras():
            display_name = f"[{self.__camera_list.backends[camera.backend].name}] {camera.name}"

            self.__ui.available_cameras_cb.addItem(display_name, camera)

        try:
            saved_entry = self.__config_manager.config.camera.camera_info

            best_entry = self.__camera_list.find_best(saved_entry)

            self.__ui.manual_mode_cb.setChecked(best_entry.manual)

            if best_entry.manual:
                for i in range(self.__ui.manual_backend_cb.count()):
                    b: CameraBackend = self.__ui.manual_backend_cb.itemData(i)
                    if b and b.index == best_entry.backend:
                        self.__ui.manual_backend_cb.setCurrentIndex(i)
                        break

                if isinstance(best_entry.index, int):
                    self.__ui.manual_index_sb.setValue(best_entry.index)
                    self.__ui.manual_index_le.setText(str(best_entry.index))
                else:
                    self.__ui.manual_index_le.setText(str(best_entry.index))
            else:
                for i in range(self.__ui.available_cameras_cb.count()):
                    c: CameraEntry = self.__ui.available_cameras_cb.itemData(i)
                    if c and c.index == best_entry.index and c.backend == best_entry.backend:
                        self.__ui.available_cameras_cb.setCurrentIndex(i)
                        break
        except Exception as e:
            _logger.warning(f"Failed to load default camera entry: {e}")

    def __set_default_values(self):
        self.__ui.width_sp.setValue((self.__config_manager.config.camera.width // 2) * 2)
        self.__ui.height_sp.setValue((self.__config_manager.config.camera.height // 2) * 2)
        self.__ui.horizontal_flip_cb.setChecked(self.__config_manager.config.camera.mirror_x)
        self.__ui.vertical_flip_cb.setChecked(self.__config_manager.config.camera.mirror_y)
        self.__ui.rotate_90_cb.setChecked(self.__config_manager.config.camera.rotate_ninety)

        self.__on_manual_mode_toggled(self.__ui.manual_mode_cb.isChecked())

    def __on_manual_mode_toggled(self, checked: bool):
        self.__ui.manual_camera_widget.setVisible(checked)
        self.__ui.available_cameras_cb.setHidden(checked)
        self.__update_manual_input_visibility()

    def __update_manual_input_visibility(self):
        backend: CameraBackend = self.__ui.manual_backend_cb.currentData()
        if not backend:
            return

        has_int = int in backend.input_type
        has_str = str in backend.input_type

        self.__ui.manual_index_sb.setVisible(has_int and not has_str)
        self.__ui.manual_index_le.setVisible(has_str)

    def __save(self):
        try:
            self.__config_manager.config.camera.width = self.__ui.width_sp.value()
            self.__config_manager.config.camera.height = self.__ui.height_sp.value()
            self.__config_manager.config.camera.mirror_x = self.__ui.horizontal_flip_cb.isChecked()
            self.__config_manager.config.camera.mirror_y = self.__ui.vertical_flip_cb.isChecked()
            self.__config_manager.config.camera.rotate_ninety = self.__ui.rotate_90_cb.isChecked()

            if self.__ui.manual_mode_cb.isChecked():
                backend: CameraBackend = self.__ui.manual_backend_cb.currentData()
                if backend:
                    has_int = int in backend.input_type
                    has_str = str in backend.input_type

                    if has_int and not has_str:
                        idx = self.__ui.manual_index_sb.value()
                    elif has_str and not has_int:
                        idx = self.__ui.manual_index_le.text()
                    else:
                        text_val = self.__ui.manual_index_le.text()
                        try:
                            parsed_int = int(text_val)
                            if str(parsed_int) == text_val:
                                idx = parsed_int
                            else:
                                idx = text_val
                        except ValueError:
                            idx = text_val

                    self.__config_manager.config.camera.camera_info = self.__camera_list.find_or_create_by_backend_and_index(
                        backend.index, idx)
            else:
                self.__config_manager.config.camera.camera_info = self.__ui.available_cameras_cb.currentData()

            self.__config_manager.write()
        except Exception:
            _logger.warning("Failed to save camera settings", exc_info=True, stack_info=True)

    def __camera_restart(self):
        self.__camera_pipeline.camera_restart_async()
        self.__init_camera_lists()
