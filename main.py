import binascii
import sys
import time

import serial
import serial.tools.list_ports
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QStandardItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QHeaderView

from Serialsetting import Ui_Form
from UI import Ui_MainWindow
from info import Ui_Info



class Thread_send(QThread):
    _signal = pyqtSignal()

    def __init__(self):
        super(Thread_send, self).__init__()
        print('发送线程启动')

    def run(self):
        while True:
            for i in range(49, 58):
                if MainWindow.stop is 0:
                    ser.write(binascii.a2b_hex('69' + hex(i).split('x')[1] + '0000' + hex(i + 105).split('x')[1]))
                    time.sleep(0.1)
                else:
                    self.quit()


class Thread_receive(QThread):
    # 定义信号,定义参数为str类型
    _signal = pyqtSignal(str, int)

    def __init__(self):
        super(Thread_receive, self).__init__()

    def run(self):
        print("The receive_data threading is start")
        balala = ''
        res_data = ''
        num = 0
        nums = 0
        status = 0
        where = 0
        firststart = 0
        while True:
            if MainWindow.stop is 0:
                size = ser.inWaiting()
                if size and nums < 58 and firststart == 0:
                    res_data = ser.read_all()
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
                    ser.flushInput()
                if size and nums >= 58:
                    firststart = 1
                    res_data = ser.read_all()
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
                            balala = ''
                            num = 0
                            nums += 1
                            if nums > 66:
                                nums = 58
                            status = 0
                    ser.flushInput()
            else:
                self.quit()


if __name__ == '__main__':
    def port_cheak():
        Com_List = []
        # 调用serial来检测电脑中存在的串口，将结果保存到List中
        port_list = list(serial.tools.list_ports.comports())
        ChildWindow.comboBox_2.clear()
        for port in port_list:
            Com_List.append(port[0])
            ChildWindow.comboBox_2.addItem(port[0])
        if len(Com_List) == 0:
            ChildWindow.comboBox_2.addItem("无可用串口")


    def port_open():
        # 从下拉选项中获取串口号
        ser.port = ChildWindow.comboBox_2.currentText()
        if ChildWindow.comboBox_2.currentText() == '无可用串口':
            window = QWidget()
            window.setWindowIcon(QIcon(":/ico/main.png"))
            reply = QMessageBox.warning(window, '警告', '串口配置出错！', QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Yes)
            return
        # 设置波特率
        ser.baudrate = int(ChildWindow.comboBox.currentText())
        # 设置数据位
        ser.bytesize = int(ChildWindow.comboBox_3.currentText())
        # 设置停止位
        ser.stopbits = int(ChildWindow.comboBox_4.currentText())
        # 设置校验位
        ser.parity = 'N'
        # 串口打开
        try:
            ser.open()
            if ser.isOpen():
                MainWindow.stop = 0
                MainWindow.label_4.setText("Open")
                MainWindow.toolButton.setEnabled(False)
                MainWindow.toolButton_2.setEnabled(True)
                MainWindow.toolButton_4.setEnabled(True)
                MainWindow.label_3.show()
                Receiveme.start()
                send_data()
                Sendal.start()
        except BaseException:
            window = QWidget()
            window.setWindowIcon(QIcon(":/ico/main.png"))
            reply = QMessageBox.warning(window, '警告', '串口配置出错！', QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Yes)
        if ser.isOpen():
            for i in range(0, 16):
                ser.write(binascii.a2b_hex('690' + hex(i).split('x')[1] + '0000' + hex(i + 105).split('x')[1]))
                time.sleep(0.05)
            for i in range(16, 58):
                ser.write(binascii.a2b_hex('69' + hex(i).split('x')[1] + '0000' + hex(i + 105).split('x')[1]))
                time.sleep(0.05)


    def send_first():
        for i in range(0, 18):
            MainWindow.listme.append(MainWindow.model.item(i, 2).text())
        for i in range(0, 15):
            MainWindow.listme.append(MainWindow.model2.item(i, 2).text())
        for i in range(0, 16):
            MainWindow.listme.append(MainWindow.model3.item(i, 2).text())


    def port_close():
        # 设置变量进行提示
        MainWindow.stop = 1
        ser.close()
        if ser.isOpen():
            MainWindow.label_4.setText("Not close")
        else:
            MainWindow.label_4.setText("Close")
            MainWindow.toolButton.setEnabled(True)
            MainWindow.toolButton_2.setEnabled(False)
            MainWindow.toolButton_4.setEnabled(False)
            MainWindow.label_3.hide()


    def mabi(li, nums):
        if nums < 18:
            MainWindow.model.setItem(nums, 2, QStandardItem(li))
        elif 18 <= nums < 33:
            MainWindow.model2.setItem(nums - 18, 2, QStandardItem(li))
        elif 33 <= nums < 49:
            MainWindow.model3.setItem(nums - 33, 2, QStandardItem(li))
        elif 49 <= nums < 58:
            MainWindow.model4.setItem(nums - 49, 2, QStandardItem(li))
            if nums == 57:
                if MainWindow.getfirst == 0:
                    send_first()
                    MainWindow.getfirst = 1
        elif 58 <= nums:
            MainWindow.model4.setItem(nums - 58, 2, QStandardItem(li))


    def send_data():
        if ser.isOpen():
            for i in range(0, 16):
                ser.write(binascii.a2b_hex('690' + hex(i).split('x')[1] + '0000' + hex(i + 105).split('x')[1]))
                time.sleep(0.05)
            for i in range(16, 58):
                ser.write(binascii.a2b_hex('69' + hex(i).split('x')[1] + '0000' + hex(i + 105).split('x')[1]))
                time.sleep(0.05)
            MainWindow.label_4.setText("发送成功")
        else:
            MainWindow.label_4.setText("发送失败")


    def changeover_model():
        result = 0
        MainWindow.stop = 1
        MainWindow.stopchange = 0
        for i in range(0, 18):
            if str(MainWindow.listme[i]) != str(MainWindow.model.item(i, 2).text()):
                if int(MainWindow.model.item(i, 2).text()) > int(MainWindow.js['limit'][i]['max']) or int(
                        MainWindow.model.item(i, 2).text()) < int(MainWindow.js['limit'][i]['min']):
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle('提示')
                    msgBox.setText('抱歉，您输入的参数存在错误！！！\n请修正后再次输入！')
                    msgBox.setWindowIcon(QIcon(':/ico/main.png'))
                    msgBox.addButton(QMessageBox.Ok)
                    msgBox.exec_()  # 模态对话框
                    MainWindow.model.setItem(i, 2, QStandardItem(str(MainWindow.listme[i])))
                    return
                if ser.isOpen():
                    if (int(MainWindow.model.item(i, 2).text())) <= 16:
                        sas = '000' + hex(int(MainWindow.model.item(i, 2).text())).split('x')[1]
                    elif 16 < (int(MainWindow.model.item(i, 2).text())) <= 255:
                        sas = '00' + hex(int(MainWindow.model.item(i, 2).text())).split('x')[1]
                    elif 255 < (int(MainWindow.model.item(i, 2).text())) <= 4095:
                        sas = '0' + hex(int(MainWindow.model.item(i, 2).text())).split('x')[1]
                    elif (int(MainWindow.model.item(i, 2).text())) > 4095:
                        sas = hex(int(MainWindow.model.item(i, 2).text())).split('x')[1]
                    result = int('68', 16) + int(hex(i), 16) + int(sas[:2], 16) + int(sas[2:], 16)
                    if i < 16:
                        if int(hex(result % 255).split('x')[1], 16) > 16:
                            ser.write(
                                binascii.a2b_hex('680' + hex(i).split('x')[1] + sas + hex(result % 255).split('x')[1]))
                        else:
                            ser.write(
                                binascii.a2b_hex(
                                    '680' + hex(i).split('x')[1] + sas + '0' + hex(result % 255).split('x')[1]))
                        time.sleep(0.05)
                    else:
                        if int(hex(result % 255).split('x')[1], 16) > 16:
                            ser.write(
                                binascii.a2b_hex('68' + hex(i).split('x')[1] + sas + hex(result % 255).split('x')[1]))
                        else:
                            ser.write(
                                binascii.a2b_hex(
                                    '68' + hex(i).split('x')[1] + sas + '0' + hex(result % 255).split('x')[1]))
                        time.sleep(0.05)
        MainWindow.stop = 0
        MainWindow.stopchange = 1
        Receiveme.start()
        Sendal.start()


    def changeover_model2():
        result = 0
        MainWindow.stop = 1
        MainWindow.stopchange = 0
        for i in range(0, 15):
            if str(MainWindow.listme[i + 18]) != str(MainWindow.model2.item(i, 2).text()):
                if int(MainWindow.model2.item(i, 2).text()) > int(MainWindow.js['limit'][i + 18]['max']) or int(
                        MainWindow.model2.item(i, 2).text()) < int(MainWindow.js['limit'][i + 18]['min']):
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle('提示')
                    msgBox.setText('抱歉，您输入的参数存在错误！！！\n请修正后再次输入！')
                    msgBox.setWindowIcon(QIcon(':/ico/main.png'))
                    msgBox.addButton(QMessageBox.Ok)
                    msgBox.exec_()  # 模态对话框
                    MainWindow.model2.setItem(i, 2, QStandardItem(str(MainWindow.listme[i + 18])))
                    return
                if ser.isOpen():
                    if (int(MainWindow.model2.item(i, 2).text())) <= 16:
                        sas = '000' + hex(int(MainWindow.model2.item(i, 2).text())).split('x')[1]
                    elif 16 < (int(MainWindow.model2.item(i, 2).text())) <= 255:
                        sas = '00' + hex(int(MainWindow.model2.item(i, 2).text())).split('x')[1]
                    elif 255 < (int(MainWindow.model2.item(i, 2).text())) <= 4095:
                        sas = '0' + hex(int(MainWindow.model2.item(i, 2).text())).split('x')[1]
                    elif (int(MainWindow.model2.item(i, 2).text())) > 4095:
                        sas = hex(int(MainWindow.model2.item(i, 2).text())).split('x')[1]
                    result = int('68', 16) + int(hex(i + 18), 16) + int(sas[:2], 16) + int(sas[2:], 16)
                    if int(hex(result % 255).split('x')[1], 16) > 16:
                        ser.write(
                            binascii.a2b_hex('68' + hex(i + 18).split('x')[1] + sas + hex(result % 255).split('x')[1]))
                    else:
                        ser.write(
                            binascii.a2b_hex(
                                '68' + hex(i + 18).split('x')[1] + sas + '0' + hex(result % 255).split('x')[1]))
                    time.sleep(0.05)
        MainWindow.stop = 0
        MainWindow.stopchange = 1
        Receiveme.start()
        Sendal.start()


    def changeover_model3():
        result = 0
        MainWindow.stop = 1
        MainWindow.stopchange = 0
        for i in range(0, 16):
            print(i)
            print(i + 33)
            if str(MainWindow.listme[i + 33]) != str(MainWindow.model3.item(i, 2).text()):
                if int(MainWindow.model3.item(i, 2).text()) > int(MainWindow.js['limit'][i + 33]['max']) or int(
                        MainWindow.model3.item(i, 2).text()) < int(MainWindow.js['limit'][i + 33]['min']):
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle('提示')
                    msgBox.setText('抱歉，您输入的参数存在错误！！！\n请修正后再次输入！')
                    msgBox.setWindowIcon(QIcon(':/ico/main.png'))
                    msgBox.addButton(QMessageBox.Ok)
                    msgBox.exec_()  # 模态对话框
                    MainWindow.model3.setItem(i, 2, QStandardItem(str(MainWindow.listme[i + 33])))
                    return
                if ser.isOpen():
                    if (int(MainWindow.model3.item(i, 2).text())) <= 16:
                        sas = '000' + hex(int(MainWindow.model3.item(i, 2).text())).split('x')[1]
                    elif 16 < (int(MainWindow.model3.item(i, 2).text())) <= 255:
                        sas = '00' + hex(int(MainWindow.model3.item(i, 2).text())).split('x')[1]
                    elif 255 < (int(MainWindow.model3.item(i, 2).text())) <= 4095:
                        sas = '0' + hex(int(MainWindow.model3.item(i, 2).text())).split('x')[1]
                    elif (int(MainWindow.model3.item(i, 2).text())) > 4095:
                        sas = hex(int(MainWindow.model3.item(i, 2).text())).split('x')[1]
                    result = int('68', 16) + int(hex(i + 33), 16) + int(sas[:2], 16) + int(sas[2:], 16)
                    if int(hex(result % 255).split('x')[1], 16) > 16:
                        ser.write(
                            binascii.a2b_hex('68' + hex(i + 33).split('x')[1] + sas + hex(result % 255).split('x')[1]))
                        print('68' + hex(i + 33).split('x')[1] + sas + hex(result % 255).split('x')[1])
                    else:
                        ser.write(
                            binascii.a2b_hex(
                                '68' + hex(i + 33).split('x')[1] + sas + '0' + hex(result % 255).split('x')[1]))
                        print('68' + hex(i + 33).split('x')[1] + sas + '0' + hex(result % 255).split('x')[1])
                    time.sleep(0.05)
        MainWindow.stop = 0
        MainWindow.stopchange = 1
        Receiveme.start()
        Sendal.start()


    def changeover_where():
        changeover_model()
        changeover_model2()
        changeover_model3()


    def Tranla():
        if MainWindow.Tranl == 0:
            MainWindow.label_4.setText("Success")
            MainWindow.toolButton.setText("Connect")
            MainWindow.toolButton_2.setText("Disconnect")
            MainWindow.toolButton_3.setText("Settings")
            MainWindow.toolButton_4.setText("Send")
            MainWindow.toolButton_5.setText("About")
            MainWindow.toolButton_6.setText("中文")
            ChildWindow.label.setText("Serial Port Baud Rate：")
            ChildWindow.label_2.setText("Serial port number：")
            ChildWindow.label_3.setText("Data bits：")
            ChildWindow.label_4.setText("Stop bit：")
            ChildWindow.pushButton.setText("Sure")
            ChildWindow.pushButton_2.setText("Cancle")
            for number in range(0, 18):
                MainWindow.model.setItem(number, 0, QStandardItem('F' + str(number)))
            MainWindow.model.setItem(0, 1, QStandardItem('Motor type(0~3)'))
            MainWindow.model.setItem(1, 1, QStandardItem('Motor rated power (0~150.0KW)'))
            MainWindow.model.setItem(2, 1, QStandardItem('Motor rated voltage (0~400.0V)'))
            MainWindow.model.setItem(3, 1, QStandardItem('Motor rated current (10.0~600.0A)'))
            MainWindow.model.setItem(4, 1, QStandardItem('motor rated frequency (10.0~300.0Hz)'))
            MainWindow.model.setItem(5, 1, QStandardItem('Motor maximum frequency (10.0~400.0Hz)'))
            MainWindow.model.setItem(6, 1, QStandardItem('motor rated speed (100~6000rpm)'))
            MainWindow.model.setItem(7, 1, QStandardItem('Maximum speed limit (0~9000rpm)'))
            MainWindow.model.setItem(8, 1,
                                     QStandardItem('Asynchronous motor no-load current (15~45% motor rated current)'))
            MainWindow.model.setItem(9, 1, QStandardItem('Rotor time constant (0~10000)'))
            MainWindow.model.setItem(10, 1, QStandardItem('No-load current boost (0~50% motor rated current)'))
            MainWindow.model.setItem(11, 1,
                                     QStandardItem('No-load current switching frequency (1~50% motor rated frequency)'))
            MainWindow.model.setItem(12, 1, QStandardItem('Encoder number of pulses per revolution (1~10000)'))
            MainWindow.model.setItem(13, 1, QStandardItem('Encoder Direction (0~1)'))
            MainWindow.model.setItem(14, 1, QStandardItem('Synchronous motor pole initial angle (0~360.0 degrees)'))
            MainWindow.model.setItem(15, 1, QStandardItem('Run Direction Direction (0~3)'))
            MainWindow.model.setItem(16, 1, QStandardItem('Reserved 1(0~32767)'))
            MainWindow.model.setItem(17, 1, QStandardItem('Keep 2(0~32767)'))

            for number in range(0, 15):
                MainWindow.model2.setItem(number, 0, QStandardItem('F' + str(number + 18)))
            MainWindow.model2.setItem(0, 1, QStandardItem('Initialization speed (10~40000)'))
            MainWindow.model2.setItem(1, 1, QStandardItem('Second Acceleration (100~40000)'))
            MainWindow.model2.setItem(2, 1, QStandardItem('Reversing acceleration (100~40000)'))
            MainWindow.model2.setItem(3, 1, QStandardItem('Deceleration (10~40000)'))
            MainWindow.model2.setItem(4, 1, QStandardItem('Brake deceleration (100~40000)'))
            MainWindow.model2.setItem(5, 1, QStandardItem('Speed KP(100~40000)'))
            MainWindow.model2.setItem(6, 1, QStandardItem('Speed KI(0~20000)'))
            MainWindow.model2.setItem(7, 1, QStandardItem('Turning frequency (0~ motor rated frequency)'))
            MainWindow.model2.setItem(8, 1, QStandardItem('Slip frequency limit (1.0~ motor rated frequency)'))
            MainWindow.model2.setItem(9, 1, QStandardItem('Speed measurement filter coefficient (0~7)'))
            MainWindow.model2.setItem(10, 1, QStandardItem('Start position MainWindow-learning (0~7)'))
            MainWindow.model2.setItem(11, 1, QStandardItem('Output current limit (0~600.0A)'))
            MainWindow.model2.setItem(12, 1, QStandardItem('Stator resistance (0~32767)mΩ'))
            MainWindow.model2.setItem(13, 1, QStandardItem('Reserved 1(0~32767)'))
            MainWindow.model2.setItem(14, 1, QStandardItem('Keep 2(0~32767)'))

            for number in range(0, 16):
                MainWindow.model3.setItem(number, 0, QStandardItem('F' + str(number + 33)))
            MainWindow.model3.setItem(0, 1, QStandardItem('Torque KP(100~40000)'))
            MainWindow.model3.setItem(1, 1, QStandardItem('Torque KI(0~20000)'))
            MainWindow.model3.setItem(2, 1, QStandardItem('Exciting KP(100~40000)'))
            MainWindow.model3.setItem(3, 1, QStandardItem('Exciting KI(0~20000)'))
            MainWindow.model3.setItem(4, 1, QStandardItem('Drive torque limit (0~400%)'))
            MainWindow.model3.setItem(5, 1, QStandardItem('Brake torque limit (0~400%)'))
            MainWindow.model3.setItem(6, 1, QStandardItem('Voltage correction factor (90~110%)'))
            MainWindow.model3.setItem(7, 1, QStandardItem('Current correction coefficient (50~200%)'))
            MainWindow.model3.setItem(8, 1, QStandardItem('Undervoltage point setting (0~1000V)'))
            MainWindow.model3.setItem(9, 1, QStandardItem('Overvoltage point setting (0~1000V)'))
            MainWindow.model3.setItem(10, 1, QStandardItem('Manufacturer parameter 1(0~65535)'))
            MainWindow.model3.setItem(11, 1, QStandardItem('Control mode selection (0~7)'))
            MainWindow.model3.setItem(12, 1, QStandardItem('High Speed ​​Torque Setting (0~400%)'))
            MainWindow.model3.setItem(13, 1, QStandardItem('Reserved 1(0~32767)'))
            MainWindow.model3.setItem(14, 1, QStandardItem('Keep 2(0~32767)'))
            MainWindow.model3.setItem(15, 1, QStandardItem('Keep 3(0~32767)'))

            for number in range(0, 9):
                MainWindow.model4.setItem(number, 0, QStandardItem('F' + str(number + 49)))
            MainWindow.model4.setItem(0, 1, QStandardItem('Output current'))
            MainWindow.model4.setItem(1, 1, QStandardItem('Motor speed'))
            MainWindow.model4.setItem(2, 1, QStandardItem('Controller Temperature'))
            MainWindow.model4.setItem(3, 1, QStandardItem('Motor temperature'))
            MainWindow.model4.setItem(4, 1, QStandardItem('Battery pack voltage'))
            MainWindow.model4.setItem(5, 1, QStandardItem('Fault information'))
            MainWindow.model4.setItem(6, 1, QStandardItem('Last fault information(0~32767)'))
            MainWindow.model4.setItem(7, 1, QStandardItem('Keep 2(0~32767)'))
            MainWindow.model4.setItem(8, 1, QStandardItem('Keep 3(0~32767)'))
            MainWindow.Tranl = 1
        else:
            MainWindow.label_4.setText("读取成功")
            MainWindow.toolButton.setText("连接")
            MainWindow.toolButton_2.setText("断开")
            MainWindow.toolButton_3.setText("配置")
            MainWindow.toolButton_4.setText("修改")
            MainWindow.toolButton_5.setText("关于")
            MainWindow.toolButton_6.setText("ENG")
            ChildWindow.label.setText("串口波特率：")
            ChildWindow.label_2.setText("串口号：")
            ChildWindow.label_3.setText("数据位：")
            ChildWindow.label_4.setText("停止位：")
            ChildWindow.pushButton.setText("确定")
            ChildWindow.pushButton_2.setText("取消")
            for number in range(0, 18):
                MainWindow.model.setItem(number, 0, QStandardItem('F' + str(number)))
            MainWindow.model.setItem(0, 1, QStandardItem('电机类型(0~3)'))
            MainWindow.model.setItem(1, 1, QStandardItem('电机额定功率(0~150.0KW)'))
            MainWindow.model.setItem(2, 1, QStandardItem('电机额定电压(0~400.0V)'))
            MainWindow.model.setItem(3, 1, QStandardItem('电机额定电流(10.0~600.0A)'))
            MainWindow.model.setItem(4, 1, QStandardItem('电机额定频率(10.0~300.0Hz)'))
            MainWindow.model.setItem(5, 1, QStandardItem('电机最大频率(10.0~400.0Hz)'))
            MainWindow.model.setItem(6, 1, QStandardItem('电机额定转速(100~6000rpm)'))
            MainWindow.model.setItem(7, 1, QStandardItem('最高转速限定(0~9000rpm)'))
            MainWindow.model.setItem(8, 1, QStandardItem('异步电机空载电流(15~45%电机额定电流)'))
            MainWindow.model.setItem(9, 1, QStandardItem('转子时间常数(0~10000)'))
            MainWindow.model.setItem(10, 1, QStandardItem('空载电流提升(0~50%电机额定电流)'))
            MainWindow.model.setItem(11, 1, QStandardItem('空载电流切换频率(1~50%电机额定频率)'))
            MainWindow.model.setItem(12, 1, QStandardItem('编码器每圈脉冲数(1~10000)'))
            MainWindow.model.setItem(13, 1, QStandardItem('编码器方向(0~1)'))
            MainWindow.model.setItem(14, 1, QStandardItem('同步电机磁极初始角度(0~360.0度)'))
            MainWindow.model.setItem(15, 1, QStandardItem('运行方向指示(0~3)'))
            MainWindow.model.setItem(16, 1, QStandardItem('保留1(0~32767)'))
            MainWindow.model.setItem(17, 1, QStandardItem('保留2(0~32767)'))

            for number in range(0, 15):
                MainWindow.model2.setItem(number, 0, QStandardItem('F' + str(number + 18)))
            MainWindow.model2.setItem(0, 1, QStandardItem('初始化速度(10~40000)'))
            MainWindow.model2.setItem(1, 1, QStandardItem('第二加速度(100~40000)'))
            MainWindow.model2.setItem(2, 1, QStandardItem('倒车加速度(100~40000)'))
            MainWindow.model2.setItem(3, 1, QStandardItem('减速度(10~40000)'))
            MainWindow.model2.setItem(4, 1, QStandardItem('刹车减速度(100~40000)'))
            MainWindow.model2.setItem(5, 1, QStandardItem('速度KP(100~40000)'))
            MainWindow.model2.setItem(6, 1, QStandardItem('速度KI(0~20000)'))
            MainWindow.model2.setItem(7, 1, QStandardItem('转折频率(0~电机额定频率)'))
            MainWindow.model2.setItem(8, 1, QStandardItem('转差频率限定(1.0~电机额定频率)'))
            MainWindow.model2.setItem(9, 1, QStandardItem('测速滤波系数(0~7)'))
            MainWindow.model2.setItem(10, 1, QStandardItem('启动位置自学习(0~7)'))
            MainWindow.model2.setItem(11, 1, QStandardItem('输出电流限定(0~600.0A)'))
            MainWindow.model2.setItem(12, 1, QStandardItem('定子电阻(0~32767)mΩ'))
            MainWindow.model2.setItem(13, 1, QStandardItem('保留1(0~32767)'))
            MainWindow.model2.setItem(14, 1, QStandardItem('保留2(0~32767)'))

            for number in range(0, 16):
                MainWindow.model3.setItem(number, 0, QStandardItem('F' + str(number + 33)))
            MainWindow.model3.setItem(0, 1, QStandardItem('转矩KP(100~40000)'))
            MainWindow.model3.setItem(1, 1, QStandardItem('转矩KI(0~20000)'))
            MainWindow.model3.setItem(2, 1, QStandardItem('激磁KP(100~40000)'))
            MainWindow.model3.setItem(3, 1, QStandardItem('激磁KI(0~20000)'))
            MainWindow.model3.setItem(4, 1, QStandardItem('驱动转矩限定(0~400%)'))
            MainWindow.model3.setItem(5, 1, QStandardItem('制动转矩限定(0~400%)'))
            MainWindow.model3.setItem(6, 1, QStandardItem('电压校正系数(90~110%)'))
            MainWindow.model3.setItem(7, 1, QStandardItem('电流矫正系数(50~200%)'))
            MainWindow.model3.setItem(8, 1, QStandardItem('欠压点设定(0~1000V)'))
            MainWindow.model3.setItem(9, 1, QStandardItem('过压点设定(0~1000V)'))
            MainWindow.model3.setItem(10, 1, QStandardItem('厂家参数1(0~65535)'))
            MainWindow.model3.setItem(11, 1, QStandardItem('控制模式选择(0~7)'))
            MainWindow.model3.setItem(12, 1, QStandardItem('高速转矩设定(0~400%)'))
            MainWindow.model3.setItem(13, 1, QStandardItem('保留1(0~32767)'))
            MainWindow.model3.setItem(14, 1, QStandardItem('保留2(0~32767)'))
            MainWindow.model3.setItem(15, 1, QStandardItem('保留3(0~32767)'))

            for number in range(0, 9):
                MainWindow.model4.setItem(number, 0, QStandardItem('F' + str(number + 49)))
            MainWindow.model4.setItem(0, 1, QStandardItem('输出电流'))
            MainWindow.model4.setItem(1, 1, QStandardItem('电机转速'))
            MainWindow.model4.setItem(2, 1, QStandardItem('控制器温度'))
            MainWindow.model4.setItem(3, 1, QStandardItem('电机温度'))
            MainWindow.model4.setItem(4, 1, QStandardItem('电池组电压'))
            MainWindow.model4.setItem(5, 1, QStandardItem('故障信息'))
            MainWindow.model4.setItem(6, 1, QStandardItem('保留1(0~32767)'))
            MainWindow.model4.setItem(7, 1, QStandardItem('保留2(0~32767)'))
            MainWindow.model4.setItem(8, 1, QStandardItem('保留3(0~32767)'))
            MainWindow.tableView.setModel(MainWindow.model)
            MainWindow.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            MainWindow.tableView.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
            MainWindow.tableView.verticalHeader().setVisible(False)
            MainWindow.tableView_2.setModel(MainWindow.model2)
            MainWindow.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            MainWindow.tableView_2.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
            MainWindow.tableView_2.verticalHeader().setVisible(False)
            MainWindow.tableView_3.setModel(MainWindow.model3)
            MainWindow.tableView_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            MainWindow.tableView_3.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
            MainWindow.tableView_3.verticalHeader().setVisible(False)
            MainWindow.tableView_4.setModel(MainWindow.model4)
            MainWindow.tableView_4.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            MainWindow.tableView_4.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
            MainWindow.tableView_4.verticalHeader().setVisible(False)
            MainWindow.Tranl = 0


    app = QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    Mainui = QMainWindow()
    MainWindow.setupUi(Mainui)
    Mainui.show()
    MainWindow.toolButton_2.setEnabled(False)
    MainWindow.toolButton_4.setEnabled(False)
    ser = serial.Serial()
    ChildWindow = Ui_Form()
    Setui = QWidget()
    Info = Ui_Info()
    Infow = QWidget()
    ChildWindow.setupUi(Setui)
    Info.setupUi(Infow)
    port_cheak()
    Receiveme = Thread_receive()
    Receiveme._signal.connect(mabi)
    Sendal = Thread_send()
    ChildWindow.pushButton.clicked.connect(Setui.hide)
    ChildWindow.pushButton_2.clicked.connect(Setui.close)
    MainWindow.toolButton_3.clicked.connect(Setui.show)
    MainWindow.toolButton.clicked.connect(port_open)
    MainWindow.toolButton_2.clicked.connect(port_close)
    MainWindow.toolButton_4.clicked.connect(changeover_where)
    MainWindow.toolButton_6.clicked.connect(Tranla)
    MainWindow.toolButton_5.clicked.connect(Infow.show)
    sys.exit(app.exec_())

