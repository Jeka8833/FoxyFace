import logging
import threading
import time

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QSizePolicy, QSpacerItem

from src.config.ConfigManager import ConfigManager
from src.config.schemas.core.ProcessingConfig import ProcessingConfig
from src.pipline.ProcessingPipeline import ProcessingPipeline
from src.stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum
from src.ui.FoxyWindow import FoxyWindow
from src.ui.qtcreator.ui_CalibrationSettings import Ui_CalibrationWindow
from src.ui.widgets.CalibrationWidget import CalibrationWidget

_head_global: list[GeneralBlendShapeEnum] = [GeneralBlendShapeEnum.HeadPitch, GeneralBlendShapeEnum.HeadRoll,
                                             GeneralBlendShapeEnum.HeadYaw, GeneralBlendShapeEnum.HeadX,
                                             GeneralBlendShapeEnum.HeadY, GeneralBlendShapeEnum.HeadZ]

_head_upper: list[GeneralBlendShapeEnum] = [GeneralBlendShapeEnum.BrowDownLeft, GeneralBlendShapeEnum.BrowDownRight,
                                            GeneralBlendShapeEnum.BrowInnerUp, GeneralBlendShapeEnum.BrowOuterUpLeft,
                                            GeneralBlendShapeEnum.BrowOuterUpRight, GeneralBlendShapeEnum.EyeBlinkLeft,
                                            GeneralBlendShapeEnum.EyeBlinkRight, GeneralBlendShapeEnum.EyeSquintLeft,
                                            GeneralBlendShapeEnum.EyeSquintRight, GeneralBlendShapeEnum.EyeWideLeft,
                                            GeneralBlendShapeEnum.EyeWideRight, GeneralBlendShapeEnum.EyeXLeft,
                                            GeneralBlendShapeEnum.EyeXRight, GeneralBlendShapeEnum.EyeYLeft,
                                            GeneralBlendShapeEnum.EyeYRight]

_head_bottom: list[GeneralBlendShapeEnum] = [GeneralBlendShapeEnum.CheekPuffLeft, GeneralBlendShapeEnum.CheekPuffRight,
                                             GeneralBlendShapeEnum.CheekSuckLeft, GeneralBlendShapeEnum.CheekSuckRight,
                                             GeneralBlendShapeEnum.JawOpen, GeneralBlendShapeEnum.JawForward,
                                             GeneralBlendShapeEnum.JawLeft, GeneralBlendShapeEnum.JawRight,
                                             GeneralBlendShapeEnum.NoseSneerLeft, GeneralBlendShapeEnum.NoseSneerRight,
                                             GeneralBlendShapeEnum.MouthFunnel, GeneralBlendShapeEnum.MouthPucker,
                                             GeneralBlendShapeEnum.MouthLeft, GeneralBlendShapeEnum.MouthRight,
                                             GeneralBlendShapeEnum.MouthRollUpper, GeneralBlendShapeEnum.MouthRollLower,
                                             GeneralBlendShapeEnum.MouthRaiserUpper,
                                             GeneralBlendShapeEnum.MouthRaiserLower, GeneralBlendShapeEnum.MouthClosed,
                                             GeneralBlendShapeEnum.MouthSmileLeft,
                                             GeneralBlendShapeEnum.MouthSmileRight,
                                             GeneralBlendShapeEnum.MouthFrownLeft,
                                             GeneralBlendShapeEnum.MouthFrownRight,
                                             GeneralBlendShapeEnum.MouthDimpleLeft,
                                             GeneralBlendShapeEnum.MouthDimpleRight,
                                             GeneralBlendShapeEnum.MouthUpperUpLeft,
                                             GeneralBlendShapeEnum.MouthUpperUpRight,
                                             GeneralBlendShapeEnum.MouthLowerDownLeft,
                                             GeneralBlendShapeEnum.MouthLowerDownRight,
                                             GeneralBlendShapeEnum.MouthPressLeft,
                                             GeneralBlendShapeEnum.MouthPressRight,
                                             GeneralBlendShapeEnum.MouthStretchLeft,
                                             GeneralBlendShapeEnum.MouthStretchRight, GeneralBlendShapeEnum.TongueOut,
                                             GeneralBlendShapeEnum.TongueUp, GeneralBlendShapeEnum.TongueDown,
                                             GeneralBlendShapeEnum.TongueLeft, GeneralBlendShapeEnum.TongueRight,
                                             GeneralBlendShapeEnum.TongueRoll, GeneralBlendShapeEnum.TongueBendDown,
                                             GeneralBlendShapeEnum.TongueCurlUp, GeneralBlendShapeEnum.TongueSquish,
                                             GeneralBlendShapeEnum.TongueFlat, GeneralBlendShapeEnum.TongueTwistLeft,
                                             GeneralBlendShapeEnum.TongueTwistRight, GeneralBlendShapeEnum.CheekPuff,
                                             GeneralBlendShapeEnum.CheekSquintLeft,
                                             GeneralBlendShapeEnum.CheekSquintRight]

_logger = logging.getLogger(__name__)


class CalibrationWindow(FoxyWindow):
    update_statistic_event: Signal = Signal(object, object)

    def __init__(self, config_manager: ConfigManager, processing_pipeline: ProcessingPipeline):
        super().__init__()

        self.__config_manager = config_manager
        self.__processing_pipeline = processing_pipeline

        self.__ui = Ui_CalibrationWindow()
        self.__ui.setupUi(self)

        self.__calibration_widgets: dict[GeneralBlendShapeEnum, CalibrationWidget] = dict[
            GeneralBlendShapeEnum, CalibrationWidget]()
        self.__last_label_update_time: int = time.perf_counter_ns()
        self.__set_default_values()

        self.__ui.full_reset_btn.clicked.connect(self.__full_reset)
        self.__ui.save_btn.clicked.connect(self.__save)

        self.update_statistic_event.connect(self.__update_statistic_value)

        self.show()

        self.__thread = threading.Thread(target=self.__statistic_loop, daemon=True, name="Statistic Thread")
        self.__thread.start()

    def closeEvent(self, event, /):
        super().closeEvent(event)

        for widget in self.__calibration_widgets.values():
            widget.close()

        self.__ui.full_reset_btn.clicked.disconnect(self.__full_reset)
        self.__ui.save_btn.clicked.disconnect(self.__save)

        self.update_statistic_event.disconnect(self.__update_statistic_value)

    def __reset_head_center(self):
        self.__config_manager.config.media_pipe.head_rotation_transformation = []

    def __full_reset(self):
        self.__config_manager.config.processing = ProcessingConfig()
        self.__save()

    def __save(self):
        self.__config_manager.write()

    def __set_default_values(self):
        for enu in _head_global:
            calibration_widget = CalibrationWidget(enu, self.__config_manager)

            self.__ui.head_global_container.addWidget(calibration_widget)
            self.__calibration_widgets[enu] = calibration_widget
        self.__ui.head_global_container.addSpacerItem(
            QSpacerItem(20, 20, QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding))

        _head_upper.sort(key=lambda element: element.name)
        for enu in _head_upper:
            calibration_widget = CalibrationWidget(enu, self.__config_manager)

            self.__ui.head_upper_container.addWidget(calibration_widget)
            self.__calibration_widgets[enu] = calibration_widget
        self.__ui.head_upper_container.addSpacerItem(
            QSpacerItem(20, 20, QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding))

        _head_bottom.sort(key=lambda element: element.name)
        for enu in _head_bottom:
            calibration_widget = CalibrationWidget(enu, self.__config_manager)

            self.__ui.head_bottom_container.addWidget(calibration_widget)
            self.__calibration_widgets[enu] = calibration_widget
        self.__ui.head_bottom_container.addSpacerItem(
            QSpacerItem(20, 20, QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding))

    def __statistic_loop(self):
        while not self.is_closed.is_set():
            try:
                input_frame = None
                try:
                    input_frame = self.__processing_pipeline.get_ui_stream_input().poll(timeout=1.0)
                except TimeoutError:
                    pass

                output_frame = None
                try:
                    output_frame = self.__processing_pipeline.get_ui_stream_output().poll(timeout=1.0)
                except TimeoutError:
                    pass

                self.update_statistic_event.emit(input_frame.blend_shapes if input_frame else None,
                                                 output_frame.blend_shapes if output_frame else None)
            except InterruptedError:
                return
            except Exception:
                _logger.warning("Error in statistic thread", exc_info=True, stack_info=True)

    def __update_statistic_value(self, input_values: dict[GeneralBlendShapeEnum, float] | None,
                                 output_values: dict[GeneralBlendShapeEnum, float] | None):
        if time.perf_counter_ns() - self.__last_label_update_time > 250_000_000 or (
                not input_values and not output_values):
            update_label = True
            self.__last_label_update_time = time.perf_counter_ns()
        else:
            update_label = False

        for key, widget in self.__calibration_widgets.items():
            widget.update_value(update_label, input_values.get(key) if input_values else None,
                                output_values.get(key) if output_values else None)
