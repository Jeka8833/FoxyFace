import logging
from concurrent.futures import Future, ThreadPoolExecutor
from threading import Event

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QListWidget, QMessageBox

from src.config.ConfigManager import ConfigManager
from src.pipline.calibration.AutoCalibrationEndpoint import AutoCalibrationEndpoint
from src.stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum
from src.ui import UiSoundUtil
from src.ui.FoxyWindow import FoxyWindow
from src.ui.qtcreator.ui_AutoCalibrationWindow import Ui_AutoCalibrationWindow

_logger = logging.getLogger(__name__)


class AutoCalibrationWindow(FoxyWindow):
    __fail_calibration_signal: Signal = Signal()
    __update_global_state_signal: Signal = Signal()

    def __init__(self, config_manager: ConfigManager, auto_calibration_endpoint: AutoCalibrationEndpoint):
        super().__init__()

        self.__config_manager: ConfigManager = config_manager
        self.__auto_calibration_endpoint: AutoCalibrationEndpoint = auto_calibration_endpoint

        self.__ui = Ui_AutoCalibrationWindow()
        self.__ui.setupUi(self)

        self.__normal_pose_delay_future: Future[None] | None = None
        self.__normal_pose_calibration_future: Future[bool] | None = None
        self.__max_pose_calibration_future: Future[bool] | None = None

        self.__update_global_state_signal.connect(self.__update_global_state)
        self.__set_default_selection()

        self.__ui.normal_pose_delay_sp.valueChanged.connect(self.__changed_delay_normal_pose)
        self.__ui.normal_pose_selected_list.itemSelectionChanged.connect(self.__list_changed_normal_pose)
        self.__ui.max_pose_selected_list.itemSelectionChanged.connect(self.__list_changed_max_pose)

        self.__ui.normal_pose_start_btn.clicked.connect(self.__start_normal_pose_delayed)
        self.__ui.max_pose_start_btn.toggled.connect(self.__toggle_max_pose)

        self.__fail_calibration_signal.connect(self.__bad_message)

        self.__thread_pool = ThreadPoolExecutor(max_workers=1)
        self.__max_thread_stop_event: Event = Event()

        self.show()

    def closeEvent(self, event, /):
        super().closeEvent(event)

        self.__ui.normal_pose_selected_list.itemSelectionChanged.disconnect(self.__list_changed_normal_pose)
        self.__ui.max_pose_selected_list.itemSelectionChanged.disconnect(self.__list_changed_max_pose)

        self.__ui.normal_pose_delay_sp.valueChanged.disconnect(self.__changed_delay_normal_pose)
        self.__ui.normal_pose_start_btn.clicked.disconnect(self.__start_normal_pose_delayed)
        self.__ui.max_pose_start_btn.toggled.disconnect(self.__toggle_max_pose)

        self.__update_global_state_signal.disconnect(self.__update_global_state)
        self.__fail_calibration_signal.disconnect(self.__bad_message)

        self.__config_manager.write()
        self.__thread_pool.shutdown(wait=True, cancel_futures=True)

    def __start_normal_pose_delayed(self):
        delay_time = self.__ui.normal_pose_delay_sp.value()

        self.__normal_pose_delay_future = self.__thread_pool.submit(self.__start_normal_pose, delay_time)

        self.__update_global_state_signal.emit()

    def __toggle_max_pose(self, toggle: bool):
        if toggle:
            self.__max_thread_stop_event = Event()
            self.__max_pose_calibration_future = self.__auto_calibration_endpoint.auto_calibration.max_pose_async(
                self.__to_general_blend_shape(self.__ui.max_pose_selected_list), self.__max_thread_stop_event,
                timeout=3.0)

            self.__max_pose_calibration_future.add_done_callback(self.__pose_calibration_end)
        else:
            self.__max_thread_stop_event.set()

        self.__update_global_state_signal.emit()

    def __list_changed_normal_pose(self):
        self.__update_global_state_signal.emit()

        out = [value.text() for value in self.__ui.normal_pose_selected_list.selectedItems()]

        self.__config_manager.config.gui.auto_calibration_window.selection_neutral_position = out

    def __list_changed_max_pose(self):
        self.__update_global_state_signal.emit()

        out = [value.text() for value in self.__ui.max_pose_selected_list.selectedItems()]

        self.__config_manager.config.gui.auto_calibration_window.selection_max_position = out

    def __changed_delay_normal_pose(self):
        self.__config_manager.config.gui.auto_calibration_window.delay_neutral_position = self.__ui.normal_pose_delay_sp.value()

    def __bad_message(self):
        QMessageBox.critical(self, "Calibration Fail", "Are you sure you're looking at the camera? "
                                                       "Or have you selected a parameter that is not enabled.")

    def __update_global_state(self):
        is_normal_pose_calibrating = (
                                             self.__normal_pose_delay_future is not None and not self.__normal_pose_delay_future.done()) or (
                                             self.__normal_pose_calibration_future is not None and not self.__normal_pose_calibration_future.done())

        is_max_pose_calibrating = self.__max_pose_calibration_future is not None and not self.__max_pose_calibration_future.done()

        normal_pose_has_selection = bool(self.__ui.normal_pose_selected_list.selectedIndexes())
        max_pose_has_selection = bool(self.__ui.max_pose_selected_list.selectedIndexes())

        self.__ui.normal_pose_start_btn.setEnabled(
            normal_pose_has_selection and not is_normal_pose_calibrating and not is_max_pose_calibrating)
        self.__ui.max_pose_start_btn.setEnabled(max_pose_has_selection and not is_normal_pose_calibrating)

        if self.__ui.max_pose_start_btn.isChecked():
            self.__ui.max_pose_start_btn.setText("Stop Calibration")
        else:
            self.__ui.max_pose_start_btn.setText("Start Calibration")

        self.__ui.normal_pose_selected_list.setDisabled(is_normal_pose_calibrating)
        self.__ui.max_pose_selected_list.setDisabled(is_max_pose_calibrating)

    def __start_normal_pose(self, wait_sec: int = 0):
        if (wait_sec <= 0 and self.is_closed.is_set()) or self.is_closed.wait(wait_sec):
            self.__update_global_state_signal.emit()
            return

        UiSoundUtil.play_start_sound()

        self.__normal_pose_calibration_future = self.__auto_calibration_endpoint.auto_calibration.neutral_pose_async(
            self.__to_general_blend_shape(self.__ui.normal_pose_selected_list),
            self.__has_rotation(self.__ui.normal_pose_selected_list), average_time=3.0)

        self.__normal_pose_calibration_future.add_done_callback(self.__pose_calibration_end)

    def __pose_calibration_end(self, future: Future[bool]):
        try:
            if future.result():
                UiSoundUtil.play_good_sound()

                return
        except Exception:
            _logger.warning("Failed to calibrate normal/max pose", exc_info=True, stack_info=True)
        finally:
            self.__ui.max_pose_start_btn.setChecked(False)
            self.__update_global_state_signal.emit()

        self.__fail_calibration_signal.emit()

        UiSoundUtil.play_fail_sound()

    def __set_default_selection(self):
        try:
            self.__ui.normal_pose_delay_sp.setValue(
                self.__config_manager.config.gui.auto_calibration_window.delay_neutral_position)

            normal_pose_copy = self.__config_manager.config.gui.auto_calibration_window.selection_neutral_position.copy()
            max_pose_copy = self.__config_manager.config.gui.auto_calibration_window.selection_max_position.copy()

            for i in range(self.__ui.normal_pose_selected_list.count()):
                element = self.__ui.normal_pose_selected_list.item(i)

                element.setSelected(True if element.text() in normal_pose_copy else False)

            for i in range(self.__ui.max_pose_selected_list.count()):
                element = self.__ui.max_pose_selected_list.item(i)

                element.setSelected(True if element.text() in max_pose_copy else False)
        except Exception:
            _logger.warning("Failed to set default selection", exc_info=True, stack_info=True)

        self.__update_global_state_signal.emit()

    @staticmethod
    def __to_general_blend_shape(list_ui: QListWidget) -> list[GeneralBlendShapeEnum]:
        out = []

        for element in list_ui.selectedItems():
            try:
                out.append(GeneralBlendShapeEnum[element.text()])
            except Exception:
                pass

        return out

    @staticmethod
    def __has_rotation(list_ui: QListWidget) -> bool:
        for element in list_ui.selectedItems():
            if element.text() == "HeadRotation":
                return True

        return False
