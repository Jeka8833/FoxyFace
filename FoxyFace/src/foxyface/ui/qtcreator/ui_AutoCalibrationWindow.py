# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AutoCalibrationWindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_AutoCalibrationWindow(object):
    def setupUi(self, AutoCalibrationWindow):
        if not AutoCalibrationWindow.objectName():
            AutoCalibrationWindow.setObjectName(u"AutoCalibrationWindow")
        AutoCalibrationWindow.resize(306, 397)
        self.centralwidget = QWidget(AutoCalibrationWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName(u"tabs")
        self.normal_pose_tab = QWidget()
        self.normal_pose_tab.setObjectName(u"normal_pose_tab")
        self.verticalLayout_2 = QVBoxLayout(self.normal_pose_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.normal_pose_hint_sp = QLabel(self.normal_pose_tab)
        self.normal_pose_hint_sp.setObjectName(u"normal_pose_hint_sp")
        self.normal_pose_hint_sp.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.normal_pose_hint_sp.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.normal_pose_hint_sp)

        self.normal_pose_selected_list = QListWidget(self.normal_pose_tab)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        QListWidgetItem(self.normal_pose_selected_list)
        self.normal_pose_selected_list.setObjectName(u"normal_pose_selected_list")
        self.normal_pose_selected_list.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.normal_pose_selected_list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.normal_pose_selected_list.setSortingEnabled(True)

        self.verticalLayout_2.addWidget(self.normal_pose_selected_list)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.normal_pose_delay_lb = QLabel(self.normal_pose_tab)
        self.normal_pose_delay_lb.setObjectName(u"normal_pose_delay_lb")

        self.horizontalLayout.addWidget(self.normal_pose_delay_lb)

        self.normal_pose_delay_sp = QSpinBox(self.normal_pose_tab)
        self.normal_pose_delay_sp.setObjectName(u"normal_pose_delay_sp")
        self.normal_pose_delay_sp.setMaximum(60)
        self.normal_pose_delay_sp.setValue(5)

        self.horizontalLayout.addWidget(self.normal_pose_delay_sp)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.normal_pose_start_btn = QPushButton(self.normal_pose_tab)
        self.normal_pose_start_btn.setObjectName(u"normal_pose_start_btn")
        self.normal_pose_start_btn.setCheckable(False)

        self.horizontalLayout.addWidget(self.normal_pose_start_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tabs.addTab(self.normal_pose_tab, "")
        self.max_pose_tab = QWidget()
        self.max_pose_tab.setObjectName(u"max_pose_tab")
        self.verticalLayout_3 = QVBoxLayout(self.max_pose_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.max_pose_hint_lb = QLabel(self.max_pose_tab)
        self.max_pose_hint_lb.setObjectName(u"max_pose_hint_lb")
        self.max_pose_hint_lb.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.max_pose_hint_lb)

        self.max_pose_selected_list = QListWidget(self.max_pose_tab)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        QListWidgetItem(self.max_pose_selected_list)
        self.max_pose_selected_list.setObjectName(u"max_pose_selected_list")
        self.max_pose_selected_list.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.max_pose_selected_list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.max_pose_selected_list.setSortingEnabled(True)

        self.verticalLayout_3.addWidget(self.max_pose_selected_list)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.max_pose_start_btn = QPushButton(self.max_pose_tab)
        self.max_pose_start_btn.setObjectName(u"max_pose_start_btn")
        self.max_pose_start_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.max_pose_start_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.tabs.addTab(self.max_pose_tab, "")

        self.verticalLayout.addWidget(self.tabs)

        AutoCalibrationWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AutoCalibrationWindow)

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AutoCalibrationWindow)
    # setupUi

    def retranslateUi(self, AutoCalibrationWindow):
        AutoCalibrationWindow.setWindowTitle(QCoreApplication.translate("AutoCalibrationWindow", u"Auto Calibration", None))
        self.normal_pose_hint_sp.setText(QCoreApplication.translate("AutoCalibrationWindow", u"To calibrate, select the desired parameters, find a comfortable position, press the \u201cStart Calibration\u201d button, do not move and look exactly at the center of the VRChat window for a few seconds after the beep.", None))

        __sortingEnabled = self.normal_pose_selected_list.isSortingEnabled()
        self.normal_pose_selected_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.normal_pose_selected_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("AutoCalibrationWindow", u"BrowDownLeft", None));
        ___qlistwidgetitem1 = self.normal_pose_selected_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("AutoCalibrationWindow", u"BrowDownRight", None));
        ___qlistwidgetitem2 = self.normal_pose_selected_list.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("AutoCalibrationWindow", u"BrowInnerUp", None));
        ___qlistwidgetitem3 = self.normal_pose_selected_list.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("AutoCalibrationWindow", u"BrowOuterUpLeft", None));
        ___qlistwidgetitem4 = self.normal_pose_selected_list.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("AutoCalibrationWindow", u"BrowOuterUpRight", None));
        ___qlistwidgetitem5 = self.normal_pose_selected_list.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("AutoCalibrationWindow", u"CheekPuff", None));
        ___qlistwidgetitem6 = self.normal_pose_selected_list.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("AutoCalibrationWindow", u"CheekPuffLeft", None));
        ___qlistwidgetitem7 = self.normal_pose_selected_list.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("AutoCalibrationWindow", u"CheekPuffRight", None));
        ___qlistwidgetitem8 = self.normal_pose_selected_list.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("AutoCalibrationWindow", u"CheekSquintLeft", None));
        ___qlistwidgetitem9 = self.normal_pose_selected_list.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("AutoCalibrationWindow", u"CheekSquintRight", None));
        ___qlistwidgetitem10 = self.normal_pose_selected_list.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("AutoCalibrationWindow", u"CheekSuckLeft", None));
        ___qlistwidgetitem11 = self.normal_pose_selected_list.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("AutoCalibrationWindow", u"CheekSuckRight", None));
        ___qlistwidgetitem12 = self.normal_pose_selected_list.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("AutoCalibrationWindow", u"EyeBlinkLeft", None));
        ___qlistwidgetitem13 = self.normal_pose_selected_list.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("AutoCalibrationWindow", u"EyeBlinkRight", None));
        ___qlistwidgetitem14 = self.normal_pose_selected_list.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("AutoCalibrationWindow", u"EyeSquintLeft", None));
        ___qlistwidgetitem15 = self.normal_pose_selected_list.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("AutoCalibrationWindow", u"EyeSquintRight", None));
        ___qlistwidgetitem16 = self.normal_pose_selected_list.item(16)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("AutoCalibrationWindow", u"EyeWideLeft", None));
        ___qlistwidgetitem17 = self.normal_pose_selected_list.item(17)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("AutoCalibrationWindow", u"EyeWideRight", None));
        ___qlistwidgetitem18 = self.normal_pose_selected_list.item(18)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("AutoCalibrationWindow", u"EyeXLeft", None));
        ___qlistwidgetitem19 = self.normal_pose_selected_list.item(19)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("AutoCalibrationWindow", u"EyeXRight", None));
        ___qlistwidgetitem20 = self.normal_pose_selected_list.item(20)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("AutoCalibrationWindow", u"EyeYLeft", None));
        ___qlistwidgetitem21 = self.normal_pose_selected_list.item(21)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("AutoCalibrationWindow", u"EyeYRight", None));
        ___qlistwidgetitem22 = self.normal_pose_selected_list.item(22)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("AutoCalibrationWindow", u"HeadRotation", None));
        ___qlistwidgetitem23 = self.normal_pose_selected_list.item(23)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("AutoCalibrationWindow", u"HeadX", None));
        ___qlistwidgetitem24 = self.normal_pose_selected_list.item(24)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("AutoCalibrationWindow", u"HeadY", None));
        ___qlistwidgetitem25 = self.normal_pose_selected_list.item(25)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("AutoCalibrationWindow", u"HeadZ", None));
        ___qlistwidgetitem26 = self.normal_pose_selected_list.item(26)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("AutoCalibrationWindow", u"JawForward", None));
        ___qlistwidgetitem27 = self.normal_pose_selected_list.item(27)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("AutoCalibrationWindow", u"JawLeft", None));
        ___qlistwidgetitem28 = self.normal_pose_selected_list.item(28)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("AutoCalibrationWindow", u"JawOpen", None));
        ___qlistwidgetitem29 = self.normal_pose_selected_list.item(29)
        ___qlistwidgetitem29.setText(QCoreApplication.translate("AutoCalibrationWindow", u"JawRight", None));
        ___qlistwidgetitem30 = self.normal_pose_selected_list.item(30)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthClosed", None));
        ___qlistwidgetitem31 = self.normal_pose_selected_list.item(31)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthDimpleLeft", None));
        ___qlistwidgetitem32 = self.normal_pose_selected_list.item(32)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthDimpleRight", None));
        ___qlistwidgetitem33 = self.normal_pose_selected_list.item(33)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthFrownLeft", None));
        ___qlistwidgetitem34 = self.normal_pose_selected_list.item(34)
        ___qlistwidgetitem34.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthFrownRight", None));
        ___qlistwidgetitem35 = self.normal_pose_selected_list.item(35)
        ___qlistwidgetitem35.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthFunnel", None));
        ___qlistwidgetitem36 = self.normal_pose_selected_list.item(36)
        ___qlistwidgetitem36.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthLeft", None));
        ___qlistwidgetitem37 = self.normal_pose_selected_list.item(37)
        ___qlistwidgetitem37.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthLowerDownLeft", None));
        ___qlistwidgetitem38 = self.normal_pose_selected_list.item(38)
        ___qlistwidgetitem38.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthLowerDownRight", None));
        ___qlistwidgetitem39 = self.normal_pose_selected_list.item(39)
        ___qlistwidgetitem39.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthPressLeft", None));
        ___qlistwidgetitem40 = self.normal_pose_selected_list.item(40)
        ___qlistwidgetitem40.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthPressRight", None));
        ___qlistwidgetitem41 = self.normal_pose_selected_list.item(41)
        ___qlistwidgetitem41.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthPucker", None));
        ___qlistwidgetitem42 = self.normal_pose_selected_list.item(42)
        ___qlistwidgetitem42.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthRaiserLower", None));
        ___qlistwidgetitem43 = self.normal_pose_selected_list.item(43)
        ___qlistwidgetitem43.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthRaiserUpper", None));
        ___qlistwidgetitem44 = self.normal_pose_selected_list.item(44)
        ___qlistwidgetitem44.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthRight", None));
        ___qlistwidgetitem45 = self.normal_pose_selected_list.item(45)
        ___qlistwidgetitem45.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthRollLower", None));
        ___qlistwidgetitem46 = self.normal_pose_selected_list.item(46)
        ___qlistwidgetitem46.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthRollUpper", None));
        ___qlistwidgetitem47 = self.normal_pose_selected_list.item(47)
        ___qlistwidgetitem47.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthSmileLeft", None));
        ___qlistwidgetitem48 = self.normal_pose_selected_list.item(48)
        ___qlistwidgetitem48.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthSmileRight", None));
        ___qlistwidgetitem49 = self.normal_pose_selected_list.item(49)
        ___qlistwidgetitem49.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthStretchLeft", None));
        ___qlistwidgetitem50 = self.normal_pose_selected_list.item(50)
        ___qlistwidgetitem50.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthStretchRight", None));
        ___qlistwidgetitem51 = self.normal_pose_selected_list.item(51)
        ___qlistwidgetitem51.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthUpperUpLeft", None));
        ___qlistwidgetitem52 = self.normal_pose_selected_list.item(52)
        ___qlistwidgetitem52.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthUpperUpRight", None));
        ___qlistwidgetitem53 = self.normal_pose_selected_list.item(53)
        ___qlistwidgetitem53.setText(QCoreApplication.translate("AutoCalibrationWindow", u"NoseSneerLeft", None));
        ___qlistwidgetitem54 = self.normal_pose_selected_list.item(54)
        ___qlistwidgetitem54.setText(QCoreApplication.translate("AutoCalibrationWindow", u"NoseSneerRight", None));
        ___qlistwidgetitem55 = self.normal_pose_selected_list.item(55)
        ___qlistwidgetitem55.setText(QCoreApplication.translate("AutoCalibrationWindow", u"TongueBendDown", None));
        ___qlistwidgetitem56 = self.normal_pose_selected_list.item(56)
        ___qlistwidgetitem56.setText(QCoreApplication.translate("AutoCalibrationWindow", u"TongueCurlUp", None));
        ___qlistwidgetitem57 = self.normal_pose_selected_list.item(57)
        ___qlistwidgetitem57.setText(QCoreApplication.translate("AutoCalibrationWindow", u"TongueDown", None));
        ___qlistwidgetitem58 = self.normal_pose_selected_list.item(58)
        ___qlistwidgetitem58.setText(QCoreApplication.translate("AutoCalibrationWindow", u"TongueFlat", None));
        ___qlistwidgetitem59 = self.normal_pose_selected_list.item(59)
        ___qlistwidgetitem59.setText(QCoreApplication.translate("AutoCalibrationWindow", u"TongueLeft", None));
        ___qlistwidgetitem60 = self.normal_pose_selected_list.item(60)
        ___qlistwidgetitem60.setText(QCoreApplication.translate("AutoCalibrationWindow", u"TongueOut", None));
        ___qlistwidgetitem61 = self.normal_pose_selected_list.item(61)
        ___qlistwidgetitem61.setText(QCoreApplication.translate("AutoCalibrationWindow", u"TongueRight", None));
        ___qlistwidgetitem62 = self.normal_pose_selected_list.item(62)
        ___qlistwidgetitem62.setText(QCoreApplication.translate("AutoCalibrationWindow", u"TongueRoll", None));
        ___qlistwidgetitem63 = self.normal_pose_selected_list.item(63)
        ___qlistwidgetitem63.setText(QCoreApplication.translate("AutoCalibrationWindow", u"TongueSquish", None));
        ___qlistwidgetitem64 = self.normal_pose_selected_list.item(64)
        ___qlistwidgetitem64.setText(QCoreApplication.translate("AutoCalibrationWindow", u"TongueTwistLeft", None));
        ___qlistwidgetitem65 = self.normal_pose_selected_list.item(65)
        ___qlistwidgetitem65.setText(QCoreApplication.translate("AutoCalibrationWindow", u"TongueTwistRight", None));
        ___qlistwidgetitem66 = self.normal_pose_selected_list.item(66)
        ___qlistwidgetitem66.setText(QCoreApplication.translate("AutoCalibrationWindow", u"TongueUp", None));
        self.normal_pose_selected_list.setSortingEnabled(__sortingEnabled)

        self.normal_pose_delay_lb.setText(QCoreApplication.translate("AutoCalibrationWindow", u"Delay Start (Seconds):", None))
        self.normal_pose_start_btn.setText(QCoreApplication.translate("AutoCalibrationWindow", u"Start Calibration", None))
        self.tabs.setTabText(self.tabs.indexOf(self.normal_pose_tab), QCoreApplication.translate("AutoCalibrationWindow", u"Calibrate Neutral Pose", None))
        self.max_pose_hint_lb.setText(QCoreApplication.translate("AutoCalibrationWindow", u"To calibrate, select the desired parameters and press the \"Start Calibration\" button. After that, tense the selected muscles (or what you have selected) in any order. It is not necessary to tense the muscles too much (you need to find a force that is comfortable for you).", None))

        __sortingEnabled1 = self.max_pose_selected_list.isSortingEnabled()
        self.max_pose_selected_list.setSortingEnabled(False)
        ___qlistwidgetitem67 = self.max_pose_selected_list.item(0)
        ___qlistwidgetitem67.setText(QCoreApplication.translate("AutoCalibrationWindow", u"BrowDownLeft", None));
        ___qlistwidgetitem68 = self.max_pose_selected_list.item(1)
        ___qlistwidgetitem68.setText(QCoreApplication.translate("AutoCalibrationWindow", u"BrowDownRight", None));
        ___qlistwidgetitem69 = self.max_pose_selected_list.item(2)
        ___qlistwidgetitem69.setText(QCoreApplication.translate("AutoCalibrationWindow", u"BrowInnerUp", None));
        ___qlistwidgetitem70 = self.max_pose_selected_list.item(3)
        ___qlistwidgetitem70.setText(QCoreApplication.translate("AutoCalibrationWindow", u"BrowOuterUpLeft", None));
        ___qlistwidgetitem71 = self.max_pose_selected_list.item(4)
        ___qlistwidgetitem71.setText(QCoreApplication.translate("AutoCalibrationWindow", u"BrowOuterUpRight", None));
        ___qlistwidgetitem72 = self.max_pose_selected_list.item(5)
        ___qlistwidgetitem72.setText(QCoreApplication.translate("AutoCalibrationWindow", u"CheekPuff", None));
        ___qlistwidgetitem73 = self.max_pose_selected_list.item(6)
        ___qlistwidgetitem73.setText(QCoreApplication.translate("AutoCalibrationWindow", u"CheekPuffLeft", None));
        ___qlistwidgetitem74 = self.max_pose_selected_list.item(7)
        ___qlistwidgetitem74.setText(QCoreApplication.translate("AutoCalibrationWindow", u"CheekPuffRight", None));
        ___qlistwidgetitem75 = self.max_pose_selected_list.item(8)
        ___qlistwidgetitem75.setText(QCoreApplication.translate("AutoCalibrationWindow", u"CheekSquintLeft", None));
        ___qlistwidgetitem76 = self.max_pose_selected_list.item(9)
        ___qlistwidgetitem76.setText(QCoreApplication.translate("AutoCalibrationWindow", u"CheekSquintRight", None));
        ___qlistwidgetitem77 = self.max_pose_selected_list.item(10)
        ___qlistwidgetitem77.setText(QCoreApplication.translate("AutoCalibrationWindow", u"CheekSuckLeft", None));
        ___qlistwidgetitem78 = self.max_pose_selected_list.item(11)
        ___qlistwidgetitem78.setText(QCoreApplication.translate("AutoCalibrationWindow", u"CheekSuckRight", None));
        ___qlistwidgetitem79 = self.max_pose_selected_list.item(12)
        ___qlistwidgetitem79.setText(QCoreApplication.translate("AutoCalibrationWindow", u"EyeBlinkLeft", None));
        ___qlistwidgetitem80 = self.max_pose_selected_list.item(13)
        ___qlistwidgetitem80.setText(QCoreApplication.translate("AutoCalibrationWindow", u"EyeBlinkRight", None));
        ___qlistwidgetitem81 = self.max_pose_selected_list.item(14)
        ___qlistwidgetitem81.setText(QCoreApplication.translate("AutoCalibrationWindow", u"EyeSquintLeft", None));
        ___qlistwidgetitem82 = self.max_pose_selected_list.item(15)
        ___qlistwidgetitem82.setText(QCoreApplication.translate("AutoCalibrationWindow", u"EyeSquintRight", None));
        ___qlistwidgetitem83 = self.max_pose_selected_list.item(16)
        ___qlistwidgetitem83.setText(QCoreApplication.translate("AutoCalibrationWindow", u"EyeWideLeft", None));
        ___qlistwidgetitem84 = self.max_pose_selected_list.item(17)
        ___qlistwidgetitem84.setText(QCoreApplication.translate("AutoCalibrationWindow", u"EyeWideRight", None));
        ___qlistwidgetitem85 = self.max_pose_selected_list.item(18)
        ___qlistwidgetitem85.setText(QCoreApplication.translate("AutoCalibrationWindow", u"EyeXLeft", None));
        ___qlistwidgetitem86 = self.max_pose_selected_list.item(19)
        ___qlistwidgetitem86.setText(QCoreApplication.translate("AutoCalibrationWindow", u"EyeXRight", None));
        ___qlistwidgetitem87 = self.max_pose_selected_list.item(20)
        ___qlistwidgetitem87.setText(QCoreApplication.translate("AutoCalibrationWindow", u"EyeYLeft", None));
        ___qlistwidgetitem88 = self.max_pose_selected_list.item(21)
        ___qlistwidgetitem88.setText(QCoreApplication.translate("AutoCalibrationWindow", u"EyeYRight", None));
        ___qlistwidgetitem89 = self.max_pose_selected_list.item(22)
        ___qlistwidgetitem89.setText(QCoreApplication.translate("AutoCalibrationWindow", u"HeadX", None));
        ___qlistwidgetitem90 = self.max_pose_selected_list.item(23)
        ___qlistwidgetitem90.setText(QCoreApplication.translate("AutoCalibrationWindow", u"HeadY", None));
        ___qlistwidgetitem91 = self.max_pose_selected_list.item(24)
        ___qlistwidgetitem91.setText(QCoreApplication.translate("AutoCalibrationWindow", u"HeadZ", None));
        ___qlistwidgetitem92 = self.max_pose_selected_list.item(25)
        ___qlistwidgetitem92.setText(QCoreApplication.translate("AutoCalibrationWindow", u"JawForward", None));
        ___qlistwidgetitem93 = self.max_pose_selected_list.item(26)
        ___qlistwidgetitem93.setText(QCoreApplication.translate("AutoCalibrationWindow", u"JawLeft", None));
        ___qlistwidgetitem94 = self.max_pose_selected_list.item(27)
        ___qlistwidgetitem94.setText(QCoreApplication.translate("AutoCalibrationWindow", u"JawOpen", None));
        ___qlistwidgetitem95 = self.max_pose_selected_list.item(28)
        ___qlistwidgetitem95.setText(QCoreApplication.translate("AutoCalibrationWindow", u"JawRight", None));
        ___qlistwidgetitem96 = self.max_pose_selected_list.item(29)
        ___qlistwidgetitem96.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthClosed", None));
        ___qlistwidgetitem97 = self.max_pose_selected_list.item(30)
        ___qlistwidgetitem97.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthDimpleLeft", None));
        ___qlistwidgetitem98 = self.max_pose_selected_list.item(31)
        ___qlistwidgetitem98.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthDimpleRight", None));
        ___qlistwidgetitem99 = self.max_pose_selected_list.item(32)
        ___qlistwidgetitem99.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthFrownLeft", None));
        ___qlistwidgetitem100 = self.max_pose_selected_list.item(33)
        ___qlistwidgetitem100.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthFrownRight", None));
        ___qlistwidgetitem101 = self.max_pose_selected_list.item(34)
        ___qlistwidgetitem101.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthFunnel", None));
        ___qlistwidgetitem102 = self.max_pose_selected_list.item(35)
        ___qlistwidgetitem102.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthLeft", None));
        ___qlistwidgetitem103 = self.max_pose_selected_list.item(36)
        ___qlistwidgetitem103.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthLowerDownLeft", None));
        ___qlistwidgetitem104 = self.max_pose_selected_list.item(37)
        ___qlistwidgetitem104.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthLowerDownRight", None));
        ___qlistwidgetitem105 = self.max_pose_selected_list.item(38)
        ___qlistwidgetitem105.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthPressLeft", None));
        ___qlistwidgetitem106 = self.max_pose_selected_list.item(39)
        ___qlistwidgetitem106.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthPressRight", None));
        ___qlistwidgetitem107 = self.max_pose_selected_list.item(40)
        ___qlistwidgetitem107.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthPucker", None));
        ___qlistwidgetitem108 = self.max_pose_selected_list.item(41)
        ___qlistwidgetitem108.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthRaiserLower", None));
        ___qlistwidgetitem109 = self.max_pose_selected_list.item(42)
        ___qlistwidgetitem109.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthRaiserUpper", None));
        ___qlistwidgetitem110 = self.max_pose_selected_list.item(43)
        ___qlistwidgetitem110.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthRight", None));
        ___qlistwidgetitem111 = self.max_pose_selected_list.item(44)
        ___qlistwidgetitem111.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthRollLower", None));
        ___qlistwidgetitem112 = self.max_pose_selected_list.item(45)
        ___qlistwidgetitem112.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthRollUpper", None));
        ___qlistwidgetitem113 = self.max_pose_selected_list.item(46)
        ___qlistwidgetitem113.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthSmileLeft", None));
        ___qlistwidgetitem114 = self.max_pose_selected_list.item(47)
        ___qlistwidgetitem114.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthSmileRight", None));
        ___qlistwidgetitem115 = self.max_pose_selected_list.item(48)
        ___qlistwidgetitem115.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthStretchLeft", None));
        ___qlistwidgetitem116 = self.max_pose_selected_list.item(49)
        ___qlistwidgetitem116.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthStretchRight", None));
        ___qlistwidgetitem117 = self.max_pose_selected_list.item(50)
        ___qlistwidgetitem117.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthUpperUpLeft", None));
        ___qlistwidgetitem118 = self.max_pose_selected_list.item(51)
        ___qlistwidgetitem118.setText(QCoreApplication.translate("AutoCalibrationWindow", u"MouthUpperUpRight", None));
        ___qlistwidgetitem119 = self.max_pose_selected_list.item(52)
        ___qlistwidgetitem119.setText(QCoreApplication.translate("AutoCalibrationWindow", u"NoseSneerLeft", None));
        ___qlistwidgetitem120 = self.max_pose_selected_list.item(53)
        ___qlistwidgetitem120.setText(QCoreApplication.translate("AutoCalibrationWindow", u"NoseSneerRight", None));
        ___qlistwidgetitem121 = self.max_pose_selected_list.item(54)
        ___qlistwidgetitem121.setText(QCoreApplication.translate("AutoCalibrationWindow", u"TongueBendDown", None));
        ___qlistwidgetitem122 = self.max_pose_selected_list.item(55)
        ___qlistwidgetitem122.setText(QCoreApplication.translate("AutoCalibrationWindow", u"TongueCurlUp", None));
        ___qlistwidgetitem123 = self.max_pose_selected_list.item(56)
        ___qlistwidgetitem123.setText(QCoreApplication.translate("AutoCalibrationWindow", u"TongueDown", None));
        ___qlistwidgetitem124 = self.max_pose_selected_list.item(57)
        ___qlistwidgetitem124.setText(QCoreApplication.translate("AutoCalibrationWindow", u"TongueFlat", None));
        ___qlistwidgetitem125 = self.max_pose_selected_list.item(58)
        ___qlistwidgetitem125.setText(QCoreApplication.translate("AutoCalibrationWindow", u"TongueLeft", None));
        ___qlistwidgetitem126 = self.max_pose_selected_list.item(59)
        ___qlistwidgetitem126.setText(QCoreApplication.translate("AutoCalibrationWindow", u"TongueOut", None));
        ___qlistwidgetitem127 = self.max_pose_selected_list.item(60)
        ___qlistwidgetitem127.setText(QCoreApplication.translate("AutoCalibrationWindow", u"TongueRight", None));
        ___qlistwidgetitem128 = self.max_pose_selected_list.item(61)
        ___qlistwidgetitem128.setText(QCoreApplication.translate("AutoCalibrationWindow", u"TongueRoll", None));
        ___qlistwidgetitem129 = self.max_pose_selected_list.item(62)
        ___qlistwidgetitem129.setText(QCoreApplication.translate("AutoCalibrationWindow", u"TongueSquish", None));
        ___qlistwidgetitem130 = self.max_pose_selected_list.item(63)
        ___qlistwidgetitem130.setText(QCoreApplication.translate("AutoCalibrationWindow", u"TongueTwistLeft", None));
        ___qlistwidgetitem131 = self.max_pose_selected_list.item(64)
        ___qlistwidgetitem131.setText(QCoreApplication.translate("AutoCalibrationWindow", u"TongueTwistRight", None));
        ___qlistwidgetitem132 = self.max_pose_selected_list.item(65)
        ___qlistwidgetitem132.setText(QCoreApplication.translate("AutoCalibrationWindow", u"TongueUp", None));
        self.max_pose_selected_list.setSortingEnabled(__sortingEnabled1)

        self.max_pose_start_btn.setText(QCoreApplication.translate("AutoCalibrationWindow", u"Start Calibration", None))
        self.tabs.setTabText(self.tabs.indexOf(self.max_pose_tab), QCoreApplication.translate("AutoCalibrationWindow", u"Calibrate Max Pose", None))
    # retranslateUi

