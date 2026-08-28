# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CalibrationSettingsItem.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QHBoxLayout, QLabel, QProgressBar, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_CalibrationSettingsItem(object):
    def setupUi(self, CalibrationSettingsItem):
        if not CalibrationSettingsItem.objectName():
            CalibrationSettingsItem.setObjectName(u"CalibrationSettingsItem")
        CalibrationSettingsItem.resize(326, 162)
        self.verticalLayout = QVBoxLayout(CalibrationSettingsItem)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_frame = QHBoxLayout()
        self.header_frame.setObjectName(u"header_frame")
        self.name_and_value_lb = QLabel(CalibrationSettingsItem)
        self.name_and_value_lb.setObjectName(u"name_and_value_lb")
        self.name_and_value_lb.setText(u"BlendShapeName: -0.0001")

        self.header_frame.addWidget(self.name_and_value_lb)

        self.source_combobox = QComboBox(CalibrationSettingsItem)
        self.source_combobox.addItem(u"Disabled")
        self.source_combobox.addItem(u"MediaPipe")
        self.source_combobox.addItem(u"Babble")
        self.source_combobox.setObjectName(u"source_combobox")

        self.header_frame.addWidget(self.source_combobox)


        self.verticalLayout.addLayout(self.header_frame)

        self.spin_boxes_frame = QHBoxLayout()
        self.spin_boxes_frame.setObjectName(u"spin_boxes_frame")
        self.negative_sp_frame = QWidget(CalibrationSettingsItem)
        self.negative_sp_frame.setObjectName(u"negative_sp_frame")
        self.verticalLayout_2 = QVBoxLayout(self.negative_sp_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.negative_lb = QLabel(self.negative_sp_frame)
        self.negative_lb.setObjectName(u"negative_lb")

        self.verticalLayout_2.addWidget(self.negative_lb)

        self.negative_sp = QDoubleSpinBox(self.negative_sp_frame)
        self.negative_sp.setObjectName(u"negative_sp")
        self.negative_sp.setDecimals(6)
        self.negative_sp.setMinimum(-1000.000000000000000)
        self.negative_sp.setMaximum(1000.000000000000000)
        self.negative_sp.setSingleStep(0.001000000000000)
        self.negative_sp.setValue(-1.000000000000000)

        self.verticalLayout_2.addWidget(self.negative_sp)


        self.spin_boxes_frame.addWidget(self.negative_sp_frame)

        self.neutral_sp_frame = QWidget(CalibrationSettingsItem)
        self.neutral_sp_frame.setObjectName(u"neutral_sp_frame")
        self.verticalLayout_3 = QVBoxLayout(self.neutral_sp_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.neutral_lb = QLabel(self.neutral_sp_frame)
        self.neutral_lb.setObjectName(u"neutral_lb")

        self.verticalLayout_3.addWidget(self.neutral_lb)

        self.neutral_sp = QDoubleSpinBox(self.neutral_sp_frame)
        self.neutral_sp.setObjectName(u"neutral_sp")
        self.neutral_sp.setDecimals(6)
        self.neutral_sp.setMinimum(-1000.000000000000000)
        self.neutral_sp.setMaximum(1000.000000000000000)
        self.neutral_sp.setSingleStep(0.001000000000000)

        self.verticalLayout_3.addWidget(self.neutral_sp)


        self.spin_boxes_frame.addWidget(self.neutral_sp_frame)

        self.positive_sp_frame = QWidget(CalibrationSettingsItem)
        self.positive_sp_frame.setObjectName(u"positive_sp_frame")
        self.verticalLayout_4 = QVBoxLayout(self.positive_sp_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.positive_lb = QLabel(self.positive_sp_frame)
        self.positive_lb.setObjectName(u"positive_lb")

        self.verticalLayout_4.addWidget(self.positive_lb)

        self.positive_sp = QDoubleSpinBox(self.positive_sp_frame)
        self.positive_sp.setObjectName(u"positive_sp")
        self.positive_sp.setDecimals(6)
        self.positive_sp.setMinimum(-1000.000000000000000)
        self.positive_sp.setMaximum(1000.000000000000000)
        self.positive_sp.setSingleStep(0.001000000000000)
        self.positive_sp.setValue(1.000000000000000)

        self.verticalLayout_4.addWidget(self.positive_sp)


        self.spin_boxes_frame.addWidget(self.positive_sp_frame)


        self.verticalLayout.addLayout(self.spin_boxes_frame)

        self.output_lb = QLabel(CalibrationSettingsItem)
        self.output_lb.setObjectName(u"output_lb")
        self.output_lb.setText(u"Output: 0.000")
        self.output_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.output_lb)

        self.progress_bar_frame = QHBoxLayout()
        self.progress_bar_frame.setSpacing(0)
        self.progress_bar_frame.setObjectName(u"progress_bar_frame")
        self.negative_part_pb = QProgressBar(CalibrationSettingsItem)
        self.negative_part_pb.setObjectName(u"negative_part_pb")
        self.negative_part_pb.setMaximum(128)
        self.negative_part_pb.setValue(0)
        self.negative_part_pb.setTextVisible(False)
        self.negative_part_pb.setInvertedAppearance(True)

        self.progress_bar_frame.addWidget(self.negative_part_pb)

        self.positive_part_pb = QProgressBar(CalibrationSettingsItem)
        self.positive_part_pb.setObjectName(u"positive_part_pb")
        self.positive_part_pb.setMaximum(128)
        self.positive_part_pb.setValue(0)
        self.positive_part_pb.setTextVisible(False)

        self.progress_bar_frame.addWidget(self.positive_part_pb)


        self.verticalLayout.addLayout(self.progress_bar_frame)

        self.line = QFrame(CalibrationSettingsItem)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)


        self.retranslateUi(CalibrationSettingsItem)

        self.source_combobox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(CalibrationSettingsItem)
    # setupUi

    def retranslateUi(self, CalibrationSettingsItem):

        self.negative_lb.setText(QCoreApplication.translate("CalibrationSettingsItem", u"Max Negative:", None))
        self.neutral_lb.setText(QCoreApplication.translate("CalibrationSettingsItem", u"Neutral:", None))
        self.positive_lb.setText(QCoreApplication.translate("CalibrationSettingsItem", u"Max Positive:", None))
        pass
    # retranslateUi

