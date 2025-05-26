# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MediaPipeSettings.ui'
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
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_MediaPipeSettings(object):
    def setupUi(self, MediaPipeSettings):
        if not MediaPipeSettings.objectName():
            MediaPipeSettings.setObjectName(u"MediaPipeSettings")
        MediaPipeSettings.resize(189, 417)
        self.centralwidget = QWidget(MediaPipeSettings)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.enable_fps_limit_cb = QCheckBox(self.centralwidget)
        self.enable_fps_limit_cb.setObjectName(u"enable_fps_limit_cb")

        self.verticalLayout.addWidget(self.enable_fps_limit_cb)

        self.max_fps_lb = QLabel(self.centralwidget)
        self.max_fps_lb.setObjectName(u"max_fps_lb")

        self.verticalLayout.addWidget(self.max_fps_lb)

        self.max_fps_sp = QSpinBox(self.centralwidget)
        self.max_fps_sp.setObjectName(u"max_fps_sp")
        self.max_fps_sp.setEnabled(False)
        self.max_fps_sp.setMinimum(1)
        self.max_fps_sp.setMaximum(1000)

        self.verticalLayout.addWidget(self.max_fps_sp)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.warning_lbl = QLabel(self.centralwidget)
        self.warning_lbl.setObjectName(u"warning_lbl")
        font = QFont()
        font.setPointSize(11)
        self.warning_lbl.setFont(font)
        self.warning_lbl.setWordWrap(True)

        self.verticalLayout.addWidget(self.warning_lbl)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.try_gpu_cb = QCheckBox(self.centralwidget)
        self.try_gpu_cb.setObjectName(u"try_gpu_cb")
        self.try_gpu_cb.setEnabled(True)
        self.try_gpu_cb.setChecked(True)

        self.verticalLayout.addWidget(self.try_gpu_cb)

        self.mfdc_lbl = QLabel(self.centralwidget)
        self.mfdc_lbl.setObjectName(u"mfdc_lbl")

        self.verticalLayout.addWidget(self.mfdc_lbl)

        self.mfdc_sp = QDoubleSpinBox(self.centralwidget)
        self.mfdc_sp.setObjectName(u"mfdc_sp")
        self.mfdc_sp.setMaximum(1.000000000000000)
        self.mfdc_sp.setSingleStep(0.100000000000000)
        self.mfdc_sp.setValue(0.500000000000000)

        self.verticalLayout.addWidget(self.mfdc_sp)

        self.mfpc_lbl = QLabel(self.centralwidget)
        self.mfpc_lbl.setObjectName(u"mfpc_lbl")

        self.verticalLayout.addWidget(self.mfpc_lbl)

        self.mfpc_sp = QDoubleSpinBox(self.centralwidget)
        self.mfpc_sp.setObjectName(u"mfpc_sp")
        self.mfpc_sp.setMaximum(1.000000000000000)
        self.mfpc_sp.setSingleStep(0.100000000000000)
        self.mfpc_sp.setValue(0.500000000000000)

        self.verticalLayout.addWidget(self.mfpc_sp)

        self.mtc_lbl = QLabel(self.centralwidget)
        self.mtc_lbl.setObjectName(u"mtc_lbl")

        self.verticalLayout.addWidget(self.mtc_lbl)

        self.mtc_sp = QDoubleSpinBox(self.centralwidget)
        self.mtc_sp.setObjectName(u"mtc_sp")
        self.mtc_sp.setMaximum(1.000000000000000)
        self.mtc_sp.setSingleStep(0.100000000000000)
        self.mtc_sp.setValue(0.500000000000000)

        self.verticalLayout.addWidget(self.mtc_sp)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.save_btn = QPushButton(self.centralwidget)
        self.save_btn.setObjectName(u"save_btn")

        self.horizontalLayout_2.addWidget(self.save_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MediaPipeSettings.setCentralWidget(self.centralwidget)

        self.retranslateUi(MediaPipeSettings)
        self.enable_fps_limit_cb.toggled.connect(self.max_fps_sp.setEnabled)

        QMetaObject.connectSlotsByName(MediaPipeSettings)
    # setupUi

    def retranslateUi(self, MediaPipeSettings):
        MediaPipeSettings.setWindowTitle(QCoreApplication.translate("MediaPipeSettings", u"MediaPipe Settings", None))
        self.enable_fps_limit_cb.setText(QCoreApplication.translate("MediaPipeSettings", u"Enable FPS Limit", None))
        self.max_fps_lb.setText(QCoreApplication.translate("MediaPipeSettings", u"Max FPS Limit:", None))
        self.warning_lbl.setText(QCoreApplication.translate("MediaPipeSettings", u"All settings below will be applied only after restarting FoxyFace application!", None))
#if QT_CONFIG(tooltip)
        self.try_gpu_cb.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.try_gpu_cb.setText(QCoreApplication.translate("MediaPipeSettings", u"Try using GPU acceleration", None))
#if QT_CONFIG(tooltip)
        self.mfdc_lbl.setToolTip(QCoreApplication.translate("MediaPipeSettings", u"The minimum confidence score for the face detection to be considered successful.", None))
#endif // QT_CONFIG(tooltip)
        self.mfdc_lbl.setText(QCoreApplication.translate("MediaPipeSettings", u"Min face detection confidence:", None))
#if QT_CONFIG(tooltip)
        self.mfdc_sp.setToolTip(QCoreApplication.translate("MediaPipeSettings", u"The minimum confidence score for the face detection to be considered successful.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.mfpc_lbl.setToolTip(QCoreApplication.translate("MediaPipeSettings", u"The minimum confidence score of face presence score in the face landmark detection.", None))
#endif // QT_CONFIG(tooltip)
        self.mfpc_lbl.setText(QCoreApplication.translate("MediaPipeSettings", u"Min face presence confidence:", None))
#if QT_CONFIG(tooltip)
        self.mfpc_sp.setToolTip(QCoreApplication.translate("MediaPipeSettings", u"The minimum confidence score of face presence score in the face landmark detection.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.mtc_lbl.setToolTip(QCoreApplication.translate("MediaPipeSettings", u"The minimum confidence score for the face tracking to be considered successful.", None))
#endif // QT_CONFIG(tooltip)
        self.mtc_lbl.setText(QCoreApplication.translate("MediaPipeSettings", u"Min tracking confidence:", None))
#if QT_CONFIG(tooltip)
        self.mtc_sp.setToolTip(QCoreApplication.translate("MediaPipeSettings", u"The minimum confidence score for the face tracking to be considered successful.", None))
#endif // QT_CONFIG(tooltip)
        self.save_btn.setText(QCoreApplication.translate("MediaPipeSettings", u"Save", None))
    # retranslateUi

