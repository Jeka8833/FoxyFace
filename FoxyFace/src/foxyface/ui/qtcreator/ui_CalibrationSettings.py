# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CalibrationSettings.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_CalibrationWindow(object):
    def setupUi(self, CalibrationWindow):
        if not CalibrationWindow.objectName():
            CalibrationWindow.setObjectName(u"CalibrationWindow")
        CalibrationWindow.resize(800, 600)
        self.main_frame_layout = QWidget(CalibrationWindow)
        self.main_frame_layout.setObjectName(u"main_frame_layout")
        self.verticalLayout_2 = QVBoxLayout(self.main_frame_layout)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.main_frame_layout)
        self.tabWidget.setObjectName(u"tabWidget")
        self.head_upper = QWidget()
        self.head_upper.setObjectName(u"head_upper")
        self.verticalLayout_3 = QVBoxLayout(self.head_upper)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.head_upper_scroll = QScrollArea(self.head_upper)
        self.head_upper_scroll.setObjectName(u"head_upper_scroll")
        self.head_upper_scroll.setWidgetResizable(True)
        self.head_upper_widget = QWidget()
        self.head_upper_widget.setObjectName(u"head_upper_widget")
        self.head_upper_widget.setGeometry(QRect(0, 0, 758, 500))
        self.verticalLayout_6 = QVBoxLayout(self.head_upper_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.head_upper_container = QVBoxLayout()
        self.head_upper_container.setObjectName(u"head_upper_container")

        self.verticalLayout_6.addLayout(self.head_upper_container)

        self.head_upper_scroll.setWidget(self.head_upper_widget)

        self.verticalLayout_3.addWidget(self.head_upper_scroll)

        self.tabWidget.addTab(self.head_upper, "")
        self.head_bottom = QWidget()
        self.head_bottom.setObjectName(u"head_bottom")
        self.verticalLayout = QVBoxLayout(self.head_bottom)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.head_bottom_scroll = QScrollArea(self.head_bottom)
        self.head_bottom_scroll.setObjectName(u"head_bottom_scroll")
        self.head_bottom_scroll.setWidgetResizable(True)
        self.head_bottom_widget = QWidget()
        self.head_bottom_widget.setObjectName(u"head_bottom_widget")
        self.head_bottom_widget.setGeometry(QRect(0, 0, 758, 500))
        self.verticalLayout_8 = QVBoxLayout(self.head_bottom_widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.head_bottom_container = QVBoxLayout()
        self.head_bottom_container.setObjectName(u"head_bottom_container")

        self.verticalLayout_8.addLayout(self.head_bottom_container)

        self.head_bottom_scroll.setWidget(self.head_bottom_widget)

        self.verticalLayout.addWidget(self.head_bottom_scroll)

        self.tabWidget.addTab(self.head_bottom, "")
        self.head_global = QWidget()
        self.head_global.setObjectName(u"head_global")
        self.horizontalLayout_4 = QHBoxLayout(self.head_global)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.head_global_scroll = QScrollArea(self.head_global)
        self.head_global_scroll.setObjectName(u"head_global_scroll")
        self.head_global_scroll.setWidgetResizable(True)
        self.head_global_widget = QWidget()
        self.head_global_widget.setObjectName(u"head_global_widget")
        self.head_global_widget.setGeometry(QRect(0, 0, 758, 500))
        self.verticalLayout_4 = QVBoxLayout(self.head_global_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.head_global_container = QVBoxLayout()
        self.head_global_container.setObjectName(u"head_global_container")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.head_center_lb = QLabel(self.head_global_widget)
        self.head_center_lb.setObjectName(u"head_center_lb")

        self.horizontalLayout.addWidget(self.head_center_lb)

        self.reset_head_center_btn = QPushButton(self.head_global_widget)
        self.reset_head_center_btn.setObjectName(u"reset_head_center_btn")

        self.horizontalLayout.addWidget(self.reset_head_center_btn)


        self.head_global_container.addLayout(self.horizontalLayout)

        self.line = QFrame(self.head_global_widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.head_global_container.addWidget(self.line)


        self.verticalLayout_4.addLayout(self.head_global_container)

        self.head_global_scroll.setWidget(self.head_global_widget)

        self.horizontalLayout_4.addWidget(self.head_global_scroll)

        self.tabWidget.addTab(self.head_global, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.footer_layout = QHBoxLayout()
        self.footer_layout.setObjectName(u"footer_layout")
        self.full_reset_btn = QPushButton(self.main_frame_layout)
        self.full_reset_btn.setObjectName(u"full_reset_btn")

        self.footer_layout.addWidget(self.full_reset_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.footer_layout.addItem(self.horizontalSpacer_2)

        self.save_btn = QPushButton(self.main_frame_layout)
        self.save_btn.setObjectName(u"save_btn")

        self.footer_layout.addWidget(self.save_btn)


        self.verticalLayout_2.addLayout(self.footer_layout)

        CalibrationWindow.setCentralWidget(self.main_frame_layout)

        self.retranslateUi(CalibrationWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(CalibrationWindow)
    # setupUi

    def retranslateUi(self, CalibrationWindow):
        CalibrationWindow.setWindowTitle(QCoreApplication.translate("CalibrationWindow", u"Manual Calibration", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.head_upper), QCoreApplication.translate("CalibrationWindow", u"Head Upper", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.head_bottom), QCoreApplication.translate("CalibrationWindow", u"Head Bottom", None))
        self.head_center_lb.setText(QCoreApplication.translate("CalibrationWindow", u"Center Head Rotation:", None))
        self.reset_head_center_btn.setText(QCoreApplication.translate("CalibrationWindow", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.head_global), QCoreApplication.translate("CalibrationWindow", u"Head Global", None))
        self.full_reset_btn.setText(QCoreApplication.translate("CalibrationWindow", u"Full Reset", None))
        self.save_btn.setText(QCoreApplication.translate("CalibrationWindow", u"Apply and Save", None))
    # retranslateUi

