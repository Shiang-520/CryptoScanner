# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstLayout.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, QUrl
import threading
#from FirstLayout import Ui_MainWindow
from binance.client import Client
from binance.enums import Enum

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Crypto Scanner")
        MainWindow.resize(600, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 580, 580))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setIconSize(QtCore.QSize(16, 16))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.ScanButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ScanButton.setFont(font)
        self.ScanButton.setIconSize(QtCore.QSize(16, 16))
        self.ScanButton.setObjectName("ScanButton")
        self.horizontalLayout_2.addWidget(self.ScanButton)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayout_3.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 476, 18))
        self.menubar.setObjectName("menubar")
        self.menuKey_Management = QtWidgets.QMenu(self.menubar)
        self.menuKey_Management.setObjectName("menuKey_Management")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.menuKey_Management.addAction(self.actionNew)
        self.menuKey_Management.addAction(self.actionDelete)
        self.menubar.addAction(self.menuKey_Management.menuAction())
        self.menuKey_Management.setEnabled(False)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Crypto Scanner"))
        self.label.setText(_translate("MainWindow", "Time Frame:"))
        self.comboBox.setCurrentText(_translate("MainWindow", "4H"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1H"))
        self.comboBox.setItemText(1, _translate("MainWindow", "4H"))
        self.ScanButton.setText(_translate("MainWindow", "SCAN"))
        #self.progressBar.setFormat(_translate("MainWindow", "%p"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Pair Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Close"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "SMA30"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "SMA45"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "SMA60"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Stage"))
        #self.tableWidget.resizeColumnsToContents()
        self.menuKey_Management.setTitle(_translate("MainWindow", "Key Management"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))

class ScanThread(QThread):
    progress_updated = pyqtSignal(int)
    progress_data = pyqtSignal(list)

    def __init__(self, client, period):
        super().__init__()
        self.is_Running = True
        self.period = period
        self.client = client

    def run(self):
        symbol_info = self.client.get_exchange_info()['symbols']

        index = 0
        count = len(symbol_info)

        for s in symbol_info:
            PairName = s['symbol']
            if 'USDT' in PairName:
                #print (PairName)
                historicalData = self.client.get_historical_klines(PairName, self.period, "11 day ago UTC")
                if len(historicalData) < 61:
                    index += 1
                    continue

                [close, sma30, sma45, sma60, sma30_1, sma45_1, sma60_1] = self.ComputeSMA(historicalData, self.period)
                stage = self.ComputeStage([sma30, sma45, sma60, sma30_1, sma45_1, sma60_1], close)

                if stage > 0:
                    data = [PairName, close, sma30, sma45, sma60, stage]
                    self.progress_data.emit(data)

            index += 1
            percentage = int((index * 100) / count)
            #print (index, count, percentage, PairName)
            self.progress_updated.emit(percentage)
        self.is_Running = False

    def stop(self):
        self.is_Running = False

    
    def ComputeSMA(self, historicalData, period):
        result = [0, 0, 0, 0, 0, 0]
        sma30 = 0
        sma45 = 0
        sma60 = 0
        datacount = len(historicalData)

        smaCount = 0
        for i in range(datacount-2, 0, -1):
            close = float(historicalData[i][4])
            if smaCount < 30:
                sma30 += close
            elif smaCount < 45:
                sma45 += close
            elif smaCount < 60:
                sma60 += close
            else:
                break
            smaCount += 1

        sma45 += sma30
        sma60 += sma45

        result[0] = round(sma30/30, 6)
        result[1] = round(sma45/45, 6)
        result[2] = round(sma60/60, 6)

        sma30 = 0
        sma45 = 0
        sma60 = 0
        smaCount = 0
        for i in range(datacount-3, 0, -1):
            close = float(historicalData[i][4])
            if smaCount < 30:
                sma30 += close
            elif smaCount < 45:
                sma45 += close
            elif smaCount < 60:
                sma60 += close
            else:
                break
            smaCount += 1
        sma45 += sma30
        sma60 += sma45

        result[3] = round(sma30/30, 6)
        result[4] = round(sma45/45, 6)
        result[5] = round(sma60/60, 6)
        #print (result[0], result[1], result[2], result[3], result[4], result[5])
        return (round(float(historicalData[datacount-1][4]), 6), result[0], result[1], result[2], result[3], result[4], result[5])

    def ComputeStage(self, sma, close):
        stage = 0
        sma30_curr = sma[0]
        sma45_curr = sma[1]
        sma60_curr = sma[2]
        sma30_prev = sma[3]
        sma45_prev = sma[4]
        sma60_prev = sma[5]

        #print (close, sma30_curr, sma45_curr, sma60_curr, sma30_prev, sma45_prev, sma60_prev)
        if close > sma30_curr and close > sma45_curr and close > sma60_curr:
            stage = 1
            if close > sma30_prev and close > sma45_prev and close > sma60_prev:
                stage = 2

        return stage

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()

        self.ScanWorker = None
        self.ui.setupUi(self)
        self.ui.ScanButton.clicked.connect(self.ScanBtnClicked)

        api_key = "xxx"
        api_secret = "xxx"
        self.client = Client(api_key, api_secret)

    def ScanBtnClicked(self):
        self.ui.progressBar.setValue(0)
        self.ui.ScanButton.setEnabled(False)

        if self.ui.comboBox.currentText() == '4H':
            period = Client.KLINE_INTERVAL_4HOUR
        elif self.ui.comboBox.currentText() == '1H':
            period = Client.KLINE_INTERVAL_1HOUR
        else:
            period = Client.KLINE_INTERVAL_4HOUR

        self.ScanWorker = ScanThread(self.client, period)
        self.ScanWorker.progress_data.connect(self.update_table)
        self.ScanWorker.progress_updated.connect(self.update_progress)
        self.ScanWorker.start()

        self.ui.tableWidget.cellDoubleClicked.connect(self.on_table_double_click)

    def update_progress(self, progress):
        self.ui.progressBar.setValue(progress)
        if progress >= 99:
            self.ui.ScanButton.setEnabled(True)
            self.ui.progressBar.setValue(100)
            #self.ui.label.setText("Done!")

    def update_table(self, data):
        #print (data)
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)
        for i in range(0, 6, 1):
            item = QtWidgets.QTableWidgetItem(str(data[i]))
            self.ui.tableWidget.setItem(row, i, item)
            Font = item.font()
            Font.setPointSize(8)
            item.setFont(Font)
        self.ui.tableWidget.resizeColumnsToContents()
    
    def on_table_double_click(self, row, column):
        item = self.ui.tableWidget.item(row, 0)
        link = "https://www.tradingview.com/chart/?symbol=BINANCE:" + item.text()
        QtGui.QDesktopServices.openUrl(QUrl(link))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())