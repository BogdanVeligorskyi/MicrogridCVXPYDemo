# -*- coding: utf-8 -*-
import math
import random
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
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.optimizeButton = QPushButton(self.verticalLayoutWidget)
        self.optimizeButton.setObjectName(u"optimizeButton")

        self.gridLayout_2.addWidget(self.optimizeButton, 0, 0, 1, 1)

        self.simulatePVButton = QPushButton(self.verticalLayoutWidget)
        self.simulatePVButton.setObjectName(u"simulatePVButton")

        self.gridLayout_2.addWidget(self.simulatePVButton, 0, 1, 1, 1)

        self.simulateLoadButton = QPushButton(self.verticalLayoutWidget)
        self.simulateLoadButton.setObjectName(u"simulateLoadButton")

        self.gridLayout_2.addWidget(self.simulateLoadButton, 0, 2, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalLayoutOptimize.addLayout(self.verticalLayout)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 881, 541))
        self.verticalLayoutInputParams = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayoutInputParams.setObjectName(u"verticalLayoutInputParams")
        self.verticalLayoutInputParams.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelSOCMax = QLabel(self.verticalLayoutWidget_2)
        self.labelSOCMax.setObjectName(u"labelSOCMax")

        self.gridLayout.addWidget(self.labelSOCMax, 2, 0, 1, 1)

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
        self.loadType.addItem("Enterprise")
        self.loadType.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.loadType, 9, 1, 1, 1)

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

        self.lcdSOCMin = QLCDNumber(self.verticalLayoutWidget_2)
        self.lcdSOCMin.setObjectName(u"lcdSOCMin")

        self.gridLayout.addWidget(self.lcdSOCMin, 1, 2, 1, 1)

        self.c_buy = QSpinBox(self.verticalLayoutWidget_2)
        self.c_buy.setObjectName(u"c_buy")
        self.c_buy.setMinimum(0)
        self.c_buy.setMaximum(9999)
        self.c_buy.setValue(50)

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
        self.optimizeButton.clicked.connect(self.optimize)
        self.simulatePVButton.clicked.connect(self.simulatePV)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi


    def updateSOCInitialLCD(self, value):
        self.lcdSOCInitial.display(str(value / 100))


    def updateSOCMinLCD(self, value):
        self.lcdSOCMin.display(str(value / 100))


    def updateSOCMaxLCD(self, value):
        self.lcdSOCMax.display(str(value / 100))


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.optimizeButton.setText(QCoreApplication.translate("MainWindow", u"Optimize", None))
        self.simulatePVButton.setText(QCoreApplication.translate("MainWindow", u"Simulate PV", None))
        self.simulateLoadButton.setText(QCoreApplication.translate("MainWindow", u"Simulate Load", None))
        self.labelSOCMax.setText(QCoreApplication.translate("MainWindow", u"SOC Max", None))
        self.labelSOCInitial.setText(QCoreApplication.translate("MainWindow", u"SOC Initial", None))
        self.labelPGridMax.setText(QCoreApplication.translate("MainWindow", u"P grid max", None))
        self.labelEBat.setText(QCoreApplication.translate("MainWindow", u"E bat", None))
        self.labelPChargeMax.setText(QCoreApplication.translate("MainWindow", u"P charge max", None))
        self.labelPDischargeMax.setText(QCoreApplication.translate("MainWindow", u"P discharge max", None))
        self.labelCBuy.setText(QCoreApplication.translate("MainWindow", u"C buy", None))
        self.labelSeason.setText(QCoreApplication.translate("MainWindow", u"Season", None))
        self.labelLoadType.setText(QCoreApplication.translate("MainWindow", u"Load type", None))
        self.seasonType.setCurrentText("")
        self.labelSOCMin.setText(QCoreApplication.translate("MainWindow", u"SOC Min", None))
    # retranslateUi


    def simulatePV(self):
        P_nom = []
        for i in range(24):
            P_nom.append(self.p_charge_max.value() * max(0, math.sin(math.pi * (i-6) / 12)) * (random.randrange(70, 100) / 100))
        f2 = plt.figure()
        plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                 P_nom)
        plt.xlabel("Час доби", fontsize=16)
        plt.ylabel("Генерація, кВт", fontsize=16)
        plt.legend(['P_pv'])
        plt.title('Генерація', fontsize=20)
        plt.show()

    def optimize(self):
        N = 24
        SOC_initial = self.SOC_initial_value.value() / 100
        SOC_min = self.SOC_min_value.value() / 100
        SOC_max = self.SOC_max_value.value() / 100
        dt = 1
        E_bat = self.battery_capacity.value()
        P_charge_max = 5
        P_discharge_max = 5
        P_grid_max = 5.0
        c_buy = 50

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
            P_bat <= P_discharge_max,
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

        print("cost" + str(cost.value))
        plt.style.use('tableau-colorblind10')

        f1 = plt.figure()

        plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], SOC.value)

        plt.xlabel("Час доби", fontsize=16)
        plt.ylabel("Рівень заряду", fontsize=16)
        plt.legend(['N = ' + str(N)])
        plt.title('Рівень заряду батареї (SOC)', fontsize=20)
        plt.show()

        f2 = plt.figure()
        plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], P_pv.value,
                 P_load.value)
        plt.xlabel("Час доби", fontsize=16)
        plt.ylabel("Потужність, кВт", fontsize=16)
        plt.legend(['P_pv', 'P_load'])
        plt.title('Генерація/споживання', fontsize=20)
        plt.show()
