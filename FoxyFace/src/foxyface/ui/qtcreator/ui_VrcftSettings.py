# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VrcftSettings.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QTabWidget, QToolButton, QVBoxLayout, QWidget)

class Ui_VrcftSettings(object):
    def setupUi(self, VrcftSettings):
        if not VrcftSettings.objectName():
            VrcftSettings.setObjectName(u"VrcftSettings")
        VrcftSettings.resize(333, 414)
        self.centralwidget = QWidget(VrcftSettings)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.connection_tab = QWidget()
        self.connection_tab.setObjectName(u"connection_tab")
        self.verticalLayout_2 = QVBoxLayout(self.connection_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea_2 = QScrollArea(self.connection_tab)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 291, 314))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.auto_connect_cb = QCheckBox(self.scrollAreaWidgetContents_2)
        self.auto_connect_cb.setObjectName(u"auto_connect_cb")
        self.auto_connect_cb.setChecked(True)

        self.verticalLayout_7.addWidget(self.auto_connect_cb)

        self.ip_lb = QLabel(self.scrollAreaWidgetContents_2)
        self.ip_lb.setObjectName(u"ip_lb")

        self.verticalLayout_7.addWidget(self.ip_lb)

        self.ip_le = QLineEdit(self.scrollAreaWidgetContents_2)
        self.ip_le.setObjectName(u"ip_le")
        self.ip_le.setEnabled(False)
        self.ip_le.setMaxLength(256)

        self.verticalLayout_7.addWidget(self.ip_le)

        self.port_lb = QLabel(self.scrollAreaWidgetContents_2)
        self.port_lb.setObjectName(u"port_lb")

        self.verticalLayout_7.addWidget(self.port_lb)

        self.port_sp = QSpinBox(self.scrollAreaWidgetContents_2)
        self.port_sp.setObjectName(u"port_sp")
        self.port_sp.setEnabled(False)
        self.port_sp.setMaximum(65535)
        self.port_sp.setValue(54321)

        self.verticalLayout_7.addWidget(self.port_sp)

        self.read_timeout_lb = QLabel(self.scrollAreaWidgetContents_2)
        self.read_timeout_lb.setObjectName(u"read_timeout_lb")

        self.verticalLayout_7.addWidget(self.read_timeout_lb)

        self.read_timeout_sp = QSpinBox(self.scrollAreaWidgetContents_2)
        self.read_timeout_sp.setObjectName(u"read_timeout_sp")
        self.read_timeout_sp.setMinimum(10)
        self.read_timeout_sp.setMaximum(60000)
        self.read_timeout_sp.setSingleStep(100)
        self.read_timeout_sp.setValue(2500)

        self.verticalLayout_7.addWidget(self.read_timeout_sp)

        self.bypass_cb = QCheckBox(self.scrollAreaWidgetContents_2)
        self.bypass_cb.setObjectName(u"bypass_cb")

        self.verticalLayout_7.addWidget(self.bypass_cb)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.connection_tab, "")
        self.auto_run_tab = QWidget()
        self.auto_run_tab.setObjectName(u"auto_run_tab")
        self.verticalLayout_3 = QVBoxLayout(self.auto_run_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(self.auto_run_tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 277, 360))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.run_vrchat_strategy_layout = QHBoxLayout()
        self.run_vrchat_strategy_layout.setObjectName(u"run_vrchat_strategy_layout")
        self.run_vrchat_strategy_lb = QLabel(self.scrollAreaWidgetContents)
        self.run_vrchat_strategy_lb.setObjectName(u"run_vrchat_strategy_lb")

        self.run_vrchat_strategy_layout.addWidget(self.run_vrchat_strategy_lb)

        self.run_vrchat_strategy_cb = QComboBox(self.scrollAreaWidgetContents)
        self.run_vrchat_strategy_cb.addItem("")
        self.run_vrchat_strategy_cb.addItem("")
        self.run_vrchat_strategy_cb.addItem("")
        self.run_vrchat_strategy_cb.setObjectName(u"run_vrchat_strategy_cb")

        self.run_vrchat_strategy_layout.addWidget(self.run_vrchat_strategy_cb)


        self.verticalLayout_6.addLayout(self.run_vrchat_strategy_layout)

        self.vrchat_file_path_widget = QWidget(self.scrollAreaWidgetContents)
        self.vrchat_file_path_widget.setObjectName(u"vrchat_file_path_widget")
        self.verticalLayout_4 = QVBoxLayout(self.vrchat_file_path_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.vrchat_file_path_lb = QLabel(self.vrchat_file_path_widget)
        self.vrchat_file_path_lb.setObjectName(u"vrchat_file_path_lb")

        self.verticalLayout_4.addWidget(self.vrchat_file_path_lb)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.vrchat_file_path_le = QLineEdit(self.vrchat_file_path_widget)
        self.vrchat_file_path_le.setObjectName(u"vrchat_file_path_le")

        self.horizontalLayout_4.addWidget(self.vrchat_file_path_le)

        self.vrchat_file_path_select_btn = QToolButton(self.vrchat_file_path_widget)
        self.vrchat_file_path_select_btn.setObjectName(u"vrchat_file_path_select_btn")

        self.horizontalLayout_4.addWidget(self.vrchat_file_path_select_btn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.vrchat_auto_run_error_lb = QLabel(self.vrchat_file_path_widget)
        self.vrchat_auto_run_error_lb.setObjectName(u"vrchat_auto_run_error_lb")
        self.vrchat_auto_run_error_lb.setStyleSheet(u"color: red")
        self.vrchat_auto_run_error_lb.setText(u"Error: Message")
        self.vrchat_auto_run_error_lb.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.vrchat_auto_run_error_lb)

        self.vrchat_file_path_reset_widget = QWidget(self.vrchat_file_path_widget)
        self.vrchat_file_path_reset_widget.setObjectName(u"vrchat_file_path_reset_widget")
        self.horizontalLayout_5 = QHBoxLayout(self.vrchat_file_path_reset_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.vrchat_file_path_reset_btn = QPushButton(self.vrchat_file_path_reset_widget)
        self.vrchat_file_path_reset_btn.setObjectName(u"vrchat_file_path_reset_btn")

        self.horizontalLayout_5.addWidget(self.vrchat_file_path_reset_btn)


        self.verticalLayout_4.addWidget(self.vrchat_file_path_reset_widget)


        self.verticalLayout_6.addWidget(self.vrchat_file_path_widget)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.run_vrcft_strategy_layout = QHBoxLayout()
        self.run_vrcft_strategy_layout.setObjectName(u"run_vrcft_strategy_layout")
        self.run_vrcft_strategy_lb = QLabel(self.scrollAreaWidgetContents)
        self.run_vrcft_strategy_lb.setObjectName(u"run_vrcft_strategy_lb")

        self.run_vrcft_strategy_layout.addWidget(self.run_vrcft_strategy_lb)

        self.run_vrcft_strategy_cb = QComboBox(self.scrollAreaWidgetContents)
        self.run_vrcft_strategy_cb.addItem("")
        self.run_vrcft_strategy_cb.addItem("")
        self.run_vrcft_strategy_cb.addItem("")
        self.run_vrcft_strategy_cb.setObjectName(u"run_vrcft_strategy_cb")

        self.run_vrcft_strategy_layout.addWidget(self.run_vrcft_strategy_cb)


        self.verticalLayout_6.addLayout(self.run_vrcft_strategy_layout)

        self.vrcft_file_path_widget = QWidget(self.scrollAreaWidgetContents)
        self.vrcft_file_path_widget.setObjectName(u"vrcft_file_path_widget")
        self.verticalLayout_5 = QVBoxLayout(self.vrcft_file_path_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.vrcft_file_path_lb = QLabel(self.vrcft_file_path_widget)
        self.vrcft_file_path_lb.setObjectName(u"vrcft_file_path_lb")

        self.verticalLayout_5.addWidget(self.vrcft_file_path_lb)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.vrcft_file_path_le = QLineEdit(self.vrcft_file_path_widget)
        self.vrcft_file_path_le.setObjectName(u"vrcft_file_path_le")

        self.horizontalLayout_6.addWidget(self.vrcft_file_path_le)

        self.vrcft_file_path_select_btn = QToolButton(self.vrcft_file_path_widget)
        self.vrcft_file_path_select_btn.setObjectName(u"vrcft_file_path_select_btn")

        self.horizontalLayout_6.addWidget(self.vrcft_file_path_select_btn)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.vrcft_auto_run_error_lb = QLabel(self.vrcft_file_path_widget)
        self.vrcft_auto_run_error_lb.setObjectName(u"vrcft_auto_run_error_lb")
        self.vrcft_auto_run_error_lb.setStyleSheet(u"color: red")
        self.vrcft_auto_run_error_lb.setText(u"Error: Message")
        self.vrcft_auto_run_error_lb.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.vrcft_auto_run_error_lb)

        self.vrcft_file_path_reset_widget = QWidget(self.vrcft_file_path_widget)
        self.vrcft_file_path_reset_widget.setObjectName(u"vrcft_file_path_reset_widget")
        self.horizontalLayout_7 = QHBoxLayout(self.vrcft_file_path_reset_widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.vrcft_file_path_reset_btn = QPushButton(self.vrcft_file_path_reset_widget)
        self.vrcft_file_path_reset_btn.setObjectName(u"vrcft_file_path_reset_btn")

        self.horizontalLayout_7.addWidget(self.vrcft_file_path_reset_btn)


        self.verticalLayout_5.addWidget(self.vrcft_file_path_reset_widget)


        self.verticalLayout_6.addWidget(self.vrcft_file_path_widget)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.force_run_widget = QWidget(self.auto_run_tab)
        self.force_run_widget.setObjectName(u"force_run_widget")
        self.horizontalLayout_8 = QHBoxLayout(self.force_run_widget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.force_run_btn = QPushButton(self.force_run_widget)
        self.force_run_btn.setObjectName(u"force_run_btn")

        self.horizontalLayout_8.addWidget(self.force_run_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addWidget(self.force_run_widget)

        self.tabWidget.addTab(self.auto_run_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.save_btn = QPushButton(self.centralwidget)
        self.save_btn.setObjectName(u"save_btn")

        self.horizontalLayout.addWidget(self.save_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        VrcftSettings.setCentralWidget(self.centralwidget)

        self.retranslateUi(VrcftSettings)
        self.auto_connect_cb.toggled.connect(self.ip_le.setDisabled)
        self.auto_connect_cb.toggled.connect(self.port_sp.setDisabled)
        self.vrchat_file_path_reset_btn.clicked.connect(self.vrchat_file_path_le.clear)
        self.vrcft_file_path_reset_btn.clicked.connect(self.vrcft_file_path_le.clear)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(VrcftSettings)
    # setupUi

    def retranslateUi(self, VrcftSettings):
        VrcftSettings.setWindowTitle(QCoreApplication.translate("VrcftSettings", u"VRCFT Settings", None))
        self.auto_connect_cb.setText(QCoreApplication.translate("VrcftSettings", u"Find IP and Port automatically", None))
        self.ip_lb.setText(QCoreApplication.translate("VrcftSettings", u"IP:", None))
        self.ip_le.setText(QCoreApplication.translate("VrcftSettings", u"localhost", None))
        self.port_lb.setText(QCoreApplication.translate("VrcftSettings", u"Port:", None))
        self.read_timeout_lb.setText(QCoreApplication.translate("VrcftSettings", u"VRCFT Read Timeout (milliseconds):", None))
        self.bypass_cb.setText(QCoreApplication.translate("VrcftSettings", u"Allow initialization of other VRCFT modules", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.connection_tab), QCoreApplication.translate("VrcftSettings", u"Connection", None))
        self.run_vrchat_strategy_lb.setText(QCoreApplication.translate("VrcftSettings", u"Auto Run VRChat:", None))
        self.run_vrchat_strategy_cb.setItemText(0, QCoreApplication.translate("VrcftSettings", u"Disabled", None))
        self.run_vrchat_strategy_cb.setItemText(1, QCoreApplication.translate("VrcftSettings", u"Steam Store", None))
        self.run_vrchat_strategy_cb.setItemText(2, QCoreApplication.translate("VrcftSettings", u"File Path", None))

        self.vrchat_file_path_lb.setText(QCoreApplication.translate("VrcftSettings", u"File Path:", None))
        self.vrchat_file_path_le.setPlaceholderText(QCoreApplication.translate("VrcftSettings", u"You can select a file by clicking on '...'", None))
        self.vrchat_file_path_select_btn.setText(QCoreApplication.translate("VrcftSettings", u"...", None))
        self.vrchat_file_path_reset_btn.setText(QCoreApplication.translate("VrcftSettings", u"Reset Path", None))
        self.run_vrcft_strategy_lb.setText(QCoreApplication.translate("VrcftSettings", u"Auto Run VRCFaceTracking:", None))
        self.run_vrcft_strategy_cb.setItemText(0, QCoreApplication.translate("VrcftSettings", u"Disabled", None))
        self.run_vrcft_strategy_cb.setItemText(1, QCoreApplication.translate("VrcftSettings", u"Steam Store", None))
        self.run_vrcft_strategy_cb.setItemText(2, QCoreApplication.translate("VrcftSettings", u"File Path", None))

        self.vrcft_file_path_lb.setText(QCoreApplication.translate("VrcftSettings", u"File Path:", None))
        self.vrcft_file_path_le.setPlaceholderText(QCoreApplication.translate("VrcftSettings", u"You can select a file by clicking on '...'", None))
        self.vrcft_file_path_select_btn.setText(QCoreApplication.translate("VrcftSettings", u"...", None))
        self.vrcft_file_path_reset_btn.setText(QCoreApplication.translate("VrcftSettings", u"Reset Path", None))
        self.force_run_btn.setText(QCoreApplication.translate("VrcftSettings", u"Force Run", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.auto_run_tab), QCoreApplication.translate("VrcftSettings", u"Auto Run", None))
        self.save_btn.setText(QCoreApplication.translate("VrcftSettings", u"Apply and Save", None))
    # retranslateUi

