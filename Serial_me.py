import binascii
import sys
import time

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication

from Serialsetting import Ui_Form
from UI import Ui_MainWindow

import serial.tools.list_ports
import serial


class Serial_me(Ui_Form):
    listme = []
    ser = serial.Serial()

    def port_cheak(self):
        Com_List = []
        # 调用serial来检测电脑中存在的串口，将结果保存到List中
        port_list = list(serial.tools.list_ports.comports())
        ChildWindow.comboBox_2.clear()
        for port in port_list:
            Com_List.append(port[0])
            ChildWindow.comboBox_2.addItem(port[0])
        if len(Com_List) == 0:
            ChildWindow.comboBox_2.addItem("无可用串口")

    def port_open(self):
        # 从下拉选项中获取串口号
        self.ser.port = ChildWindow.comboBox_2.currentText()
        if ChildWindow.comboBox_2.currentText() == '无可用串口':
            window = QWidget()
            window.setWindowIcon(QIcon(":/ico/main.png"))
            reply = QMessageBox.warning(window, '警告', '串口配置出错！', QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Yes)
            return
        # 设置波特率
        self.ser.baudrate = int(ChildWindow.comboBox.currentText())
        # 设置数据位
        self.ser.bytesize = int(ChildWindow.comboBox_3.currentText())
        # 设置停止位
        self.ser.stopbits = int(ChildWindow.comboBox_4.currentText())
        # 设置校验位
        self.ser.parity = 'N'
        # 串口打开
        try:
            self.ser.open()
            if self.ser.isOpen():
                ChildWindow.stop = 0
        except BaseException:
            window = QWidget()
            window.setWindowIcon(QIcon(":/ico/main.png"))
            reply = QMessageBox.warning(window, '警告', '串口配置出错！', QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Yes)
        if self.ser.isOpen():
            for i in range(0, 16):
                self.ser.write(binascii.a2b_hex('690' + hex(i).split('x')[1] + '0000' + hex(i + 105).split('x')[1]))
                time.sleep(0.05)
            for i in range(16, 58):
                self.ser.write(binascii.a2b_hex('69' + hex(i).split('x')[1] + '0000' + hex(i + 105).split('x')[1]))
                time.sleep(0.05)

    def send_first(self):
        for i in range(0, 18):
            ba.listme.append(maa.model.item(i, 2).text())
        for i in range(0, 15):
            ba.listme.append(maa.model2.item(i, 2).text())
        for i in range(0, 16):
            ba.listme.append(maa.model3.item(i, 2).text())

    def port_close(self):
        # 设置变量进行提示
        self.ser.close()
        if self.ser.isOpen():
            self.label_4.setText("Not close")
        else:
            self.label_4.setText("Close")


app = QApplication(sys.argv)
ser = serial.Serial()
ChildWindow = Ui_Form()
Setui = QWidget()
ChildWindow.setupUi(Setui)
ba = Serial_me()
ba.port_cheak()
maa = Ui_MainWindow()
ChildWindow.pushButton.clicked.connect(Setui.hide)
ChildWindow.pushButton_2.clicked.connect(Setui.close)


import G_rc
