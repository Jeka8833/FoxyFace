# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BabbleSettings.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QToolButton, QVBoxLayout, QWidget)

class Ui_BabbleSettings(object):
    def setupUi(self, BabbleSettings):
        if not BabbleSettings.objectName():
            BabbleSettings.setObjectName(u"BabbleSettings")
        BabbleSettings.resize(434, 403)
        self.centralwidget = QWidget(BabbleSettings)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.general_settings_lb = QLabel(self.centralwidget)
        self.general_settings_lb.setObjectName(u"general_settings_lb")
        font = QFont()
        font.setPointSize(11)
        self.general_settings_lb.setFont(font)
        self.general_settings_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.general_settings_lb)

        self.general_settings_line = QFrame(self.centralwidget)
        self.general_settings_line.setObjectName(u"general_settings_line")
        self.general_settings_line.setFrameShape(QFrame.Shape.HLine)
        self.general_settings_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.general_settings_line)

        self.use_babble_cb = QCheckBox(self.centralwidget)
        self.use_babble_cb.setObjectName(u"use_babble_cb")
        self.use_babble_cb.setChecked(True)

        self.verticalLayout_2.addWidget(self.use_babble_cb)

        self.max_head_rotation_y_lb = QLabel(self.centralwidget)
        self.max_head_rotation_y_lb.setObjectName(u"max_head_rotation_y_lb")

        self.verticalLayout_2.addWidget(self.max_head_rotation_y_lb)

        self.max_head_rotation_y_sp = QSpinBox(self.centralwidget)
        self.max_head_rotation_y_sp.setObjectName(u"max_head_rotation_y_sp")
        self.max_head_rotation_y_sp.setMinimum(1)
        self.max_head_rotation_y_sp.setMaximum(90)
        self.max_head_rotation_y_sp.setValue(30)

        self.verticalLayout_2.addWidget(self.max_head_rotation_y_sp)

        self.max_head_rotation_x_lb = QLabel(self.centralwidget)
        self.max_head_rotation_x_lb.setObjectName(u"max_head_rotation_x_lb")

        self.verticalLayout_2.addWidget(self.max_head_rotation_x_lb)

        self.max_head_rotation_x_sp = QSpinBox(self.centralwidget)
        self.max_head_rotation_x_sp.setObjectName(u"max_head_rotation_x_sp")
        self.max_head_rotation_x_sp.setMinimum(1)
        self.max_head_rotation_x_sp.setMaximum(90)
        self.max_head_rotation_x_sp.setValue(30)

        self.verticalLayout_2.addWidget(self.max_head_rotation_x_sp)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.filter_setting_lb = QLabel(self.centralwidget)
        self.filter_setting_lb.setObjectName(u"filter_setting_lb")
        self.filter_setting_lb.setFont(font)
        self.filter_setting_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.filter_setting_lb)

        self.filter_setting_line = QFrame(self.centralwidget)
        self.filter_setting_line.setObjectName(u"filter_setting_line")
        self.filter_setting_line.setFrameShape(QFrame.Shape.HLine)
        self.filter_setting_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.filter_setting_line)

        self.mincutoff_lb = QLabel(self.centralwidget)
        self.mincutoff_lb.setObjectName(u"mincutoff_lb")

        self.verticalLayout_2.addWidget(self.mincutoff_lb)

        self.mincutoff_sp = QDoubleSpinBox(self.centralwidget)
        self.mincutoff_sp.setObjectName(u"mincutoff_sp")
        self.mincutoff_sp.setDecimals(6)
        self.mincutoff_sp.setMinimum(0.000001000000000)
        self.mincutoff_sp.setSingleStep(0.010000000000000)
        self.mincutoff_sp.setValue(3.000000000000000)

        self.verticalLayout_2.addWidget(self.mincutoff_sp)

        self.beta_lb = QLabel(self.centralwidget)
        self.beta_lb.setObjectName(u"beta_lb")

        self.verticalLayout_2.addWidget(self.beta_lb)

        self.beta_sp = QDoubleSpinBox(self.centralwidget)
        self.beta_sp.setObjectName(u"beta_sp")
        self.beta_sp.setDecimals(6)
        self.beta_sp.setMinimum(0.000001000000000)
        self.beta_sp.setSingleStep(0.010000000000000)
        self.beta_sp.setValue(0.900000000000000)

        self.verticalLayout_2.addWidget(self.beta_sp)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.nn_settings_lb = QLabel(self.centralwidget)
        self.nn_settings_lb.setObjectName(u"nn_settings_lb")
        self.nn_settings_lb.setFont(font)
        self.nn_settings_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.nn_settings_lb)

        self.nn_settings_line = QFrame(self.centralwidget)
        self.nn_settings_line.setObjectName(u"nn_settings_line")
        self.nn_settings_line.setFrameShape(QFrame.Shape.HLine)
        self.nn_settings_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.nn_settings_line)

        self.custom_model_lb = QLabel(self.centralwidget)
        self.custom_model_lb.setObjectName(u"custom_model_lb")

        self.verticalLayout_4.addWidget(self.custom_model_lb)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.selected_path_le = QLineEdit(self.centralwidget)
        self.selected_path_le.setObjectName(u"selected_path_le")

        self.horizontalLayout_3.addWidget(self.selected_path_le)

        self.select_path_btn = QToolButton(self.centralwidget)
        self.select_path_btn.setObjectName(u"select_path_btn")

        self.horizontalLayout_3.addWidget(self.select_path_btn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.model_status_lb = QLabel(self.centralwidget)
        self.model_status_lb.setObjectName(u"model_status_lb")
        self.model_status_lb.setStyleSheet(u"color: rgb(255, 0, 4);")
        self.model_status_lb.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.model_status_lb)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.reset_model_path_btn = QPushButton(self.centralwidget)
        self.reset_model_path_btn.setObjectName(u"reset_model_path_btn")

        self.horizontalLayout_4.addWidget(self.reset_model_path_btn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.thread_count_lb = QLabel(self.centralwidget)
        self.thread_count_lb.setObjectName(u"thread_count_lb")

        self.verticalLayout_4.addWidget(self.thread_count_lb)

        self.thread_count_sp = QSpinBox(self.centralwidget)
        self.thread_count_sp.setObjectName(u"thread_count_sp")
        self.thread_count_sp.setValue(1)

        self.verticalLayout_4.addWidget(self.thread_count_sp)

        self.allow_spinning_cb = QCheckBox(self.centralwidget)
        self.allow_spinning_cb.setObjectName(u"allow_spinning_cb")

        self.verticalLayout_4.addWidget(self.allow_spinning_cb)

        self.try_use_gpu_cb = QCheckBox(self.centralwidget)
        self.try_use_gpu_cb.setObjectName(u"try_use_gpu_cb")
        self.try_use_gpu_cb.setChecked(True)
        self.try_use_gpu_cb.setTristate(False)

        self.verticalLayout_4.addWidget(self.try_use_gpu_cb)

        self.gpu_device_id_lb = QLabel(self.centralwidget)
        self.gpu_device_id_lb.setObjectName(u"gpu_device_id_lb")

        self.verticalLayout_4.addWidget(self.gpu_device_id_lb)

        self.gpu_device_id_sb = QSpinBox(self.centralwidget)
        self.gpu_device_id_sb.setObjectName(u"gpu_device_id_sb")

        self.verticalLayout_4.addWidget(self.gpu_device_id_sb)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.full_reset_btn = QPushButton(self.centralwidget)
        self.full_reset_btn.setObjectName(u"full_reset_btn")

        self.horizontalLayout.addWidget(self.full_reset_btn)

        self.provider_status_lb = QLabel(self.centralwidget)
        self.provider_status_lb.setObjectName(u"provider_status_lb")
#if QT_CONFIG(tooltip)
        self.provider_status_lb.setToolTip(u"")
#endif // QT_CONFIG(tooltip)

        self.horizontalLayout.addWidget(self.provider_status_lb)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.save_btn = QPushButton(self.centralwidget)
        self.save_btn.setObjectName(u"save_btn")

        self.horizontalLayout.addWidget(self.save_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        BabbleSettings.setCentralWidget(self.centralwidget)

        self.retranslateUi(BabbleSettings)
        self.reset_model_path_btn.clicked.connect(self.selected_path_le.clear)
        self.try_use_gpu_cb.toggled.connect(self.gpu_device_id_sb.setEnabled)
        self.use_babble_cb.toggled.connect(self.provider_status_lb.setVisible)

        QMetaObject.connectSlotsByName(BabbleSettings)
    # setupUi

    def retranslateUi(self, BabbleSettings):
        BabbleSettings.setWindowTitle(QCoreApplication.translate("BabbleSettings", u"Babble Settings", None))
        self.general_settings_lb.setText(QCoreApplication.translate("BabbleSettings", u"General Settings", None))
        self.use_babble_cb.setText(QCoreApplication.translate("BabbleSettings", u"Use Babble neural network", None))
        self.max_head_rotation_y_lb.setText(QCoreApplication.translate("BabbleSettings", u"Max head up-down rotation degree:", None))
        self.max_head_rotation_x_lb.setText(QCoreApplication.translate("BabbleSettings", u"Max head left-right rotation degree:", None))
        self.filter_setting_lb.setText(QCoreApplication.translate("BabbleSettings", u"Filter Settings", None))
        self.mincutoff_lb.setText(QCoreApplication.translate("BabbleSettings", u"Mincutoff:", None))
        self.beta_lb.setText(QCoreApplication.translate("BabbleSettings", u"Beta:", None))
        self.nn_settings_lb.setText(QCoreApplication.translate("BabbleSettings", u"Neural Network Settings", None))
        self.custom_model_lb.setText(QCoreApplication.translate("BabbleSettings", u"Custom Babble Model Path:", None))
        self.selected_path_le.setPlaceholderText(QCoreApplication.translate("BabbleSettings", u"Default Model", None))
        self.select_path_btn.setText(QCoreApplication.translate("BabbleSettings", u"...", None))
        self.model_status_lb.setText(QCoreApplication.translate("BabbleSettings", u"Update the model for better face tracking!", None))
        self.reset_model_path_btn.setText(QCoreApplication.translate("BabbleSettings", u"Reset Model Path", None))
        self.thread_count_lb.setText(QCoreApplication.translate("BabbleSettings", u"Thread Count:", None))
        self.allow_spinning_cb.setText(QCoreApplication.translate("BabbleSettings", u"Allow Spinning", None))
        self.try_use_gpu_cb.setText(QCoreApplication.translate("BabbleSettings", u"Try to use GPU acceleration", None))
        self.gpu_device_id_lb.setText(QCoreApplication.translate("BabbleSettings", u"GPU Device ID:", None))
        self.full_reset_btn.setText(QCoreApplication.translate("BabbleSettings", u"Full Reset", None))
        self.provider_status_lb.setText(QCoreApplication.translate("BabbleSettings", u"Provider: Unknown", None))
        self.save_btn.setText(QCoreApplication.translate("BabbleSettings", u"Apply and Save", None))
    # retranslateUi

