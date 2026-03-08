# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CameraSettings.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_CameraSettings(object):
    def setupUi(self, CameraSettings):
        if not CameraSettings.objectName():
            CameraSettings.setObjectName(u"CameraSettings")
        CameraSettings.resize(229, 287)
        self.centralwidget = QWidget(CameraSettings)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.camera_id_lbl = QLabel(self.centralwidget)
        self.camera_id_lbl.setObjectName(u"camera_id_lbl")

        self.verticalLayout.addWidget(self.camera_id_lbl)

        self.camera_combo = QComboBox(self.centralwidget)
        self.camera_combo.setObjectName(u"camera_combo")

        self.verticalLayout.addWidget(self.camera_combo)

        self.width_lbl = QLabel(self.centralwidget)
        self.width_lbl.setObjectName(u"width_lbl")

        self.verticalLayout.addWidget(self.width_lbl)

        self.width_sp = QSpinBox(self.centralwidget)
        self.width_sp.setObjectName(u"width_sp")
        self.width_sp.setMinimum(100)
        self.width_sp.setMaximum(100000)
        self.width_sp.setSingleStep(2)
        self.width_sp.setValue(640)

        self.verticalLayout.addWidget(self.width_sp)

        self.height_lbl = QLabel(self.centralwidget)
        self.height_lbl.setObjectName(u"height_lbl")

        self.verticalLayout.addWidget(self.height_lbl)

        self.height_sp = QSpinBox(self.centralwidget)
        self.height_sp.setObjectName(u"height_sp")
        self.height_sp.setMinimum(100)
        self.height_sp.setMaximum(100000)
        self.height_sp.setSingleStep(2)
        self.height_sp.setValue(480)

        self.verticalLayout.addWidget(self.height_sp)

        self.vertical_flip_cb = QCheckBox(self.centralwidget)
        self.vertical_flip_cb.setObjectName(u"vertical_flip_cb")

        self.verticalLayout.addWidget(self.vertical_flip_cb)

        self.horizontal_flip_cb = QCheckBox(self.centralwidget)
        self.horizontal_flip_cb.setObjectName(u"horizontal_flip_cb")

        self.verticalLayout.addWidget(self.horizontal_flip_cb)

        self.rotate_90_cb = QCheckBox(self.centralwidget)
        self.rotate_90_cb.setObjectName(u"rotate_90_cb")

        self.verticalLayout.addWidget(self.rotate_90_cb)

        self.bottom_buttons = QHBoxLayout()
        self.bottom_buttons.setObjectName(u"bottom_buttons")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.bottom_buttons.addItem(self.horizontalSpacer)

        self.apply_and_save_btn = QPushButton(self.centralwidget)
        self.apply_and_save_btn.setObjectName(u"apply_and_save_btn")

        self.bottom_buttons.addWidget(self.apply_and_save_btn)


        self.verticalLayout.addLayout(self.bottom_buttons)

        CameraSettings.setCentralWidget(self.centralwidget)

        self.retranslateUi(CameraSettings)

        QMetaObject.connectSlotsByName(CameraSettings)
    # setupUi

    def retranslateUi(self, CameraSettings):
        CameraSettings.setWindowTitle(QCoreApplication.translate("CameraSettings", u"Camera Settings", None))
        self.camera_id_lbl.setText(QCoreApplication.translate("CameraSettings", u"Camera:", None))
        self.width_lbl.setText(QCoreApplication.translate("CameraSettings", u"Width:", None))
        self.height_lbl.setText(QCoreApplication.translate("CameraSettings", u"Height:", None))
        self.vertical_flip_cb.setText(QCoreApplication.translate("CameraSettings", u"Vertical Flip", None))
        self.horizontal_flip_cb.setText(QCoreApplication.translate("CameraSettings", u"Horizontal Flip", None))
        self.rotate_90_cb.setText(QCoreApplication.translate("CameraSettings", u"Rotate 90 Degree ", None))
        self.apply_and_save_btn.setText(QCoreApplication.translate("CameraSettings", u"Apply and Save", None))
    # retranslateUi

