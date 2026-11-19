# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MicrogridCVXPYUIdKMqSC.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,
    QMetaObject, QRect,
    QSize, Qt)
from PySide6.QtWidgets import (QComboBox, QGridLayout, QLabel,
                               QMenuBar, QPushButton,
                               QSlider, QSpinBox, QStatusBar, QVBoxLayout,
                               QWidget, QLCDNumber)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(881, 623)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 540, 881, 48))
        self.verticalLayoutOptimize = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayoutOptimize.setObjectName(u"verticalLayoutOptimize")
        self.verticalLayoutOptimize.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)

        self.verticalLayoutOptimize.addWidget(self.pushButton)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 881, 541))
        self.verticalLayoutInputParams = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayoutInputParams.setObjectName(u"verticalLayoutInputParams")
        self.verticalLayoutInputParams.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelLoadType = QLabel(self.verticalLayoutWidget_2)
        self.labelLoadType.setObjectName(u"labelLoadType")

        self.gridLayout.addWidget(self.labelLoadType, 9, 0, 1, 1)

        self.battery_capacity = QSpinBox(self.verticalLayoutWidget_2)
        self.battery_capacity.setObjectName(u"battery_capacity")
        self.battery_capacity.setMinimum(10)

        self.gridLayout.addWidget(self.battery_capacity, 3, 1, 1, 1)

        self.labelPChargeMax = QLabel(self.verticalLayoutWidget_2)
        self.labelPChargeMax.setObjectName(u"labelPChargeMax")

        self.gridLayout.addWidget(self.labelPChargeMax, 4, 0, 1, 1)

        self.labelSOCInitial = QLabel(self.verticalLayoutWidget_2)
        self.labelSOCInitial.setObjectName(u"labelSOCInitial")

        self.gridLayout.addWidget(self.labelSOCInitial, 0, 0, 1, 1)

        self.SOC_min_value = QSlider(self.verticalLayoutWidget_2)
        self.SOC_min_value.setObjectName(u"SOC_min_value")
        self.SOC_min_value.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.SOC_min_value, 1, 1, 1, 1)

        self.labelSOCMax = QLabel(self.verticalLayoutWidget_2)
        self.labelSOCMax.setObjectName(u"labelSOCMax")

        self.gridLayout.addWidget(self.labelSOCMax, 2, 0, 1, 1)

        self.labelCBuy = QLabel(self.verticalLayoutWidget_2)
        self.labelCBuy.setObjectName(u"labelCBuy")

        self.gridLayout.addWidget(self.labelCBuy, 7, 0, 1, 1)

        self.labelSOCMin = QLabel(self.verticalLayoutWidget_2)
        self.labelSOCMin.setObjectName(u"labelSOCMin")

        self.gridLayout.addWidget(self.labelSOCMin, 1, 0, 1, 1)

        self.labelEBat = QLabel(self.verticalLayoutWidget_2)
        self.labelEBat.setObjectName(u"labelEBat")

        self.gridLayout.addWidget(self.labelEBat, 3, 0, 1, 1)

        self.loadType = QComboBox(self.verticalLayoutWidget_2)
        self.loadType.setObjectName(u"loadType")
        self.loadType.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.loadType, 9, 1, 1, 1)

        self.seasonType = QComboBox(self.verticalLayoutWidget_2)
        self.seasonType.setObjectName(u"seasonType")
        self.seasonType.setEditable(False)

        self.gridLayout.addWidget(self.seasonType, 8, 1, 1, 1)

        self.SOC_max_value = QSlider(self.verticalLayoutWidget_2)
        self.SOC_max_value.setObjectName(u"SOC_max_value")
        self.SOC_max_value.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.SOC_max_value, 2, 1, 1, 1)

        self.p_grid_max = QSpinBox(self.verticalLayoutWidget_2)
        self.p_grid_max.setObjectName(u"p_grid_max")

        self.gridLayout.addWidget(self.p_grid_max, 6, 1, 1, 1)

        self.p_discharge_max = QSpinBox(self.verticalLayoutWidget_2)
        self.p_discharge_max.setObjectName(u"p_discharge_max")

        self.gridLayout.addWidget(self.p_discharge_max, 5, 1, 1, 1)

        self.labelSeason = QLabel(self.verticalLayoutWidget_2)
        self.labelSeason.setObjectName(u"labelSeason")

        self.gridLayout.addWidget(self.labelSeason, 8, 0, 1, 1)

        self.p_charge_max = QSpinBox(self.verticalLayoutWidget_2)
        self.p_charge_max.setObjectName(u"p_charge_max")

        self.gridLayout.addWidget(self.p_charge_max, 4, 1, 1, 1)

        self.labelPDischargeMax = QLabel(self.verticalLayoutWidget_2)
        self.labelPDischargeMax.setObjectName(u"labelPDischargeMax")

        self.gridLayout.addWidget(self.labelPDischargeMax, 5, 0, 1, 1)

        self.labelPGridMax = QLabel(self.verticalLayoutWidget_2)
        self.labelPGridMax.setObjectName(u"labelPGridMax")

        self.gridLayout.addWidget(self.labelPGridMax, 6, 0, 1, 1)

        self.SOC_initial_value = QSlider(self.verticalLayoutWidget_2)
        self.SOC_initial_value.setObjectName(u"SOC_initial_value")
        self.SOC_initial_value.setMinimum(10)
        self.SOC_initial_value.setMaximum(90)
        self.SOC_initial_value.setValue(55)
        self.SOC_initial_value.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.SOC_initial_value, 0, 1, 1, 1)

        self.c_buy = QSpinBox(self.verticalLayoutWidget_2)
        self.c_buy.setObjectName(u"c_buy")

        self.gridLayout.addWidget(self.c_buy, 7, 1, 1, 1)

        self.lcdSOCInitial = QLCDNumber(self.verticalLayoutWidget_2)
        self.lcdSOCInitial.setObjectName(u"lcdSOCInitial")

        self.gridLayout.addWidget(self.lcdSOCInitial, 0, 2, 1, 1)

        self.lcdSOCMin = QLCDNumber(self.verticalLayoutWidget_2)
        self.lcdSOCMin.setObjectName(u"lcdSOCMin")

        self.gridLayout.addWidget(self.lcdSOCMin, 1, 2, 1, 1)

        self.lcdSOCMax = QLCDNumber(self.verticalLayoutWidget_2)
        self.lcdSOCMax.setObjectName(u"lcdSOCMax")

        self.gridLayout.addWidget(self.lcdSOCMax, 2, 2, 1, 1)


        self.verticalLayoutInputParams.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 881, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Optimize", None))
        self.labelLoadType.setText(QCoreApplication.translate("MainWindow", u"Load type", None))
        self.labelPChargeMax.setText(QCoreApplication.translate("MainWindow", u"P charge max", None))
        self.labelSOCInitial.setText(QCoreApplication.translate("MainWindow", u"SOC Initial", None))
        self.labelSOCMax.setText(QCoreApplication.translate("MainWindow", u"SOC Max", None))
        self.labelCBuy.setText(QCoreApplication.translate("MainWindow", u"C buy", None))
        self.labelSOCMin.setText(QCoreApplication.translate("MainWindow", u"SOC Min", None))
        self.labelEBat.setText(QCoreApplication.translate("MainWindow", u"E bat", None))
        self.seasonType.setCurrentText("")
        self.labelSeason.setText(QCoreApplication.translate("MainWindow", u"Season", None))
        self.labelPDischargeMax.setText(QCoreApplication.translate("MainWindow", u"P discharge max", None))
        self.labelPGridMax.setText(QCoreApplication.translate("MainWindow", u"P grid max", None))
    # retranslateUi