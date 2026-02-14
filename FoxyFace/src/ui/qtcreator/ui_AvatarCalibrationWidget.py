# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AvatarCalibrationWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QSplitter, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_AvatarCalibrationWidget(object):
    def setupUi(self, AvatarCalibrationWidget):
        if not AvatarCalibrationWidget.objectName():
            AvatarCalibrationWidget.setObjectName(u"AvatarCalibrationWidget")
        AvatarCalibrationWidget.resize(713, 445)
        self.verticalLayout = QVBoxLayout(AvatarCalibrationWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.avatar_enabled_cb = QCheckBox(AvatarCalibrationWidget)
        self.avatar_enabled_cb.setObjectName(u"avatar_enabled_cb")
        self.avatar_enabled_cb.setChecked(True)

        self.verticalLayout.addWidget(self.avatar_enabled_cb)

        self.tabWidget = QTabWidget(AvatarCalibrationWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_3 = QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_2 = QWidget(self.tab)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.splitter = QSplitter(self.widget_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.widget_3 = QWidget(self.splitter)
        self.widget_3.setObjectName(u"widget_3")
        self.splitter.addWidget(self.widget_3)
        self.widget_4 = QWidget(self.splitter)
        self.widget_4.setObjectName(u"widget_4")
        self.splitter.addWidget(self.widget_4)

        self.horizontalLayout_2.addWidget(self.splitter)


        self.horizontalLayout_3.addWidget(self.widget_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.widget = QWidget(AvatarCalibrationWidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.avatar_reset_btn = QPushButton(self.widget)
        self.avatar_reset_btn.setObjectName(u"avatar_reset_btn")

        self.horizontalLayout.addWidget(self.avatar_reset_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.avatar_import_btn = QPushButton(self.widget)
        self.avatar_import_btn.setObjectName(u"avatar_import_btn")

        self.horizontalLayout.addWidget(self.avatar_import_btn)

        self.avatar_export_btn = QPushButton(self.widget)
        self.avatar_export_btn.setObjectName(u"avatar_export_btn")

        self.horizontalLayout.addWidget(self.avatar_export_btn)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(AvatarCalibrationWidget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AvatarCalibrationWidget)
    # setupUi

    def retranslateUi(self, AvatarCalibrationWidget):
        AvatarCalibrationWidget.setWindowTitle(QCoreApplication.translate("AvatarCalibrationWidget", u"Form", None))
        self.avatar_enabled_cb.setText(QCoreApplication.translate("AvatarCalibrationWidget", u"Avatar Enabled", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("AvatarCalibrationWidget", u"Avatar Endpoints", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("AvatarCalibrationWidget", u"Solver Inputs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("AvatarCalibrationWidget", u"Solver Outputs", None))
        self.avatar_reset_btn.setText(QCoreApplication.translate("AvatarCalibrationWidget", u"Reset Avatar", None))
        self.avatar_import_btn.setText(QCoreApplication.translate("AvatarCalibrationWidget", u"Import Avatar", None))
        self.avatar_export_btn.setText(QCoreApplication.translate("AvatarCalibrationWidget", u"Export Avatar", None))
    # retranslateUi

