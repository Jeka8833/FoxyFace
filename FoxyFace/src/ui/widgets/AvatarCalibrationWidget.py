import logging
from collections.abc import Callable
from pathlib import Path
from typing import Any

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QCheckBox, QFileDialog, QTableWidgetItem
from blendshape_router.router.EndpointEncoderInterface import EndpointEncoderInterface

from src.config.ConfigManager import ConfigManager
from src.config.ConfigUpdateListener import ConfigUpdateListener
from src.config.schemas.avatar.AvatarConfig import AvatarConfig
from src.stream.senders.AvatarEndpoint import AvatarEndpoint
from src.ui.qtcreator.ui_AvatarCalibrationWidget import Ui_AvatarCalibrationWidget

_logger = logging.getLogger(__name__)

# 1. Add background change for enabled elements in the list
# 2. Add buttons for graph visualization
# 3. Add the possibility to disable nodes in VRchat endpoints
# 4. Fix Node column width in the table
# 5. Change background for the scrollbar panel
class AvatarCalibrationWidget(QWidget):
    __update_signal: Signal = Signal()

    def __init__(self, avatar_endpoint: AvatarEndpoint):
        super().__init__()

        self.avatar_endpoint = avatar_endpoint

        self.__ui = Ui_AvatarCalibrationWidget()
        self.__ui.setupUi(self)

        self.__endpoints_names: dict[str, EndpointEncoderInterface] = {}
        self.__input_checkboxes: dict[str, QCheckBox] = {}
        self.__output_checkboxes: dict[str, QCheckBox] = {}
        self.__selected_endpoint: EndpointEncoderInterface | None = None

        self.__register_signals()

        self.__build_checkbox_lists()
        self.__build_endpoint_list()

        self.__avatar_config_changes: ConfigUpdateListener = self.__register_avatar_config_changes()

    @property
    def avatar_endpoint(self) -> AvatarEndpoint:
        return self.__avatar_endpoint

    @avatar_endpoint.setter
    def avatar_endpoint(self, value: AvatarEndpoint):
        if not isinstance(value, AvatarEndpoint):
            raise TypeError("value must be of type AvatarEndpoint")

        self.__avatar_endpoint = value

    def closeEvent(self, event, /):
        super().closeEvent(event)

        self.__avatar_config_changes.unregister()
        self.__unregister_signal()

    def __register_signals(self):
        self.__update_signal.connect(self.__solvers_update)
        self.__ui.endpoint_enable_cb.toggled.connect(self.__changed_enable_cb)
        self.__ui.endpoint_test_btn.toggled.connect(self.__changed_test_btn)
        self.__ui.apply_btn.clicked.connect(self.__apply_btn)
        self.__ui.avatar_reset_btn.clicked.connect(self.__reset_avatar_but)
        self.__ui.avatar_import_btn.clicked.connect(self.__import_avatar_but)
        self.__ui.avatar_export_btn.clicked.connect(self.__export_avatar_but)
        self.__ui.endpoint_list_lw.currentRowChanged.connect(self.__endpoint_list_changed)

    def __unregister_signal(self):
        self.__update_signal.disconnect(self.__solvers_update)
        self.__ui.endpoint_enable_cb.toggled.disconnect(self.__changed_enable_cb)
        self.__ui.endpoint_test_btn.toggled.disconnect(self.__changed_test_btn)
        self.__ui.apply_btn.clicked.disconnect(self.__apply_btn)
        self.__ui.avatar_reset_btn.clicked.disconnect(self.__reset_avatar_but)
        self.__ui.avatar_import_btn.clicked.disconnect(self.__import_avatar_but)
        self.__ui.avatar_export_btn.clicked.disconnect(self.__export_avatar_but)
        self.__ui.endpoint_list_lw.currentRowChanged.disconnect(self.__endpoint_list_changed)

    def __build_endpoint_list(self):
        for endpoint in self.avatar_endpoint.endpoints:
            self.__endpoints_names[endpoint.id_str()] = endpoint

            self.__ui.endpoint_list_lw.addItem(endpoint.id_str())

        self.__ui.endpoint_list_lw.setCurrentRow(0)

    def __build_checkbox_lists(self):
        self.__build_solver_checkboxes(
            self.avatar_endpoint.solver_inputs,
            self.__ui.solver_input_scroll_widget,
            self.__input_checkboxes,
            lambda: self.avatar_endpoint.config_manager.config.disable_solver_input_nodes
        )
        self.__build_solver_checkboxes(
            self.avatar_endpoint.solver_outputs,
            self.__ui.solver_output_scroll_area_widget,
            self.__output_checkboxes,
            lambda: self.avatar_endpoint.config_manager.config.disable_solver_output_nodes
        )

    def __build_solver_checkboxes(self, nodes, widget, storage_dict, get_disabled_nodes: Callable[[], set[str]]):
        layout = QVBoxLayout()
        for node in sorted(nodes, key=lambda x: x.id):
            checkbox = QCheckBox(node.id, parent=self)

            checkbox.toggled.connect(
                lambda checked, id_=node.id, getter=get_disabled_nodes:
                self.__checkbox_changed(checked, id_, getter)
            )
            layout.addWidget(checkbox)
            storage_dict[node.id] = checkbox

        widget.setLayout(layout)

    def __solvers_update(self):
        disabled_inputs = self.avatar_endpoint.config_manager.config.disable_solver_input_nodes
        self.__update_checkbox_states(self.__input_checkboxes, disabled_inputs)

        disabled_outputs = self.avatar_endpoint.config_manager.config.disable_solver_output_nodes
        self.__update_checkbox_states(self.__output_checkboxes, disabled_outputs)

    @staticmethod
    def __update_checkbox_states(storage_dict: dict[str, QCheckBox], disabled_nodes: set[str]):
        for node_id, checkbox in storage_dict.items():
            is_enabled = node_id not in disabled_nodes

            if checkbox.isChecked() != is_enabled:
                checkbox.blockSignals(True)
                checkbox.setChecked(is_enabled)
                checkbox.blockSignals(False)

    def __endpoint_list_changed(self):
        selected_endpoint_text = self.__ui.endpoint_list_lw.currentItem().text()

        for endpoint in self.avatar_endpoint.endpoints:
            if endpoint.id_str() == selected_endpoint_text:
                self.__selected_endpoint = endpoint
                break

        if self.__selected_endpoint is None:
            return

        self.__ui.endpoint_name_lb.setText(self.__selected_endpoint.id_str())

        self.__ui.endpoint_enable_cb.setChecked(
            self.__selected_endpoint.id_str() not in self.avatar_endpoint.config_manager.config.disable_output_encoders
        )

        self.__changed_test_btn(self.__ui.endpoint_test_btn.isChecked())

        self.__ui.used_nodes_table.setRowCount(0)
        for i, (node, step) in enumerate(self.__selected_endpoint.get_used_nodes().items()):
            self.__ui.used_nodes_table.insertRow(i)
            self.__ui.used_nodes_table.setItem(i, 0, QTableWidgetItem(node.id))
            self.__ui.used_nodes_table.setItem(i, 1, QTableWidgetItem(self.__format_float(node.min_value)))
            self.__ui.used_nodes_table.setItem(i, 2, QTableWidgetItem(self.__format_float(node.max_value)))
            self.__ui.used_nodes_table.setItem(i, 3, QTableWidgetItem(self.__format_float(step.value)))

    @staticmethod
    def __format_float(value: float) -> str:
        if value == 0 or abs(value) >= 1e-2:
            return f"{value:.2f}"
        else:
            return f"{value:.2e}"

    @staticmethod
    def __checkbox_changed(checked: bool, id_: str, get_disabled_nodes: Callable[[], set[str]]):
        if checked:
            get_disabled_nodes().discard(id_)
        else:
            get_disabled_nodes().add(id_)

    def __register_avatar_config_changes(self) -> ConfigUpdateListener[AvatarConfig]:
        watch_array: list[Callable[[AvatarConfig], Any]] = [
            lambda config: config.disable_solver_input_nodes,
            lambda config: config.disable_solver_output_nodes,
            lambda config: config.disable_output_encoders
        ]

        return self.avatar_endpoint.config_manager.create_update_listener(self.__avatar_config_changed, watch_array,
                                                                          True)

    def __avatar_config_changed(self, config_manager: ConfigManager[AvatarConfig]):
        self.__update_signal.emit()

    def __changed_enable_cb(self):
        is_checked = self.__ui.endpoint_enable_cb.isChecked()
        if not is_checked:
            self.__ui.endpoint_test_btn.setChecked(False)

        selected_endpoint = self.__selected_endpoint
        if selected_endpoint is None:
            return

        if is_checked:
            self.avatar_endpoint.config_manager.config.disable_output_encoders.discard(selected_endpoint.id_str())
        else:
            self.avatar_endpoint.config_manager.config.disable_output_encoders.add(selected_endpoint.id_str())

    def __changed_test_btn(self, state: bool):
        if state:
            self.__ui.endpoint_test_btn.setText("Stop")

            selected_endpoint = self.__selected_endpoint
            if selected_endpoint is None:
                return

            self.avatar_endpoint.test_endpoint_callable(selected_endpoint)
        else:
            self.__ui.endpoint_test_btn.setText("Start")

            self.avatar_endpoint.stop_all_test_endpoint_callable()

    def __apply_btn(self):
        self.avatar_endpoint.config_manager.write()

    def __reset_avatar_but(self):
        self.avatar_endpoint.config_manager.hard_reset()

    def __import_avatar_but(self):
        try:
            file_path, _ = QFileDialog.getOpenFileName(
                self,
                "Open Avatar Config File",
                "",
                "JSON Files (*.json)"
            )

            if file_path:
                self.avatar_endpoint.config_manager.import_file_or_crash(Path(file_path))
        except Exception:
            _logger.warning("Failed to import avatar config", exc_info=True, stack_info=True)

    def __export_avatar_but(self):
        try:
            file_path, _ = QFileDialog.getSaveFileName(
                self,
                "Export Avatar Config File",
                "",
                "JSON Files (*.json)"
            )

            if file_path:
                self.avatar_endpoint.config_manager.export_file(Path(file_path))
        except Exception:
            _logger.warning("Failed to export avatar config", exc_info=True, stack_info=True)
