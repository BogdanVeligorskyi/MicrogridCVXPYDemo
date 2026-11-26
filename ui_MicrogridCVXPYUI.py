# -*- coding: utf-8 -*-
import math
import random
from asyncio.windows_events import NULL
from email import message
from pickletools import optimize

################################################################################
## Form generated from reading UI file 'MicrogridCVXPYUIdKMqSC.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import cvxpy as cp
import matplotlib.pyplot as plt
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtWidgets import (QComboBox, QGridLayout, QLabel, QMenuBar, QPushButton,
                               QSlider, QSpinBox, QStatusBar, QVBoxLayout,
                               QWidget, QLCDNumber, QCheckBox, QMessageBox, QLineEdit)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(881, 470)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 400, 881, 48))
        self.verticalLayoutOptimize = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayoutOptimize.setObjectName(u"verticalLayoutOptimize")
        self.verticalLayoutOptimize.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.optimizeButtonPVandPgrid = QPushButton(self.verticalLayoutWidget)
        self.optimizeButtonPVandPgrid.setObjectName(u"optimizeButtonPVandPgrid")

        self.gridLayout_2.addWidget(self.optimizeButtonPVandPgrid, 0, 0, 1, 1)

        self.optimizeButtonPloadandPgrid = QPushButton(self.verticalLayoutWidget)
        self.optimizeButtonPloadandPgrid.setObjectName(u"optimizeButtonPloadandPgrid")

        self.gridLayout_2.addWidget(self.optimizeButtonPloadandPgrid, 0, 1, 1, 1)

        self.simulatePVButton = QPushButton(self.verticalLayoutWidget)
        self.simulatePVButton.setObjectName(u"simulatePVButton")

        self.gridLayout_2.addWidget(self.simulatePVButton, 0, 2, 1, 1)

        self.simulateLoadButton = QPushButton(self.verticalLayoutWidget)
        self.simulateLoadButton.setObjectName(u"simulateLoadButton")

        self.gridLayout_2.addWidget(self.simulateLoadButton, 0, 3, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalLayoutOptimize.addLayout(self.verticalLayout)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 881, 400))
        self.verticalLayoutInputParams = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayoutInputParams.setObjectName(u"verticalLayoutInputParams")
        self.verticalLayoutInputParams.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelSOCMax = QLabel(self.verticalLayoutWidget_2)
        self.labelSOCMax.setObjectName(u"labelSOCMax")

        self.gridLayout.addWidget(self.labelSOCMax, 2, 0, 1, 1)

        self.labelPgridUnavailable = QLabel(self.verticalLayoutWidget_2)
        self.labelPgridUnavailable.setObjectName(u"labelPgridUnavailable")

        self.gridLayout.addWidget(self.labelPgridUnavailable, 11, 0, 1, 1)

        self.SOC_min_value = QSlider(self.verticalLayoutWidget_2)
        self.SOC_min_value.setObjectName(u"SOC_min_value")
        self.SOC_min_value.setMinimum(0)
        self.SOC_min_value.setMaximum(20)
        self.SOC_min_value.setValue(10)
        self.SOC_min_value.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.SOC_min_value, 1, 1, 1, 1)

        self.p_discharge_max = QSpinBox(self.verticalLayoutWidget_2)
        self.p_discharge_max.setObjectName(u"p_discharge_max")

        self.gridLayout.addWidget(self.p_discharge_max, 5, 1, 1, 1)

        self.p_charge_max = QSpinBox(self.verticalLayoutWidget_2)
        self.p_charge_max.setObjectName(u"p_charge_max")
        self.p_charge_max.setMaximum(10)
        self.p_charge_max.setMinimum(1)
        self.p_discharge_max.setMaximum(10)
        self.p_discharge_max.setMinimum(1)
        self.p_charge_max.setValue(5)
        self.p_discharge_max.setValue(5)

        self.fLoad = None

        self.gridLayout.addWidget(self.p_charge_max, 4, 1, 1, 1)

        self.labelSOCInitial = QLabel(self.verticalLayoutWidget_2)
        self.labelSOCInitial.setObjectName(u"labelSOCInitial")

        self.gridLayout.addWidget(self.labelSOCInitial, 0, 0, 1, 1)

        self.labelPGridMax = QLabel(self.verticalLayoutWidget_2)
        self.labelPGridMax.setObjectName(u"labelPGridMax")

        self.gridLayout.addWidget(self.labelPGridMax, 6, 0, 1, 1)

        self.labelEBat = QLabel(self.verticalLayoutWidget_2)
        self.labelEBat.setObjectName(u"labelEBat")

        self.gridLayout.addWidget(self.labelEBat, 3, 0, 1, 1)

        self.loadType = QComboBox(self.verticalLayoutWidget_2)
        self.loadType.setObjectName(u"loadType")
        self.loadType.addItem("Private house")
        self.loadType.addItem("Enterprise Typical")
        self.loadType.addItem("Enterprise 24/7")
        self.loadType.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.loadType, 9, 1, 1, 1)

        self.dayOfWeekType = QComboBox(self.verticalLayoutWidget_2)
        self.dayOfWeekType.setObjectName(u"dayOfWeekType")
        self.dayOfWeekType.addItem("Weekday")
        self.dayOfWeekType.addItem("Weekend")
        self.dayOfWeekType.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.dayOfWeekType, 10, 1, 1, 1)

        self.labelPChargeMax = QLabel(self.verticalLayoutWidget_2)
        self.labelPChargeMax.setObjectName(u"labelPChargeMax")

        self.gridLayout.addWidget(self.labelPChargeMax, 4, 0, 1, 1)

        self.labelPDischargeMax = QLabel(self.verticalLayoutWidget_2)
        self.labelPDischargeMax.setObjectName(u"labelPDischargeMax")

        self.gridLayout.addWidget(self.labelPDischargeMax, 5, 0, 1, 1)

        self.lcdSOCInitial = QLCDNumber(self.verticalLayoutWidget_2)
        self.lcdSOCInitial.setObjectName(u"lcdSOCInitial")

        self.gridLayout.addWidget(self.lcdSOCInitial, 0, 2, 1, 1)

        self.labelCBuy = QLabel(self.verticalLayoutWidget_2)
        self.labelCBuy.setObjectName(u"labelCBuy")

        self.gridLayout.addWidget(self.labelCBuy, 7, 0, 1, 1)

        self.labelSeason = QLabel(self.verticalLayoutWidget_2)
        self.labelSeason.setObjectName(u"labelSeason")

        self.gridLayout.addWidget(self.labelSeason, 8, 0, 1, 1)

        self.labelDayOfWeek = QLabel(self.verticalLayoutWidget_2)
        self.labelDayOfWeek.setObjectName(u"labelDayOfWeek")

        self.gridLayout.addWidget(self.labelDayOfWeek, 10, 0, 1, 1)

        self.lcdSOCMin = QLCDNumber(self.verticalLayoutWidget_2)
        self.lcdSOCMin.setObjectName(u"lcdSOCMin")

        self.gridLayout.addWidget(self.lcdSOCMin, 1, 2, 1, 1)

        self.c_buy = QSpinBox(self.verticalLayoutWidget_2)
        self.c_buy.setObjectName(u"c_buy")
        self.c_buy.setMinimum(0)
        self.c_buy.setMaximum(9999)
        self.c_buy.setValue(50)
        self.c_buy.setEnabled(False)

        self.gridLayout.addWidget(self.c_buy, 7, 1, 1, 1)

        self.lcdSOCMax = QLCDNumber(self.verticalLayoutWidget_2)
        self.lcdSOCMax.setObjectName(u"lcdSOCMax")

        self.gridLayout.addWidget(self.lcdSOCMax, 2, 2, 1, 1)

        self.labelLoadType = QLabel(self.verticalLayoutWidget_2)
        self.labelLoadType.setObjectName(u"labelLoadType")

        self.gridLayout.addWidget(self.labelLoadType, 9, 0, 1, 1)

        self.SOC_max_value = QSlider(self.verticalLayoutWidget_2)
        self.SOC_max_value.setObjectName(u"SOC_max_value")
        self.SOC_max_value.setMinimum(80)
        self.SOC_max_value.setMaximum(100)
        self.SOC_max_value.setValue(90)
        self.SOC_max_value.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.SOC_max_value, 2, 1, 1, 1)

        self.seasonType = QComboBox(self.verticalLayoutWidget_2)
        self.seasonType.setObjectName(u"seasonType")
        self.seasonType.addItem("Summer")
        self.seasonType.addItem("Winter")
        self.seasonType.setEditable(False)

        self.gridLayout.addWidget(self.seasonType, 8, 1, 1, 1)

        self.p_grid_max = QSpinBox(self.verticalLayoutWidget_2)
        self.p_grid_max.setObjectName(u"p_grid_max")
        self.p_grid_max.setMinimum(0)
        self.p_grid_max.setMaximum(100)
        self.p_grid_max.setValue(0)
        self.p_grid_max.setEnabled(False)

        self.gridLayout.addWidget(self.p_grid_max, 6, 1, 1, 1)

        self.labelSOCMin = QLabel(self.verticalLayoutWidget_2)
        self.labelSOCMin.setObjectName(u"labelSOCMin")

        self.gridLayout.addWidget(self.labelSOCMin, 1, 0, 1, 1)

        self.battery_capacity = QSpinBox(self.verticalLayoutWidget_2)
        self.battery_capacity.setObjectName(u"battery_capacity")
        self.battery_capacity.setMinimum(10)
        self.battery_capacity.setMaximum(100)
        self.battery_capacity.setValue(50)

        self.gridLayout.addWidget(self.battery_capacity, 3, 1, 1, 1)

        self.SOC_initial_value = QSlider(self.verticalLayoutWidget_2)
        self.SOC_initial_value.setObjectName(u"SOC_initial_value")
        self.SOC_initial_value.setMinimum(20)
        self.SOC_initial_value.setMaximum(80)
        self.SOC_initial_value.setValue(55)
        self.SOC_initial_value.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.SOC_initial_value, 0, 1, 1, 1)

        self.checkOverride = QCheckBox(self.verticalLayoutWidget_2)
        self.checkOverride.setObjectName(u"checkOverride")
        self.gridLayout.addWidget(self.checkOverride, 13, 1, 1, 1)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.lineEdit, 11, 1, 1, 1)

        self.checkPgridUsage = QCheckBox(self.verticalLayoutWidget_2)
        self.checkPgridUsage.setObjectName(u"checkPgridUsage")
        self.gridLayout.addWidget(self.checkPgridUsage, 12, 1, 1, 1)

        self.verticalLayoutInputParams.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 881, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.lcdSOCInitial.display(str(0.55))
        self.lcdSOCMin.display(str(0.1))
        self.lcdSOCMax.display(str(0.9))

        self.retranslateUi(MainWindow)
        self.SOC_initial_value.valueChanged.connect(self.updateSOCInitialLCD)
        self.SOC_min_value.valueChanged.connect(self.updateSOCMinLCD)
        self.SOC_max_value.valueChanged.connect(self.updateSOCMaxLCD)
        self.optimizeButtonPVandPgrid.clicked.connect(self.optimizePVandPgrid)
        self.optimizeButtonPloadandPgrid.clicked.connect(self.optimizePloadandPgrid)
        self.simulatePVButton.clicked.connect(self.simulatePV)
        self.simulateLoadButton.clicked.connect(self.simulateLoad)
        self.checkPgridUsage.checkStateChanged.connect(self.stateChangePgrid)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi


    def stateChangePgrid(self):
        self.p_grid_max.setEnabled(not self.p_grid_max.isEnabled())
        self.c_buy.setEnabled(not self.c_buy.isEnabled())
        self.lineEdit.setEnabled(not self.lineEdit.isEnabled())


    def updateSOCInitialLCD(self, value):
        self.lcdSOCInitial.display(str(value / 100))


    def updateSOCMinLCD(self, value):
        self.lcdSOCMin.display(str(value / 100))


    def updateSOCMaxLCD(self, value):
        self.lcdSOCMax.display(str(value / 100))


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Microgrid Optimizer", None))
        self.optimizeButtonPVandPgrid.setText(QCoreApplication.translate("MainWindow", u"Optimize Ppv and Pgrid", None))
        self.optimizeButtonPloadandPgrid.setText(QCoreApplication.translate("MainWindow", u"Optimize Pload and Pgrid", None))
        self.simulatePVButton.setText(QCoreApplication.translate("MainWindow", u"Simulate PV", None))
        self.simulateLoadButton.setText(QCoreApplication.translate("MainWindow", u"Simulate Load", None))
        self.labelSOCMax.setText(QCoreApplication.translate("MainWindow", u"SOC Max", None))
        self.labelSOCInitial.setText(QCoreApplication.translate("MainWindow", u"SOC Initial", None))
        self.labelPGridMax.setText(QCoreApplication.translate("MainWindow", u"P grid max, W", None))
        self.labelEBat.setText(QCoreApplication.translate("MainWindow", u"E bat, kW", None))
        self.labelPChargeMax.setText(QCoreApplication.translate("MainWindow", u"P charge max, W", None))
        self.labelPDischargeMax.setText(QCoreApplication.translate("MainWindow", u"P discharge max, W", None))
        self.labelCBuy.setText(QCoreApplication.translate("MainWindow", u"C buy, c.u.", None))
        self.labelSeason.setText(QCoreApplication.translate("MainWindow", u"Season", None))
        self.labelLoadType.setText(QCoreApplication.translate("MainWindow", u"Load type", None))
        self.labelDayOfWeek.setText(QCoreApplication.translate("MainWindow", u"Day of week", None))
        self.labelSOCMin.setText(QCoreApplication.translate("MainWindow", u"SOC Min", None))
        self.labelPgridUnavailable.setText(QCoreApplication.translate("MainWindow", u"Pgrid Unavailable, hours", None))
        self.checkOverride.setText(QCoreApplication.translate("MainWindow", u"Override results in table (for simulation modes)", None))
        self.checkPgridUsage.setText(QCoreApplication.translate("MainWindow", u"Import Pgrid if available", None))
    # retranslateUi


    def simulatePV(self):
        P_nom = []
        if self.seasonType.currentText() == "Summer":
            for i in range(24):
              P_nom.append((self.p_charge_max.value() * max(0, math.sin(math.pi * (i-6) / 12)) * (random.randrange(70, 100) / 100)))
        else:
            for i in range(24):
              P_nom.append((max(0, self.p_charge_max.value() * math.sin(math.pi * (i-8) / 8) - 2.5) * (random.randrange(40, 100) / 100)))
        f2 = plt.figure()
        plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                 P_nom)
        plt.xlabel("Time of the day, hour", fontsize=16)
        plt.ylabel("Generation, kW", fontsize=16)
        plt.title('Generation', fontsize=20)
        plt.show()
        return P_nom


    def simulateLoad(self):
        P_nom = []
        cold_season = 0
        if self.seasonType.currentText() == "Winter":
            cold_season = 1.5
        if self.loadType.currentText() == "Enterprise Typical":
            if self.dayOfWeekType.currentText() == "Weekend":
                for i in range(24):
                    loadValue = 0
                    if i <= 7:
                        loadValue = 2.0 * (random.randrange(70, 100) / 100)
                        P_nom.append(max(1.8, loadValue))
                    if i >= 8 and i < 13:
                        loadValue = cold_season + 2.5 * (random.randrange(70, 100) / 100)
                        P_nom.append(max(2.1, loadValue))
                    if i >= 13 and i < 21:
                        loadValue = cold_season + 2.5 * (random.randrange(70, 100) / 100)
                        P_nom.append(max(2.1, loadValue))
                    if i >= 21 and i < 24:
                        loadValue = cold_season + 2.0 * (random.randrange(70, 100) / 100)
                        P_nom.append(max(1.8, loadValue))
                    print(loadValue)
            else:
                for i in range(24):
                    loadValue = 0
                    if i <= 7:
                        loadValue = 2.0 * (random.randrange(70, 100) / 100)
                        P_nom.append(max(1.8, loadValue))
                    if i >= 8 and i < 13:
                        loadValue = cold_season + 4.5 * (random.randrange(70, 100) / 100)
                        P_nom.append(max(3.9, loadValue))
                    if i >= 13 and i < 14:
                        loadValue = cold_season + 3.0 * (random.randrange(70, 100) / 100)
                        P_nom.append(max(2.4, loadValue))
                    if i >= 14 and i < 17:
                        loadValue = cold_season + 4.5 * (random.randrange(70, 100) / 100)
                        P_nom.append(max(3.9, loadValue))
                    if i >= 17 and i <= 24:
                        loadValue = 2.0 * (random.randrange(70, 100) / 100)
                        P_nom.append(max(1.8, loadValue))
                    print(loadValue)
        elif self.loadType.currentText() == "Enterprise 24/7":
            for i in range(24):
                loadValue = 0
                if i <= 8:
                    loadValue = cold_season + 4.5 * (random.randrange(70, 100) / 100)
                    P_nom.append(max(4.2, loadValue))
                if i > 8 and i < 16:
                    loadValue = cold_season + 2.5 * (random.randrange(70, 100) / 100)
                    P_nom.append(max(2.1, loadValue))
                if i >= 16 and i <= 24:
                    loadValue = cold_season + 4.5 * (random.randrange(70, 100) / 100)
                    P_nom.append(max(4.2, loadValue))
                print(loadValue)
        elif self.loadType.currentText() == "Private house":
            if self.dayOfWeekType.currentText() == "Weekend":
                for i in range(24):
                    loadValue = 0
                    if i <= 5:
                        loadValue = cold_season + 0.5 * (random.randrange(70, 100) / 100)
                        P_nom.append(max(0.2, loadValue))
                    if i >= 6 and i < 9:
                        loadValue = cold_season + 2.5 * (random.randrange(70, 100) / 100)
                        P_nom.append(max(1.5, loadValue))
                    if i >= 9 and i <= 21:
                        loadValue = cold_season + 2.0 * (random.randrange(70, 100) / 100)
                        P_nom.append(max(1.7, loadValue))
                    if i > 21 and i <= 24:
                        loadValue = cold_season + 0.5 * (random.randrange(70, 100) / 100)
                        P_nom.append(max(0.2, loadValue))
                    print(loadValue)
            else:
                for i in range(24):
                    loadValue = 0
                    if i <= 5:
                        loadValue = cold_season + 0.5 * (random.randrange(70, 100) / 100)
                        P_nom.append(max(0.2, loadValue))
                    if i >= 6 and i < 9:
                        loadValue = cold_season + 2.5 * (random.randrange(70, 100) / 100)
                        P_nom.append(max(1.5, loadValue))
                    if i >= 9 and i <= 17:
                        loadValue = cold_season + 0.5 * (random.randrange(70, 100) / 100)
                        P_nom.append(max(0.5, loadValue))
                    if i > 17 and i < 21:
                        loadValue = cold_season + 3.5 * (random.randrange(70, 100) / 100)
                        P_nom.append(max(2.5, loadValue))
                    if i >= 21 and i <= 24:
                        loadValue = cold_season + 1.5 * (random.randrange(70, 100) / 100)
                        P_nom.append(max(1.2, loadValue))
                    print(loadValue)
        if not self.fLoad:
            self.fLoad = plt.figure()
        if not self.checkOverride.isChecked():
            self.fLoad.clear()
        plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                 P_nom)
        plt.xlabel("Time of the day, hour", fontsize=16)
        plt.ylabel("Power consumption, kW", fontsize=16)
        plt.title('Power consumption (Pload)', fontsize=20)
        self.fLoad.canvas.draw()
        plt.show()
        return P_nom

    def optimizePloadandPgrid(self):
        N = 24
        SOC_initial = self.SOC_initial_value.value() / 100
        SOC_min = self.SOC_min_value.value() / 100
        SOC_max = self.SOC_max_value.value() / 100
        dt = 1
        E_bat = self.battery_capacity.value()
        P_charge_max = self.p_charge_max.value()
        P_discharge_max = self.p_discharge_max.value()
        P_grid_max = self.p_grid_max.value()
        c_buy = self.p_grid_max.value()

        SOC = cp.Variable(N)
        P_bat = cp.Variable(N)
        P_grid = cp.Variable(N)
        P_load = cp.Variable(N)
        P_pv = cp.Variable(N)

        # початкове значення заряду
        constraints = [
            SOC[0] == SOC_initial
        ]

        for t in range(N - 1):
            # реалізація заряду батареї
            constraints += [
                SOC[t + 1] ==
                SOC[t] - P_bat[t] * dt / E_bat
            ]

        # обмеження на рівень заряду батареї
        constraints += [
            SOC >= SOC_min,
            SOC <= SOC_max,
            P_bat >= -P_charge_max,
            P_bat <= P_discharge_max
        ]

        # рівняння балансу
        P_grid = P_load - P_pv - P_bat

        # обмеження на імпорт електроенергії з централізованого джерела
        constraints += [
            P_grid <= P_grid_max,
            P_grid >= 0
        ]

        P_pv_arr = self.simulatePV()

        constraints += [
            P_pv[0] == P_pv_arr[0],
            P_pv[1] == P_pv_arr[1],
            P_pv[2] == P_pv_arr[2],
            P_pv[3] == P_pv_arr[3],
            P_pv[4] == P_pv_arr[4],
            P_pv[5] == P_pv_arr[5],
            P_pv[6] == P_pv_arr[6],
            P_pv[7] == P_pv_arr[7],
            P_pv[8] == P_pv_arr[8],
            P_pv[9] == P_pv_arr[9],
            P_pv[10] == P_pv_arr[10],
            P_pv[11] == P_pv_arr[11],
            P_pv[12] == P_pv_arr[12],
            P_pv[13] == P_pv_arr[13],
            P_pv[14] == P_pv_arr[14],
            P_pv[15] == P_pv_arr[15],
            P_pv[16] == P_pv_arr[16],
            P_pv[17] == P_pv_arr[17],
            P_pv[18] == P_pv_arr[18],
            P_pv[19] == P_pv_arr[19],
            P_pv[20] == P_pv_arr[20],
            P_pv[21] == P_pv_arr[21],
            P_pv[22] == P_pv_arr[22],
            P_pv[23] == P_pv_arr[23]
        ]

        # обмеження на попит (він завжди є впродовж доби)
        constraints += [
            P_load >= 0
        ]

        cost = cp.sum(
            cp.multiply(c_buy, P_grid)
        ) * dt

        problem = cp.Problem(cp.Minimize(cost), constraints)

        problem.solve()
        print(problem.status)
        print("SOC:")
        print(SOC.value)
        print("P_bat:")
        print(P_bat.value)
        print("P_pv:")
        print(P_pv.value)
        print("P_load:")
        print(P_load.value)
        print("P_grid:")
        print(P_grid.value)

        if problem.status != cp.OPTIMAL:
            message = QMessageBox()
            message.setWindowTitle("Warning")
            message.setText(
                "Cannot calculate the optimal load. Try to increase Pgrid value or adjust SOC initial or E bat")
            message.exec()
            return
        print("cost" + str(cost.value))
        plt.style.use('tableau-colorblind10')

        f1 = plt.figure()
        plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], SOC.value)
        plt.xlabel("Time of the day, hour", fontsize=16)
        plt.ylabel("State of charge", fontsize=16)
        plt.title('State of charge (SOC)', fontsize=20)
        plt.show()

        f2 = plt.figure()
        plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], P_pv.value,
                 P_load.value)
        plt.legend(['Ppv', 'Pload'])
        plt.xlabel("Time of the day, hour", fontsize=16)
        plt.ylabel("Generation, kW", fontsize=16)
        plt.title('PV Generation (Ppv) and power consumption (Pload)', fontsize=20)
        plt.show()

        f3 = plt.figure()
        plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], P_grid.value)
        plt.xlabel("Time of the day, hour", fontsize=16)
        plt.ylabel("Electricity import, kW", fontsize=16)
        plt.title('Import (Pgrid)', fontsize=20)
        plt.show()


    def optimizePVandPgrid(self):
        N = 24
        SOC_initial = self.SOC_initial_value.value() / 100
        SOC_min = self.SOC_min_value.value() / 100
        SOC_max = self.SOC_max_value.value() / 100
        dt = 1
        E_bat = self.battery_capacity.value()
        P_charge_max = self.p_charge_max.value()
        P_discharge_max = self.p_discharge_max.value()
        P_grid_max = self.p_grid_max.value()
        c_buy = self.p_grid_max.value()

        SOC = cp.Variable(N)
        P_bat = cp.Variable(N)
        P_grid = cp.Variable(N)
        P_load = cp.Variable(N)
        P_pv = cp.Variable(N)

        # початкове значення заряду
        constraints = [
            SOC[0] == SOC_initial
        ]

        for t in range(N - 1):
            # реалізація заряду батареї
            constraints += [
                SOC[t + 1] ==
                SOC[t] - P_bat[t] * dt / E_bat
            ]

        # обмеження на рівень заряду батареї
        constraints += [
            SOC >= SOC_min,
            SOC <= SOC_max,
            P_bat >= -P_charge_max,
            P_bat <= P_discharge_max
        ]

        # рівняння балансу
        P_grid = P_load - P_pv - P_bat

        # обмеження на імпорт електроенергії з централізованого джерела
        constraints += [
            P_grid <= P_grid_max,
            P_grid >= 0
        ]

        # обмеження на PV-генерацію
        constraints += [
            P_pv >= 0,
            P_pv[0] == 0,
            P_pv[1] == 0,
            P_pv[2] == 0,
            P_pv[3] == 0,
            P_pv[4] == 0,
            P_pv[5] == 0,
            P_pv[21] == 0,
            P_pv[22] == 0,
            P_pv[23] == 0,
            P_pv[12] == 5,
            P_pv[13] == 5
        ]

        P_load_arr = self.simulateLoad()

        # обмеження на попит (він завжди є впродовж доби)
        constraints += [
            P_load >= 0,
            P_load[0] == P_load_arr[0],
            P_load[1] == P_load_arr[1],
            P_load[2] == P_load_arr[2],
            P_load[3] == P_load_arr[3],
            P_load[4] == P_load_arr[4],
            P_load[5] == P_load_arr[5],
            P_load[6] == P_load_arr[6],
            P_load[7] == P_load_arr[7],
            P_load[8] == P_load_arr[8],
            P_load[9] == P_load_arr[9],
            P_load[10] == P_load_arr[10],
            P_load[11] == P_load_arr[11],
            P_load[12] == P_load_arr[12],
            P_load[13] == P_load_arr[13],
            P_load[14] == P_load_arr[14],
            P_load[15] == P_load_arr[15],
            P_load[16] == P_load_arr[16],
            P_load[17] == P_load_arr[17],
            P_load[18] == P_load_arr[18],
            P_load[19] == P_load_arr[19],
            P_load[20] == P_load_arr[20],
            P_load[21] == P_load_arr[21],
            P_load[22] == P_load_arr[22],
            P_load[23] == P_load_arr[23]
        ]

        P_grid_limits = []
        if self.lineEdit.text() and not self.lineEdit.isEnabled():
            print("Empty Pgrid!")
        else:
            P_grid_limits = self.lineEdit.text().split(" ")
            for i in range(len(P_grid_limits)):
                if not P_grid_limits[i].isdecimal():
                    continue
                index = int(P_grid_limits[i])

                # обмеження на імпорт електроенергії (у т.ч і графіки відключень)
                constraints += [
                    P_grid[index] == 0
                ]

        cost = cp.sum(
            cp.multiply(c_buy, P_grid)
        ) * dt

        problem = cp.Problem(cp.Minimize(cost), constraints)

        problem.solve()
        print(problem.status)
        print("SOC:")
        print(SOC.value)
        print("P_bat:")
        print(P_bat.value)
        print("P_pv:")
        print(P_pv.value)
        print("P_load:")
        print(P_load.value)
        print("P_grid:")
        print(P_grid.value)

        if problem.status != cp.OPTIMAL:
            message = QMessageBox()
            message.setWindowTitle("Warning")
            message.setText("Cannot calculate the optimal generation. Try to increase Pgrid value or adjust SOC initial")
            message.exec()
            return

        print("cost" + str(cost.value))
        plt.style.use('tableau-colorblind10')

        plt.figure()
        plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], SOC.value)
        plt.xlabel("Time of the day, hour", fontsize=16)
        plt.ylabel("State of charge", fontsize=16)
        plt.title('State of charge (SOC)', fontsize=20)
        plt.show()

        plt.figure()
        plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], P_pv.value,
                 P_load.value)
        plt.legend(['Ppv', 'Pload'])
        plt.xlabel("Time of the day, hour", fontsize=16)
        plt.ylabel("Power consumption, kW", fontsize=16)
        plt.title('Generation (Ppv) and consumption (Pload)', fontsize=20)
        plt.show()

        plt.figure()
        plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], P_grid.value)
        plt.xlabel("Time of the day, hour", fontsize=16)
        plt.ylabel("Electricity import, kW", fontsize=16)
        plt.title('Import (Pgrid)', fontsize=20)
        plt.show()
