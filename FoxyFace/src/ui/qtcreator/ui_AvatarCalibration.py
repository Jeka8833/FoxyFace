# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AvatarCalibration.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_AvatarCalibration(object):
    def setupUi(self, AvatarCalibration):
        if not AvatarCalibration.objectName():
            AvatarCalibration.setObjectName(u"AvatarCalibration")
        AvatarCalibration.resize(800, 600)
        self.centralwidget = QWidget(AvatarCalibration)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout = QHBoxLayout(self.page)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.connection_list_widget = QTabWidget(self.page)
        self.connection_list_widget.setObjectName(u"connection_list_widget")

        self.horizontalLayout.addWidget(self.connection_list_widget)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout = QVBoxLayout(self.page_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.no_connection_lb = QLabel(self.page_2)
        self.no_connection_lb.setObjectName(u"no_connection_lb")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.no_connection_lb.setFont(font)
        self.no_connection_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.no_connection_lb)

        self.no_connection_description_lb = QLabel(self.page_2)
        self.no_connection_description_lb.setObjectName(u"no_connection_description_lb")
        font1 = QFont()
        font1.setPointSize(12)
        self.no_connection_description_lb.setFont(font1)

        self.verticalLayout.addWidget(self.no_connection_description_lb)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget = QWidget(self.page_2)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.open_connection_settings_btn = QPushButton(self.widget)
        self.open_connection_settings_btn.setObjectName(u"open_connection_settings_btn")
        font2 = QFont()
        font2.setPointSize(11)
        self.open_connection_settings_btn.setFont(font2)

        self.horizontalLayout_2.addWidget(self.open_connection_settings_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.widget)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        AvatarCalibration.setCentralWidget(self.centralwidget)

        self.retranslateUi(AvatarCalibration)

        self.stackedWidget.setCurrentIndex(1)
        self.connection_list_widget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(AvatarCalibration)
    # setupUi

    def retranslateUi(self, AvatarCalibration):
        AvatarCalibration.setWindowTitle(QCoreApplication.translate("AvatarCalibration", u"MainWindow", None))
        self.no_connection_lb.setText(QCoreApplication.translate("AvatarCalibration", u"No connected avatars", None))
        self.no_connection_description_lb.setText("")
        self.open_connection_settings_btn.setText(QCoreApplication.translate("AvatarCalibration", u"Open Connection Settings", None))
    # retranslateUi

