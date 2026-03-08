import logging

from src.config.ConfigManager import ConfigManager
from src.stream.camera.CameraEnumerator import CameraEnumerator, CameraInfo
from src.ui.FoxyWindow import FoxyWindow
from src.ui.qtcreator.ui_camerasettings import Ui_CameraSettings

_logger = logging.getLogger(__name__)


class CameraSettingsWindow(FoxyWindow):
    def __init__(self, config_manager: ConfigManager):
        super().__init__()

        self.__config_manager = config_manager
        self.__available_cameras: list[CameraInfo] = []

        self.__ui = Ui_CameraSettings()
        self.__ui.setupUi(self)

        self.__ui.apply_and_save_btn.clicked.connect(self.__save)
        self.__ui.height_sp.installEventFilter(self)
        self.__ui.width_sp.installEventFilter(self)

        self.__populate_cameras()
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

    def closeEvent(self, event, /):
        super().closeEvent(event)

        self.__ui.apply_and_save_btn.clicked.disconnect(self.__save)

    def __populate_cameras(self):
        """Populate the camera combo box with available cameras."""
        try:
            self.__available_cameras = CameraEnumerator.get_available_cameras()
            self.__ui.camera_combo.clear()
            
            if not self.__available_cameras:
                # No cameras found, add a placeholder
                self.__ui.camera_combo.addItem("No cameras found")
                self.__ui.camera_combo.setEnabled(False)
            else:
                for camera_info in self.__available_cameras:
                    # Store camera name as item text and index as user data
                    self.__ui.camera_combo.addItem(camera_info.name, camera_info.index)
        except Exception:
            _logger.warning("Failed to enumerate cameras", exc_info=True, stack_info=True)
            self.__ui.camera_combo.addItem("Error loading cameras")
            self.__ui.camera_combo.setEnabled(False)

    def __set_default_values(self):
        # Set camera selection based on saved camera_name or camera_id
        camera_name = self.__config_manager.config.camera.camera_name
        camera_id = self.__config_manager.config.camera.camera_id
        
        # Try to find camera by name first
        selected_index = -1
        if camera_name:
            for i in range(self.__ui.camera_combo.count()):
                if self.__ui.camera_combo.itemText(i) == camera_name:
                    selected_index = i
                    break
        
        # If not found by name, try to find by camera ID
        if selected_index == -1:
            for i in range(self.__ui.camera_combo.count()):
                if self.__ui.camera_combo.itemData(i) == camera_id:
                    selected_index = i
                    break
        
        # Set the selection, defaulting to first item (index 0) if nothing matches
        if selected_index >= 0:
            self.__ui.camera_combo.setCurrentIndex(selected_index)
        elif self.__ui.camera_combo.count() > 0:
            self.__ui.camera_combo.setCurrentIndex(0)
        
        self.__ui.width_sp.setValue((self.__config_manager.config.camera.width // 2) * 2)
        self.__ui.height_sp.setValue((self.__config_manager.config.camera.height // 2) * 2)
        self.__ui.horizontal_flip_cb.setChecked(self.__config_manager.config.camera.mirror_x)
        self.__ui.vertical_flip_cb.setChecked(self.__config_manager.config.camera.mirror_y)
        self.__ui.rotate_90_cb.setChecked(self.__config_manager.config.camera.rotate_ninety)

    def __save(self):
        try:
            # Get selected camera info from combo box
            current_index = self.__ui.camera_combo.currentIndex()
            if current_index >= 0 and self.__ui.camera_combo.isEnabled():
                camera_name = self.__ui.camera_combo.itemText(current_index)
                camera_id = self.__ui.camera_combo.itemData(current_index)
                
                # Save both camera_name (preferred) and camera_id (fallback)
                self.__config_manager.config.camera.camera_name = camera_name
                self.__config_manager.config.camera.camera_id = camera_id if camera_id is not None else 0
            
            self.__config_manager.config.camera.width = self.__ui.width_sp.value()
            self.__config_manager.config.camera.height = self.__ui.height_sp.value()
            self.__config_manager.config.camera.mirror_x = self.__ui.horizontal_flip_cb.isChecked()
            self.__config_manager.config.camera.mirror_y = self.__ui.vertical_flip_cb.isChecked()
            self.__config_manager.config.camera.rotate_ninety = self.__ui.rotate_90_cb.isChecked()

            self.__config_manager.write()
        except Exception:
            _logger.warning("Failed to save camera settings", exc_info=True, stack_info=True)
