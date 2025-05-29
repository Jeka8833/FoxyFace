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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_VrcftSettings(object):
    def setupUi(self, VrcftSettings):
        if not VrcftSettings.objectName():
            VrcftSettings.setObjectName(u"VrcftSettings")
        VrcftSettings.resize(290, 264)
        self.centralwidget = QWidget(VrcftSettings)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.auto_connect_cb = QCheckBox(self.centralwidget)
        self.auto_connect_cb.setObjectName(u"auto_connect_cb")
        self.auto_connect_cb.setChecked(True)

        self.verticalLayout.addWidget(self.auto_connect_cb)

        self.ip_lb = QLabel(self.centralwidget)
        self.ip_lb.setObjectName(u"ip_lb")

        self.verticalLayout.addWidget(self.ip_lb)

        self.ip_le = QLineEdit(self.centralwidget)
        self.ip_le.setObjectName(u"ip_le")
        self.ip_le.setEnabled(False)
        self.ip_le.setMaxLength(256)

        self.verticalLayout.addWidget(self.ip_le)

        self.port_lb = QLabel(self.centralwidget)
        self.port_lb.setObjectName(u"port_lb")

        self.verticalLayout.addWidget(self.port_lb)

        self.port_sp = QSpinBox(self.centralwidget)
        self.port_sp.setObjectName(u"port_sp")
        self.port_sp.setEnabled(False)
        self.port_sp.setMaximum(65535)
        self.port_sp.setValue(54321)

        self.verticalLayout.addWidget(self.port_sp)

        self.read_timeout_lb = QLabel(self.centralwidget)
        self.read_timeout_lb.setObjectName(u"read_timeout_lb")

        self.verticalLayout.addWidget(self.read_timeout_lb)

        self.read_timeout_sp = QSpinBox(self.centralwidget)
        self.read_timeout_sp.setObjectName(u"read_timeout_sp")
        self.read_timeout_sp.setMinimum(10)
        self.read_timeout_sp.setMaximum(60000)
        self.read_timeout_sp.setSingleStep(100)
        self.read_timeout_sp.setValue(2500)

        self.verticalLayout.addWidget(self.read_timeout_sp)

        self.bypass_cb = QCheckBox(self.centralwidget)
        self.bypass_cb.setObjectName(u"bypass_cb")

        self.verticalLayout.addWidget(self.bypass_cb)

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
        self.save_btn.setText(QCoreApplication.translate("VrcftSettings", u"Apply and Save", None))
    # retranslateUi

