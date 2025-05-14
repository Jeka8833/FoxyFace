# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HasUpdateWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_HasUpdateWindow(object):
    def setupUi(self, HasUpdateWindow):
        if not HasUpdateWindow.objectName():
            HasUpdateWindow.setObjectName(u"HasUpdateWindow")
        HasUpdateWindow.resize(368, 156)
        self.centralwidget = QWidget(HasUpdateWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_lb = QLabel(self.centralwidget)
        self.header_lb.setObjectName(u"header_lb")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.header_lb.setFont(font)
        self.header_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.header_lb.setWordWrap(True)

        self.verticalLayout.addWidget(self.header_lb)

        self.version_lb = QLabel(self.centralwidget)
        self.version_lb.setObjectName(u"version_lb")
        self.version_lb.setText(u"FoxyFace update: 1.0.0.0 ->1.0.0.0")
        self.version_lb.setWordWrap(True)

        self.verticalLayout.addWidget(self.version_lb)

        self.description_lb = QLabel(self.centralwidget)
        self.description_lb.setObjectName(u"description_lb")
        self.description_lb.setWordWrap(True)

        self.verticalLayout.addWidget(self.description_lb)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.open_btn = QPushButton(self.centralwidget)
        self.open_btn.setObjectName(u"open_btn")

        self.horizontalLayout.addWidget(self.open_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ignore_update_btn = QPushButton(self.centralwidget)
        self.ignore_update_btn.setObjectName(u"ignore_update_btn")

        self.horizontalLayout.addWidget(self.ignore_update_btn)

        self.close_btn = QPushButton(self.centralwidget)
        self.close_btn.setObjectName(u"close_btn")

        self.horizontalLayout.addWidget(self.close_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        HasUpdateWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HasUpdateWindow)
        self.open_btn.clicked.connect(HasUpdateWindow.close)
        self.ignore_update_btn.clicked.connect(HasUpdateWindow.close)
        self.close_btn.clicked.connect(HasUpdateWindow.close)

        QMetaObject.connectSlotsByName(HasUpdateWindow)
    # setupUi

    def retranslateUi(self, HasUpdateWindow):
        HasUpdateWindow.setWindowTitle(QCoreApplication.translate("HasUpdateWindow", u"FoxyFace has Update", None))
        self.header_lb.setText(QCoreApplication.translate("HasUpdateWindow", u"A new update for FoxyFace has been found", None))
        self.description_lb.setText(QCoreApplication.translate("HasUpdateWindow", u"Clicking on the \"Open Browser\" button will open a link in the browser from which you can download the latest version of the program.", None))
        self.open_btn.setText(QCoreApplication.translate("HasUpdateWindow", u"Open Browser", None))
        self.ignore_update_btn.setText(QCoreApplication.translate("HasUpdateWindow", u"Ignore Update", None))
        self.close_btn.setText(QCoreApplication.translate("HasUpdateWindow", u"Close", None))
    # retranslateUi

