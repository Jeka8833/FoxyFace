# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AutoRunSettings.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_AutoRunSettings(object):
    def setupUi(self, AutoRunSettings):
        if not AutoRunSettings.objectName():
            AutoRunSettings.setObjectName(u"AutoRunSettings")
        AutoRunSettings.resize(333, 406)
        self.centralwidget = QWidget(AutoRunSettings)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 313, 324))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.run_vrchat_strategy_layout = QHBoxLayout()
        self.run_vrchat_strategy_layout.setObjectName(u"run_vrchat_strategy_layout")
        self.run_vrchat_strategy_lb = QLabel(self.scrollAreaWidgetContents)
        self.run_vrchat_strategy_lb.setObjectName(u"run_vrchat_strategy_lb")

        self.run_vrchat_strategy_layout.addWidget(self.run_vrchat_strategy_lb)

        self.run_vrchat_strategy_cb = QComboBox(self.scrollAreaWidgetContents)
        self.run_vrchat_strategy_cb.addItem("")
        self.run_vrchat_strategy_cb.addItem("")
        self.run_vrchat_strategy_cb.addItem("")
        self.run_vrchat_strategy_cb.setObjectName(u"run_vrchat_strategy_cb")

        self.run_vrchat_strategy_layout.addWidget(self.run_vrchat_strategy_cb)


        self.verticalLayout_6.addLayout(self.run_vrchat_strategy_layout)

        self.vrchat_file_path_widget = QWidget(self.scrollAreaWidgetContents)
        self.vrchat_file_path_widget.setObjectName(u"vrchat_file_path_widget")
        self.verticalLayout_4 = QVBoxLayout(self.vrchat_file_path_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.vrchat_file_path_lb = QLabel(self.vrchat_file_path_widget)
        self.vrchat_file_path_lb.setObjectName(u"vrchat_file_path_lb")

        self.verticalLayout_4.addWidget(self.vrchat_file_path_lb)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.vrchat_file_path_le = QLineEdit(self.vrchat_file_path_widget)
        self.vrchat_file_path_le.setObjectName(u"vrchat_file_path_le")

        self.horizontalLayout_4.addWidget(self.vrchat_file_path_le)

        self.vrchat_file_path_select_btn = QToolButton(self.vrchat_file_path_widget)
        self.vrchat_file_path_select_btn.setObjectName(u"vrchat_file_path_select_btn")

        self.horizontalLayout_4.addWidget(self.vrchat_file_path_select_btn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.vrchat_auto_run_error_lb = QLabel(self.vrchat_file_path_widget)
        self.vrchat_auto_run_error_lb.setObjectName(u"vrchat_auto_run_error_lb")
        self.vrchat_auto_run_error_lb.setStyleSheet(u"color: red")
        self.vrchat_auto_run_error_lb.setText(u"Error: Message")
        self.vrchat_auto_run_error_lb.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.vrchat_auto_run_error_lb)

        self.vrchat_file_path_reset_widget = QWidget(self.vrchat_file_path_widget)
        self.vrchat_file_path_reset_widget.setObjectName(u"vrchat_file_path_reset_widget")
        self.horizontalLayout_5 = QHBoxLayout(self.vrchat_file_path_reset_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.vrchat_file_path_reset_btn = QPushButton(self.vrchat_file_path_reset_widget)
        self.vrchat_file_path_reset_btn.setObjectName(u"vrchat_file_path_reset_btn")

        self.horizontalLayout_5.addWidget(self.vrchat_file_path_reset_btn)


        self.verticalLayout_4.addWidget(self.vrchat_file_path_reset_widget)


        self.verticalLayout_6.addWidget(self.vrchat_file_path_widget)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.run_vrcft_strategy_layout = QHBoxLayout()
        self.run_vrcft_strategy_layout.setObjectName(u"run_vrcft_strategy_layout")
        self.run_vrcft_strategy_lb = QLabel(self.scrollAreaWidgetContents)
        self.run_vrcft_strategy_lb.setObjectName(u"run_vrcft_strategy_lb")

        self.run_vrcft_strategy_layout.addWidget(self.run_vrcft_strategy_lb)

        self.run_vrcft_strategy_cb = QComboBox(self.scrollAreaWidgetContents)
        self.run_vrcft_strategy_cb.addItem("")
        self.run_vrcft_strategy_cb.addItem("")
        self.run_vrcft_strategy_cb.addItem("")
        self.run_vrcft_strategy_cb.setObjectName(u"run_vrcft_strategy_cb")

        self.run_vrcft_strategy_layout.addWidget(self.run_vrcft_strategy_cb)


        self.verticalLayout_6.addLayout(self.run_vrcft_strategy_layout)

        self.vrcft_file_path_widget = QWidget(self.scrollAreaWidgetContents)
        self.vrcft_file_path_widget.setObjectName(u"vrcft_file_path_widget")
        self.verticalLayout_5 = QVBoxLayout(self.vrcft_file_path_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.vrcft_file_path_lb = QLabel(self.vrcft_file_path_widget)
        self.vrcft_file_path_lb.setObjectName(u"vrcft_file_path_lb")

        self.verticalLayout_5.addWidget(self.vrcft_file_path_lb)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.vrcft_file_path_le = QLineEdit(self.vrcft_file_path_widget)
        self.vrcft_file_path_le.setObjectName(u"vrcft_file_path_le")

        self.horizontalLayout_6.addWidget(self.vrcft_file_path_le)

        self.vrcft_file_path_select_btn = QToolButton(self.vrcft_file_path_widget)
        self.vrcft_file_path_select_btn.setObjectName(u"vrcft_file_path_select_btn")

        self.horizontalLayout_6.addWidget(self.vrcft_file_path_select_btn)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.vrcft_auto_run_error_lb = QLabel(self.vrcft_file_path_widget)
        self.vrcft_auto_run_error_lb.setObjectName(u"vrcft_auto_run_error_lb")
        self.vrcft_auto_run_error_lb.setStyleSheet(u"color: red")
        self.vrcft_auto_run_error_lb.setText(u"Error: Message")
        self.vrcft_auto_run_error_lb.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.vrcft_auto_run_error_lb)

        self.vrcft_file_path_reset_widget = QWidget(self.vrcft_file_path_widget)
        self.vrcft_file_path_reset_widget.setObjectName(u"vrcft_file_path_reset_widget")
        self.horizontalLayout_7 = QHBoxLayout(self.vrcft_file_path_reset_widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.vrcft_file_path_reset_btn = QPushButton(self.vrcft_file_path_reset_widget)
        self.vrcft_file_path_reset_btn.setObjectName(u"vrcft_file_path_reset_btn")

        self.horizontalLayout_7.addWidget(self.vrcft_file_path_reset_btn)


        self.verticalLayout_5.addWidget(self.vrcft_file_path_reset_widget)


        self.verticalLayout_6.addWidget(self.vrcft_file_path_widget)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.force_run_widget = QWidget(self.centralwidget)
        self.force_run_widget.setObjectName(u"force_run_widget")
        self.horizontalLayout_8 = QHBoxLayout(self.force_run_widget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.force_run_btn = QPushButton(self.force_run_widget)
        self.force_run_btn.setObjectName(u"force_run_btn")

        self.horizontalLayout_8.addWidget(self.force_run_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.force_run_widget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.save_btn = QPushButton(self.centralwidget)
        self.save_btn.setObjectName(u"save_btn")

        self.horizontalLayout.addWidget(self.save_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        AutoRunSettings.setCentralWidget(self.centralwidget)

        self.retranslateUi(AutoRunSettings)
        self.vrchat_file_path_reset_btn.clicked.connect(self.vrchat_file_path_le.clear)
        self.vrcft_file_path_reset_btn.clicked.connect(self.vrcft_file_path_le.clear)

        QMetaObject.connectSlotsByName(AutoRunSettings)
    # setupUi

    def retranslateUi(self, AutoRunSettings):
        AutoRunSettings.setWindowTitle(QCoreApplication.translate("AutoRunSettings", u"VRCFT Settings", None))
        self.run_vrchat_strategy_lb.setText(QCoreApplication.translate("AutoRunSettings", u"Auto Run VRChat:", None))
        self.run_vrchat_strategy_cb.setItemText(0, QCoreApplication.translate("AutoRunSettings", u"Disabled", None))
        self.run_vrchat_strategy_cb.setItemText(1, QCoreApplication.translate("AutoRunSettings", u"Steam Store", None))
        self.run_vrchat_strategy_cb.setItemText(2, QCoreApplication.translate("AutoRunSettings", u"File Path", None))

        self.vrchat_file_path_lb.setText(QCoreApplication.translate("AutoRunSettings", u"File Path:", None))
        self.vrchat_file_path_le.setPlaceholderText(QCoreApplication.translate("AutoRunSettings", u"You can select a file by clicking on '...'", None))
        self.vrchat_file_path_select_btn.setText(QCoreApplication.translate("AutoRunSettings", u"...", None))
        self.vrchat_file_path_reset_btn.setText(QCoreApplication.translate("AutoRunSettings", u"Reset Path", None))
        self.run_vrcft_strategy_lb.setText(QCoreApplication.translate("AutoRunSettings", u"Auto Run VRCFaceTracking:", None))
        self.run_vrcft_strategy_cb.setItemText(0, QCoreApplication.translate("AutoRunSettings", u"Disabled", None))
        self.run_vrcft_strategy_cb.setItemText(1, QCoreApplication.translate("AutoRunSettings", u"Steam Store", None))
        self.run_vrcft_strategy_cb.setItemText(2, QCoreApplication.translate("AutoRunSettings", u"File Path", None))

        self.vrcft_file_path_lb.setText(QCoreApplication.translate("AutoRunSettings", u"File Path:", None))
        self.vrcft_file_path_le.setPlaceholderText(QCoreApplication.translate("AutoRunSettings", u"You can select a file by clicking on '...'", None))
        self.vrcft_file_path_select_btn.setText(QCoreApplication.translate("AutoRunSettings", u"...", None))
        self.vrcft_file_path_reset_btn.setText(QCoreApplication.translate("AutoRunSettings", u"Reset Path", None))
        self.force_run_btn.setText(QCoreApplication.translate("AutoRunSettings", u"Force Run", None))
        self.save_btn.setText(QCoreApplication.translate("AutoRunSettings", u"Apply and Save", None))
    # retranslateUi

