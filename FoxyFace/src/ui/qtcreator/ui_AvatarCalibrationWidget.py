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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSplitter,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_AvatarCalibrationWidget(object):
    def setupUi(self, AvatarCalibrationWidget):
        if not AvatarCalibrationWidget.objectName():
            AvatarCalibrationWidget.setObjectName(u"AvatarCalibrationWidget")
        AvatarCalibrationWidget.resize(713, 445)
        self.verticalLayout = QVBoxLayout(AvatarCalibrationWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(AvatarCalibrationWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.avatar_endpoint_tab = QWidget()
        self.avatar_endpoint_tab.setObjectName(u"avatar_endpoint_tab")
        self.horizontalLayout_3 = QHBoxLayout(self.avatar_endpoint_tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_2 = QWidget(self.avatar_endpoint_tab)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.splitter = QSplitter(self.widget_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.endpoint_list_widget = QWidget(self.splitter)
        self.endpoint_list_widget.setObjectName(u"endpoint_list_widget")
        self.verticalLayout_4 = QVBoxLayout(self.endpoint_list_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.endpoint_list_lw = QListWidget(self.endpoint_list_widget)
        self.endpoint_list_lw.setObjectName(u"endpoint_list_lw")
        self.endpoint_list_lw.setSortingEnabled(True)

        self.verticalLayout_4.addWidget(self.endpoint_list_lw)

        self.splitter.addWidget(self.endpoint_list_widget)
        self.endpoint_info_widget = QWidget(self.splitter)
        self.endpoint_info_widget.setObjectName(u"endpoint_info_widget")
        self.verticalLayout_3 = QVBoxLayout(self.endpoint_info_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.endpoint_name_lb = QLabel(self.endpoint_info_widget)
        self.endpoint_name_lb.setObjectName(u"endpoint_name_lb")

        self.verticalLayout_3.addWidget(self.endpoint_name_lb)

        self.line = QFrame(self.endpoint_info_widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.endpoint_enable_cb = QCheckBox(self.endpoint_info_widget)
        self.endpoint_enable_cb.setObjectName(u"endpoint_enable_cb")
        self.endpoint_enable_cb.setChecked(True)

        self.verticalLayout_3.addWidget(self.endpoint_enable_cb)

        self.used_nodes_lb = QLabel(self.endpoint_info_widget)
        self.used_nodes_lb.setObjectName(u"used_nodes_lb")

        self.verticalLayout_3.addWidget(self.used_nodes_lb)

        self.used_nodes_list_widget = QWidget(self.endpoint_info_widget)
        self.used_nodes_list_widget.setObjectName(u"used_nodes_list_widget")

        self.verticalLayout_3.addWidget(self.used_nodes_list_widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.endpoint_test_widget = QWidget(self.endpoint_info_widget)
        self.endpoint_test_widget.setObjectName(u"endpoint_test_widget")
        self.horizontalLayout_5 = QHBoxLayout(self.endpoint_test_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.endpoint_test_lb = QLabel(self.endpoint_test_widget)
        self.endpoint_test_lb.setObjectName(u"endpoint_test_lb")

        self.horizontalLayout_5.addWidget(self.endpoint_test_lb)

        self.endpoint_test_btn = QPushButton(self.endpoint_test_widget)
        self.endpoint_test_btn.setObjectName(u"endpoint_test_btn")
        self.endpoint_test_btn.setCheckable(True)
        self.endpoint_test_btn.setChecked(False)

        self.horizontalLayout_5.addWidget(self.endpoint_test_btn)


        self.verticalLayout_3.addWidget(self.endpoint_test_widget)

        self.splitter.addWidget(self.endpoint_info_widget)

        self.horizontalLayout_2.addWidget(self.splitter)


        self.horizontalLayout_3.addWidget(self.widget_2)

        self.tabWidget.addTab(self.avatar_endpoint_tab, "")
        self.solver_input_tab = QWidget()
        self.solver_input_tab.setObjectName(u"solver_input_tab")
        self.verticalLayout_2 = QVBoxLayout(self.solver_input_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.solver_input_scroll_sa = QScrollArea(self.solver_input_tab)
        self.solver_input_scroll_sa.setObjectName(u"solver_input_scroll_sa")
        self.solver_input_scroll_sa.setWidgetResizable(True)
        self.solver_input_scroll_widget = QWidget()
        self.solver_input_scroll_widget.setObjectName(u"solver_input_scroll_widget")
        self.solver_input_scroll_widget.setGeometry(QRect(0, 0, 689, 347))
        self.solver_input_scroll_sa.setWidget(self.solver_input_scroll_widget)

        self.verticalLayout_2.addWidget(self.solver_input_scroll_sa)

        self.tabWidget.addTab(self.solver_input_tab, "")
        self.solver_output_tab = QWidget()
        self.solver_output_tab.setObjectName(u"solver_output_tab")
        self.horizontalLayout_4 = QHBoxLayout(self.solver_output_tab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.solver_output_scroll_area_sa = QScrollArea(self.solver_output_tab)
        self.solver_output_scroll_area_sa.setObjectName(u"solver_output_scroll_area_sa")
        self.solver_output_scroll_area_sa.setWidgetResizable(True)
        self.solver_output_scroll_area_widget = QWidget()
        self.solver_output_scroll_area_widget.setObjectName(u"solver_output_scroll_area_widget")
        self.solver_output_scroll_area_widget.setGeometry(QRect(0, 0, 689, 347))
        self.solver_output_scroll_area_sa.setWidget(self.solver_output_scroll_area_widget)

        self.horizontalLayout_4.addWidget(self.solver_output_scroll_area_sa)

        self.tabWidget.addTab(self.solver_output_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.bottom_panel_widget = QWidget(AvatarCalibrationWidget)
        self.bottom_panel_widget.setObjectName(u"bottom_panel_widget")
        self.horizontalLayout = QHBoxLayout(self.bottom_panel_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.avatar_reset_btn = QPushButton(self.bottom_panel_widget)
        self.avatar_reset_btn.setObjectName(u"avatar_reset_btn")

        self.horizontalLayout.addWidget(self.avatar_reset_btn)

        self.horizontalSpacer = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.avatar_import_btn = QPushButton(self.bottom_panel_widget)
        self.avatar_import_btn.setObjectName(u"avatar_import_btn")

        self.horizontalLayout.addWidget(self.avatar_import_btn)

        self.avatar_export_btn = QPushButton(self.bottom_panel_widget)
        self.avatar_export_btn.setObjectName(u"avatar_export_btn")

        self.horizontalLayout.addWidget(self.avatar_export_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.apply_btn = QPushButton(self.bottom_panel_widget)
        self.apply_btn.setObjectName(u"apply_btn")

        self.horizontalLayout.addWidget(self.apply_btn)


        self.verticalLayout.addWidget(self.bottom_panel_widget)


        self.retranslateUi(AvatarCalibrationWidget)
        self.endpoint_enable_cb.toggled.connect(self.endpoint_test_btn.setEnabled)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AvatarCalibrationWidget)
    # setupUi

    def retranslateUi(self, AvatarCalibrationWidget):
        AvatarCalibrationWidget.setWindowTitle(QCoreApplication.translate("AvatarCalibrationWidget", u"Form", None))
        self.endpoint_name_lb.setText(QCoreApplication.translate("AvatarCalibrationWidget", u"Endpoint Name", None))
        self.endpoint_enable_cb.setText(QCoreApplication.translate("AvatarCalibrationWidget", u"Enabled", None))
        self.used_nodes_lb.setText(QCoreApplication.translate("AvatarCalibrationWidget", u"Used Nodes and precision:", None))
        self.endpoint_test_lb.setText(QCoreApplication.translate("AvatarCalibrationWidget", u"Test Endpoint:", None))
        self.endpoint_test_btn.setText(QCoreApplication.translate("AvatarCalibrationWidget", u"Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.avatar_endpoint_tab), QCoreApplication.translate("AvatarCalibrationWidget", u"Avatar Endpoints", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.solver_input_tab), QCoreApplication.translate("AvatarCalibrationWidget", u"Solver Inputs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.solver_output_tab), QCoreApplication.translate("AvatarCalibrationWidget", u"Solver Outputs", None))
        self.avatar_reset_btn.setText(QCoreApplication.translate("AvatarCalibrationWidget", u"Reset Avatar", None))
        self.avatar_import_btn.setText(QCoreApplication.translate("AvatarCalibrationWidget", u"Import Avatar", None))
        self.avatar_export_btn.setText(QCoreApplication.translate("AvatarCalibrationWidget", u"Export Avatar", None))
        self.apply_btn.setText(QCoreApplication.translate("AvatarCalibrationWidget", u"Apply and Save", None))
    # retranslateUi

