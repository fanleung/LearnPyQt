import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.QtCore import QTimer
from ui_server import Ui_Form
import socket
import threading
import stopThreading
import datetime
import os

class Pyqt5_Serial(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(Pyqt5_Serial, self).__init__()
        self.setupUi(self)
        self.init()
        self.setWindowTitle("TCP 服务端")

        self.sock = None
        self.sockState = None
        self.server_thread = None
        self.client_socket_list = list()

    def init(self):
        # 获取本地IP
        self.socket_connect_button_2.clicked.connect(self.getLocalIP)

        # 开启服务器
        self.socket_connect_button.clicked.connect(self.socket_connect)

        # 关闭服务器
        self.socket_disconnect_button.clicked.connect(self.socket_disconnect)

        # 发送数据按钮
        self.data_send_button.clicked.connect(self.data_send)

        # 清除发送窗口
        self.send_clear_button.clicked.connect(self.send_data_clear)

        # 清除接收窗口
        self.rece_clear_button.clicked.connect(self.receive_data_clear)

        # 保存接收文件
        self.rece_clear_button_2.clicked.connect(self.save_receive)

        # 打开文本文件
        self.send_clear_button_2.clicked.connect(self.openFile)

        # 定时器发送数据
        self.timer_send = QTimer(self)
        self.timer_send.timeout.connect(self.data_send)
        self.hex_send_2.stateChanged.connect(self.data_send_timer)

        # 测试
        self.lineEdit.setText("127.0.0.1")
        self.lineEdit_2.setText("1234")

    # 获取本机ip
    def getLocalIP(self):
        myaddr = socket.gethostbyname(socket.getfqdn(socket.gethostname()))
        self.lineEdit.setText(myaddr)

    # 开启服务器
    def socket_connect(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 绑定地址和端口
            self.sock.bind(('127.0.0.1', int(self.lineEdit_2.text())))
            # 监听端口，传入的参数指定等待连接的最大数量
            self.sock.listen(5)
            # 取消主动断开连接四次握手后的TIME_WAIT状态
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # 设定套接字为非阻塞式
            self.sock.setblocking(False)
        except OSError as e:
            print(e)
            QMessageBox.critical(self, "Port Error", "失败，请检查！")
            return None

        except ConnectionRefusedError as e:
            print(e)
            QMessageBox.critical(self, "Port Error", "失败，请检查！")
            return None

        self.socket_connect_button.setEnabled(False)
        self.socket_disconnect_button.setEnabled(True)
        self.formGroupBox.setTitle("TCP 服务配置   (已开启)")
        self.sockState = True

        # 创建线程接收数据
        self.server_thread = threading.Thread(target=self.data_receive)
        self.server_thread.start()

    # 关闭服务端
    def socket_disconnect(self):
        stopThreading.stop_thread(self.server_thread)
        try:
            self.sock.shutdown(2)
            self.sock.close()
        except:
            pass
        self.socket_connect_button.setEnabled(True)
        self.socket_disconnect_button.setEnabled(False)
        self.formGroupBox.setTitle("TCP 客户端配置   (已关闭)")
        self.sock.close()
        self.sockState = False

    # 发送数据
    def data_send(self):
        if self.sockState:
            input_s = self.s3__send_text.toPlainText()
            if input_s != "":
                # 非空字符串
                if self.hex_send.isChecked():
                    # hex发送
                    input_s = input_s.strip()
                    send_list = []
                    while input_s != '':
                        try:
                            num = int(input_s[0:2], 16)
                        except ValueError:
                            QMessageBox.critical(self, 'wrong data', '请输入十六进制数据，以空格分开!')
                            return None
                        input_s = input_s[2:].strip()
                        send_list.append(num)
                    input_s = bytes(send_list)
                    for client, address in self.client_socket_list:
                        client.send(input_s)

                else:
                    # ascii发送
                    input_s = (input_s + '\r\n')
                    for client, address in self.client_socket_list:
                        client.send(input_s.encode('gb2312'))
        else:
            pass

    # 接收数据
    def data_receive(self):
        while True:
            try:
                client_socket, client_address = self.sock.accept()
            except Exception as e:
                pass
            else:
                client_socket.setblocking(False)

                self.client_socket_list.append((client_socket, client_address))

            for client, address in self.client_socket_list:
                try:
                    data = client.recv(1024)
                except Exception as e:
                    pass
                else:
                    if data:
                        # hex显示
                        if self.hex_receive.checkState():
                            out_s = ''
                            for i in range(0, len(data)):
                                out_s = out_s + '{:02X}'.format(data[i]) + ' '
                            # self.s2__receive_text.insertPlainText(out_s)
                            self.s2__receive_text.append("[{}] 来自IP:{} 端口:{}\n{}".format(self.getCurrentTimeString(), address[0], address[1], out_s))

                        else:
                            # 串口接收到的字符串为b'123',要转化成unicode字符串才能输出到窗口中去
                            self.s2__receive_text.append("[{}] 来自IP:{} 端口:{}\n{}".format(self.getCurrentTimeString(), address[0], address[1], data.decode('gb2312', 'ignore')))
                            # 使用 insertPlainText 的话可能会导致CPU使用率过大
                            # self.s2__receive_text.insertPlainText(data)
                            pass

                        # 获取到text光标
                        textCursor = self.s2__receive_text.textCursor()
                        # 滚动到底部
                        textCursor.movePosition(textCursor.End)
                        # 设置光标到text中去
                        self.s2__receive_text.setTextCursor(textCursor)
                    else:
                        client.close()
                        self.client_socket_list.remove((client, address))

    # 定时发送数据
    def data_send_timer(self):
        if self.hex_send_2.isChecked():
            self.timer_send.start(int(self.lineEdit_3.text()))
            self.lineEdit_3.setEnabled(False)
        else:
            self.timer_send.stop()
            self.lineEdit_3.setEnabled(True)


    # 清除发送显示
    def send_data_clear(self):
        self.s3__send_text.setText("")

    # 清除接收显示
    def receive_data_clear(self):
        self.s2__receive_text.setText("")

    def getCurrentTimeString(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # 保存文件
    def save_receive(self):
        if os.path.exists("server_receive.txt"):
            os.remove("server_receive.txt")
        file = open("server_receive.txt", 'w')
        # 获取接收的数据
        file.write(self.s2__receive_text.toPlainText())
        file.close()

        QMessageBox.information(self, "提示", "已保存在 server_receive.txt 文件！")

    # 打开文件
    def openFile(self):
        # 打开文本
        fname = QFileDialog.getOpenFileName(self, 'Open file')
        if os.path.splitext(fname[0])[1] == '.txt':
            file = open(fname[0])
            self.s3__send_text.setText(file.read())
        else:
            # 提示不支持此文件格式
            QMessageBox.information(self, "提示", "当前仅支持.txt文件")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = Pyqt5_Serial()
    myshow.show()
    sys.exit(app.exec_())


