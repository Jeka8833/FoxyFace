# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ManualCalibrationAvatar.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_ManualCalibrationAvatar(object):
    def setupUi(self, ManualCalibrationAvatar):
        if not ManualCalibrationAvatar.objectName():
            ManualCalibrationAvatar.setObjectName(u"ManualCalibrationAvatar")
        ManualCalibrationAvatar.resize(800, 600)
        self.centralwidget = QWidget(ManualCalibrationAvatar)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget_2 = QTabWidget(self.tab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout = QVBoxLayout(self.tab_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")

        self.verticalLayout_3.addWidget(self.tabWidget_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.widget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.checkBox = QCheckBox(self.widget_2)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout.addWidget(self.checkBox)

        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.widget_2)

        ManualCalibrationAvatar.setCentralWidget(self.centralwidget)

        self.retranslateUi(ManualCalibrationAvatar)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ManualCalibrationAvatar)
    # setupUi

    def retranslateUi(self, ManualCalibrationAvatar):
        ManualCalibrationAvatar.setWindowTitle(QCoreApplication.translate("ManualCalibrationAvatar", u"MainWindow", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("ManualCalibrationAvatar", u"Avatar Parameters", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("ManualCalibrationAvatar", u"Solver Input", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("ManualCalibrationAvatar", u"VRChat/ChilloutVR", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("ManualCalibrationAvatar", u"Tab 2", None))
        self.pushButton_4.setText(QCoreApplication.translate("ManualCalibrationAvatar", u"Avatar Parameter Reset", None))
        self.checkBox.setText(QCoreApplication.translate("ManualCalibrationAvatar", u"Allways use on this avatar", None))
        self.pushButton_2.setText(QCoreApplication.translate("ManualCalibrationAvatar", u"Import File", None))
        self.pushButton.setText(QCoreApplication.translate("ManualCalibrationAvatar", u"Export File", None))
    # retranslateUi

