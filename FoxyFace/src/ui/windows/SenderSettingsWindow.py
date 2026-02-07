import logging

from PySide6.QtWidgets import QFileDialog

from src.config.ConfigManager import ConfigManager
from src.config.schemas.main.core.sender.FoxyFaceSenderConfig import FoxyFaceSenderConfig
from src.config.schemas.main.core.sender.IFacialMocapSenderConfig import IFacialMocapSenderConfig
from src.config.schemas.main.core.sender.MeowFaceSenderConfig import MeowFaceSenderConfig
from src.config.schemas.main.core.sender.VRChatSenderConfig import VRChatSenderConfig
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
        vrchat_config: VRChatSenderConfig = self.__config_manager.config.sender.vrchat

        self.__ui.vrchat_enable_cb.setChecked(vrchat_config.enabled)
        self.__ui.vrchat_avatare_request_period_sb.setValue(
            vrchat_config.avatar_update_period)
        self.__ui.vrchat_error_sleep_time_sb.setValue(
            vrchat_config.avatar_error_sleep_time)
        self.__ui.vrchat_close_connectio_sb.setValue(
            vrchat_config.avatar_close_connection_after_retries)
        self.__ui.vrchat_zeroconf_sb.setValue(vrchat_config.zeroconf_timeout)
        self.__ui.vrchat_enable_solver_cb.setChecked(vrchat_config.solver_enabled)
        self.__ui.vrchat_solver_model_le.setText(vrchat_config.solver_model_path)
        self.__ui.vrchat_solver_sercision_slider.setValue(
            int(vrchat_config.solver_interleaved_vertices_percentage * 100))
        self.__ui.vrchat_solver_threads_sb.setValue(vrchat_config.solver_threads)
        self.__ui.vrchat_solver_max_fps_sb.setValue(vrchat_config.solver_max_cps)
        self.__ui.vrchat_cache_invalidate_sb.setValue(
            vrchat_config.cache_invalidate_timeout)
        self.__ui.vrchat_cache_sync_sb.setValue(vrchat_config.cache_full_sync_period)
        self.__ui.vrchat_cache_float_percision_sb.setValue(
            vrchat_config.cache_float_precision)
        self.__ui.vrchat_cache_bundle_sb.setValue(vrchat_config.osc_bundle_size)
        self.__ui.vrchat_avatar_config_le.setText(vrchat_config.avatar_config_folder)

        ifacialmocap_config: IFacialMocapSenderConfig = self.__config_manager.config.sender.ifacialmocap

        self.__ui.ifm_enable_cb.setChecked(ifacialmocap_config.enabled)
        self.__ui.ifm_use_facemotion3d_protocol.setChecked(ifacialmocap_config.facemotion3d_compatibility)
        self.__ui.ifm_ip_auto_find_cb.setChecked(ifacialmocap_config.auto_connect_enabled)
        self.__ui.ifm_ip_le.setText(ifacialmocap_config.ip)
        self.__ui.ifm_port_sb.setValue(ifacialmocap_config.port)
        self.__ui.ifm_enable_solver_cb.setChecked(ifacialmocap_config.solver_enabled)
        self.__ui.ifm_solver_model_le.setText(ifacialmocap_config.solver_model_path)
        self.__ui.ifm_solver_sercision_slider.setValue(
            int(ifacialmocap_config.solver_interleaved_vertices_percentage * 100))
        self.__ui.ifm_solver_threads_sb.setValue(ifacialmocap_config.solver_threads)
        self.__ui.ifm_solver_max_fps_sb.setValue(ifacialmocap_config.solver_max_cps)
        self.__ui.ifm_cache_invalidate_sb.setValue(ifacialmocap_config.cache_invalidate_timeout)
        self.__ui.ifm_cache_sync_sb.setValue(ifacialmocap_config.cache_full_sync_period)
        self.__ui.ifm_cache_ping_sb.setValue(ifacialmocap_config.udp_ping_interval)
        self.__ui.ifm_cache_float_percision_sb.setValue(ifacialmocap_config.cache_float_precision)
        self.__ui.ifm_avatar_config_le.setText(ifacialmocap_config.avatar_config_file)

        meowface_config: MeowFaceSenderConfig = self.__config_manager.config.sender.meowface

        self.__ui.meowface_enable_cb.setChecked(meowface_config.enabled)
        self.__ui.meowface_ip_auto_find_cb.setChecked(meowface_config.auto_connect_enabled)
        self.__ui.meowface_ip_le.setText(meowface_config.ip)
        self.__ui.meowface_port_sb.setValue(meowface_config.port)
        self.__ui.meowface_enable_solver_cb.setChecked(meowface_config.solver_enabled)
        self.__ui.meowface_solver_model_le.setText(meowface_config.solver_model_path)
        self.__ui.meowface_solver_percision_slider.setValue(
            int(meowface_config.solver_interleaved_vertices_percentage * 100))
        self.__ui.meowface_solver_threads_sb.setValue(meowface_config.solver_threads)
        self.__ui.meowface_solver_max_fps_sb.setValue(meowface_config.solver_max_cps)
        self.__ui.meowface_cache_invalidate_sb.setValue(meowface_config.cache_invalidate_timeout)
        self.__ui.meowface_cache_sync_sb.setValue(meowface_config.cache_full_sync_period)
        self.__ui.meowface_cache_ping_sb.setValue(meowface_config.udp_ping_interval)
        self.__ui.meowface_cache_float_percision_sb.setValue(meowface_config.cache_float_precision)
        self.__ui.meowface_avatar_config_le.setText(meowface_config.avatar_config_file)

        foxyface_config: FoxyFaceSenderConfig = self.__config_manager.config.sender.foxyface

        self.__ui.foxyface_enable_cb.setChecked(foxyface_config.enabled)
        self.__ui.foxyface_ip_auto_find_cb.setChecked(foxyface_config.auto_connect_enabled)
        self.__ui.foxyface_ip_le.setText(foxyface_config.ip)
        self.__ui.foxyface_port_sb.setValue(foxyface_config.port)
        self.__ui.host_read_timeout_sb.setValue(foxyface_config.host_read_timeout)
        self.__ui.foxyface_enable_solver_cb.setChecked(foxyface_config.solver_enabled)
        self.__ui.foxyface_solver_model_le.setText(foxyface_config.solver_model_path)
        self.__ui.foxyface_solver_sercision_slider.setValue(
            int(foxyface_config.solver_interleaved_vertices_percentage * 100))
        self.__ui.foxyface_solver_threads_sb.setValue(foxyface_config.solver_threads)
        self.__ui.foxyface_solver_max_fps_sb.setValue(foxyface_config.solver_max_cps)
        self.__ui.foxyface_cache_invalidate_sb.setValue(foxyface_config.cache_invalidate_timeout)
        self.__ui.foxyface_cache_sync_sb.setValue(foxyface_config.cache_full_sync_period)
        self.__ui.foxyface_cache_ping_sb.setValue(foxyface_config.udp_ping_interval)
        self.__ui.foxyface_cache_float_percision_sb.setValue(foxyface_config.cache_float_precision)
        self.__ui.foxyface_avatar_config_le.setText(foxyface_config.avatar_config_file)

    def __save(self):
        try:
            vrchat_config: VRChatSenderConfig = self.__config_manager.config.sender.vrchat

            vrchat_config.enabled = self.__ui.vrchat_enable_cb.isChecked()
            vrchat_config.avatar_update_period = self.__ui.vrchat_avatare_request_period_sb.value()
            vrchat_config.avatar_error_sleep_time = self.__ui.vrchat_error_sleep_time_sb.value()
            vrchat_config.avatar_close_connection_after_retries = self.__ui.vrchat_close_connectio_sb.value()
            vrchat_config.zeroconf_timeout = self.__ui.vrchat_zeroconf_sb.value()
            vrchat_config.solver_enabled = self.__ui.vrchat_enable_solver_cb.isChecked()
            vrchat_config.solver_model_path = self.__ui.vrchat_solver_model_le.text()
            vrchat_config.solver_interleaved_vertices_percentage = self.__ui.vrchat_solver_sercision_slider.value() / 100.0
            vrchat_config.solver_threads = self.__ui.vrchat_solver_threads_sb.value()
            vrchat_config.solver_max_cps = self.__ui.vrchat_solver_max_fps_sb.value()
            vrchat_config.cache_invalidate_timeout = self.__ui.vrchat_cache_invalidate_sb.value()
            vrchat_config.cache_full_sync_period = self.__ui.vrchat_cache_sync_sb.value()
            vrchat_config.cache_float_precision = self.__ui.vrchat_cache_float_percision_sb.value()
            vrchat_config.osc_bundle_size = self.__ui.vrchat_cache_bundle_sb.value()
            vrchat_config.avatar_config_folder = self.__ui.vrchat_avatar_config_le.text()

            ifacialmocap_config: IFacialMocapSenderConfig = self.__config_manager.config.sender.ifacialmocap

            ifacialmocap_config.enabled = self.__ui.ifm_enable_cb.isChecked()
            ifacialmocap_config.facemotion3d_compatibility = self.__ui.ifm_use_facemotion3d_protocol.isChecked()
            ifacialmocap_config.auto_connect_enabled = self.__ui.ifm_ip_auto_find_cb.isChecked()
            ifacialmocap_config.ip = self.__ui.ifm_ip_le.text()
            ifacialmocap_config.port = self.__ui.ifm_port_sb.value()
            ifacialmocap_config.solver_enabled = self.__ui.ifm_enable_solver_cb.isChecked()
            ifacialmocap_config.solver_model_path = self.__ui.ifm_solver_model_le.text()
            ifacialmocap_config.solver_interleaved_vertices_percentage = self.__ui.ifm_solver_sercision_slider.value() / 100.0
            ifacialmocap_config.solver_threads = self.__ui.ifm_solver_threads_sb.value()
            ifacialmocap_config.solver_max_cps = self.__ui.ifm_solver_max_fps_sb.value()
            ifacialmocap_config.cache_invalidate_timeout = self.__ui.ifm_cache_invalidate_sb.value()
            ifacialmocap_config.cache_full_sync_period = self.__ui.ifm_cache_sync_sb.value()
            ifacialmocap_config.udp_ping_interval = self.__ui.ifm_cache_ping_sb.value()
            ifacialmocap_config.cache_float_precision = self.__ui.ifm_cache_float_percision_sb.value()
            ifacialmocap_config.avatar_config_file = self.__ui.ifm_avatar_config_le.text()

            meowface_config: MeowFaceSenderConfig = self.__config_manager.config.sender.meowface

            meowface_config.enabled = self.__ui.meowface_enable_cb.isChecked()
            meowface_config.auto_connect_enabled = self.__ui.meowface_ip_auto_find_cb.isChecked()
            meowface_config.ip = self.__ui.meowface_ip_le.text()
            meowface_config.port = self.__ui.meowface_port_sb.value()
            meowface_config.solver_enabled = self.__ui.meowface_enable_solver_cb.isChecked()
            meowface_config.solver_model_path = self.__ui.meowface_solver_model_le.text()
            meowface_config.solver_interleaved_vertices_percentage = self.__ui.meowface_solver_percision_slider.value() / 100.0
            meowface_config.solver_threads = self.__ui.meowface_solver_threads_sb.value()
            meowface_config.solver_max_cps = self.__ui.meowface_solver_max_fps_sb.value()
            meowface_config.cache_invalidate_timeout = self.__ui.meowface_cache_invalidate_sb.value()
            meowface_config.cache_full_sync_period = self.__ui.meowface_cache_sync_sb.value()
            meowface_config.udp_ping_interval = self.__ui.meowface_cache_ping_sb.value()
            meowface_config.cache_float_precision = self.__ui.meowface_cache_float_percision_sb.value()
            meowface_config.avatar_config_file = self.__ui.meowface_avatar_config_le.text()

            foxyface_config: FoxyFaceSenderConfig = self.__config_manager.config.sender.foxyface

            foxyface_config.enabled = self.__ui.foxyface_enable_cb.isChecked()
            foxyface_config.auto_connect_enabled = self.__ui.foxyface_ip_auto_find_cb.isChecked()
            foxyface_config.ip = self.__ui.foxyface_ip_le.text()
            foxyface_config.port = self.__ui.foxyface_port_sb.value()
            foxyface_config.host_read_timeout = self.__ui.host_read_timeout_sb.value()
            foxyface_config.solver_enabled = self.__ui.foxyface_enable_solver_cb.isChecked()
            foxyface_config.solver_model_path = self.__ui.foxyface_solver_model_le.text()
            foxyface_config.solver_interleaved_vertices_percentage = self.__ui.foxyface_solver_sercision_slider.value() / 100.0
            foxyface_config.solver_threads = self.__ui.foxyface_solver_threads_sb.value()
            foxyface_config.solver_max_cps = self.__ui.foxyface_solver_max_fps_sb.value()
            foxyface_config.cache_invalidate_timeout = self.__ui.foxyface_cache_invalidate_sb.value()
            foxyface_config.cache_full_sync_period = self.__ui.foxyface_cache_sync_sb.value()
            foxyface_config.udp_ping_interval = self.__ui.foxyface_cache_ping_sb.value()
            foxyface_config.cache_float_precision = self.__ui.foxyface_cache_float_percision_sb.value()
            foxyface_config.avatar_config_file = self.__ui.foxyface_avatar_config_le.text()

            self.__config_manager.write()
        except Exception:
            _logger.exception("Failed to save config")

    @staticmethod
    def __wheel_event(event):
        event.ignore()
