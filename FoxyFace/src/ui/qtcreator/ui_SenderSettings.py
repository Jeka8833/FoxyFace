# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SenderSettings.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QTabWidget, QToolButton,
    QVBoxLayout, QWidget)

class Ui_SenderSettings(object):
    def setupUi(self, SenderSettings):
        if not SenderSettings.objectName():
            SenderSettings.setObjectName(u"SenderSettings")
        SenderSettings.resize(894, 681)
        self.centralwidget = QWidget(SenderSettings)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollArea = QScrollArea(self.tab_4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 852, 583))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.vrchat_enable_cb = QCheckBox(self.scrollAreaWidgetContents)
        self.vrchat_enable_cb.setObjectName(u"vrchat_enable_cb")
        self.vrchat_enable_cb.setChecked(True)

        self.verticalLayout.addWidget(self.vrchat_enable_cb)

        self.widget_2 = QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_9 = QVBoxLayout(self.widget_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.vrchat_connection_lb = QLabel(self.widget_2)
        self.vrchat_connection_lb.setObjectName(u"vrchat_connection_lb")
        font = QFont()
        font.setPointSize(12)
        self.vrchat_connection_lb.setFont(font)
        self.vrchat_connection_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vrchat_connection_lb.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.vrchat_connection_lb)

        self.vrchat_connection_lb_line = QFrame(self.widget_2)
        self.vrchat_connection_lb_line.setObjectName(u"vrchat_connection_lb_line")
        self.vrchat_connection_lb_line.setFrameShape(QFrame.Shape.HLine)
        self.vrchat_connection_lb_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.vrchat_connection_lb_line)

        self.vrchat_avatare_request_period_widget = QWidget(self.widget_2)
        self.vrchat_avatare_request_period_widget.setObjectName(u"vrchat_avatare_request_period_widget")
        self.horizontalLayout_13 = QHBoxLayout(self.vrchat_avatare_request_period_widget)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.vrchat_avatare_request_period_lb = QLabel(self.vrchat_avatare_request_period_widget)
        self.vrchat_avatare_request_period_lb.setObjectName(u"vrchat_avatare_request_period_lb")

        self.horizontalLayout_13.addWidget(self.vrchat_avatare_request_period_lb)

        self.vrchat_avatare_request_period_sb = QDoubleSpinBox(self.vrchat_avatare_request_period_widget)
        self.vrchat_avatare_request_period_sb.setObjectName(u"vrchat_avatare_request_period_sb")
        self.vrchat_avatare_request_period_sb.setMinimum(0.010000000000000)
        self.vrchat_avatare_request_period_sb.setMaximum(60.000000000000000)
        self.vrchat_avatare_request_period_sb.setSingleStep(0.100000000000000)
        self.vrchat_avatare_request_period_sb.setValue(0.500000000000000)

        self.horizontalLayout_13.addWidget(self.vrchat_avatare_request_period_sb)


        self.verticalLayout_9.addWidget(self.vrchat_avatare_request_period_widget)

        self.vrchat_error_sleep_tim_widget = QWidget(self.widget_2)
        self.vrchat_error_sleep_tim_widget.setObjectName(u"vrchat_error_sleep_tim_widget")
        self.horizontalLayout_12 = QHBoxLayout(self.vrchat_error_sleep_tim_widget)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.vrchat_error_sleep_tim_lb = QLabel(self.vrchat_error_sleep_tim_widget)
        self.vrchat_error_sleep_tim_lb.setObjectName(u"vrchat_error_sleep_tim_lb")

        self.horizontalLayout_12.addWidget(self.vrchat_error_sleep_tim_lb)

        self.vrchat_error_sleep_tim_sb = QDoubleSpinBox(self.vrchat_error_sleep_tim_widget)
        self.vrchat_error_sleep_tim_sb.setObjectName(u"vrchat_error_sleep_tim_sb")
        self.vrchat_error_sleep_tim_sb.setMinimum(0.010000000000000)
        self.vrchat_error_sleep_tim_sb.setMaximum(60.000000000000000)
        self.vrchat_error_sleep_tim_sb.setValue(5.000000000000000)

        self.horizontalLayout_12.addWidget(self.vrchat_error_sleep_tim_sb)


        self.verticalLayout_9.addWidget(self.vrchat_error_sleep_tim_widget)

        self.vrchat_close_connectio_widget = QWidget(self.widget_2)
        self.vrchat_close_connectio_widget.setObjectName(u"vrchat_close_connectio_widget")
        self.horizontalLayout_11 = QHBoxLayout(self.vrchat_close_connectio_widget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.vrchat_close_connectio_lb = QLabel(self.vrchat_close_connectio_widget)
        self.vrchat_close_connectio_lb.setObjectName(u"vrchat_close_connectio_lb")

        self.horizontalLayout_11.addWidget(self.vrchat_close_connectio_lb)

        self.vrchat_close_connectio_sb = QSpinBox(self.vrchat_close_connectio_widget)
        self.vrchat_close_connectio_sb.setObjectName(u"vrchat_close_connectio_sb")
        self.vrchat_close_connectio_sb.setMinimum(1)
        self.vrchat_close_connectio_sb.setMaximum(10000)
        self.vrchat_close_connectio_sb.setValue(3)

        self.horizontalLayout_11.addWidget(self.vrchat_close_connectio_sb)


        self.verticalLayout_9.addWidget(self.vrchat_close_connectio_widget)

        self.vrchat_zeroconf_widget = QWidget(self.widget_2)
        self.vrchat_zeroconf_widget.setObjectName(u"vrchat_zeroconf_widget")
        self.horizontalLayout_14 = QHBoxLayout(self.vrchat_zeroconf_widget)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.vrchat_zeroconf_lb = QLabel(self.vrchat_zeroconf_widget)
        self.vrchat_zeroconf_lb.setObjectName(u"vrchat_zeroconf_lb")

        self.horizontalLayout_14.addWidget(self.vrchat_zeroconf_lb)

        self.vrchat_zeroconf_sb = QDoubleSpinBox(self.vrchat_zeroconf_widget)
        self.vrchat_zeroconf_sb.setObjectName(u"vrchat_zeroconf_sb")
        self.vrchat_zeroconf_sb.setMinimum(1.000000000000000)
        self.vrchat_zeroconf_sb.setValue(3.000000000000000)

        self.horizontalLayout_14.addWidget(self.vrchat_zeroconf_sb)


        self.verticalLayout_9.addWidget(self.vrchat_zeroconf_widget)

        self.vrchat_solver_lb = QLabel(self.widget_2)
        self.vrchat_solver_lb.setObjectName(u"vrchat_solver_lb")
        self.vrchat_solver_lb.setFont(font)
        self.vrchat_solver_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vrchat_solver_lb.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.vrchat_solver_lb)

        self.vrchat_solver_line = QFrame(self.widget_2)
        self.vrchat_solver_line.setObjectName(u"vrchat_solver_line")
        self.vrchat_solver_line.setFrameShape(QFrame.Shape.HLine)
        self.vrchat_solver_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.vrchat_solver_line)

        self.vrchat_enable_solver_cb = QCheckBox(self.widget_2)
        self.vrchat_enable_solver_cb.setObjectName(u"vrchat_enable_solver_cb")
        self.vrchat_enable_solver_cb.setChecked(True)

        self.verticalLayout_9.addWidget(self.vrchat_enable_solver_cb)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_10 = QVBoxLayout(self.widget_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.vrchat_solver_model_widget = QWidget(self.widget_3)
        self.vrchat_solver_model_widget.setObjectName(u"vrchat_solver_model_widget")
        self.horizontalLayout_3 = QHBoxLayout(self.vrchat_solver_model_widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.vrchat_solver_model_lb = QLabel(self.vrchat_solver_model_widget)
        self.vrchat_solver_model_lb.setObjectName(u"vrchat_solver_model_lb")

        self.horizontalLayout_3.addWidget(self.vrchat_solver_model_lb)

        self.vrchat_solver_model_le = QLineEdit(self.vrchat_solver_model_widget)
        self.vrchat_solver_model_le.setObjectName(u"vrchat_solver_model_le")

        self.horizontalLayout_3.addWidget(self.vrchat_solver_model_le)

        self.vrchat_solver_model_btn = QToolButton(self.vrchat_solver_model_widget)
        self.vrchat_solver_model_btn.setObjectName(u"vrchat_solver_model_btn")

        self.horizontalLayout_3.addWidget(self.vrchat_solver_model_btn)


        self.verticalLayout_10.addWidget(self.vrchat_solver_model_widget)

        self.vrchat_solver_sercision_widget = QWidget(self.widget_3)
        self.vrchat_solver_sercision_widget.setObjectName(u"vrchat_solver_sercision_widget")
        self.horizontalLayout_5 = QHBoxLayout(self.vrchat_solver_sercision_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.vrchat_solver_sercision_lb = QLabel(self.vrchat_solver_sercision_widget)
        self.vrchat_solver_sercision_lb.setObjectName(u"vrchat_solver_sercision_lb")

        self.horizontalLayout_5.addWidget(self.vrchat_solver_sercision_lb)

        self.vrchat_solver_sercision_slider = QSlider(self.vrchat_solver_sercision_widget)
        self.vrchat_solver_sercision_slider.setObjectName(u"vrchat_solver_sercision_slider")
        self.vrchat_solver_sercision_slider.setMinimum(1)
        self.vrchat_solver_sercision_slider.setMaximum(100)
        self.vrchat_solver_sercision_slider.setValue(80)
        self.vrchat_solver_sercision_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_5.addWidget(self.vrchat_solver_sercision_slider)


        self.verticalLayout_10.addWidget(self.vrchat_solver_sercision_widget)

        self.vrchat_solver_threads_widget = QWidget(self.widget_3)
        self.vrchat_solver_threads_widget.setObjectName(u"vrchat_solver_threads_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.vrchat_solver_threads_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.vrchat_solver_threads_lb = QLabel(self.vrchat_solver_threads_widget)
        self.vrchat_solver_threads_lb.setObjectName(u"vrchat_solver_threads_lb")

        self.horizontalLayout_4.addWidget(self.vrchat_solver_threads_lb)

        self.vrchat_solver_threads_sb = QSpinBox(self.vrchat_solver_threads_widget)
        self.vrchat_solver_threads_sb.setObjectName(u"vrchat_solver_threads_sb")
        self.vrchat_solver_threads_sb.setMinimum(1)
        self.vrchat_solver_threads_sb.setMaximum(32)
        self.vrchat_solver_threads_sb.setValue(2)

        self.horizontalLayout_4.addWidget(self.vrchat_solver_threads_sb)


        self.verticalLayout_10.addWidget(self.vrchat_solver_threads_widget)

        self.vrchat_solver_max_fps_widget = QWidget(self.widget_3)
        self.vrchat_solver_max_fps_widget.setObjectName(u"vrchat_solver_max_fps_widget")
        self.horizontalLayout_6 = QHBoxLayout(self.vrchat_solver_max_fps_widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.vrchat_solver_max_fps_lb = QLabel(self.vrchat_solver_max_fps_widget)
        self.vrchat_solver_max_fps_lb.setObjectName(u"vrchat_solver_max_fps_lb")

        self.horizontalLayout_6.addWidget(self.vrchat_solver_max_fps_lb)

        self.vrchat_solver_max_fps_sb = QSpinBox(self.vrchat_solver_max_fps_widget)
        self.vrchat_solver_max_fps_sb.setObjectName(u"vrchat_solver_max_fps_sb")
        self.vrchat_solver_max_fps_sb.setMinimum(1)
        self.vrchat_solver_max_fps_sb.setMaximum(120)
        self.vrchat_solver_max_fps_sb.setValue(30)

        self.horizontalLayout_6.addWidget(self.vrchat_solver_max_fps_sb)


        self.verticalLayout_10.addWidget(self.vrchat_solver_max_fps_widget)


        self.verticalLayout_9.addWidget(self.widget_3)

        self.vrchat_cache_lb = QLabel(self.widget_2)
        self.vrchat_cache_lb.setObjectName(u"vrchat_cache_lb")
        self.vrchat_cache_lb.setFont(font)
        self.vrchat_cache_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vrchat_cache_lb.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.vrchat_cache_lb)

        self.vrchat_cache_line = QFrame(self.widget_2)
        self.vrchat_cache_line.setObjectName(u"vrchat_cache_line")
        self.vrchat_cache_line.setFrameShape(QFrame.Shape.HLine)
        self.vrchat_cache_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.vrchat_cache_line)

        self.vrchat_cache_invalidate_widget = QWidget(self.widget_2)
        self.vrchat_cache_invalidate_widget.setObjectName(u"vrchat_cache_invalidate_widget")
        self.horizontalLayout_7 = QHBoxLayout(self.vrchat_cache_invalidate_widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.vrchat_cache_invalidate_lb = QLabel(self.vrchat_cache_invalidate_widget)
        self.vrchat_cache_invalidate_lb.setObjectName(u"vrchat_cache_invalidate_lb")

        self.horizontalLayout_7.addWidget(self.vrchat_cache_invalidate_lb)

        self.vrchat_cache_invalidate_sb = QDoubleSpinBox(self.vrchat_cache_invalidate_widget)
        self.vrchat_cache_invalidate_sb.setObjectName(u"vrchat_cache_invalidate_sb")
        self.vrchat_cache_invalidate_sb.setMaximum(60.000000000000000)
        self.vrchat_cache_invalidate_sb.setValue(5.000000000000000)

        self.horizontalLayout_7.addWidget(self.vrchat_cache_invalidate_sb)


        self.verticalLayout_9.addWidget(self.vrchat_cache_invalidate_widget)

        self.vrchat_cache_sync_widget = QWidget(self.widget_2)
        self.vrchat_cache_sync_widget.setObjectName(u"vrchat_cache_sync_widget")
        self.horizontalLayout_8 = QHBoxLayout(self.vrchat_cache_sync_widget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.vrchat_cache_sync_lb = QLabel(self.vrchat_cache_sync_widget)
        self.vrchat_cache_sync_lb.setObjectName(u"vrchat_cache_sync_lb")

        self.horizontalLayout_8.addWidget(self.vrchat_cache_sync_lb)

        self.vrchat_cache_sync_sb = QDoubleSpinBox(self.vrchat_cache_sync_widget)
        self.vrchat_cache_sync_sb.setObjectName(u"vrchat_cache_sync_sb")
        self.vrchat_cache_sync_sb.setMaximum(60.000000000000000)
        self.vrchat_cache_sync_sb.setValue(5.000000000000000)

        self.horizontalLayout_8.addWidget(self.vrchat_cache_sync_sb)


        self.verticalLayout_9.addWidget(self.vrchat_cache_sync_widget)

        self.vrchat_cache_float_percision_widget = QWidget(self.widget_2)
        self.vrchat_cache_float_percision_widget.setObjectName(u"vrchat_cache_float_percision_widget")
        self.horizontalLayout_9 = QHBoxLayout(self.vrchat_cache_float_percision_widget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.vrchat_cache_float_percision_lb = QLabel(self.vrchat_cache_float_percision_widget)
        self.vrchat_cache_float_percision_lb.setObjectName(u"vrchat_cache_float_percision_lb")

        self.horizontalLayout_9.addWidget(self.vrchat_cache_float_percision_lb)

        self.vrchat_cache_float_percision_sb = QDoubleSpinBox(self.vrchat_cache_float_percision_widget)
        self.vrchat_cache_float_percision_sb.setObjectName(u"vrchat_cache_float_percision_sb")
        self.vrchat_cache_float_percision_sb.setDecimals(6)
        self.vrchat_cache_float_percision_sb.setMaximum(0.500000000000000)
        self.vrchat_cache_float_percision_sb.setValue(0.003906000000000)

        self.horizontalLayout_9.addWidget(self.vrchat_cache_float_percision_sb)


        self.verticalLayout_9.addWidget(self.vrchat_cache_float_percision_widget)

        self.vrchat_cache_bundle_widget = QWidget(self.widget_2)
        self.vrchat_cache_bundle_widget.setObjectName(u"vrchat_cache_bundle_widget")
        self.horizontalLayout_10 = QHBoxLayout(self.vrchat_cache_bundle_widget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.vrchat_cache_bundle_lb = QLabel(self.vrchat_cache_bundle_widget)
        self.vrchat_cache_bundle_lb.setObjectName(u"vrchat_cache_bundle_lb")

        self.horizontalLayout_10.addWidget(self.vrchat_cache_bundle_lb)

        self.vrchat_cache_bundle_sb = QSpinBox(self.vrchat_cache_bundle_widget)
        self.vrchat_cache_bundle_sb.setObjectName(u"vrchat_cache_bundle_sb")
        self.vrchat_cache_bundle_sb.setMinimum(100)
        self.vrchat_cache_bundle_sb.setMaximum(65506)
        self.vrchat_cache_bundle_sb.setValue(4096)

        self.horizontalLayout_10.addWidget(self.vrchat_cache_bundle_sb)


        self.verticalLayout_9.addWidget(self.vrchat_cache_bundle_widget)


        self.verticalLayout.addWidget(self.widget_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea_2 = QScrollArea(self.tab)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 852, 583))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ifm_enable_cb = QCheckBox(self.scrollAreaWidgetContents_2)
        self.ifm_enable_cb.setObjectName(u"ifm_enable_cb")

        self.verticalLayout_3.addWidget(self.ifm_enable_cb)

        self.widget_4 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setEnabled(True)
        self.verticalLayout_11 = QVBoxLayout(self.widget_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.ifm_connection_lb = QLabel(self.widget_4)
        self.ifm_connection_lb.setObjectName(u"ifm_connection_lb")
        self.ifm_connection_lb.setFont(font)
        self.ifm_connection_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.ifm_connection_lb)

        self.ifm_connection_lline = QFrame(self.widget_4)
        self.ifm_connection_lline.setObjectName(u"ifm_connection_lline")
        self.ifm_connection_lline.setFrameShape(QFrame.Shape.HLine)
        self.ifm_connection_lline.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_11.addWidget(self.ifm_connection_lline)

        self.ifm_ip_auto_find_cb = QCheckBox(self.widget_4)
        self.ifm_ip_auto_find_cb.setObjectName(u"ifm_ip_auto_find_cb")
        self.ifm_ip_auto_find_cb.setChecked(True)

        self.verticalLayout_11.addWidget(self.ifm_ip_auto_find_cb)

        self.ifm_ip_widget = QWidget(self.widget_4)
        self.ifm_ip_widget.setObjectName(u"ifm_ip_widget")
        self.horizontalLayout_15 = QHBoxLayout(self.ifm_ip_widget)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.ifm_ip_lb = QLabel(self.ifm_ip_widget)
        self.ifm_ip_lb.setObjectName(u"ifm_ip_lb")

        self.horizontalLayout_15.addWidget(self.ifm_ip_lb)

        self.ifm_ip_le = QLineEdit(self.ifm_ip_widget)
        self.ifm_ip_le.setObjectName(u"ifm_ip_le")
        self.ifm_ip_le.setEnabled(False)
        self.ifm_ip_le.setMaxLength(256)

        self.horizontalLayout_15.addWidget(self.ifm_ip_le)


        self.verticalLayout_11.addWidget(self.ifm_ip_widget)

        self.ifm_port_widget = QWidget(self.widget_4)
        self.ifm_port_widget.setObjectName(u"ifm_port_widget")
        self.horizontalLayout_16 = QHBoxLayout(self.ifm_port_widget)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.ifm_port_lb = QLabel(self.ifm_port_widget)
        self.ifm_port_lb.setObjectName(u"ifm_port_lb")

        self.horizontalLayout_16.addWidget(self.ifm_port_lb)

        self.ifm_port_sb = QSpinBox(self.ifm_port_widget)
        self.ifm_port_sb.setObjectName(u"ifm_port_sb")
        self.ifm_port_sb.setEnabled(False)
        self.ifm_port_sb.setMaximum(65535)
        self.ifm_port_sb.setValue(49983)

        self.horizontalLayout_16.addWidget(self.ifm_port_sb)


        self.verticalLayout_11.addWidget(self.ifm_port_widget)

        self.ifm_solver_lb = QLabel(self.widget_4)
        self.ifm_solver_lb.setObjectName(u"ifm_solver_lb")
        self.ifm_solver_lb.setFont(font)
        self.ifm_solver_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.ifm_solver_lb)

        self.ifm_solver_line = QFrame(self.widget_4)
        self.ifm_solver_line.setObjectName(u"ifm_solver_line")
        self.ifm_solver_line.setFrameShape(QFrame.Shape.HLine)
        self.ifm_solver_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_11.addWidget(self.ifm_solver_line)

        self.ifm_enable_solver_cb = QCheckBox(self.widget_4)
        self.ifm_enable_solver_cb.setObjectName(u"ifm_enable_solver_cb")
        self.ifm_enable_solver_cb.setChecked(True)

        self.verticalLayout_11.addWidget(self.ifm_enable_solver_cb)

        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_12 = QVBoxLayout(self.widget_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.ifm_solver_model_widget = QWidget(self.widget_5)
        self.ifm_solver_model_widget.setObjectName(u"ifm_solver_model_widget")
        self.horizontalLayout_17 = QHBoxLayout(self.ifm_solver_model_widget)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.ifm_solver_model_lb = QLabel(self.ifm_solver_model_widget)
        self.ifm_solver_model_lb.setObjectName(u"ifm_solver_model_lb")

        self.horizontalLayout_17.addWidget(self.ifm_solver_model_lb)

        self.ifm_solver_model_le = QLineEdit(self.ifm_solver_model_widget)
        self.ifm_solver_model_le.setObjectName(u"ifm_solver_model_le")

        self.horizontalLayout_17.addWidget(self.ifm_solver_model_le)

        self.ifm_solver_model_btn = QToolButton(self.ifm_solver_model_widget)
        self.ifm_solver_model_btn.setObjectName(u"ifm_solver_model_btn")

        self.horizontalLayout_17.addWidget(self.ifm_solver_model_btn)


        self.verticalLayout_12.addWidget(self.ifm_solver_model_widget)

        self.ifm_solver_sercision_widget = QWidget(self.widget_5)
        self.ifm_solver_sercision_widget.setObjectName(u"ifm_solver_sercision_widget")
        self.horizontalLayout_19 = QHBoxLayout(self.ifm_solver_sercision_widget)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.ifm_solver_sercision_lb = QLabel(self.ifm_solver_sercision_widget)
        self.ifm_solver_sercision_lb.setObjectName(u"ifm_solver_sercision_lb")

        self.horizontalLayout_19.addWidget(self.ifm_solver_sercision_lb)

        self.ifm_solver_sercision_slider = QSlider(self.ifm_solver_sercision_widget)
        self.ifm_solver_sercision_slider.setObjectName(u"ifm_solver_sercision_slider")
        self.ifm_solver_sercision_slider.setMinimum(1)
        self.ifm_solver_sercision_slider.setMaximum(100)
        self.ifm_solver_sercision_slider.setValue(80)
        self.ifm_solver_sercision_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_19.addWidget(self.ifm_solver_sercision_slider)


        self.verticalLayout_12.addWidget(self.ifm_solver_sercision_widget)

        self.ifm_solver_threads_widget = QWidget(self.widget_5)
        self.ifm_solver_threads_widget.setObjectName(u"ifm_solver_threads_widget")
        self.horizontalLayout_18 = QHBoxLayout(self.ifm_solver_threads_widget)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.ifm_solver_threads_lb = QLabel(self.ifm_solver_threads_widget)
        self.ifm_solver_threads_lb.setObjectName(u"ifm_solver_threads_lb")

        self.horizontalLayout_18.addWidget(self.ifm_solver_threads_lb)

        self.ifm_solver_threads_sb = QSpinBox(self.ifm_solver_threads_widget)
        self.ifm_solver_threads_sb.setObjectName(u"ifm_solver_threads_sb")
        self.ifm_solver_threads_sb.setMinimum(1)
        self.ifm_solver_threads_sb.setMaximum(32)
        self.ifm_solver_threads_sb.setValue(2)

        self.horizontalLayout_18.addWidget(self.ifm_solver_threads_sb)


        self.verticalLayout_12.addWidget(self.ifm_solver_threads_widget)

        self.ifm_solver_max_fps_widget = QWidget(self.widget_5)
        self.ifm_solver_max_fps_widget.setObjectName(u"ifm_solver_max_fps_widget")
        self.horizontalLayout_20 = QHBoxLayout(self.ifm_solver_max_fps_widget)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.ifm_solver_max_fps_lb = QLabel(self.ifm_solver_max_fps_widget)
        self.ifm_solver_max_fps_lb.setObjectName(u"ifm_solver_max_fps_lb")

        self.horizontalLayout_20.addWidget(self.ifm_solver_max_fps_lb)

        self.ifm_solver_max_fps_sb = QSpinBox(self.ifm_solver_max_fps_widget)
        self.ifm_solver_max_fps_sb.setObjectName(u"ifm_solver_max_fps_sb")
        self.ifm_solver_max_fps_sb.setMinimum(1)
        self.ifm_solver_max_fps_sb.setMaximum(120)
        self.ifm_solver_max_fps_sb.setValue(30)

        self.horizontalLayout_20.addWidget(self.ifm_solver_max_fps_sb)


        self.verticalLayout_12.addWidget(self.ifm_solver_max_fps_widget)


        self.verticalLayout_11.addWidget(self.widget_5)

        self.ifm_cache_lb = QLabel(self.widget_4)
        self.ifm_cache_lb.setObjectName(u"ifm_cache_lb")
        self.ifm_cache_lb.setFont(font)
        self.ifm_cache_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.ifm_cache_lb)

        self.ifm_cache_line = QFrame(self.widget_4)
        self.ifm_cache_line.setObjectName(u"ifm_cache_line")
        self.ifm_cache_line.setFrameShape(QFrame.Shape.HLine)
        self.ifm_cache_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_11.addWidget(self.ifm_cache_line)

        self.ifm_cache_invalidate_widget = QWidget(self.widget_4)
        self.ifm_cache_invalidate_widget.setObjectName(u"ifm_cache_invalidate_widget")
        self.horizontalLayout_27 = QHBoxLayout(self.ifm_cache_invalidate_widget)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.ifm_cache_invalidate_lb = QLabel(self.ifm_cache_invalidate_widget)
        self.ifm_cache_invalidate_lb.setObjectName(u"ifm_cache_invalidate_lb")

        self.horizontalLayout_27.addWidget(self.ifm_cache_invalidate_lb)

        self.ifm_cache_invalidate_sb = QDoubleSpinBox(self.ifm_cache_invalidate_widget)
        self.ifm_cache_invalidate_sb.setObjectName(u"ifm_cache_invalidate_sb")
        self.ifm_cache_invalidate_sb.setMaximum(60.000000000000000)
        self.ifm_cache_invalidate_sb.setValue(5.000000000000000)

        self.horizontalLayout_27.addWidget(self.ifm_cache_invalidate_sb)


        self.verticalLayout_11.addWidget(self.ifm_cache_invalidate_widget)

        self.ifm_cache_sync_widget = QWidget(self.widget_4)
        self.ifm_cache_sync_widget.setObjectName(u"ifm_cache_sync_widget")
        self.horizontalLayout_28 = QHBoxLayout(self.ifm_cache_sync_widget)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.ifm_cache_sync_lb = QLabel(self.ifm_cache_sync_widget)
        self.ifm_cache_sync_lb.setObjectName(u"ifm_cache_sync_lb")

        self.horizontalLayout_28.addWidget(self.ifm_cache_sync_lb)

        self.ifm_cache_sync_sb = QDoubleSpinBox(self.ifm_cache_sync_widget)
        self.ifm_cache_sync_sb.setObjectName(u"ifm_cache_sync_sb")
        self.ifm_cache_sync_sb.setMaximum(60.000000000000000)
        self.ifm_cache_sync_sb.setValue(0.000000000000000)

        self.horizontalLayout_28.addWidget(self.ifm_cache_sync_sb)


        self.verticalLayout_11.addWidget(self.ifm_cache_sync_widget)

        self.ifm_cache_ping_widget = QWidget(self.widget_4)
        self.ifm_cache_ping_widget.setObjectName(u"ifm_cache_ping_widget")
        self.horizontalLayout_30 = QHBoxLayout(self.ifm_cache_ping_widget)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.ifm_cache_ping_lb = QLabel(self.ifm_cache_ping_widget)
        self.ifm_cache_ping_lb.setObjectName(u"ifm_cache_ping_lb")

        self.horizontalLayout_30.addWidget(self.ifm_cache_ping_lb)

        self.ifm_cache_ping_sb = QDoubleSpinBox(self.ifm_cache_ping_widget)
        self.ifm_cache_ping_sb.setObjectName(u"ifm_cache_ping_sb")
        self.ifm_cache_ping_sb.setDecimals(3)
        self.ifm_cache_ping_sb.setMinimum(0.001000000000000)
        self.ifm_cache_ping_sb.setMaximum(60.000000000000000)
        self.ifm_cache_ping_sb.setValue(0.017000000000000)

        self.horizontalLayout_30.addWidget(self.ifm_cache_ping_sb)


        self.verticalLayout_11.addWidget(self.ifm_cache_ping_widget)

        self.ifm_cache_float_percision_widget = QWidget(self.widget_4)
        self.ifm_cache_float_percision_widget.setObjectName(u"ifm_cache_float_percision_widget")
        self.horizontalLayout_29 = QHBoxLayout(self.ifm_cache_float_percision_widget)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.ifm_cache_float_percision_lb = QLabel(self.ifm_cache_float_percision_widget)
        self.ifm_cache_float_percision_lb.setObjectName(u"ifm_cache_float_percision_lb")

        self.horizontalLayout_29.addWidget(self.ifm_cache_float_percision_lb)

        self.ifm_cache_float_percision_sb = QDoubleSpinBox(self.ifm_cache_float_percision_widget)
        self.ifm_cache_float_percision_sb.setObjectName(u"ifm_cache_float_percision_sb")
        self.ifm_cache_float_percision_sb.setDecimals(6)
        self.ifm_cache_float_percision_sb.setMinimum(0.000000000000000)
        self.ifm_cache_float_percision_sb.setMaximum(0.500000000000000)
        self.ifm_cache_float_percision_sb.setValue(0.003906000000000)

        self.horizontalLayout_29.addWidget(self.ifm_cache_float_percision_sb)


        self.verticalLayout_11.addWidget(self.ifm_cache_float_percision_widget)


        self.verticalLayout_3.addWidget(self.widget_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_5 = QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea_3 = QScrollArea(self.tab_2)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 852, 583))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.meowface_enable_cb = QCheckBox(self.scrollAreaWidgetContents_4)
        self.meowface_enable_cb.setObjectName(u"meowface_enable_cb")

        self.verticalLayout_7.addWidget(self.meowface_enable_cb)

        self.widget_6 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_13 = QVBoxLayout(self.widget_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.meowface_connection_lb = QLabel(self.widget_6)
        self.meowface_connection_lb.setObjectName(u"meowface_connection_lb")
        self.meowface_connection_lb.setFont(font)
        self.meowface_connection_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.meowface_connection_lb)

        self.meowface_connection_line = QFrame(self.widget_6)
        self.meowface_connection_line.setObjectName(u"meowface_connection_line")
        self.meowface_connection_line.setFrameShape(QFrame.Shape.HLine)
        self.meowface_connection_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.meowface_connection_line)

        self.meowface_ip_auto_find_cb = QCheckBox(self.widget_6)
        self.meowface_ip_auto_find_cb.setObjectName(u"meowface_ip_auto_find_cb")
        self.meowface_ip_auto_find_cb.setChecked(True)

        self.verticalLayout_13.addWidget(self.meowface_ip_auto_find_cb)

        self.meowface_ip_widget = QWidget(self.widget_6)
        self.meowface_ip_widget.setObjectName(u"meowface_ip_widget")
        self.horizontalLayout_64 = QHBoxLayout(self.meowface_ip_widget)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.meowface_ip_lb = QLabel(self.meowface_ip_widget)
        self.meowface_ip_lb.setObjectName(u"meowface_ip_lb")

        self.horizontalLayout_64.addWidget(self.meowface_ip_lb)

        self.meowface_ip_le = QLineEdit(self.meowface_ip_widget)
        self.meowface_ip_le.setObjectName(u"meowface_ip_le")
        self.meowface_ip_le.setEnabled(False)
        self.meowface_ip_le.setMaxLength(256)

        self.horizontalLayout_64.addWidget(self.meowface_ip_le)


        self.verticalLayout_13.addWidget(self.meowface_ip_widget)

        self.meowface_port_widget = QWidget(self.widget_6)
        self.meowface_port_widget.setObjectName(u"meowface_port_widget")
        self.horizontalLayout_70 = QHBoxLayout(self.meowface_port_widget)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.meowface_port_lb = QLabel(self.meowface_port_widget)
        self.meowface_port_lb.setObjectName(u"meowface_port_lb")

        self.horizontalLayout_70.addWidget(self.meowface_port_lb)

        self.meowface_port_sb = QSpinBox(self.meowface_port_widget)
        self.meowface_port_sb.setObjectName(u"meowface_port_sb")
        self.meowface_port_sb.setEnabled(False)
        self.meowface_port_sb.setMaximum(65535)
        self.meowface_port_sb.setValue(49983)

        self.horizontalLayout_70.addWidget(self.meowface_port_sb)


        self.verticalLayout_13.addWidget(self.meowface_port_widget)

        self.meowface_solver_lb = QLabel(self.widget_6)
        self.meowface_solver_lb.setObjectName(u"meowface_solver_lb")
        self.meowface_solver_lb.setFont(font)
        self.meowface_solver_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.meowface_solver_lb)

        self.meowface_solver_line = QFrame(self.widget_6)
        self.meowface_solver_line.setObjectName(u"meowface_solver_line")
        self.meowface_solver_line.setFrameShape(QFrame.Shape.HLine)
        self.meowface_solver_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.meowface_solver_line)

        self.meowface_enable_solver_cb = QCheckBox(self.widget_6)
        self.meowface_enable_solver_cb.setObjectName(u"meowface_enable_solver_cb")
        self.meowface_enable_solver_cb.setChecked(True)

        self.verticalLayout_13.addWidget(self.meowface_enable_solver_cb)

        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setEnabled(True)
        self.verticalLayout_14 = QVBoxLayout(self.widget_7)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.meowface_solver_model_widget = QWidget(self.widget_7)
        self.meowface_solver_model_widget.setObjectName(u"meowface_solver_model_widget")
        self.horizontalLayout_68 = QHBoxLayout(self.meowface_solver_model_widget)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.meowface_solver_model_lb = QLabel(self.meowface_solver_model_widget)
        self.meowface_solver_model_lb.setObjectName(u"meowface_solver_model_lb")

        self.horizontalLayout_68.addWidget(self.meowface_solver_model_lb)

        self.meowface_solver_model_le = QLineEdit(self.meowface_solver_model_widget)
        self.meowface_solver_model_le.setObjectName(u"meowface_solver_model_le")

        self.horizontalLayout_68.addWidget(self.meowface_solver_model_le)

        self.meowface_solver_model_btn = QToolButton(self.meowface_solver_model_widget)
        self.meowface_solver_model_btn.setObjectName(u"meowface_solver_model_btn")

        self.horizontalLayout_68.addWidget(self.meowface_solver_model_btn)


        self.verticalLayout_14.addWidget(self.meowface_solver_model_widget)

        self.meowface_solver_sercision_widget = QWidget(self.widget_7)
        self.meowface_solver_sercision_widget.setObjectName(u"meowface_solver_sercision_widget")
        self.horizontalLayout_61 = QHBoxLayout(self.meowface_solver_sercision_widget)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.meowface_solver_sercision_lb = QLabel(self.meowface_solver_sercision_widget)
        self.meowface_solver_sercision_lb.setObjectName(u"meowface_solver_sercision_lb")

        self.horizontalLayout_61.addWidget(self.meowface_solver_sercision_lb)

        self.meowface_solver_sercision_slider = QSlider(self.meowface_solver_sercision_widget)
        self.meowface_solver_sercision_slider.setObjectName(u"meowface_solver_sercision_slider")
        self.meowface_solver_sercision_slider.setMinimum(1)
        self.meowface_solver_sercision_slider.setMaximum(100)
        self.meowface_solver_sercision_slider.setValue(80)
        self.meowface_solver_sercision_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_61.addWidget(self.meowface_solver_sercision_slider)


        self.verticalLayout_14.addWidget(self.meowface_solver_sercision_widget)

        self.meowface_solver_threads_widget = QWidget(self.widget_7)
        self.meowface_solver_threads_widget.setObjectName(u"meowface_solver_threads_widget")
        self.horizontalLayout_62 = QHBoxLayout(self.meowface_solver_threads_widget)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.meowface_solver_threads_lb = QLabel(self.meowface_solver_threads_widget)
        self.meowface_solver_threads_lb.setObjectName(u"meowface_solver_threads_lb")

        self.horizontalLayout_62.addWidget(self.meowface_solver_threads_lb)

        self.meowface_solver_threads_sb = QSpinBox(self.meowface_solver_threads_widget)
        self.meowface_solver_threads_sb.setObjectName(u"meowface_solver_threads_sb")
        self.meowface_solver_threads_sb.setMinimum(1)
        self.meowface_solver_threads_sb.setMaximum(32)
        self.meowface_solver_threads_sb.setValue(2)

        self.horizontalLayout_62.addWidget(self.meowface_solver_threads_sb)


        self.verticalLayout_14.addWidget(self.meowface_solver_threads_widget)

        self.meowface_solver_max_fps_widget = QWidget(self.widget_7)
        self.meowface_solver_max_fps_widget.setObjectName(u"meowface_solver_max_fps_widget")
        self.horizontalLayout_66 = QHBoxLayout(self.meowface_solver_max_fps_widget)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.meowface_solver_max_fps_lb = QLabel(self.meowface_solver_max_fps_widget)
        self.meowface_solver_max_fps_lb.setObjectName(u"meowface_solver_max_fps_lb")

        self.horizontalLayout_66.addWidget(self.meowface_solver_max_fps_lb)

        self.meowface_solver_max_fps_sb = QSpinBox(self.meowface_solver_max_fps_widget)
        self.meowface_solver_max_fps_sb.setObjectName(u"meowface_solver_max_fps_sb")
        self.meowface_solver_max_fps_sb.setMinimum(1)
        self.meowface_solver_max_fps_sb.setMaximum(120)
        self.meowface_solver_max_fps_sb.setValue(30)

        self.horizontalLayout_66.addWidget(self.meowface_solver_max_fps_sb)


        self.verticalLayout_14.addWidget(self.meowface_solver_max_fps_widget)


        self.verticalLayout_13.addWidget(self.widget_7)

        self.meowface_cache_lb = QLabel(self.widget_6)
        self.meowface_cache_lb.setObjectName(u"meowface_cache_lb")
        self.meowface_cache_lb.setFont(font)
        self.meowface_cache_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.meowface_cache_lb)

        self.meowface_cache_line = QFrame(self.widget_6)
        self.meowface_cache_line.setObjectName(u"meowface_cache_line")
        self.meowface_cache_line.setFrameShape(QFrame.Shape.HLine)
        self.meowface_cache_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.meowface_cache_line)

        self.meowface_cache_invalidate_widget = QWidget(self.widget_6)
        self.meowface_cache_invalidate_widget.setObjectName(u"meowface_cache_invalidate_widget")
        self.horizontalLayout_69 = QHBoxLayout(self.meowface_cache_invalidate_widget)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.meowface_cache_invalidate_lb = QLabel(self.meowface_cache_invalidate_widget)
        self.meowface_cache_invalidate_lb.setObjectName(u"meowface_cache_invalidate_lb")

        self.horizontalLayout_69.addWidget(self.meowface_cache_invalidate_lb)

        self.meowface_cache_invalidate_sb = QDoubleSpinBox(self.meowface_cache_invalidate_widget)
        self.meowface_cache_invalidate_sb.setObjectName(u"meowface_cache_invalidate_sb")
        self.meowface_cache_invalidate_sb.setMaximum(60.000000000000000)
        self.meowface_cache_invalidate_sb.setValue(5.000000000000000)

        self.horizontalLayout_69.addWidget(self.meowface_cache_invalidate_sb)


        self.verticalLayout_13.addWidget(self.meowface_cache_invalidate_widget)

        self.meowface_cache_sync_widget = QWidget(self.widget_6)
        self.meowface_cache_sync_widget.setObjectName(u"meowface_cache_sync_widget")
        self.horizontalLayout_63 = QHBoxLayout(self.meowface_cache_sync_widget)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.meowface_cache_sync_lb = QLabel(self.meowface_cache_sync_widget)
        self.meowface_cache_sync_lb.setObjectName(u"meowface_cache_sync_lb")

        self.horizontalLayout_63.addWidget(self.meowface_cache_sync_lb)

        self.meowface_cache_sync_sb = QDoubleSpinBox(self.meowface_cache_sync_widget)
        self.meowface_cache_sync_sb.setObjectName(u"meowface_cache_sync_sb")
        self.meowface_cache_sync_sb.setMaximum(60.000000000000000)
        self.meowface_cache_sync_sb.setValue(5.000000000000000)

        self.horizontalLayout_63.addWidget(self.meowface_cache_sync_sb)


        self.verticalLayout_13.addWidget(self.meowface_cache_sync_widget)

        self.meowface_cache_ping_widget = QWidget(self.widget_6)
        self.meowface_cache_ping_widget.setObjectName(u"meowface_cache_ping_widget")
        self.horizontalLayout_67 = QHBoxLayout(self.meowface_cache_ping_widget)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.meowface_cache_ping_lb = QLabel(self.meowface_cache_ping_widget)
        self.meowface_cache_ping_lb.setObjectName(u"meowface_cache_ping_lb")

        self.horizontalLayout_67.addWidget(self.meowface_cache_ping_lb)

        self.meowface_cache_ping_sb = QDoubleSpinBox(self.meowface_cache_ping_widget)
        self.meowface_cache_ping_sb.setObjectName(u"meowface_cache_ping_sb")
        self.meowface_cache_ping_sb.setDecimals(3)
        self.meowface_cache_ping_sb.setMinimum(0.001000000000000)
        self.meowface_cache_ping_sb.setMaximum(60.000000000000000)
        self.meowface_cache_ping_sb.setValue(0.500000000000000)

        self.horizontalLayout_67.addWidget(self.meowface_cache_ping_sb)


        self.verticalLayout_13.addWidget(self.meowface_cache_ping_widget)

        self.meowface_cache_float_percision_widget = QWidget(self.widget_6)
        self.meowface_cache_float_percision_widget.setObjectName(u"meowface_cache_float_percision_widget")
        self.horizontalLayout_65 = QHBoxLayout(self.meowface_cache_float_percision_widget)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.meowface_cache_float_percision_lb = QLabel(self.meowface_cache_float_percision_widget)
        self.meowface_cache_float_percision_lb.setObjectName(u"meowface_cache_float_percision_lb")

        self.horizontalLayout_65.addWidget(self.meowface_cache_float_percision_lb)

        self.meowface_cache_float_percision_sb = QDoubleSpinBox(self.meowface_cache_float_percision_widget)
        self.meowface_cache_float_percision_sb.setObjectName(u"meowface_cache_float_percision_sb")
        self.meowface_cache_float_percision_sb.setDecimals(6)
        self.meowface_cache_float_percision_sb.setMinimum(0.000000000000000)
        self.meowface_cache_float_percision_sb.setMaximum(0.500000000000000)
        self.meowface_cache_float_percision_sb.setValue(0.003906000000000)

        self.horizontalLayout_65.addWidget(self.meowface_cache_float_percision_sb)


        self.verticalLayout_13.addWidget(self.meowface_cache_float_percision_widget)


        self.verticalLayout_7.addWidget(self.widget_6)

        self.verticalSpacer_3 = QSpacerItem(20, 104, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_5.addWidget(self.scrollArea_3)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_6 = QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.scrollArea_4 = QScrollArea(self.tab_3)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 852, 583))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.foxyface_enable_cb = QCheckBox(self.scrollAreaWidgetContents_5)
        self.foxyface_enable_cb.setObjectName(u"foxyface_enable_cb")

        self.verticalLayout_8.addWidget(self.foxyface_enable_cb)

        self.widget_8 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_15 = QVBoxLayout(self.widget_8)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.foxyface_connection_lb = QLabel(self.widget_8)
        self.foxyface_connection_lb.setObjectName(u"foxyface_connection_lb")
        self.foxyface_connection_lb.setFont(font)
        self.foxyface_connection_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.foxyface_connection_lb)

        self.foxyface_connection_line = QFrame(self.widget_8)
        self.foxyface_connection_line.setObjectName(u"foxyface_connection_line")
        self.foxyface_connection_line.setFrameShape(QFrame.Shape.HLine)
        self.foxyface_connection_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_15.addWidget(self.foxyface_connection_line)

        self.foxyface_ip_auto_find_cb = QCheckBox(self.widget_8)
        self.foxyface_ip_auto_find_cb.setObjectName(u"foxyface_ip_auto_find_cb")
        self.foxyface_ip_auto_find_cb.setChecked(True)

        self.verticalLayout_15.addWidget(self.foxyface_ip_auto_find_cb)

        self.foxyface_ip_widget = QWidget(self.widget_8)
        self.foxyface_ip_widget.setObjectName(u"foxyface_ip_widget")
        self.horizontalLayout_103 = QHBoxLayout(self.foxyface_ip_widget)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.horizontalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.foxyface_ip_lb = QLabel(self.foxyface_ip_widget)
        self.foxyface_ip_lb.setObjectName(u"foxyface_ip_lb")

        self.horizontalLayout_103.addWidget(self.foxyface_ip_lb)

        self.foxyface_ip_le = QLineEdit(self.foxyface_ip_widget)
        self.foxyface_ip_le.setObjectName(u"foxyface_ip_le")
        self.foxyface_ip_le.setEnabled(False)
        self.foxyface_ip_le.setMaxLength(256)

        self.horizontalLayout_103.addWidget(self.foxyface_ip_le)


        self.verticalLayout_15.addWidget(self.foxyface_ip_widget)

        self.foxyface_port_widget = QWidget(self.widget_8)
        self.foxyface_port_widget.setObjectName(u"foxyface_port_widget")
        self.horizontalLayout_109 = QHBoxLayout(self.foxyface_port_widget)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.horizontalLayout_109.setContentsMargins(0, 0, 0, 0)
        self.foxyface_port_lb = QLabel(self.foxyface_port_widget)
        self.foxyface_port_lb.setObjectName(u"foxyface_port_lb")

        self.horizontalLayout_109.addWidget(self.foxyface_port_lb)

        self.foxyface_port_sb = QSpinBox(self.foxyface_port_widget)
        self.foxyface_port_sb.setObjectName(u"foxyface_port_sb")
        self.foxyface_port_sb.setEnabled(False)
        self.foxyface_port_sb.setMaximum(65535)
        self.foxyface_port_sb.setValue(49983)

        self.horizontalLayout_109.addWidget(self.foxyface_port_sb)


        self.verticalLayout_15.addWidget(self.foxyface_port_widget)

        self.foxyface_solver_lb = QLabel(self.widget_8)
        self.foxyface_solver_lb.setObjectName(u"foxyface_solver_lb")
        self.foxyface_solver_lb.setFont(font)
        self.foxyface_solver_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.foxyface_solver_lb)

        self.foxyface_solver_line = QFrame(self.widget_8)
        self.foxyface_solver_line.setObjectName(u"foxyface_solver_line")
        self.foxyface_solver_line.setFrameShape(QFrame.Shape.HLine)
        self.foxyface_solver_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_15.addWidget(self.foxyface_solver_line)

        self.foxyface_enable_solver_cb = QCheckBox(self.widget_8)
        self.foxyface_enable_solver_cb.setObjectName(u"foxyface_enable_solver_cb")
        self.foxyface_enable_solver_cb.setChecked(True)

        self.verticalLayout_15.addWidget(self.foxyface_enable_solver_cb)

        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_16 = QVBoxLayout(self.widget_9)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.foxyface_solver_model_widget = QWidget(self.widget_9)
        self.foxyface_solver_model_widget.setObjectName(u"foxyface_solver_model_widget")
        self.horizontalLayout_107 = QHBoxLayout(self.foxyface_solver_model_widget)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.foxyface_solver_model_lb = QLabel(self.foxyface_solver_model_widget)
        self.foxyface_solver_model_lb.setObjectName(u"foxyface_solver_model_lb")

        self.horizontalLayout_107.addWidget(self.foxyface_solver_model_lb)

        self.foxyface_solver_model_le = QLineEdit(self.foxyface_solver_model_widget)
        self.foxyface_solver_model_le.setObjectName(u"foxyface_solver_model_le")

        self.horizontalLayout_107.addWidget(self.foxyface_solver_model_le)

        self.foxyface_solver_model_btn = QToolButton(self.foxyface_solver_model_widget)
        self.foxyface_solver_model_btn.setObjectName(u"foxyface_solver_model_btn")

        self.horizontalLayout_107.addWidget(self.foxyface_solver_model_btn)


        self.verticalLayout_16.addWidget(self.foxyface_solver_model_widget)

        self.foxyface_solver_sercision_widget = QWidget(self.widget_9)
        self.foxyface_solver_sercision_widget.setObjectName(u"foxyface_solver_sercision_widget")
        self.horizontalLayout_100 = QHBoxLayout(self.foxyface_solver_sercision_widget)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_100.setContentsMargins(0, 0, 0, 0)
        self.foxyface_solver_sercision_lb = QLabel(self.foxyface_solver_sercision_widget)
        self.foxyface_solver_sercision_lb.setObjectName(u"foxyface_solver_sercision_lb")

        self.horizontalLayout_100.addWidget(self.foxyface_solver_sercision_lb)

        self.foxyface_solver_sercision_slider = QSlider(self.foxyface_solver_sercision_widget)
        self.foxyface_solver_sercision_slider.setObjectName(u"foxyface_solver_sercision_slider")
        self.foxyface_solver_sercision_slider.setMinimum(1)
        self.foxyface_solver_sercision_slider.setMaximum(100)
        self.foxyface_solver_sercision_slider.setValue(80)
        self.foxyface_solver_sercision_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_100.addWidget(self.foxyface_solver_sercision_slider)


        self.verticalLayout_16.addWidget(self.foxyface_solver_sercision_widget)

        self.foxyface_solver_threads_widget = QWidget(self.widget_9)
        self.foxyface_solver_threads_widget.setObjectName(u"foxyface_solver_threads_widget")
        self.horizontalLayout_101 = QHBoxLayout(self.foxyface_solver_threads_widget)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.foxyface_solver_threads_lb = QLabel(self.foxyface_solver_threads_widget)
        self.foxyface_solver_threads_lb.setObjectName(u"foxyface_solver_threads_lb")

        self.horizontalLayout_101.addWidget(self.foxyface_solver_threads_lb)

        self.foxyface_solver_threads_sb = QSpinBox(self.foxyface_solver_threads_widget)
        self.foxyface_solver_threads_sb.setObjectName(u"foxyface_solver_threads_sb")
        self.foxyface_solver_threads_sb.setMinimum(1)
        self.foxyface_solver_threads_sb.setMaximum(32)
        self.foxyface_solver_threads_sb.setValue(2)

        self.horizontalLayout_101.addWidget(self.foxyface_solver_threads_sb)


        self.verticalLayout_16.addWidget(self.foxyface_solver_threads_widget)

        self.foxyface_solver_max_fps_widget = QWidget(self.widget_9)
        self.foxyface_solver_max_fps_widget.setObjectName(u"foxyface_solver_max_fps_widget")
        self.horizontalLayout_105 = QHBoxLayout(self.foxyface_solver_max_fps_widget)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.horizontalLayout_105.setContentsMargins(0, 0, 0, 0)
        self.foxyface_solver_max_fps_lb = QLabel(self.foxyface_solver_max_fps_widget)
        self.foxyface_solver_max_fps_lb.setObjectName(u"foxyface_solver_max_fps_lb")

        self.horizontalLayout_105.addWidget(self.foxyface_solver_max_fps_lb)

        self.foxyface_solver_max_fps_sb = QSpinBox(self.foxyface_solver_max_fps_widget)
        self.foxyface_solver_max_fps_sb.setObjectName(u"foxyface_solver_max_fps_sb")
        self.foxyface_solver_max_fps_sb.setMinimum(1)
        self.foxyface_solver_max_fps_sb.setMaximum(120)
        self.foxyface_solver_max_fps_sb.setValue(30)

        self.horizontalLayout_105.addWidget(self.foxyface_solver_max_fps_sb)


        self.verticalLayout_16.addWidget(self.foxyface_solver_max_fps_widget)


        self.verticalLayout_15.addWidget(self.widget_9)

        self.foxyface_cache_lb = QLabel(self.widget_8)
        self.foxyface_cache_lb.setObjectName(u"foxyface_cache_lb")
        self.foxyface_cache_lb.setFont(font)
        self.foxyface_cache_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.foxyface_cache_lb)

        self.foxyface_cache_line = QFrame(self.widget_8)
        self.foxyface_cache_line.setObjectName(u"foxyface_cache_line")
        self.foxyface_cache_line.setFrameShape(QFrame.Shape.HLine)
        self.foxyface_cache_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_15.addWidget(self.foxyface_cache_line)

        self.foxyface_cache_invalidate_widget = QWidget(self.widget_8)
        self.foxyface_cache_invalidate_widget.setObjectName(u"foxyface_cache_invalidate_widget")
        self.horizontalLayout_108 = QHBoxLayout(self.foxyface_cache_invalidate_widget)
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.horizontalLayout_108.setContentsMargins(0, 0, 0, 0)
        self.foxyface_cache_invalidate_lb = QLabel(self.foxyface_cache_invalidate_widget)
        self.foxyface_cache_invalidate_lb.setObjectName(u"foxyface_cache_invalidate_lb")

        self.horizontalLayout_108.addWidget(self.foxyface_cache_invalidate_lb)

        self.foxyface_cache_invalidate_sb = QDoubleSpinBox(self.foxyface_cache_invalidate_widget)
        self.foxyface_cache_invalidate_sb.setObjectName(u"foxyface_cache_invalidate_sb")
        self.foxyface_cache_invalidate_sb.setMaximum(60.000000000000000)
        self.foxyface_cache_invalidate_sb.setValue(5.000000000000000)

        self.horizontalLayout_108.addWidget(self.foxyface_cache_invalidate_sb)


        self.verticalLayout_15.addWidget(self.foxyface_cache_invalidate_widget)

        self.foxyface_cache_sync_widget = QWidget(self.widget_8)
        self.foxyface_cache_sync_widget.setObjectName(u"foxyface_cache_sync_widget")
        self.horizontalLayout_102 = QHBoxLayout(self.foxyface_cache_sync_widget)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.horizontalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.foxyface_cache_sync_lb = QLabel(self.foxyface_cache_sync_widget)
        self.foxyface_cache_sync_lb.setObjectName(u"foxyface_cache_sync_lb")

        self.horizontalLayout_102.addWidget(self.foxyface_cache_sync_lb)

        self.foxyface_cache_sync_sb = QDoubleSpinBox(self.foxyface_cache_sync_widget)
        self.foxyface_cache_sync_sb.setObjectName(u"foxyface_cache_sync_sb")
        self.foxyface_cache_sync_sb.setMaximum(60.000000000000000)
        self.foxyface_cache_sync_sb.setValue(5.000000000000000)

        self.horizontalLayout_102.addWidget(self.foxyface_cache_sync_sb)


        self.verticalLayout_15.addWidget(self.foxyface_cache_sync_widget)

        self.foxyface_cache_ping_widget = QWidget(self.widget_8)
        self.foxyface_cache_ping_widget.setObjectName(u"foxyface_cache_ping_widget")
        self.horizontalLayout_106 = QHBoxLayout(self.foxyface_cache_ping_widget)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.horizontalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.foxyface_cache_ping_lb = QLabel(self.foxyface_cache_ping_widget)
        self.foxyface_cache_ping_lb.setObjectName(u"foxyface_cache_ping_lb")

        self.horizontalLayout_106.addWidget(self.foxyface_cache_ping_lb)

        self.foxyface_cache_ping_sb = QDoubleSpinBox(self.foxyface_cache_ping_widget)
        self.foxyface_cache_ping_sb.setObjectName(u"foxyface_cache_ping_sb")
        self.foxyface_cache_ping_sb.setDecimals(3)
        self.foxyface_cache_ping_sb.setMinimum(0.001000000000000)
        self.foxyface_cache_ping_sb.setMaximum(60.000000000000000)
        self.foxyface_cache_ping_sb.setValue(2.500000000000000)

        self.horizontalLayout_106.addWidget(self.foxyface_cache_ping_sb)


        self.verticalLayout_15.addWidget(self.foxyface_cache_ping_widget)

        self.foxyface_cache_float_percision_widget = QWidget(self.widget_8)
        self.foxyface_cache_float_percision_widget.setObjectName(u"foxyface_cache_float_percision_widget")
        self.horizontalLayout_104 = QHBoxLayout(self.foxyface_cache_float_percision_widget)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.horizontalLayout_104.setContentsMargins(0, 0, 0, 0)
        self.foxyface_cache_float_percision_lb = QLabel(self.foxyface_cache_float_percision_widget)
        self.foxyface_cache_float_percision_lb.setObjectName(u"foxyface_cache_float_percision_lb")

        self.horizontalLayout_104.addWidget(self.foxyface_cache_float_percision_lb)

        self.foxyface_cache_float_percision_sb = QDoubleSpinBox(self.foxyface_cache_float_percision_widget)
        self.foxyface_cache_float_percision_sb.setObjectName(u"foxyface_cache_float_percision_sb")
        self.foxyface_cache_float_percision_sb.setDecimals(6)
        self.foxyface_cache_float_percision_sb.setMinimum(0.000000000000000)
        self.foxyface_cache_float_percision_sb.setMaximum(0.500000000000000)
        self.foxyface_cache_float_percision_sb.setValue(0.003906000000000)

        self.horizontalLayout_104.addWidget(self.foxyface_cache_float_percision_sb)


        self.verticalLayout_15.addWidget(self.foxyface_cache_float_percision_widget)


        self.verticalLayout_8.addWidget(self.widget_8)

        self.verticalSpacer_4 = QSpacerItem(20, 104, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_6.addWidget(self.scrollArea_4)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_4.addWidget(self.tabWidget)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.full_reset_btn = QPushButton(self.widget)
        self.full_reset_btn.setObjectName(u"full_reset_btn")

        self.horizontalLayout.addWidget(self.full_reset_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.save_btn = QPushButton(self.widget)
        self.save_btn.setObjectName(u"save_btn")

        self.horizontalLayout.addWidget(self.save_btn)


        self.verticalLayout_4.addWidget(self.widget)

        SenderSettings.setCentralWidget(self.centralwidget)

        self.retranslateUi(SenderSettings)
        self.vrchat_enable_cb.toggled.connect(self.widget_2.setVisible)
        self.vrchat_enable_solver_cb.toggled.connect(self.widget_3.setVisible)
        self.ifm_enable_cb.toggled.connect(self.widget_4.setVisible)
        self.ifm_enable_solver_cb.toggled.connect(self.widget_5.setVisible)
        self.meowface_ip_auto_find_cb.toggled.connect(self.meowface_ip_le.setDisabled)
        self.meowface_ip_auto_find_cb.toggled.connect(self.meowface_port_sb.setDisabled)
        self.ifm_ip_auto_find_cb.toggled.connect(self.ifm_ip_le.setDisabled)
        self.ifm_ip_auto_find_cb.toggled.connect(self.ifm_port_sb.setDisabled)
        self.foxyface_ip_auto_find_cb.toggled.connect(self.foxyface_ip_le.setDisabled)
        self.foxyface_ip_auto_find_cb.toggled.connect(self.foxyface_port_sb.setDisabled)
        self.meowface_enable_cb.toggled.connect(self.widget_6.setVisible)
        self.meowface_enable_solver_cb.toggled.connect(self.widget_7.setEnabled)
        self.foxyface_enable_cb.toggled.connect(self.widget_8.setVisible)
        self.foxyface_enable_solver_cb.toggled.connect(self.widget_9.setVisible)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(SenderSettings)
    # setupUi

    def retranslateUi(self, SenderSettings):
        SenderSettings.setWindowTitle(QCoreApplication.translate("SenderSettings", u"MainWindow", None))
        self.vrchat_enable_cb.setText(QCoreApplication.translate("SenderSettings", u"Enable VRChat Routing", None))
        self.vrchat_connection_lb.setText(QCoreApplication.translate("SenderSettings", u"Connection", None))
        self.vrchat_avatare_request_period_lb.setText(QCoreApplication.translate("SenderSettings", u"Avatar Request Period:", None))
        self.vrchat_avatare_request_period_sb.setSuffix(QCoreApplication.translate("SenderSettings", u" seconds", None))
        self.vrchat_error_sleep_tim_lb.setText(QCoreApplication.translate("SenderSettings", u"Sleep time after error:", None))
        self.vrchat_error_sleep_tim_sb.setSuffix(QCoreApplication.translate("SenderSettings", u" seconds", None))
        self.vrchat_close_connectio_lb.setText(QCoreApplication.translate("SenderSettings", u"Close connection after", None))
        self.vrchat_close_connectio_sb.setSuffix(QCoreApplication.translate("SenderSettings", u" retries", None))
        self.vrchat_zeroconf_lb.setText(QCoreApplication.translate("SenderSettings", u"Zeroconf Timeout", None))
        self.vrchat_zeroconf_sb.setSuffix(QCoreApplication.translate("SenderSettings", u" seconds", None))
        self.vrchat_solver_lb.setText(QCoreApplication.translate("SenderSettings", u"Solver", None))
        self.vrchat_enable_solver_cb.setText(QCoreApplication.translate("SenderSettings", u"Solver Enabled", None))
        self.vrchat_solver_model_lb.setText(QCoreApplication.translate("SenderSettings", u"Model Path:", None))
        self.vrchat_solver_model_le.setPlaceholderText(QCoreApplication.translate("SenderSettings", u"Default Model", None))
        self.vrchat_solver_model_btn.setText(QCoreApplication.translate("SenderSettings", u"...", None))
        self.vrchat_solver_sercision_lb.setText(QCoreApplication.translate("SenderSettings", u"Solver Precision (80%): ", None))
        self.vrchat_solver_threads_lb.setText(QCoreApplication.translate("SenderSettings", u"Thread Count:", None))
        self.vrchat_solver_max_fps_lb.setText(QCoreApplication.translate("SenderSettings", u"Max Solver FPS:", None))
        self.vrchat_cache_lb.setText(QCoreApplication.translate("SenderSettings", u"OSC Cache", None))
        self.vrchat_cache_invalidate_lb.setText(QCoreApplication.translate("SenderSettings", u"Invalidate after:", None))
        self.vrchat_cache_invalidate_sb.setSuffix(QCoreApplication.translate("SenderSettings", u" seconds", None))
        self.vrchat_cache_sync_lb.setText(QCoreApplication.translate("SenderSettings", u"Full Sync Period:", None))
        self.vrchat_cache_sync_sb.setSuffix(QCoreApplication.translate("SenderSettings", u" seconds", None))
        self.vrchat_cache_float_percision_lb.setText(QCoreApplication.translate("SenderSettings", u"Float precision:", None))
        self.vrchat_cache_bundle_lb.setText(QCoreApplication.translate("SenderSettings", u"OSC Bundle Size:", None))
        self.vrchat_cache_bundle_sb.setSuffix(QCoreApplication.translate("SenderSettings", u" bytes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("SenderSettings", u"VRChat/ChilloutVR", None))
        self.ifm_enable_cb.setText(QCoreApplication.translate("SenderSettings", u"Enable iFacialMocap Router", None))
        self.ifm_connection_lb.setText(QCoreApplication.translate("SenderSettings", u"Connection", None))
        self.ifm_ip_auto_find_cb.setText(QCoreApplication.translate("SenderSettings", u"Auto Search IP/Port", None))
        self.ifm_ip_lb.setText(QCoreApplication.translate("SenderSettings", u"IP:", None))
        self.ifm_ip_le.setText(QCoreApplication.translate("SenderSettings", u"localhost", None))
        self.ifm_port_lb.setText(QCoreApplication.translate("SenderSettings", u"Port:", None))
        self.ifm_solver_lb.setText(QCoreApplication.translate("SenderSettings", u"Solver", None))
        self.ifm_enable_solver_cb.setText(QCoreApplication.translate("SenderSettings", u"Solver Enabled", None))
        self.ifm_solver_model_lb.setText(QCoreApplication.translate("SenderSettings", u"Model Path:", None))
        self.ifm_solver_model_le.setPlaceholderText(QCoreApplication.translate("SenderSettings", u"Default Model", None))
        self.ifm_solver_model_btn.setText(QCoreApplication.translate("SenderSettings", u"...", None))
        self.ifm_solver_sercision_lb.setText(QCoreApplication.translate("SenderSettings", u"Solver Precision (80%): ", None))
        self.ifm_solver_threads_lb.setText(QCoreApplication.translate("SenderSettings", u"Thread Count:", None))
        self.ifm_solver_max_fps_lb.setText(QCoreApplication.translate("SenderSettings", u"Max Solver FPS:", None))
        self.ifm_cache_lb.setText(QCoreApplication.translate("SenderSettings", u"UDP Cache", None))
        self.ifm_cache_invalidate_lb.setText(QCoreApplication.translate("SenderSettings", u"Invalidate after:", None))
        self.ifm_cache_invalidate_sb.setSuffix(QCoreApplication.translate("SenderSettings", u" seconds", None))
        self.ifm_cache_sync_lb.setText(QCoreApplication.translate("SenderSettings", u"Full Sync Period:", None))
        self.ifm_cache_sync_sb.setSuffix(QCoreApplication.translate("SenderSettings", u" seconds", None))
        self.ifm_cache_ping_lb.setText(QCoreApplication.translate("SenderSettings", u"Ping Interval:", None))
        self.ifm_cache_ping_sb.setSuffix(QCoreApplication.translate("SenderSettings", u" seconds", None))
        self.ifm_cache_float_percision_lb.setText(QCoreApplication.translate("SenderSettings", u"Float precision:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("SenderSettings", u"iFacialMocap", None))
        self.meowface_enable_cb.setText(QCoreApplication.translate("SenderSettings", u"Enable MeowFace Router", None))
        self.meowface_connection_lb.setText(QCoreApplication.translate("SenderSettings", u"Connection", None))
        self.meowface_ip_auto_find_cb.setText(QCoreApplication.translate("SenderSettings", u"Auto Search IP/Port", None))
        self.meowface_ip_lb.setText(QCoreApplication.translate("SenderSettings", u"IP:", None))
        self.meowface_ip_le.setText(QCoreApplication.translate("SenderSettings", u"localhost", None))
        self.meowface_port_lb.setText(QCoreApplication.translate("SenderSettings", u"Port:", None))
        self.meowface_solver_lb.setText(QCoreApplication.translate("SenderSettings", u"Solver", None))
        self.meowface_enable_solver_cb.setText(QCoreApplication.translate("SenderSettings", u"Solver Enabled", None))
        self.meowface_solver_model_lb.setText(QCoreApplication.translate("SenderSettings", u"Model Path:", None))
        self.meowface_solver_model_le.setPlaceholderText(QCoreApplication.translate("SenderSettings", u"Default Model", None))
        self.meowface_solver_model_btn.setText(QCoreApplication.translate("SenderSettings", u"...", None))
        self.meowface_solver_sercision_lb.setText(QCoreApplication.translate("SenderSettings", u"Solver Precision (80%): ", None))
        self.meowface_solver_threads_lb.setText(QCoreApplication.translate("SenderSettings", u"Thread Count:", None))
        self.meowface_solver_max_fps_lb.setText(QCoreApplication.translate("SenderSettings", u"Max Solver FPS:", None))
        self.meowface_cache_lb.setText(QCoreApplication.translate("SenderSettings", u"UDP Cache", None))
        self.meowface_cache_invalidate_lb.setText(QCoreApplication.translate("SenderSettings", u"Invalidate after:", None))
        self.meowface_cache_invalidate_sb.setSuffix(QCoreApplication.translate("SenderSettings", u" seconds", None))
        self.meowface_cache_sync_lb.setText(QCoreApplication.translate("SenderSettings", u"Full Sync Period:", None))
        self.meowface_cache_sync_sb.setSuffix(QCoreApplication.translate("SenderSettings", u" seconds", None))
        self.meowface_cache_ping_lb.setText(QCoreApplication.translate("SenderSettings", u"Ping Interval:", None))
        self.meowface_cache_ping_sb.setSuffix(QCoreApplication.translate("SenderSettings", u" seconds", None))
        self.meowface_cache_float_percision_lb.setText(QCoreApplication.translate("SenderSettings", u"Float precision:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("SenderSettings", u"MeowFace", None))
        self.foxyface_enable_cb.setText(QCoreApplication.translate("SenderSettings", u"Enable FoxyFace Router", None))
        self.foxyface_connection_lb.setText(QCoreApplication.translate("SenderSettings", u"Connection", None))
        self.foxyface_ip_auto_find_cb.setText(QCoreApplication.translate("SenderSettings", u"Auto Search IP/Port", None))
        self.foxyface_ip_lb.setText(QCoreApplication.translate("SenderSettings", u"IP:", None))
        self.foxyface_ip_le.setText(QCoreApplication.translate("SenderSettings", u"localhost", None))
        self.foxyface_port_lb.setText(QCoreApplication.translate("SenderSettings", u"Port:", None))
        self.foxyface_solver_lb.setText(QCoreApplication.translate("SenderSettings", u"Solver", None))
        self.foxyface_enable_solver_cb.setText(QCoreApplication.translate("SenderSettings", u"Solver Enabled", None))
        self.foxyface_solver_model_lb.setText(QCoreApplication.translate("SenderSettings", u"Model Path:", None))
        self.foxyface_solver_model_le.setPlaceholderText(QCoreApplication.translate("SenderSettings", u"Default Model", None))
        self.foxyface_solver_model_btn.setText(QCoreApplication.translate("SenderSettings", u"...", None))
        self.foxyface_solver_sercision_lb.setText(QCoreApplication.translate("SenderSettings", u"Solver Precision (80%): ", None))
        self.foxyface_solver_threads_lb.setText(QCoreApplication.translate("SenderSettings", u"Thread Count:", None))
        self.foxyface_solver_max_fps_lb.setText(QCoreApplication.translate("SenderSettings", u"Max Solver FPS:", None))
        self.foxyface_cache_lb.setText(QCoreApplication.translate("SenderSettings", u"UDP Cache", None))
        self.foxyface_cache_invalidate_lb.setText(QCoreApplication.translate("SenderSettings", u"Invalidate after:", None))
        self.foxyface_cache_invalidate_sb.setSuffix(QCoreApplication.translate("SenderSettings", u" seconds", None))
        self.foxyface_cache_sync_lb.setText(QCoreApplication.translate("SenderSettings", u"Full Sync Period:", None))
        self.foxyface_cache_sync_sb.setSuffix(QCoreApplication.translate("SenderSettings", u" seconds", None))
        self.foxyface_cache_ping_lb.setText(QCoreApplication.translate("SenderSettings", u"Ping Interval:", None))
        self.foxyface_cache_ping_sb.setSuffix(QCoreApplication.translate("SenderSettings", u" seconds", None))
        self.foxyface_cache_float_percision_lb.setText(QCoreApplication.translate("SenderSettings", u"Float precision:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("SenderSettings", u"FoxyFace", None))
        self.full_reset_btn.setText(QCoreApplication.translate("SenderSettings", u"Full Reset", None))
        self.save_btn.setText(QCoreApplication.translate("SenderSettings", u"Apply and Save", None))
    # retranslateUi

