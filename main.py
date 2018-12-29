# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '串口界面.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import binascii
import sys, time
# import threading

import serial

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtGui import QStandardItem, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView

import serial.tools.list_ports


class Ui_MainWindow(object):
    ser = serial.Serial()
    stop = -1
    listme = []
    stopchange = -1
    getfirst = 0

    def setupUi(self, MainWindow):
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
        self.pushButton1.setGeometry(QtCore.QRect(0, 510, 70, 30))
        self.pushButton1.setObjectName("pushButton")
        self.pushButton1.setText('修改')
        self.pushButton1.setEnabled(False)

        self.pushButton2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton2.setGeometry(QtCore.QRect(0, 510, 70, 30))
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.setText('修改')
        self.pushButton2.setEnabled(False)

        self.pushButton3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton3.setGeometry(QtCore.QRect(0, 510, 70, 30))
        self.pushButton3.setObjectName("pushButton")
        self.pushButton3.setText('修改')
        self.pushButton3.setEnabled(False)

        self.pushButton4 = QtWidgets.QPushButton(self.tab)
        self.pushButton4.setGeometry(QtCore.QRect(0, 580, 70, 30))
        self.pushButton4.setObjectName("pushButton")
        self.pushButton4.setText('端口检测')

        self.pushButton5 = QtWidgets.QPushButton(self.tab)
        self.pushButton5.setGeometry(QtCore.QRect(0, 650, 70, 30))
        self.pushButton5.setObjectName("pushButton")
        self.pushButton5.setText('打开端口')
        self.pushButton5.setEnabled(False)

        # self.pushButton6 = QtWidgets.QPushButton(self.tab)
        # self.pushButton6.setGeometry(QtCore.QRect(80, 510, 80, 30))
        # self.pushButton6.setObjectName("pushButton")
        # self.pushButton6.setText('重新获取信息')
        # self.pushButton6.setEnabled(False)

        self.pushButton7 = QtWidgets.QPushButton(self.tab)
        self.pushButton7.setGeometry(QtCore.QRect(80, 650, 70, 30))
        self.pushButton7.setObjectName("pushButton")
        self.pushButton7.setText('关闭端口')
        self.pushButton7.setEnabled(False)

        self.model = QtGui.QStandardItemModel(self.tableView)
        self.model.setRowCount(10)
        self.model.setColumnCount(3)
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "序号")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "参数描述")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "数值")

        self.model2 = QtGui.QStandardItemModel(self.tableView2)
        self.model2.setRowCount(10)
        self.model2.setColumnCount(3)
        self.model2.setHeaderData(0, QtCore.Qt.Horizontal, "序号")
        self.model2.setHeaderData(1, QtCore.Qt.Horizontal, "参数描述")
        self.model2.setHeaderData(2, QtCore.Qt.Horizontal, "数值")

        self.model3 = QtGui.QStandardItemModel(self.tableView3)
        self.model3.setRowCount(10)
        self.model3.setColumnCount(3)
        self.model3.setHeaderData(0, QtCore.Qt.Horizontal, "序号")
        self.model3.setHeaderData(1, QtCore.Qt.Horizontal, "参数描述")
        self.model3.setHeaderData(2, QtCore.Qt.Horizontal, "数值")

        self.model4 = QtGui.QStandardItemModel(self.tableView4)
        self.model4.setRowCount(9)
        self.model4.setColumnCount(3)
        self.model4.setHeaderData(0, QtCore.Qt.Horizontal, "序号")
        self.model4.setHeaderData(1, QtCore.Qt.Horizontal, "参数描述")
        self.model4.setHeaderData(2, QtCore.Qt.Horizontal, "数值")

        self.lable = QtWidgets.QLabel(self.tab)
        self.lable.setObjectName('lable')
        self.lable.setText('请先检测端口')
        self.lable.setGeometry(QtCore.QRect(0, 620, 75, 22))

        self.comboBox_4 = QtWidgets.QComboBox(self.tab)
        self.comboBox_4.setGeometry(QtCore.QRect(0, 550, 70, 22))
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
        self.model.setItem(0, 1, QStandardItem('电机类型(0~3)'))
        self.model.setItem(1, 1, QStandardItem('电机额定功率(0~150.0KW)'))
        self.model.setItem(2, 1, QStandardItem('电机额定电压(0~400.0V)'))
        self.model.setItem(3, 1, QStandardItem('电机额定电流(10.0~600.0A)'))
        self.model.setItem(4, 1, QStandardItem('电机额定频率(10.0~300.0Hz)'))
        self.model.setItem(5, 1, QStandardItem('电机最大频率(10.0~400.0Hz)'))
        self.model.setItem(6, 1, QStandardItem('电机额定转速(100~6000rpm)'))
        self.model.setItem(7, 1, QStandardItem('最高转速限定(0~9000rpm)'))
        self.model.setItem(8, 1, QStandardItem('异步电机空载电流(15~45%电机额定电流)'))
        self.model.setItem(9, 1, QStandardItem('转子时间常数(0~10000)'))
        self.model.setItem(10, 1, QStandardItem('空载电流提升(0~50%电机额定电流)'))
        self.model.setItem(11, 1, QStandardItem('空载电流切换频率(1~50%电机额定频率)'))
        self.model.setItem(12, 1, QStandardItem('编码器每圈脉冲数(1~10000)'))
        self.model.setItem(13, 1, QStandardItem('编码器方向(0~1)'))
        self.model.setItem(14, 1, QStandardItem('同步电机磁极初始角度(0~360.0度)'))
        self.model.setItem(15, 1, QStandardItem('运行方向指示(0~3)'))
        self.model.setItem(16, 1, QStandardItem('保留1(0~32767)'))
        self.model.setItem(17, 1, QStandardItem('保留2(0~32767)'))

        for number in range(0, 15):
            self.model2.setItem(number, 0, QStandardItem('F' + str(number + 18)))
        self.model2.setItem(0, 1, QStandardItem('初始化速度(10~40000)'))
        self.model2.setItem(1, 1, QStandardItem('第二加速度(100~40000)'))
        self.model2.setItem(2, 1, QStandardItem('倒车加速度(100~40000)'))
        self.model2.setItem(3, 1, QStandardItem('减速度(10~40000)'))
        self.model2.setItem(4, 1, QStandardItem('刹车减速度(100~40000)'))
        self.model2.setItem(5, 1, QStandardItem('速度KP(100~40000)'))
        self.model2.setItem(6, 1, QStandardItem('速度KI(0~20000)'))
        self.model2.setItem(7, 1, QStandardItem('转折频率(0~电机额定频率)'))
        self.model2.setItem(8, 1, QStandardItem('转差频率限定(1.0~电机额定频率)'))
        self.model2.setItem(9, 1, QStandardItem('测速滤波系数(0~7)'))
        self.model2.setItem(10, 1, QStandardItem('启动位置自学习(0~7)'))
        self.model2.setItem(11, 1, QStandardItem('输出电流限定(0~600.0A)'))
        self.model2.setItem(12, 1, QStandardItem('定子电阻(0~32767)mΩ'))
        self.model2.setItem(13, 1, QStandardItem('保留1(0~32767)'))
        self.model2.setItem(14, 1, QStandardItem('保留2(0~32767)'))

        for number in range(0, 16):
            self.model3.setItem(number, 0, QStandardItem('F' + str(number + 33)))
        self.model3.setItem(0, 1, QStandardItem('转矩KP(100~40000)'))
        self.model3.setItem(1, 1, QStandardItem('转矩KI(0~20000)'))
        self.model3.setItem(2, 1, QStandardItem('激磁KP(100~40000)'))
        self.model3.setItem(3, 1, QStandardItem('激磁KI(0~20000)'))
        self.model3.setItem(4, 1, QStandardItem('驱动转矩限定(0~400%)'))
        self.model3.setItem(5, 1, QStandardItem('制动转矩限定(0~400%)'))
        self.model3.setItem(6, 1, QStandardItem('电压校正系数(90~110%)'))
        self.model3.setItem(7, 1, QStandardItem('电流矫正系数(50~200%)'))
        self.model3.setItem(8, 1, QStandardItem('欠压点设定(0~1000V)'))
        self.model3.setItem(9, 1, QStandardItem('过压点设定(0~1000V)'))
        self.model3.setItem(10, 1, QStandardItem('厂家参数1(0~65535)'))
        self.model3.setItem(11, 1, QStandardItem('控制模式选择(0~7)'))
        self.model3.setItem(12, 1, QStandardItem('高速转矩设定(0~400%)'))
        self.model3.setItem(13, 1, QStandardItem('保留1(0~32767)'))
        self.model3.setItem(14, 1, QStandardItem('保留2(0~32767)'))
        self.model3.setItem(15, 1, QStandardItem('保留3(0~32767)'))

        for number in range(0, 9):
            self.model4.setItem(number, 0, QStandardItem('F' + str(number + 49)))
        self.model4.setItem(0, 1, QStandardItem('输出电流'))
        self.model4.setItem(1, 1, QStandardItem('电机转速'))
        self.model4.setItem(2, 1, QStandardItem('控制器温度'))
        self.model4.setItem(3, 1, QStandardItem('电机温度'))
        self.model4.setItem(4, 1, QStandardItem('电池组电压'))
        self.model4.setItem(5, 1, QStandardItem('故障信息'))
        self.model4.setItem(6, 1, QStandardItem('保留1(0~32767)'))
        self.model4.setItem(7, 1, QStandardItem('保留2(0~32767)'))
        self.model4.setItem(8, 1, QStandardItem('保留3(0~32767)'))

        # 数据的行宽依据第二列自适应
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

        # 串口检测按钮
        self.pushButton4.clicked.connect(self.port_cheak)
        # 串口打开按钮
        self.pushButton5.clicked.connect(self.port_open)
        # 串口关闭按钮
        self.pushButton7.clicked.connect(self.port_close)
        # 数据修改发送按钮
        self.pushButton1.clicked.connect(self.changeover_model)

        self.pushButton2.clicked.connect(self.changeover_model2)
        self.pushButton3.clicked.connect(self.changeover_model3)

        # 读取串口接收信息进程
        self.thread = Mythread()
        # 信号发送，修改界面的消息
        self.thread._signal.connect(self.mabi)
        # 不断发送信息
        self.thread2 = Mythread_send()

        # self.thread3 = Mythread_change()
        #         # self.thread3._signal.connect(self.mabi)

    # 串口检测函数
    def port_cheak(self):
        Com_List = []
        # 调用serial来检测电脑中存在的串口，将结果保存到List中
        port_list = list(serial.tools.list_ports.comports())
        self.comboBox_4.clear()
        for port in port_list:
            Com_List.append(port[0])
            self.comboBox_4.addItem(port[0])
            self.lable.setText('查找到端口')
            # 将串口打开按钮和串口关闭按钮设置为可点击
            self.pushButton5.setEnabled(True)
            self.pushButton7.setEnabled(True)
        if len(Com_List) == 0:
            self.lable.setText("没查找到串口")

    # 串口打开函数
    def port_open(self):
        # 从下拉选项中获取串口号
        self.ser.port = self.comboBox_4.currentText()
        # 设置波特率
        self.ser.baudrate = int(9600)
        # 设置数据位
        self.ser.bytesize = int(8)
        # 设置停止位
        self.ser.stopbits = int(1)
        # 设置校验位
        self.ser.parity = 'N'
        # 串口打开
        self.ser.open()
        if self.ser.isOpen():
            Ui_MainWindow.stop = 0
            self.pushButton1.setEnabled(True)
            self.pushButton2.setEnabled(True)
            self.pushButton3.setEnabled(True)
            self.pushButton5.setEnabled(False)
            # self.pushButton6.setEnabled(True)
            self.lable.setText("端口打开成功")
            self.thread.start()
            self.send_data()
            self.thread2.start()
            time.sleep(1)

            # self.t1 = threading.Thread(target=self.receive_data)
            # self.t1.setDaemon(True)
            # self.t1.start()
        else:
            self.lable.setText("打开失败")

    # 根据接受的信息位置进行UI的输出定位
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

    # 端口关闭函数
    def port_close(self):
        # 设置变量进行提示
        Ui_MainWindow.stop = 1
        self.ser.close()
        if (self.ser.isOpen()):
            self.lable.setText("关闭失败")
        else:
            self.pushButton1.setEnabled(False)
            self.pushButton2.setEnabled(False)
            self.pushButton3.setEnabled(False)
            self.pushButton5.setEnabled(True)
            # self.pushButton6.setEnabled(False)
            self.lable.setText("关闭成功")

    # 以十六位发送信息，这是第一次的全部查询信息发送
    def send_data(self):
        if self.ser.isOpen():
            for i in range(0, 16):
                self.ser.write(binascii.a2b_hex('690' + hex(i).split('x')[1] + '0000' + hex(i + 105).split('x')[1]))
                time.sleep(0.05)
            for i in range(16, 58):
                self.ser.write(binascii.a2b_hex('69' + hex(i).split('x')[1] + '0000' + hex(i + 105).split('x')[1]))
                time.sleep(0.05)
            self.lable.setText("发送成功")
        else:
            self.lable.setText("发送失败")

    # 获取参数信息，保存到List中，用于后来的修改对比！！
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
        # self.thread3.start()
        for i in range(0, 18):
            if str(self.listme[i]) != str(self.model.item(i, 2).text()):
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
                        self.ser.write(binascii.a2b_hex('680' + hex(i).split('x')[1] + sas + hex(result % 255).split('x')[1]))
                        time.sleep(0.05)
                    else:
                        print(result)
                        self.ser.write(binascii.a2b_hex('68' + hex(i).split('x')[1] + sas + hex(result % 255).split('x')[1]))
                        time.sleep(0.05)
        Ui_MainWindow.stopchange = 1
        self.thread.start()
        self.thread2.start()

    def changeover_model2(self):
        result = 0
        Ui_MainWindow.stop = 1
        Ui_MainWindow.stopchange = 0
        # self.thread3.start()
        for i in range(0, 15):
            if str(self.listme[i + 18]) != str(self.model2.item(i, 2).text()):
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
                    self.ser.write(binascii.a2b_hex('68' + hex(i + 18).split('x')[1] + sas + hex(result % 255).split('x')[1]))
                    time.sleep(0.05)
        Ui_MainWindow.stopchange = 1
        self.thread.start()
        self.thread2.start()

    def changeover_model3(self):
        result = 0
        Ui_MainWindow.stop = 1
        Ui_MainWindow.stopchange = 0
        # self.thread3.start()
        for i in range(0, 16):
            if str(self.listme[i + 33] != self.model3.item(i, 2).text()):
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
                    self.ser.write(binascii.a2b_hex('68' + hex(i+33).split('x')[1] + sas + hex(result % 255).split('x')[1]))
                    time.sleep(0.05)
        Ui_MainWindow.stopchange = 1
        self.thread.start()
        self.thread2.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "信息查看"))
        MainWindow.setWindowIcon(QIcon('./ico/main.png'))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "数据回显F0~F17"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "数据回显F18~F32"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "数据回显F33~F48"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "数据回显F49~F57"))
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
    # 定义信号,定义参数为str类型
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
                                self._signal.emit(str(int(balala, 16)), where)
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
        print('发送线程启动')

    def run(self):
        # self.ser.write(binascii.a2b_hex('690500006E'))
        while (True):
            for i in range(49, 58):
                if (Ui_MainWindow.stop is 0):
                    self.ser.write(binascii.a2b_hex('69' + hex(i).split('x')[1] + '0000' + hex(i + 105).split('x')[1]))
                    time.sleep(0.1)
                else:
                    self.quit()


# class Mythread_change(QThread, Ui_MainWindow):
#     _signal = pyqtSignal(str, int)
#
#     def __init__(self):
#         super(Mythread_change, self).__init__()
#         print('接受线程启动')
#
#     def run(self):
#         num = 0
#         where = 0
#         status = 0
#         balala = ''
#         while (True):
#             if Ui_MainWindow.stopchange is 0:
#                 size = self.ser.inWaiting()
#                 if size:
#                     res_data = self.ser.read_all()
#                     if str(binascii.b2a_hex(res_data).decode()) == '58':
#                         status = 1
#                     if status == 1:
#                         num += 1
#                         if num == 2:
#                             where = int(binascii.b2a_hex(res_data).decode(), 16)
#                         if num == 3 or num == 4:
#                             balala += binascii.b2a_hex(res_data).decode()
#                         if num == 5:
#                             print(str(int(balala, 16)))
#                             self._signal.emit(str(int(balala, 16)), where)
#                             balala = ''
#                             num = 0
#                             status = 0
#                     self.ser.flushInput()
#             else:
#                 self.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    Form = QMainWindow()
    MainWindow.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
