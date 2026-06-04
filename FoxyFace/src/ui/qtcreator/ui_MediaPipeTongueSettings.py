# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MediaPipeTongueSettings.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_MediaPipeTongueSettings(object):
    def setupUi(self, MediaPipeTongueSettings):
        if not MediaPipeTongueSettings.objectName():
            MediaPipeTongueSettings.setObjectName(u"MediaPipeTongueSettings")
        MediaPipeTongueSettings.resize(508, 480)
        self.centralwidget = QWidget(MediaPipeTongueSettings)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.general_settings_zone_lb = QLabel(self.centralwidget)
        self.general_settings_zone_lb.setObjectName(u"general_settings_zone_lb")
        font = QFont()
        font.setPointSize(11)
        self.general_settings_zone_lb.setFont(font)
        self.general_settings_zone_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.general_settings_zone_lb)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.use_nn_cb = QCheckBox(self.centralwidget)
        self.use_nn_cb.setObjectName(u"use_nn_cb")
        self.use_nn_cb.setChecked(True)

        self.verticalLayout.addWidget(self.use_nn_cb)

        self.verticalSpacer = QSpacerItem(0, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.image_padding_zone_lb = QLabel(self.centralwidget)
        self.image_padding_zone_lb.setObjectName(u"image_padding_zone_lb")
        self.image_padding_zone_lb.setFont(font)
        self.image_padding_zone_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.image_padding_zone_lb)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.left_right_pad_lb = QLabel(self.centralwidget)
        self.left_right_pad_lb.setObjectName(u"left_right_pad_lb")

        self.verticalLayout.addWidget(self.left_right_pad_lb)

        self.left_right_pad_sb = QSpinBox(self.centralwidget)
        self.left_right_pad_sb.setObjectName(u"left_right_pad_sb")
        self.left_right_pad_sb.setMaximum(127)
        self.left_right_pad_sb.setValue(64)

        self.verticalLayout.addWidget(self.left_right_pad_sb)

        self.top_pad_lb = QLabel(self.centralwidget)
        self.top_pad_lb.setObjectName(u"top_pad_lb")

        self.verticalLayout.addWidget(self.top_pad_lb)

        self.top_pad_sb = QSpinBox(self.centralwidget)
        self.top_pad_sb.setObjectName(u"top_pad_sb")
        self.top_pad_sb.setMaximum(127)
        self.top_pad_sb.setValue(64)

        self.verticalLayout.addWidget(self.top_pad_sb)

        self.bottom_pad_lb = QLabel(self.centralwidget)
        self.bottom_pad_lb.setObjectName(u"bottom_pad_lb")

        self.verticalLayout.addWidget(self.bottom_pad_lb)

        self.bottom_pad_sb = QSpinBox(self.centralwidget)
        self.bottom_pad_sb.setObjectName(u"bottom_pad_sb")
        self.bottom_pad_sb.setMaximum(127)
        self.bottom_pad_sb.setValue(64)

        self.verticalLayout.addWidget(self.bottom_pad_sb)

        self.verticalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.nn_setting_zone_lb = QLabel(self.centralwidget)
        self.nn_setting_zone_lb.setObjectName(u"nn_setting_zone_lb")
        self.nn_setting_zone_lb.setFont(font)
        self.nn_setting_zone_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.nn_setting_zone_lb)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_5)

        self.cpu_spin = QCheckBox(self.centralwidget)
        self.cpu_spin.setObjectName(u"cpu_spin")

        self.verticalLayout_2.addWidget(self.cpu_spin)

        self.provider_lb = QLabel(self.centralwidget)
        self.provider_lb.setObjectName(u"provider_lb")

        self.verticalLayout_2.addWidget(self.provider_lb)

        self.provider_cb = QComboBox(self.centralwidget)
        self.provider_cb.setObjectName(u"provider_cb")

        self.verticalLayout_2.addWidget(self.provider_cb)

        self.gpu_id_lb = QLabel(self.centralwidget)
        self.gpu_id_lb.setObjectName(u"gpu_id_lb")

        self.verticalLayout_2.addWidget(self.gpu_id_lb)

        self.gpu_id_sb = QSpinBox(self.centralwidget)
        self.gpu_id_sb.setObjectName(u"gpu_id_sb")

        self.verticalLayout_2.addWidget(self.gpu_id_sb)

        self.cpu_threads_lb = QLabel(self.centralwidget)
        self.cpu_threads_lb.setObjectName(u"cpu_threads_lb")

        self.verticalLayout_2.addWidget(self.cpu_threads_lb)

        self.cpu_threads_sb = QSpinBox(self.centralwidget)
        self.cpu_threads_sb.setObjectName(u"cpu_threads_sb")
        self.cpu_threads_sb.setMinimum(1)

        self.verticalLayout_2.addWidget(self.cpu_threads_sb)

        self.error_message_lb = QLabel(self.centralwidget)
        self.error_message_lb.setObjectName(u"error_message_lb")
        self.error_message_lb.setStyleSheet(u"color: rgb(255, 0, 4);")

        self.verticalLayout_2.addWidget(self.error_message_lb)

        self.verticalSpacer_4 = QSpacerItem(0, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.filter_settings_zone_lb = QLabel(self.centralwidget)
        self.filter_settings_zone_lb.setObjectName(u"filter_settings_zone_lb")
        self.filter_settings_zone_lb.setFont(font)
        self.filter_settings_zone_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.filter_settings_zone_lb)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_4)

        self.mincutoff_lb = QLabel(self.centralwidget)
        self.mincutoff_lb.setObjectName(u"mincutoff_lb")

        self.verticalLayout_2.addWidget(self.mincutoff_lb)

        self.mincutoff_dsb = QDoubleSpinBox(self.centralwidget)
        self.mincutoff_dsb.setObjectName(u"mincutoff_dsb")
        self.mincutoff_dsb.setDecimals(6)
        self.mincutoff_dsb.setMinimum(0.000001000000000)
        self.mincutoff_dsb.setSingleStep(0.001000000000000)
        self.mincutoff_dsb.setValue(1.000000000000000)

        self.verticalLayout_2.addWidget(self.mincutoff_dsb)

        self.beta_lb = QLabel(self.centralwidget)
        self.beta_lb.setObjectName(u"beta_lb")

        self.verticalLayout_2.addWidget(self.beta_lb)

        self.beta_dsb = QDoubleSpinBox(self.centralwidget)
        self.beta_dsb.setObjectName(u"beta_dsb")
        self.beta_dsb.setDecimals(6)
        self.beta_dsb.setMinimum(0.000001000000000)
        self.beta_dsb.setSingleStep(0.001000000000000)
        self.beta_dsb.setValue(0.000100000000000)

        self.verticalLayout_2.addWidget(self.beta_dsb)

        self.verticalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.full_reset_btn = QPushButton(self.centralwidget)
        self.full_reset_btn.setObjectName(u"full_reset_btn")

        self.horizontalLayout_2.addWidget(self.full_reset_btn)

        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.apply_and_save_btn = QPushButton(self.centralwidget)
        self.apply_and_save_btn.setObjectName(u"apply_and_save_btn")

        self.horizontalLayout_2.addWidget(self.apply_and_save_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        MediaPipeTongueSettings.setCentralWidget(self.centralwidget)

        self.retranslateUi(MediaPipeTongueSettings)

        QMetaObject.connectSlotsByName(MediaPipeTongueSettings)
    # setupUi

    def retranslateUi(self, MediaPipeTongueSettings):
        MediaPipeTongueSettings.setWindowTitle(QCoreApplication.translate("MediaPipeTongueSettings", u"MediaPipe Tongue Settings", None))
        self.general_settings_zone_lb.setText(QCoreApplication.translate("MediaPipeTongueSettings", u"General Settings", None))
        self.use_nn_cb.setText(QCoreApplication.translate("MediaPipeTongueSettings", u"Use MediaPipe Tongue neural network", None))
        self.image_padding_zone_lb.setText(QCoreApplication.translate("MediaPipeTongueSettings", u"Image Padding", None))
        self.left_right_pad_lb.setText(QCoreApplication.translate("MediaPipeTongueSettings", u"Left/Riget padding:", None))
        self.top_pad_lb.setText(QCoreApplication.translate("MediaPipeTongueSettings", u"Top padding:", None))
        self.bottom_pad_lb.setText(QCoreApplication.translate("MediaPipeTongueSettings", u"Bottom padding:", None))
        self.nn_setting_zone_lb.setText(QCoreApplication.translate("MediaPipeTongueSettings", u"Neural Network Settings", None))
        self.cpu_spin.setText(QCoreApplication.translate("MediaPipeTongueSettings", u"CPU Wait Spin", None))
        self.provider_lb.setText(QCoreApplication.translate("MediaPipeTongueSettings", u"Provider:", None))
        self.gpu_id_lb.setText(QCoreApplication.translate("MediaPipeTongueSettings", u"GPU Device ID:", None))
        self.cpu_threads_lb.setText(QCoreApplication.translate("MediaPipeTongueSettings", u"CPU Threads:", None))
        self.error_message_lb.setText(QCoreApplication.translate("MediaPipeTongueSettings", u"Error: ", None))
        self.filter_settings_zone_lb.setText(QCoreApplication.translate("MediaPipeTongueSettings", u"Filter Settings", None))
        self.mincutoff_lb.setText(QCoreApplication.translate("MediaPipeTongueSettings", u"Mincutoff:", None))
        self.beta_lb.setText(QCoreApplication.translate("MediaPipeTongueSettings", u"Beta:", None))
        self.full_reset_btn.setText(QCoreApplication.translate("MediaPipeTongueSettings", u"Full Reset", None))
        self.apply_and_save_btn.setText(QCoreApplication.translate("MediaPipeTongueSettings", u"Apply and Save", None))
    # retranslateUi

