# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Serial interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import binascii
import json
import sys, time

import serial

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtGui import QStandardItem, QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QMessageBox

import serial.tools.list_ports


class Ui_MainWindow(object):
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    ser = serial.Serial()
    stop = -1
    listme = []
    stopchange = -1
    getfirst = 0
    js = json.load(open('./limit.json'))

    def setupUi(self, MainWindow):
        self._translate = QtCore.QCoreApplication.translate
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 730)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 600, 730))
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab_1")
        self.tabWidget.addTab(self.tab, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_4, "")

        self.tableView = QtWidgets.QTableView(self.tab)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 600, 500))
        self.tableView.setObjectName("tableView")

        self.tableView2 = QtWidgets.QTableView(self.tab_2)
        self.tableView2.setGeometry(QtCore.QRect(0, 0, 600, 500))
        self.tableView2.setObjectName("tableView2")

        self.tableView3 = QtWidgets.QTableView(self.tab_3)
        self.tableView3.setGeometry(QtCore.QRect(0, 0, 600, 500))
        self.tableView3.setObjectName("tableView3")

        self.tableView4 = QtWidgets.QTableView(self.tab_4)
        self.tableView4.setGeometry(QtCore.QRect(0, 0, 600, 300))
        self.tableView4.setObjectName("tableView4")

        self.pushButton1 = QtWidgets.QPushButton(self.tab)
        self.pushButton1.setGeometry(QtCore.QRect(0, 510, 160, 30))
        self.pushButton1.setObjectName("pushButton")
        self.pushButton1.setText("send modification")
        self.pushButton1.setFont(self.font)
        self.pushButton1.setIcon(QIcon('./ico/send.png'))
        self.pushButton1.setEnabled(False)

        self.pushButton2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton2.setGeometry(QtCore.QRect(0, 510, 160, 30))
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.setText("send modification")
        self.pushButton2.setFont(self.font)
        self.pushButton2.setIcon(QIcon('./ico/send.png'))
        self.pushButton2.setEnabled(False)

        self.pushButton3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton3.setGeometry(QtCore.QRect(0, 510, 160, 30))
        self.pushButton3.setObjectName("pushButton")
        self.pushButton3.setText('send modify')
        self.pushButton3.setFont(self.font)
        self.pushButton3.setIcon(QIcon('./ico/send.png'))
        self.pushButton3.setEnabled(False)

        self.pushButton4 = QtWidgets.QPushButton(self.tab)
        self.pushButton4.setGeometry(QtCore.QRect(180, 510, 180, 30))
        self.pushButton4.setObjectName("pushButton")
        self.pushButton4.setFont(self.font)
        self.pushButton4.setIcon(QIcon('./ico/detect.png'))
        self.pushButton4.setText('serial port detection')

        self.pushButton5 = QtWidgets.QPushButton(self.tab)
        self.pushButton5.setGeometry(QtCore.QRect(0, 550, 160, 30))
        self.pushButton5.setObjectName("pushButton")
        self.pushButton5.setText('open serial port')
        self.pushButton5.setFont(self.font)
        self.pushButton5.setIcon(QIcon('./ico/connection.png'))
        self.pushButton5.setEnabled(False)

        self.pushButton7 = QtWidgets.QPushButton(self.tab)
        self.pushButton7.setGeometry(QtCore.QRect(180, 550, 180, 30))
        self.pushButton7.setObjectName("pushButton")
        self.pushButton7.setText('close serial port')
        self.pushButton7.setFont(self.font)
        self.pushButton7.setIcon(QIcon('./ico/disconnected.png'))
        self.pushButton7.setEnabled(False)

        self.advertisement = QtWidgets.QLabel(self.tab)
        self.advertisement.setPixmap(QPixmap('./ico/advertisement.png').scaledToHeight(90))
        self.advertisement.setGeometry(QtCore.QRect(55, 560, 400, 200))

        self.model = QtGui.QStandardItemModel(self.tableView)
        self.model.setRowCount(10)
        self.model.setColumnCount(3)
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "serial number")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Parameter Description")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Value")

        self.model2 = QtGui.QStandardItemModel(self.tableView2)
        self.model2.setRowCount(10)
        self.model2.setColumnCount(3)
        self.model2.setHeaderData(0, QtCore.Qt.Horizontal, "serial number")
        self.model2.setHeaderData(1, QtCore.Qt.Horizontal, "Parameter Description")
        self.model2.setHeaderData(2, QtCore.Qt.Horizontal, "Value")

        self.model3 = QtGui.QStandardItemModel(self.tableView3)
        self.model3.setRowCount(10)
        self.model3.setColumnCount(3)
        self.model3.setHeaderData(0, QtCore.Qt.Horizontal, "serial number")
        self.model3.setHeaderData(1, QtCore.Qt.Horizontal, "Parameter Description")
        self.model3.setHeaderData(2, QtCore.Qt.Horizontal, "Value")

        self.model4 = QtGui.QStandardItemModel(self.tableView4)
        self.model4.setRowCount(9)
        self.model4.setColumnCount(3)
        self.model4.setHeaderData(0, QtCore.Qt.Horizontal, "serial number")
        self.model4.setHeaderData(1, QtCore.Qt.Horizontal, "Parameter Description")
        self.model4.setHeaderData(2, QtCore.Qt.Horizontal, "Value")

        self.lable = QtWidgets.QLabel(self.tab)
        self.lable.setObjectName('lable')
        self.lable.setText('Please check the serial port first')
        self.lable.setFont(self.font)
        self.lable.setAlignment(QtCore.Qt.AlignCenter)
        self.lable.setGeometry(QtCore.QRect(180, 590, 250, 22))

        self.comboBox_4 = QtWidgets.QComboBox(self.tab)
        self.comboBox_4.setGeometry(QtCore.QRect(0, 590, 160, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")

        for number in range(0, 18):
            self.model.setItem(number, 0, QStandardItem('F' + str(number)))
        self.model.setItem(0, 1, QStandardItem('motor type(0~3)'))
        self.model.setItem(1, 1, QStandardItem('Motor rated power (0~150.0KW)'))
        self.model.setItem(2, 1, QStandardItem('Motor rated voltage (0~400.0V)'))
        self.model.setItem(3, 1, QStandardItem('Motor rated current (10.0~600.0A)'))
        self.model.setItem(4, 1, QStandardItem('motor rated frequency (10.0~300.0Hz)'))
        self.model.setItem(5, 1, QStandardItem('Motor maximum frequency (10.0~400.0Hz)'))
        self.model.setItem(6, 1, QStandardItem('motor rated speed (100~6000rpm)'))
        self.model.setItem(7, 1, QStandardItem('Maximum speed limit (0~9000rpm)'))
        self.model.setItem(8, 1, QStandardItem('Asynchronous motor no-load current (15~45% motor rated current)'))
        self.model.setItem(9, 1, QStandardItem('rotor time constant (0~10000)'))
        self.model.setItem(10, 1, QStandardItem('No-load current boost (0~50% motor rated current)'))
        self.model.setItem(11, 1, QStandardItem('No-load current switching frequency (1~50% motor rated frequency)'))
        self.model.setItem(12, 1, QStandardItem('Encoder number of pulses per revolution (1~10000)'))
        self.model.setItem(13, 1, QStandardItem('Encoder Direction (0~1)'))
        self.model.setItem(14, 1, QStandardItem('synchronous motor pole initial angle (0~360.0 degrees)'))
        self.model.setItem(15, 1, QStandardItem('Run Direction Direction (0~3)'))
        self.model.setItem(16, 1, QStandardItem('Reserved 1(0~32767)'))
        self.model.setItem(17, 1, QStandardItem('Keep 2(0~32767)'))

        for number in range(0, 15):
            self.model2.setItem(number, 0, QStandardItem('F' + str(number + 18)))
        self.model2.setItem(0, 1, QStandardItem('initialization speed (10~40000)'))
        self.model2.setItem(1, 1, QStandardItem('Second Acceleration (100~40000)'))
        self.model2.setItem(2, 1, QStandardItem('Reversing acceleration (100~40000)'))
        self.model2.setItem(3, 1, QStandardItem('Deceleration (10~40000)'))
        self.model2.setItem(4, 1, QStandardItem('Brake deceleration (100~40000)'))
        self.model2.setItem(5, 1, QStandardItem('Speed ​​KP(100~40000)'))
        self.model2.setItem(6, 1, QStandardItem('Speed ​​KI(0~20000)'))
        self.model2.setItem(7, 1, QStandardItem(' turning frequency (0~ motor rated frequency)'))
        self.model2.setItem(8, 1, QStandardItem('slip frequency limit (1.0~ motor rated frequency)'))
        self.model2.setItem(9, 1, QStandardItem('speed measurement filter coefficient (0~7)'))
        self.model2.setItem(10, 1, QStandardItem('Start position self-learning (0~7)'))
        self.model2.setItem(11, 1, QStandardItem('output current limit (0~600.0A)'))
        self.model2.setItem(12, 1, QStandardItem('stator resistance (0~32767)mΩ'))
        self.model2.setItem(13, 1, QStandardItem('reserved 1(0~32767)'))
        self.model2.setItem(14, 1, QStandardItem('Keep 2(0~32767)'))

        for number in range(0, 16):
            self.model3.setItem(number, 0, QStandardItem('F' + str(number + 33)))
        self.model3.setItem(0, 1, QStandardItem('torque KP(100~40000)'))
        self.model3.setItem(1, 1, QStandardItem('torque KI(0~20000)'))
        self.model3.setItem(2, 1, QStandardItem('Exciting KP(100~40000)'))
        self.model3.setItem(3, 1, QStandardItem('Exciting KI(0~20000)'))
        self.model3.setItem(4, 1, QStandardItem('drive torque limit (0~400%)'))
        self.model3.setItem(5, 1, QStandardItem('Brake torque limit (0~400%)'))
        self.model3.setItem(6, 1, QStandardItem('voltage correction factor (90~110%)'))
        self.model3.setItem(7, 1, QStandardItem('current correction coefficient (50~200%)'))
        self.model3.setItem(8, 1, QStandardItem('Undervoltage point setting (0~1000V)'))
        self.model3.setItem(9, 1, QStandardItem('overvoltage point setting (0~1000V)'))
        self.model3.setItem(10, 1, QStandardItem('manufacturer parameter 1(0~65535)'))
        self.model3.setItem(11, 1, QStandardItem('Control mode selection (0~7)'))
        self.model3.setItem(12, 1, QStandardItem('High Speed ​​Torque Setting (0~400%)'))
        self.model3.setItem(13, 1, QStandardItem('reserved 1(0~32767)'))
        self.model3.setItem(14, 1, QStandardItem('Keep 2(0~32767)'))
        self.model3.setItem(15, 1, QStandardItem('Keep 3(0~32767)'))

        for number in range(0, 9):
            self.model4.setItem(number, 0, QStandardItem('F' + str(number + 49)))
        self.model4.setItem(0, 1, QStandardItem('output current'))
        self.model4.setItem(1, 1, QStandardItem('motor speed'))
        self.model4.setItem(2, 1, QStandardItem('Controller Temperature'))
        self.model4.setItem(3, 1, QStandardItem('motor temperature'))
        self.model4.setItem(4, 1, QStandardItem('battery pack voltage'))
        self.model4.setItem(5, 1, QStandardItem('fault information'))
        self.model4.setItem(6, 1, QStandardItem('Reserved 1(0~32767)'))
        self.model4.setItem(7, 1, QStandardItem('Keep 2(0~32767)'))
        self.model4.setItem(8, 1, QStandardItem('Keep 3(0~32767)'))

        # Data line width is based on the second column adaptive
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tableView.verticalHeader().setVisible(False)

        self.tableView2.setModel(self.model2)
        self.tableView2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView2.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tableView2.verticalHeader().setVisible(False)

        self.tableView3.setModel(self.model3)
        self.tableView3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView3.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tableView3.verticalHeader().setVisible(False)

        self.tableView4.setModel(self.model4)
        self.tableView4.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView4.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tableView4.verticalHeader().setVisible(False)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Serial detection button
        self.pushButton4.clicked.connect(self.port_cheak)
        # Serial open button
        self.pushButton5.clicked.connect(self.port_open)
        # Serial off button
        self.pushButton7.clicked.connect(self.port_close)
        # Data modification send button
        self.pushButton1.clicked.connect(self.changeover_model)

        self.pushButton2.clicked.connect(self.changeover_model2)
        self.pushButton3.clicked.connect(self.changeover_model3)

        # Read the serial port receiving information process
        self.thread = Mythread()
        # 信号送, modify the interface message
        self.thread._signal.connect(self.mabi)
        # Continuously send information
        self.thread2 = Mythread_send()

    # Serial port detection function
    def port_cheak(self):
        com_List = []
        # Call serial to detect the serial port existing in the computer and save the result to the List.
        port_list = list(serial.tools.list_ports.comports())
        self.comboBox_4.clear()
        for port in port_list:
            com_List.append(port[0])
            self.comboBox_4.addItem(port[0])
            self.lable.setText('find to port')
            # Set the serial port open button and serial port close button to be clickable
            self.pushButton5.setEnabled(True)
            self.pushButton7.setEnabled(True)
        if len(com_List) == 0:
            self.lable.setText("Not found to serial port")

    # Serial open function
    def port_open(self):
        # Get the serial port number from the drop-down option
        self.ser.port = self.comboBox_4.currentText()
        # Set the baud rate
        self.ser.baudrate = int(9600)
        # 设置数据位
        self.ser.bytesize = int(8)
        # Set stop bit
        self.ser.stopbits = int(1)
        # Set check digit
        self.ser.parity = 'N'
        # Serial open
        self.ser.open()
        if self.ser.isOpen():
            Ui_MainWindow.stop = 0
            self.pushButton1.setEnabled(True)
            self.pushButton2.setEnabled(True)
            self.pushButton3.setEnabled(True)
            self.pushButton5.setEnabled(False)
            # self.pushButton6.setEnabled(True)
            self.lable.setText("Port opened successfully")
            self.thread.start()
            self.send_data()
            self.thread2.start()
        else:
            self.lable.setText("open failed")

    # Output UI positioning based on the accepted information location
    def mabi(self, li, nums):
        if nums < 18:
            self.model.setItem(nums, 2, QStandardItem(li))
        elif 18 <= nums < 33:
            self.model2.setItem(nums - 18, 2, QStandardItem(li))
        elif 33 <= nums < 49:
            self.model3.setItem(nums - 33, 2, QStandardItem(li))
        elif 49 <= nums < 58:
            self.model4.setItem(nums - 49, 2, QStandardItem(li))
            if nums == 57:
                if self.getfirst == 0:
                    self.send_first()
                    self.getfirst = 1
        elif 58 <= nums:
            self.model4.setItem(nums - 58, 2, QStandardItem(li))

    # Close function
    def port_close(self):
        # set variables to prompt
        Ui_MainWindow.stop = 1
        self.ser.close()
        if self.ser.isOpen():
            self.lable.setText("close failed")
        else:
            self.pushButton1.setEnabled(False)
            self.pushButton2.setEnabled(False)
            self.pushButton3.setEnabled(False)
            self.pushButton5.setEnabled(True)
            self.lable.setText("closed successfully")

    # Send information by 16 bits, this is the first time all the information is sent.
    def send_data(self):
        if self.ser.isOpen():
            for i in range(0, 16):
                self.ser.write(binascii.a2b_hex('690' + hex(i).split('x')[1] + '0000' + hex(i + 105).split('x')[1]))
                time.sleep(0.05)
            for i in range(16, 58):
                self.ser.write(binascii.a2b_hex('69' + hex(i).split('x')[1] + '0000' + hex(i + 105).split('x')[1]))
                time.sleep(0.05)
            self.lable.setText("send success")
        else:
            self.lable.setText("send failed")

    # Get the parameter information and save it to the List for later modification and comparison! !
    def send_first(self):
        for i in range(0, 18):
            self.listme.append(self.model.item(i, 2).text())
        for i in range(0, 15):
            self.listme.append(self.model2.item(i, 2).text())
        for i in range(0, 16):
            self.listme.append(self.model3.item(i, 2).text())

    def changeover_model(self):
        result = 0
        Ui_MainWindow.stop = 1
        Ui_MainWindow.stopchange = 0
        for i in range(0, 18):
            if str(self.listme[i]) != str(self.model.item(i, 2).text()):
                if int(self.model.item(i, 2).text()) > int(self.js['limit'][i]['max']) or int(self.model.item(i, 2).text()) < int(self.js['limit'][i]['min']):
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle('Tip')
                    msgBox.setText('Sorry, the parameter you entered is wrong!!! \nPlease correct it and enter it again!')
                    msgBox.setWindowIcon(QIcon('./ico/main.png'))
                    msgBox.addButton(QMessageBox.Ok)
                    msgBox.exec_()  # modal dialog box
                    self.model.setItem(i, 2, QStandardItem(str(self.listme[i])))
                    return
                if self.ser.isOpen():
                    if (int(self.model.item(i, 2).text())) <= 16:
                        sas = '000' + hex(int(self.model.item(i, 2).text())).split('x')[1]
                    elif 16 < (int(self.model.item(i, 2).text())) <= 255:
                        sas = '00' + hex(int(self.model.item(i, 2).text())).split('x')[1]
                    elif 255 < (int(self.model.item(i, 2).text())) <= 4095:
                        sas = '0' + hex(int(self.model.item(i, 2).text())).split('x')[1]
                    elif (int(self.model.item(i, 2).text())) > 4095:
                        sas = hex(int(self.model.item(i, 2).text())).split('x')[1]
                    result = int('68', 16) + int(hex(i), 16) + int(sas[:2], 16) + int(sas[2:], 16)
                    if i < 16:
                        self.ser.write(
                            binascii.a2b_hex('680' + hex(i).split('x')[1] + sas + hex(result % 255).split('x')[1]))
                        time.sleep(0.05)
                    else:
                        print(result)
                        self.ser.write(
                            binascii.a2b_hex('68' + hex(i).split('x')[1] + sas + hex(result % 255).split('x')[1]))
                        time.sleep(0.05)
        Ui_MainWindow.stopchange = 1
        self.thread.start()
        self.thread2.start()

    def changeover_model2(self):
        result = 0
        Ui_MainWindow.stop = 1
        Ui_MainWindow.stopchange = 0
        for i in range(0, 15):
            if str(self.listme[i + 18]) != str(self.model2.item(i, 2).text()):
                if int(self.model.item(i, 2).text()) > int(self.js['limit'][i+18]['max']) or int(self.model.item(i, 2).text()) < int(self.js['limit'][i+18]['min']):
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle('Tip')
                    msgBox.setText('Sorry, the parameter you entered is wrong!!! \nPlease correct it and enter it again!')
                    msgBox.setWindowIcon(QIcon('./ico/main.png'))
                    msgBox.addButton(QMessageBox.Ok)
                    msgBox.exec_()  # modal dialog box
                    self.model.setItem(i, 2, QStandardItem(str(self.listme[i+18])))
                    return
                if self.ser.isOpen():
                    if (int(self.model2.item(i, 2).text())) <= 16:
                        sas = '000' + hex(int(self.model2.item(i, 2).text())).split('x')[1]
                    elif 16 < (int(self.model2.item(i, 2).text())) <= 255:
                        sas = '00' + hex(int(self.model2.item(i, 2).text())).split('x')[1]
                    elif 255 < (int(self.model2.item(i, 2).text())) <= 4095:
                        sas = '0' + hex(int(self.model2.item(i, 2).text())).split('x')[1]
                    elif (int(self.model2.item(i, 2).text())) > 4095:
                        sas = hex(int(self.model2.item(i, 2).text())).split('x')[1]
                    result = int('68', 16) + int(hex(i + 18), 16) + int(sas[:2], 16) + int(sas[2:], 16)
                    self.ser.write(
                        binascii.a2b_hex('68' + hex(i + 18).split('x')[1] + sas + hex(result % 255).split('x')[1]))
                    time.sleep(0.05)
        Ui_MainWindow.stopchange = 1
        self.thread.start()
        self.thread2.start()

    def changeover_model3(self):
        result = 0
        Ui_MainWindow.stop = 1
        Ui_MainWindow.stopchange = 0
        for i in range(0, 16):
            if str(self.listme[i + 33] != self.model3.item(i, 2).text()):
                if int(self.model.item(i, 2).text()) > int(self.js['limit'][i+33]['max']) or int(self.model.item(i, 2).text()) < int(self.js['limit'][i+33]['min']):
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle('Tip')
                    msgBox.setText('Sorry, the parameter you entered is wrong!!! \nPlease correct it and enter it again!')
                    msgBox.setWindowIcon(QIcon('./ico/main.png'))
                    msgBox.addButton(QMessageBox.Ok)
                    msgBox.exec_()  # modal dialog box
                    self.model.setItem(i, 2, QStandardItem(str(self.listme[i+33])))
                    return
                if self.ser.isOpen():
                    if (int(self.model3.item(i, 2).text())) <= 16:
                        sas = '000' + hex(int(self.model3.item(i, 2).text())).split('x')[1]
                    elif 16 < (int(self.model3.item(i, 2).text())) <= 255:
                        sas = '00' + hex(int(self.model3.item(i, 2).text())).split('x')[1]
                    elif 255 < (int(self.model3.item(i, 2).text())) <= 4095:
                        sas = '0' + hex(int(self.model3.item(i, 2).text())).split('x')[1]
                    elif (int(self.model3.item(i, 2).text())) > 4095:
                        sas = hex(int(self.model3.item(i, 2).text())).split('x')[1]
                    result = int('68', 16) + int(hex(i + 33), 16) + int(sas[:2], 16) + int(sas[2:], 16)
                    self.ser.write(
                        binascii.a2b_hex('68' + hex(i + 33).split('x')[1] + sas + hex(result % 255).split('x')[1]))
                    time.sleep(0.05)
        Ui_MainWindow.stopchange = 1
        self.thread.start()
        self.thread2.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jackos Control debugging software"))
        MainWindow.setWindowIcon(QIcon('./ico/main.png'))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Motor Parameters"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Control Parameter One"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Control Parameter 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "real-time status"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "COM1"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "COM2"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "COM3"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "COM4"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "COM5"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "COM6"))
        self.comboBox_4.setItemText(6, _translate("MainWindow", "COM7"))
        self.comboBox_4.setItemText(7, _translate("MainWindow", "COM8"))
        self.comboBox_4.setItemText(8, _translate("MainWindow", "COM9"))
        self.comboBox_4.setItemText(9, _translate("MainWindow", "COM10"))


class Mythread(QThread, Ui_MainWindow):
    # define the signal, define the parameter as str type
    _signal = pyqtSignal(str, int)

    def __init__(self):
        super(Mythread, self).__init__()

    def run(self):
        print("The receive_data threading is start")
        balala = ''
        res_data = ''
        num = 0
        nums = 0
        status = 0
        where = 0
        firststart = 0
        while (True):
            if (Ui_MainWindow.stop is 0):
                size = self.ser.inWaiting()
                if size and nums < 58 and firststart == 0:
                    res_data = self.ser.read_all()
                    if str(binascii.b2a_hex(res_data).decode()) == '59':
                        status = 1
                    if status == 1:
                        num += 1
                        if num == 2:
                            where = int(binascii.b2a_hex(res_data).decode(), 16)
                        if num == 3 or num == 4:
                            balala += binascii.b2a_hex(res_data).decode()
                        if num == 5:
                            self._signal.emit(str(int(balala, 16)), where)
                            balala = ''
                            num = 0
                            nums += 1
                            status = 0
                    self.ser.flushInput()
                if size and nums >= 58:
                    firststart = 1
                    res_data = self.ser.read_all()
                    if str(binascii.b2a_hex(res_data).decode()) == '59':
                        status = 1
                    if status == 1:
                        num += 1
                        if num == 2:
                            where = int(binascii.b2a_hex(res_data).decode(), 16)
                        if num == 3 or num == 4:
                            balala += binascii.b2a_hex(res_data).decode()
                        if num == 5:
                            if int(balala, 16) < 10000 and where >= 49:
                                self._signal.emit(str(int(balala, 16) * 0.1), where)
                                print(where)
                            balala = ''
                            num = 0
                            nums += 1
                            if nums > 66:
                                nums = 58
                            status = 0
                    self.ser.flushInput()
            else:
                self.quit()


class Mythread_send(QThread, Ui_MainWindow):
    _signal = pyqtSignal()

    def __init__(self):
        super(Mythread_send, self).__init__()
        print('send thread start')

    def run(self):
        while (True):
            for i in range(49, 58):
                if (Ui_MainWindow.stop is 0):
                    self.ser.write(binascii.a2b_hex('69' + hex(i).split('x')[1] + '0000' + hex(i + 105).split('x')[1]))
                    time.sleep(0.1)
                else:
                    self.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    form = QMainWindow()
    MainWindow.setupUi(form)
    form.show()
    sys.exit(app.exec_())
