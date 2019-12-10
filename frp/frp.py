from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QLabel, QApplication, QGridLayout, QMessageBox)
import sys
import os

# import win32api
import os
import psutil
# import subprocess

ID_string = ""



# 判断进程是否在运行
def judgeprocess(processname):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == processname:
            return True
    else:
        return False


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建三个输入框
        self.nameLabel = QLabel("输入边缘路由的ID:")
        self.nameLineEdit = QLineEdit(self)


        self.mainLayout = QGridLayout(self)
        self.mainLayout.addWidget(self.nameLabel, 0, 0)  # 控件名，行，列，占用行数，占用列数，对齐方式
        self.mainLayout.addWidget(self.nameLineEdit, 0, 1, 1, 1)


        self.btn = QPushButton('开启', self)
        self.btn.move(100, 220)
        self.btn.clicked.connect(self.generateText)

        # 窗口大小设置
        self.setGeometry(300, 300, 300, 260)
        self.setWindowTitle('FRP 穿透软件')
        self.show()

    def generateText(self):
        ID_string = self.nameLineEdit.text()

        if len(ID_string) != 18:
            QMessageBox.information(self, "Information",
                                    "ID不符合长度要求, 请检查")
        # todo 跳出提示框，完成
        else:
            if judgeprocess('frpc.exe') == True:
                # 关闭程序 , 这里调用了 system ，打包需要打开窗口，改为 subprocess
                os.system("taskkill /F /IM frpc.exe")
                # self.process.terminate()


                # 这里生成文件
            if os.path.exists("frpc.ini"):
                os.remove("frpc.ini")
            file = open("frpc.ini", 'w')

            # file.write("your name: %s\r\n" % self.nameLineEdit.text())
            file.write("# frpc.ini\n\
            [common]\n\
            server_addr = test01.zds-t.com\n\
            server_port = 7000\n\
            \n\
            [{0}]\n\
            type = stcp\n\
            # stcp 的访问者\n\
            role = visitor\n\
            # 要访问的 stcp 代理的名字\n\
            server_name = {1}\n\
            sk = abcdefg\n\
            # 绑定本地端口用于访问 ssh 服务\n\
            bind_addr = 127.0.0.1\n\
            bind_port = 6000".format(ID_string, ID_string))

            file.close()

            # wechat
            # win32api.ShellExecute(0, 'open', r'"frpc.exe"', '', '', 1)
            os.popen("frpc.exe")
            # self.process = subprocess.Popen("frpc.exe", shell=True)
            QMessageBox.information(self, "Information",
                                    "已运行")




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())