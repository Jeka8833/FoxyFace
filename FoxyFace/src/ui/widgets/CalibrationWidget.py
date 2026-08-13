from typing import Any, Callable

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from src.config.ConfigManager import ConfigManager
from src.config.ConfigUpdateListener import ConfigUpdateListener
from src.config.schemas.main.Config import Config
from src.config.schemas.main.core.enums.GeneralBlendShapeEnumConfig import GeneralBlendShapeEnumConfig
from src.stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum
from src.stream.postprocessing.calibration.BlendShapeOption import BlendShapeOption
from src.stream.postprocessing.mixer.MixerFilterStream import MixerFilterStream
from src.stream.postprocessing.mixer.MixerRoute import MixerRoute
from src.stream.postprocessing.mixer.MixerSelectionList import MixerSelectionList
from src.ui.qtcreator.ui_CalibrationSettingsItem import Ui_CalibrationSettingsItem


class CalibrationWidget(QWidget):
    __recreate_source_list: Signal = Signal(object, int, object)
    __set_negative_sp: Signal = Signal(float)
    __set_neutral_sp: Signal = Signal(float)
    __set_positive_sp: Signal = Signal(float)

    def __init__(self,
                 blend_shape_type: GeneralBlendShapeEnum,
                 config_manager: ConfigManager,
                 mixer: MixerFilterStream):
        super().__init__()

        self.__blendshape = blend_shape_type
        self.__config_manager = config_manager
        self.__mixer = mixer

        self.__mixer_selection_last_value: MixerSelectionList | None = None

        self.__ui = Ui_CalibrationSettingsItem()
        self.__ui.setupUi(self)

        self.__set_default_values()

        self.__recreate_source_list.connect(self.__recreate_source)
        self.__set_negative_sp.connect(self.__ui.negative_sp.setValue)
        self.__set_neutral_sp.connect(self.__ui.neutral_sp.setValue)
        self.__set_positive_sp.connect(self.__ui.positive_sp.setValue)

        self.__negative_options_listener = self.__register_change_negative_options()
        self.__neutral_options_listener = self.__register_change_neutral_options()
        self.__positive_options_listener = self.__register_change_positive_options()

        self.__ui.source_combobox.currentIndexChanged.connect(self.__changed_source)
        self.__ui.negative_sp.valueChanged.connect(self.__changed_negative)
        self.__ui.neutral_sp.valueChanged.connect(self.__changed_neutral)
        self.__ui.positive_sp.valueChanged.connect(self.__changed_positive)

        self.update_value(True, None, None)

    def update_value(self, update_labes: bool, input_value: float | None, output_value: float | None):
        """
        Call from window event thread
        """

        neg_pb_val = 0
        pos_pb_val = 0
        if output_value is not None:
            if abs(self.__blendshape.value.min_value) > 0.0:
                neg_pb_val = max(0, (128 * output_value) // self.__blendshape.value.min_value)

            if abs(self.__blendshape.value.max_value) > 0.0:
                pos_pb_val = max(0, (128 * output_value) // self.__blendshape.value.max_value)

        self.__ui.negative_part_pb.setValue(neg_pb_val)
        self.__ui.positive_part_pb.setValue(pos_pb_val)

        select_info = self.__mixer.get_selection_list(self.__blendshape)

        warning_list = []
        if select_info.collision is not None:
            warning_list.append(f"Collision with {select_info.collision.name}")

        if self.__ui.negative_sp.value() > self.__ui.neutral_sp.value() and self.__ui.negative_sp_frame.isVisible():
            warning_list.append("Negative > Neutral")

        if self.__ui.positive_sp.value() < self.__ui.neutral_sp.value() and self.__ui.positive_sp_frame.isVisible():
            warning_list.append("Positive < Neutral")

        if update_labes:
            if input_value is None:
                self.__ui.name_and_value_lb.setText(self.__blendshape.name)
            else:
                self.__ui.name_and_value_lb.setText(f"{self.__blendshape.name}: {input_value:.6f}")

            self.__ui.output_lb.setStyleSheet("color: red" if warning_list else "")

            output_text = f"Output: {output_value:.3f}" if output_value is not None else "Output: Nothing"

            if warning_list:
                output_text += f"; Warning: {', '.join(warning_list)}"

            self.__ui.output_lb.setText(output_text)

        if self.__mixer_selection_last_value != select_info:
            self.__mixer_selection_last_value = select_info

            self.__update_source_options(select_info)

    def closeEvent(self, event, /):
        super().closeEvent(event)

        self.__negative_options_listener.unregister()
        self.__neutral_options_listener.unregister()
        self.__positive_options_listener.unregister()

        self.__ui.source_combobox.currentIndexChanged.disconnect(self.__changed_source)
        self.__ui.negative_sp.valueChanged.disconnect(self.__changed_negative)
        self.__ui.neutral_sp.valueChanged.disconnect(self.__changed_neutral)
        self.__ui.positive_sp.valueChanged.disconnect(self.__changed_positive)

        self.__recreate_source_list.disconnect(self.__recreate_source)
        self.__set_negative_sp.disconnect(self.__ui.negative_sp.setValue)
        self.__set_neutral_sp.disconnect(self.__ui.neutral_sp.setValue)
        self.__set_positive_sp.disconnect(self.__ui.positive_sp.setValue)

    def __changed_source(self):
        current_index = self.__ui.source_combobox.currentIndex()
        if current_index < 0:
            return

        select_info = self.__mixer.get_selection_list(self.__blendshape)
        selected = select_info.all_routes[current_index]
        assert isinstance(selected, MixerRoute)

        self.__config_manager.config.processing.source[
            GeneralBlendShapeEnumConfig.from_original(self.__blendshape)] = selected

        self.__update_disabled_state()

    def __update_source_options(self, select_info: MixerSelectionList):
        select_names = [str(route) for route in select_info.all_routes]

        selected_index = select_info.all_routes.index(select_info.selected)

        if select_info.selected is not select_info.current_route:
            select_names[selected_index] = f"{select_names[selected_index]} ({select_info.current_route})"

        blocked_list = {select_info.all_routes.index(route) for route in select_info.blocked_routes}

        self.__recreate_source_list.emit(select_names, selected_index, blocked_list)

    def __recreate_source(self, source_list: list[str], selected: int, blocked_list: set[int]):
        self.__ui.source_combobox.clear()
        self.__ui.source_combobox.addItems(source_list)
        self.__ui.source_combobox.setCurrentIndex(selected)

        model = self.__ui.source_combobox.model()
        for index in blocked_list:
            if item := model.item(index):
                item.setEnabled(False)

        self.__update_disabled_state()

    def __changed_negative(self):
        option = self.__config_manager.config.processing.calibration.setdefault(
            GeneralBlendShapeEnumConfig.from_original(self.__blendshape), BlendShapeOption())

        option.max_pose_negative = self.__ui.negative_sp.value()

    def __register_change_negative_options(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.processing.calibration.get(
            GeneralBlendShapeEnumConfig.from_original(self.__blendshape), BlendShapeOption()).max_pose_negative]

        return self.__config_manager.create_update_listener(self.__update_negative_options, watch_array, True)

    def __update_negative_options(self, config_manager: ConfigManager):
        option = config_manager.config.processing.calibration.get(
            GeneralBlendShapeEnumConfig.from_original(self.__blendshape), BlendShapeOption())

        self.__set_negative_sp.emit(option.max_pose_negative)

    def __changed_neutral(self):
        option = self.__config_manager.config.processing.calibration.setdefault(
            GeneralBlendShapeEnumConfig.from_original(self.__blendshape), BlendShapeOption())

        option.neutral_pose = self.__ui.neutral_sp.value()

    def __register_change_neutral_options(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.processing.calibration.get(
            GeneralBlendShapeEnumConfig.from_original(self.__blendshape), BlendShapeOption()).neutral_pose]

        return self.__config_manager.create_update_listener(self.__update_neutral_options, watch_array, True)

    def __update_neutral_options(self, config_manager: ConfigManager):
        option = config_manager.config.processing.calibration.get(
            GeneralBlendShapeEnumConfig.from_original(self.__blendshape), BlendShapeOption())

        self.__set_neutral_sp.emit(option.neutral_pose)

    def __changed_positive(self):
        option = self.__config_manager.config.processing.calibration.setdefault(
            GeneralBlendShapeEnumConfig.from_original(self.__blendshape), BlendShapeOption())

        option.max_pose_positive = self.__ui.positive_sp.value()

    def __register_change_positive_options(self) -> ConfigUpdateListener:
        watch_array: list[Callable[[Config], Any]] = [lambda config: config.processing.calibration.get(
            GeneralBlendShapeEnumConfig.from_original(self.__blendshape), BlendShapeOption()).max_pose_positive]

        return self.__config_manager.create_update_listener(self.__update_positive_options, watch_array, True)

    def __update_positive_options(self, config_manager: ConfigManager):
        option = config_manager.config.processing.calibration.get(
            GeneralBlendShapeEnumConfig.from_original(self.__blendshape), BlendShapeOption())

        self.__set_positive_sp.emit(option.max_pose_positive)

    def __set_default_values(self):
        self.__ui.negative_sp.wheelEvent = self.__wheel_event
        self.__ui.neutral_sp.wheelEvent = self.__wheel_event
        self.__ui.positive_sp.wheelEvent = self.__wheel_event
        self.__ui.source_combobox.wheelEvent = self.__wheel_event

        self.__ui.name_and_value_lb.setText(self.__blendshape.name)

        self.__update_disabled_state()

    def __update_disabled_state(self):
        select_info = self.__mixer.get_selection_list(self.__blendshape)

        is_enabled = self.__ui.source_combobox.currentIndex() != select_info.all_routes.index(MixerRoute.DISABLED)
        allow_manual_calibration = not self.__blendshape.value.disable_calibration

        self.__ui.negative_sp_frame.setVisible(
            is_enabled and allow_manual_calibration and self.__blendshape.value.has_center)
        self.__ui.neutral_sp_frame.setVisible(is_enabled and allow_manual_calibration)
        self.__ui.positive_sp_frame.setVisible(is_enabled and allow_manual_calibration)
        self.__ui.output_lb.setVisible(is_enabled)
        self.__ui.negative_part_pb.setVisible(is_enabled and self.__blendshape.value.has_center)
        self.__ui.positive_part_pb.setVisible(is_enabled)

    @staticmethod
    def __wheel_event(event):
        event.ignore()
