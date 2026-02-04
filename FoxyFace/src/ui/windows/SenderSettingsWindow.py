import logging

from PySide6.QtWidgets import QFileDialog

from src.config.ConfigManager import ConfigManager
from src.ui.FoxyWindow import FoxyWindow
from src.ui.qtcreator.ui_SenderSettings import Ui_SenderSettings

_logger = logging.getLogger(__name__)


class SenderSettingsWindow(FoxyWindow):

    def __init__(self, config_manager: ConfigManager):
        super().__init__()

        self.__config_manager = config_manager

        self.__ui = Ui_SenderSettings()
        self.__ui.setupUi(self)

        self.__ui.save_btn.clicked.connect(self.__save)

        self.__bind_file_buttons()
        self.__bind_sliders_labels()
        self.__disable_scroll_events()
        self.__set_default_values()

        self.show()

    def __bind_file_buttons(self):
        # Solvers (File Selection)
        self.__ui.vrchat_solver_model_btn.clicked.connect(
            lambda: self.__open_file_dialog(self.__ui.vrchat_solver_model_le, 'Open Solver Model',
                                            'JSON Files (*.json)'))
        self.__ui.ifm_solver_model_btn.clicked.connect(
            lambda: self.__open_file_dialog(self.__ui.ifm_solver_model_le, 'Open Solver Model', 'JSON Files (*.json)'))
        self.__ui.meowface_solver_model_btn.clicked.connect(
            lambda: self.__open_file_dialog(self.__ui.meowface_solver_model_le, 'Open Solver Model',
                                            'JSON Files (*.json)'))
        self.__ui.foxyface_solver_model_btn.clicked.connect(
            lambda: self.__open_file_dialog(self.__ui.foxyface_solver_model_le, 'Open Solver Model',
                                            'JSON Files (*.json)'))

        # Avatar Configs (File Selection)
        self.__ui.ifm_avatar_config_btn.clicked.connect(
            lambda: self.__open_file_dialog(self.__ui.ifm_avatar_config_le, 'Open Avatar Config',
                                            'JSON Files (*.json)'))
        self.__ui.meowface_avatar_config_btn.clicked.connect(
            lambda: self.__open_file_dialog(self.__ui.meowface_avatar_config_le, 'Open Avatar Config',
                                            'JSON Files (*.json)'))
        self.__ui.foxyface_avatar_config_btn.clicked.connect(
            lambda: self.__open_file_dialog(self.__ui.foxyface_avatar_config_le, 'Open Avatar Config',
                                            'JSON Files (*.json)'))

        # Avatar Configs (Folder Selection)
        self.__ui.vrchat_avatar_config_btn.clicked.connect(
            lambda: self.__open_folder_dialog(self.__ui.vrchat_avatar_config_le, 'Open Avatar Config Folder'))

    def __open_file_dialog(self, line_edit, caption, file_filter):
        filename, _ = QFileDialog.getOpenFileName(parent=self, caption=caption, dir='.', filter=file_filter)
        if filename:
            line_edit.setText(filename)

    def __open_folder_dialog(self, line_edit, caption):
        folder = QFileDialog.getExistingDirectory(parent=self, caption=caption, dir='.')
        if folder:
            line_edit.setText(folder)

    def __bind_sliders_labels(self):
        self.__ui.vrchat_solver_sercision_slider.valueChanged.connect(
            lambda v: self.__ui.vrchat_solver_sercision_lb.setText(f"Solver Precision ({v}%): "))
        self.__ui.ifm_solver_sercision_slider.valueChanged.connect(
            lambda v: self.__ui.ifm_solver_sercision_lb.setText(f"Solver Precision ({v}%): "))
        self.__ui.meowface_solver_percision_slider.valueChanged.connect(
            lambda v: self.__ui.meowface_solver_percision_lb.setText(f"Solver Precision ({v}%): "))
        self.__ui.foxyface_solver_sercision_slider.valueChanged.connect(
            lambda v: self.__ui.foxyface_solver_sercision_lb.setText(f"Solver Precision ({v}%): "))

    def __disable_scroll_events(self):
        widgets = [
            self.__ui.vrchat_avatare_request_period_sb,
            self.__ui.vrchat_error_sleep_time_sb,
            self.__ui.vrchat_close_connectio_sb,
            self.__ui.vrchat_zeroconf_sb,
            self.__ui.vrchat_solver_sercision_slider,
            self.__ui.vrchat_solver_threads_sb,
            self.__ui.vrchat_solver_max_fps_sb,
            self.__ui.vrchat_cache_invalidate_sb,
            self.__ui.vrchat_cache_sync_sb,
            self.__ui.vrchat_cache_float_percision_sb,
            self.__ui.vrchat_cache_bundle_sb,

            self.__ui.ifm_port_sb,
            self.__ui.ifm_solver_sercision_slider,
            self.__ui.ifm_solver_threads_sb,
            self.__ui.ifm_solver_max_fps_sb,
            self.__ui.ifm_cache_invalidate_sb,
            self.__ui.ifm_cache_sync_sb,
            self.__ui.ifm_cache_ping_sb,
            self.__ui.ifm_cache_float_percision_sb,

            self.__ui.meowface_port_sb,
            self.__ui.meowface_solver_percision_slider,
            self.__ui.meowface_solver_threads_sb,
            self.__ui.meowface_solver_max_fps_sb,
            self.__ui.meowface_cache_invalidate_sb,
            self.__ui.meowface_cache_sync_sb,
            self.__ui.meowface_cache_ping_sb,
            self.__ui.meowface_cache_float_percision_sb,

            self.__ui.foxyface_port_sb,
            self.__ui.foxyface_solver_sercision_slider,
            self.__ui.foxyface_solver_threads_sb,
            self.__ui.foxyface_solver_max_fps_sb,
            self.__ui.foxyface_cache_invalidate_sb,
            self.__ui.foxyface_cache_sync_sb,
            self.__ui.foxyface_cache_ping_sb,
            self.__ui.foxyface_cache_float_percision_sb,
        ]

        for widget in widgets:
            widget.wheelEvent = self.__wheel_event

    def __set_default_values(self):
        self.__ui.vrchat_enable_cb.setChecked(self.__config_manager.config.sender.vrchat.enabled)
        self.__ui.vrchat_avatare_request_period_sb.setValue(
            self.__config_manager.config.sender.vrchat.avatar_update_period)
        self.__ui.vrchat_error_sleep_time_sb.setValue(
            self.__config_manager.config.sender.vrchat.avatar_error_sleep_time)
        self.__ui.vrchat_close_connectio_sb.setValue(
            self.__config_manager.config.sender.vrchat.avatar_close_connection_after_retries)
        self.__ui.vrchat_zeroconf_sb.setValue(self.__config_manager.config.sender.vrchat.zeroconf_timeout)
        self.__ui.vrchat_enable_solver_cb.setChecked(self.__config_manager.config.sender.vrchat.solver_enabled)
        self.__ui.vrchat_solver_model_le.setText(self.__config_manager.config.sender.vrchat.solver_model_path)
        self.__ui.vrchat_solver_sercision_slider.setValue(
            int(self.__config_manager.config.sender.vrchat.solver_interleaved_vertices_percentage * 100))
        self.__ui.vrchat_solver_threads_sb.setValue(self.__config_manager.config.sender.vrchat.solver_threads)
        self.__ui.vrchat_solver_max_fps_sb.setValue(self.__config_manager.config.sender.vrchat.solver_max_cps)
        self.__ui.vrchat_cache_invalidate_sb.setValue(
            self.__config_manager.config.sender.vrchat.cache_invalidate_timeout)
        self.__ui.vrchat_cache_sync_sb.setValue(self.__config_manager.config.sender.vrchat.cache_full_sync_period)
        self.__ui.vrchat_cache_float_percision_sb.setValue(
            self.__config_manager.config.sender.vrchat.cache_float_precision)
        self.__ui.vrchat_cache_bundle_sb.setValue(self.__config_manager.config.sender.vrchat.osc_bundle_size)
        self.__ui.vrchat_avatar_config_le.setText(self.__config_manager.config.sender.vrchat.avatar_config_folder)

        self.__ui.ifm_enable_cb.setChecked(self.__config_manager.config.sender.ifacialmocap.enabled)
        self.__ui.ifm_use_facemotion3d_protocol.setChecked(
            self.__config_manager.config.sender.ifacialmocap.facemotion3d_compatibility)
        self.__ui.ifm_ip_auto_find_cb.setChecked(self.__config_manager.config.sender.ifacialmocap.auto_connect_enabled)
        self.__ui.ifm_ip_le.setText(self.__config_manager.config.sender.ifacialmocap.ip)
        self.__ui.ifm_port_sb.setValue(self.__config_manager.config.sender.ifacialmocap.port)
        self.__ui.ifm_enable_solver_cb.setChecked(self.__config_manager.config.sender.ifacialmocap.solver_enabled)
        self.__ui.ifm_solver_model_le.setText(self.__config_manager.config.sender.ifacialmocap.solver_model_path)
        self.__ui.ifm_solver_sercision_slider.setValue(
            int(self.__config_manager.config.sender.ifacialmocap.solver_interleaved_vertices_percentage * 100))
        self.__ui.ifm_solver_threads_sb.setValue(self.__config_manager.config.sender.ifacialmocap.solver_threads)
        self.__ui.ifm_solver_max_fps_sb.setValue(self.__config_manager.config.sender.ifacialmocap.solver_max_cps)
        self.__ui.ifm_cache_invalidate_sb.setValue(
            self.__config_manager.config.sender.ifacialmocap.cache_invalidate_timeout)
        self.__ui.ifm_cache_sync_sb.setValue(self.__config_manager.config.sender.ifacialmocap.cache_full_sync_period)
        self.__ui.ifm_cache_ping_sb.setValue(
            self.__config_manager.config.sender.ifacialmocap.udp_ping_interval)
        self.__ui.ifm_cache_float_percision_sb.setValue(
            self.__config_manager.config.sender.ifacialmocap.cache_float_precision)
        self.__ui.ifm_avatar_config_le.setText(self.__config_manager.config.sender.ifacialmocap.avatar_config_file)

        self.__ui.meowface_enable_cb.setChecked(self.__config_manager.config.sender.meowface.enabled)
        self.__ui.meowface_ip_auto_find_cb.setChecked(self.__config_manager.config.sender.meowface.auto_connect_enabled)
        self.__ui.meowface_ip_le.setText(self.__config_manager.config.sender.meowface.ip)
        self.__ui.meowface_port_sb.setValue(self.__config_manager.config.sender.meowface.port)
        self.__ui.meowface_enable_solver_cb.setChecked(self.__config_manager.config.sender.meowface.solver_enabled)
        self.__ui.meowface_solver_model_le.setText(self.__config_manager.config.sender.meowface.solver_model_path)
        self.__ui.meowface_solver_percision_slider.setValue(
            int(self.__config_manager.config.sender.meowface.solver_interleaved_vertices_percentage * 100))
        self.__ui.meowface_solver_threads_sb.setValue(self.__config_manager.config.sender.meowface.solver_threads)
        self.__ui.meowface_solver_max_fps_sb.setValue(self.__config_manager.config.sender.meowface.solver_max_cps)
        self.__ui.meowface_cache_invalidate_sb.setValue(
            self.__config_manager.config.sender.meowface.cache_invalidate_timeout)
        self.__ui.meowface_cache_sync_sb.setValue(self.__config_manager.config.sender.meowface.cache_full_sync_period)
        self.__ui.meowface_cache_ping_sb.setValue(
            self.__config_manager.config.sender.meowface.udp_ping_interval)
        self.__ui.meowface_cache_float_percision_sb.setValue(
            self.__config_manager.config.sender.meowface.cache_float_precision)
        self.__ui.meowface_avatar_config_le.setText(self.__config_manager.config.sender.meowface.avatar_config_file)

        self.__ui.foxyface_enable_cb.setChecked(self.__config_manager.config.sender.foxyface.enabled)
        self.__ui.foxyface_ip_auto_find_cb.setChecked(self.__config_manager.config.sender.foxyface.auto_connect_enabled)
        self.__ui.foxyface_ip_le.setText(self.__config_manager.config.sender.foxyface.ip)
        self.__ui.foxyface_port_sb.setValue(self.__config_manager.config.sender.foxyface.port)
        self.__ui.foxyface_enable_solver_cb.setChecked(self.__config_manager.config.sender.foxyface.solver_enabled)
        self.__ui.foxyface_solver_model_le.setText(self.__config_manager.config.sender.foxyface.solver_model_path)
        self.__ui.foxyface_solver_sercision_slider.setValue(
            int(self.__config_manager.config.sender.foxyface.solver_interleaved_vertices_percentage * 100))
        self.__ui.foxyface_solver_threads_sb.setValue(self.__config_manager.config.sender.foxyface.solver_threads)
        self.__ui.foxyface_solver_max_fps_sb.setValue(self.__config_manager.config.sender.foxyface.solver_max_cps)
        self.__ui.foxyface_cache_invalidate_sb.setValue(
            self.__config_manager.config.sender.vrchat.cache_invalidate_timeout)
        self.__ui.foxyface_cache_sync_sb.setValue(self.__config_manager.config.sender.foxyface.cache_full_sync_period)
        self.__ui.foxyface_cache_ping_sb.setValue(
            self.__config_manager.config.sender.foxyface.udp_ping_interval)
        self.__ui.foxyface_cache_float_percision_sb.setValue(
            self.__config_manager.config.sender.foxyface.cache_float_precision)
        self.__ui.foxyface_avatar_config_le.setText(self.__config_manager.config.sender.foxyface.avatar_config_file)

    def __save(self):
        try:
            self.__config_manager.config.sender.vrchat.enabled = self.__ui.vrchat_enable_cb.isChecked()
            self.__config_manager.config.sender.vrchat.avatar_update_period = self.__ui.vrchat_avatare_request_period_sb.value()
            self.__config_manager.config.sender.vrchat.avatar_error_sleep_time = self.__ui.vrchat_error_sleep_time_sb.value()
            self.__config_manager.config.sender.vrchat.avatar_close_connection_after_retries = self.__ui.vrchat_close_connectio_sb.value()
            self.__config_manager.config.sender.vrchat.zeroconf_timeout = self.__ui.vrchat_zeroconf_sb.value()
            self.__config_manager.config.sender.vrchat.solver_enabled = self.__ui.vrchat_enable_solver_cb.isChecked()
            self.__config_manager.config.sender.vrchat.solver_model_path = self.__ui.vrchat_solver_model_le.text()
            self.__config_manager.config.sender.vrchat.solver_interleaved_vertices_percentage = self.__ui.vrchat_solver_sercision_slider.value() / 100.0
            self.__config_manager.config.sender.vrchat.solver_threads = self.__ui.vrchat_solver_threads_sb.value()
            self.__config_manager.config.sender.vrchat.solver_max_cps = self.__ui.vrchat_solver_max_fps_sb.value()
            self.__config_manager.config.sender.vrchat.cache_invalidate_timeout = self.__ui.vrchat_cache_invalidate_sb.value()
            self.__config_manager.config.sender.vrchat.cache_full_sync_period = self.__ui.vrchat_cache_sync_sb.value()
            self.__config_manager.config.sender.vrchat.cache_float_precision = self.__ui.vrchat_cache_float_percision_sb.value()
            self.__config_manager.config.sender.vrchat.osc_bundle_size = self.__ui.vrchat_cache_bundle_sb.value()
            self.__config_manager.config.sender.vrchat.avatar_config_folder = self.__ui.vrchat_avatar_config_le.text()

            self.__config_manager.config.sender.ifacialmocap.enabled = self.__ui.ifm_enable_cb.isChecked()
            self.__config_manager.config.sender.ifacialmocap.facemotion3d_compatibility = self.__ui.ifm_use_facemotion3d_protocol.isChecked()
            self.__config_manager.config.sender.ifacialmocap.auto_connect_enabled = self.__ui.ifm_ip_auto_find_cb.isChecked()
            self.__config_manager.config.sender.ifacialmocap.ip = self.__ui.ifm_ip_le.text()
            self.__config_manager.config.sender.ifacialmocap.port = self.__ui.ifm_port_sb.value()
            self.__config_manager.config.sender.ifacialmocap.solver_enabled = self.__ui.ifm_enable_solver_cb.isChecked()
            self.__config_manager.config.sender.ifacialmocap.solver_model_path = self.__ui.ifm_solver_model_le.text()
            self.__config_manager.config.sender.ifacialmocap.solver_interleaved_vertices_percentage = self.__ui.ifm_solver_sercision_slider.value() / 100.0
            self.__config_manager.config.sender.ifacialmocap.solver_threads = self.__ui.ifm_solver_threads_sb.value()
            self.__config_manager.config.sender.ifacialmocap.solver_max_cps = self.__ui.ifm_solver_max_fps_sb.value()
            self.__config_manager.config.sender.ifacialmocap.cache_invalidate_timeout = self.__ui.ifm_cache_invalidate_sb.value()
            self.__config_manager.config.sender.ifacialmocap.cache_full_sync_period = self.__ui.ifm_cache_sync_sb.value()
            self.__config_manager.config.sender.ifacialmocap.udp_ping_interval = self.__ui.ifm_cache_ping_sb.value()
            self.__config_manager.config.sender.ifacialmocap.cache_float_precision = self.__ui.ifm_cache_float_percision_sb.value()
            self.__config_manager.config.sender.ifacialmocap.avatar_config_file = self.__ui.ifm_avatar_config_le.text()

            self.__config_manager.config.sender.meowface.enabled = self.__ui.meowface_enable_cb.isChecked()
            self.__config_manager.config.sender.meowface.auto_connect_enabled = self.__ui.meowface_ip_auto_find_cb.isChecked()
            self.__config_manager.config.sender.meowface.ip = self.__ui.meowface_ip_le.text()
            self.__config_manager.config.sender.meowface.port = self.__ui.meowface_port_sb.value()
            self.__config_manager.config.sender.meowface.solver_enabled = self.__ui.meowface_enable_solver_cb.isChecked()
            self.__config_manager.config.sender.meowface.solver_model_path = self.__ui.meowface_solver_model_le.text()
            self.__config_manager.config.sender.meowface.solver_interleaved_vertices_percentage = self.__ui.meowface_solver_percision_slider.value() / 100.0
            self.__config_manager.config.sender.meowface.solver_threads = self.__ui.meowface_solver_threads_sb.value()
            self.__config_manager.config.sender.meowface.solver_max_cps = self.__ui.meowface_solver_max_fps_sb.value()
            self.__config_manager.config.sender.meowface.cache_invalidate_timeout = self.__ui.meowface_cache_invalidate_sb.value()
            self.__config_manager.config.sender.meowface.cache_full_sync_period = self.__ui.meowface_cache_sync_sb.value()
            self.__config_manager.config.sender.meowface.udp_ping_interval = self.__ui.meowface_cache_ping_sb.value()
            self.__config_manager.config.sender.meowface.cache_float_precision = self.__ui.meowface_cache_float_percision_sb.value()
            self.__config_manager.config.sender.meowface.avatar_config_file = self.__ui.meowface_avatar_config_le.text()

            self.__config_manager.config.sender.foxyface.enabled = self.__ui.foxyface_enable_cb.isChecked()
            self.__config_manager.config.sender.foxyface.auto_connect_enabled = self.__ui.foxyface_ip_auto_find_cb.isChecked()
            self.__config_manager.config.sender.foxyface.ip = self.__ui.foxyface_ip_le.text()
            self.__config_manager.config.sender.foxyface.port = self.__ui.foxyface_port_sb.value()
            self.__config_manager.config.sender.foxyface.solver_enabled = self.__ui.foxyface_enable_solver_cb.isChecked()
            self.__config_manager.config.sender.foxyface.solver_model_path = self.__ui.foxyface_solver_model_le.text()
            self.__config_manager.config.sender.foxyface.solver_interleaved_vertices_percentage = self.__ui.foxyface_solver_sercision_slider.value() / 100.0
            self.__config_manager.config.sender.foxyface.solver_threads = self.__ui.foxyface_solver_threads_sb.value()
            self.__config_manager.config.sender.foxyface.solver_max_cps = self.__ui.foxyface_solver_max_fps_sb.value()
            self.__config_manager.config.sender.foxyface.cache_invalidate_timeout = self.__ui.foxyface_cache_invalidate_sb.value()
            self.__config_manager.config.sender.foxyface.cache_full_sync_period = self.__ui.foxyface_cache_sync_sb.value()
            self.__config_manager.config.sender.foxyface.udp_ping_interval = self.__ui.foxyface_cache_ping_sb.value()
            self.__config_manager.config.sender.foxyface.cache_float_precision = self.__ui.foxyface_cache_float_percision_sb.value()
            self.__config_manager.config.sender.foxyface.avatar_config_file = self.__ui.foxyface_avatar_config_le.text()

            self.__config_manager.write()
        except Exception:
            _logger.exception("Failed to save config")

    @staticmethod
    def __wheel_event(event):
        event.ignore()
