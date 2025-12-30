# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(729, 203)
        self.actionSetup_AutoRun = QAction(MainWindow)
        self.actionSetup_AutoRun.setObjectName(u"actionSetup_AutoRun")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.camera_vertical_layout = QVBoxLayout()
        self.camera_vertical_layout.setObjectName(u"camera_vertical_layout")
        self.camera_zone_lbl = QLabel(self.centralwidget)
        self.camera_zone_lbl.setObjectName(u"camera_zone_lbl")
        font = QFont()
        font.setPointSize(20)
        self.camera_zone_lbl.setFont(font)
        self.camera_zone_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.camera_vertical_layout.addWidget(self.camera_zone_lbl)

        self.camera_fps_lbl = QLabel(self.centralwidget)
        self.camera_fps_lbl.setObjectName(u"camera_fps_lbl")
        font1 = QFont()
        font1.setPointSize(11)
        self.camera_fps_lbl.setFont(font1)
        self.camera_fps_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.camera_vertical_layout.addWidget(self.camera_fps_lbl)

        self.camera_zone_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.camera_vertical_layout.addItem(self.camera_zone_spacer)

        self.open_camera_preview_btn = QPushButton(self.centralwidget)
        self.open_camera_preview_btn.setObjectName(u"open_camera_preview_btn")
        self.open_camera_preview_btn.setFont(font1)

        self.camera_vertical_layout.addWidget(self.open_camera_preview_btn)

        self.open_camera_settings_btn = QPushButton(self.centralwidget)
        self.open_camera_settings_btn.setObjectName(u"open_camera_settings_btn")
        self.open_camera_settings_btn.setFont(font1)

        self.camera_vertical_layout.addWidget(self.open_camera_settings_btn)


        self.horizontalLayout_2.addLayout(self.camera_vertical_layout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.mediapipe_vertical_layout = QVBoxLayout()
        self.mediapipe_vertical_layout.setObjectName(u"mediapipe_vertical_layout")
        self.mediapipe_zone_lbl = QLabel(self.centralwidget)
        self.mediapipe_zone_lbl.setObjectName(u"mediapipe_zone_lbl")
        self.mediapipe_zone_lbl.setFont(font)
        self.mediapipe_zone_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mediapipe_vertical_layout.addWidget(self.mediapipe_zone_lbl)

        self.mediapipe_fps_lbl = QLabel(self.centralwidget)
        self.mediapipe_fps_lbl.setObjectName(u"mediapipe_fps_lbl")
        self.mediapipe_fps_lbl.setFont(font1)
        self.mediapipe_fps_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mediapipe_vertical_layout.addWidget(self.mediapipe_fps_lbl)

        self.mediapipe_latency_lbl = QLabel(self.centralwidget)
        self.mediapipe_latency_lbl.setObjectName(u"mediapipe_latency_lbl")
        self.mediapipe_latency_lbl.setFont(font1)
        self.mediapipe_latency_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mediapipe_vertical_layout.addWidget(self.mediapipe_latency_lbl)

        self.mediapipe_zone_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mediapipe_vertical_layout.addItem(self.mediapipe_zone_spacer)

        self.open_mediapipe_preview_btn = QPushButton(self.centralwidget)
        self.open_mediapipe_preview_btn.setObjectName(u"open_mediapipe_preview_btn")
        self.open_mediapipe_preview_btn.setFont(font1)

        self.mediapipe_vertical_layout.addWidget(self.open_mediapipe_preview_btn)

        self.open_mediapipe_settings_btn = QPushButton(self.centralwidget)
        self.open_mediapipe_settings_btn.setObjectName(u"open_mediapipe_settings_btn")
        self.open_mediapipe_settings_btn.setFont(font1)

        self.mediapipe_vertical_layout.addWidget(self.open_mediapipe_settings_btn)


        self.horizontalLayout_2.addLayout(self.mediapipe_vertical_layout)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.babble_vertical_layout = QVBoxLayout()
        self.babble_vertical_layout.setObjectName(u"babble_vertical_layout")
        self.babble_zone_lbl = QLabel(self.centralwidget)
        self.babble_zone_lbl.setObjectName(u"babble_zone_lbl")
        self.babble_zone_lbl.setFont(font)
        self.babble_zone_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.babble_vertical_layout.addWidget(self.babble_zone_lbl)

        self.babble_fps_lbl = QLabel(self.centralwidget)
        self.babble_fps_lbl.setObjectName(u"babble_fps_lbl")
        self.babble_fps_lbl.setFont(font1)
        self.babble_fps_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.babble_vertical_layout.addWidget(self.babble_fps_lbl)

        self.babble_latency_lbl = QLabel(self.centralwidget)
        self.babble_latency_lbl.setObjectName(u"babble_latency_lbl")
        self.babble_latency_lbl.setFont(font1)
        self.babble_latency_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.babble_vertical_layout.addWidget(self.babble_latency_lbl)

        self.babble_zone_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.babble_vertical_layout.addItem(self.babble_zone_spacer)

        self.open_babble_preview_btn = QPushButton(self.centralwidget)
        self.open_babble_preview_btn.setObjectName(u"open_babble_preview_btn")
        self.open_babble_preview_btn.setFont(font1)

        self.babble_vertical_layout.addWidget(self.open_babble_preview_btn)

        self.open_babble_setting_btn = QPushButton(self.centralwidget)
        self.open_babble_setting_btn.setObjectName(u"open_babble_setting_btn")
        self.open_babble_setting_btn.setFont(font1)

        self.babble_vertical_layout.addWidget(self.open_babble_setting_btn)


        self.horizontalLayout_2.addLayout(self.babble_vertical_layout)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_3)

        self.processing_vertical_layout = QVBoxLayout()
        self.processing_vertical_layout.setObjectName(u"processing_vertical_layout")
        self.processing_zone_lbl = QLabel(self.centralwidget)
        self.processing_zone_lbl.setObjectName(u"processing_zone_lbl")
        self.processing_zone_lbl.setFont(font)
        self.processing_zone_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.processing_vertical_layout.addWidget(self.processing_zone_lbl)

        self.processing_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.processing_vertical_layout.addItem(self.processing_spacer)

        self.open_processing_calibration_btn = QPushButton(self.centralwidget)
        self.open_processing_calibration_btn.setObjectName(u"open_processing_calibration_btn")
        self.open_processing_calibration_btn.setFont(font1)

        self.processing_vertical_layout.addWidget(self.open_processing_calibration_btn)

        self.open_processing_settings_btn = QPushButton(self.centralwidget)
        self.open_processing_settings_btn.setObjectName(u"open_processing_settings_btn")
        self.open_processing_settings_btn.setFont(font1)

        self.processing_vertical_layout.addWidget(self.open_processing_settings_btn)


        self.horizontalLayout_2.addLayout(self.processing_vertical_layout)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_4)

        self.sender_vertical_layout = QVBoxLayout()
        self.sender_vertical_layout.setObjectName(u"sender_vertical_layout")
        self.sender_zone_lbl = QLabel(self.centralwidget)
        self.sender_zone_lbl.setObjectName(u"sender_zone_lbl")
        self.sender_zone_lbl.setFont(font)
        self.sender_zone_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.sender_vertical_layout.addWidget(self.sender_zone_lbl)

        self.sender_info_lb = QLabel(self.centralwidget)
        self.sender_info_lb.setObjectName(u"sender_info_lb")
        self.sender_info_lb.setFont(font1)
        self.sender_info_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.sender_vertical_layout.addWidget(self.sender_info_lb)

        self.sender_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sender_vertical_layout.addItem(self.sender_spacer)

        self.open_avatar_calibration_btn = QPushButton(self.centralwidget)
        self.open_avatar_calibration_btn.setObjectName(u"open_avatar_calibration_btn")
        self.open_avatar_calibration_btn.setFont(font1)

        self.sender_vertical_layout.addWidget(self.open_avatar_calibration_btn)

        self.open_sender_settings_btn = QPushButton(self.centralwidget)
        self.open_sender_settings_btn.setObjectName(u"open_sender_settings_btn")
        self.open_sender_settings_btn.setFont(font1)

        self.sender_vertical_layout.addWidget(self.open_sender_settings_btn)


        self.horizontalLayout_2.addLayout(self.sender_vertical_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 729, 21))
        self.menuAutoRun = QMenu(self.menuBar)
        self.menuAutoRun.setObjectName(u"menuAutoRun")
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuAutoRun.menuAction())
        self.menuAutoRun.addAction(self.actionSetup_AutoRun)
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FoxyFace #StandWithUkraine", None))
        self.actionSetup_AutoRun.setText(QCoreApplication.translate("MainWindow", u"Setup AutoRun", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.camera_zone_lbl.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.camera_fps_lbl.setText(QCoreApplication.translate("MainWindow", u"FPS: 0.0", None))
        self.open_camera_preview_btn.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.open_camera_settings_btn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.mediapipe_zone_lbl.setText(QCoreApplication.translate("MainWindow", u"MediaPipe", None))
        self.mediapipe_fps_lbl.setText(QCoreApplication.translate("MainWindow", u"FPS: 0.0", None))
        self.mediapipe_latency_lbl.setText(QCoreApplication.translate("MainWindow", u"Latency: 0 ms", None))
        self.open_mediapipe_preview_btn.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.open_mediapipe_settings_btn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.babble_zone_lbl.setText(QCoreApplication.translate("MainWindow", u"Babble", None))
        self.babble_fps_lbl.setText(QCoreApplication.translate("MainWindow", u"FPS: 0.0", None))
        self.babble_latency_lbl.setText(QCoreApplication.translate("MainWindow", u"Latency: 0 ms", None))
        self.open_babble_preview_btn.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.open_babble_setting_btn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.processing_zone_lbl.setText(QCoreApplication.translate("MainWindow", u"Processing", None))
        self.open_processing_calibration_btn.setText(QCoreApplication.translate("MainWindow", u"Auto Calibration", None))
        self.open_processing_settings_btn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.sender_zone_lbl.setText(QCoreApplication.translate("MainWindow", u"Sender", None))
        self.sender_info_lb.setText(QCoreApplication.translate("MainWindow", u"To: iFacialMocap", None))
        self.open_avatar_calibration_btn.setText(QCoreApplication.translate("MainWindow", u"Avatar Calibration", None))
        self.open_sender_settings_btn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuAutoRun.setTitle(QCoreApplication.translate("MainWindow", u"AutoRun", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

