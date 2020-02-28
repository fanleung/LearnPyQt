import sys
import serial
import serial.tools.list_ports
from PyQt5.QtSql import QSqlQuery
from PyQt5 import QtWidgets, QtSql, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox, QLineEdit
from PyQt5.QtCore import QTimer
from ui_serialSQLite import Ui_Form
from ui_login import Ui_login
import sys
import time

class LoginUI(QtWidgets.QWidget, Ui_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("系统登陆")
        self.initUI()

    def initUI(self):
        # 点击取消关闭窗口
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.CheckAccount)
        # 设置密码不可见
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

    # 核对密码是否正确
    def CheckAccount(self):
        if self.lineEdit.text() == "邹小姨" and self.lineEdit_2.text() == "12345":
            self.close()    # 关闭登陆界面
            ex.show()
        else:
            QMessageBox.information(self, "Information",
                                    "账号或密码错误")


class Example(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("考勤系统")

        self.init()
        self.ser = serial.Serial()
        self.port_check()

        # 接收数据和发送数据数目清零
        self.data_num_received = 0
        self.lineEdit.setText(str(self.data_num_received))
        self.data_num_sended = 0
        self.lineEdit_2.setText(str(self.data_num_sended))

        # 创建一个数据库
        self.create_SQL()
        self.create_SQLTable('tbname')
        self.currentTime = ""

    def init(self):
        # 串口检测按钮
        self.s1__box_1.clicked.connect(self.port_check)

        # 串口信息显示
        self.s1__box_2.currentTextChanged.connect(self.port_imf)

        # 打开串口按钮
        self.open_button.clicked.connect(self.port_open)

        # 关闭串口按钮
        self.close_button.clicked.connect(self.port_close)

        # 发送数据按钮
        self.s3__send_button.clicked.connect(self.data_send)

        # 定时发送数据
        self.timer_send = QTimer()
        self.timer_send.timeout.connect(self.data_send)
        self.timer_send_cb.stateChanged.connect(self.data_send_timer)

        # 定时器接收数据
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.data_receive)

        # 清除发送窗口
        self.s3__clear_button.clicked.connect(self.send_data_clear)

        # 清除接收窗口
        self.s2__clear_button.clicked.connect(self.receive_data_clear)

        # 添加按钮
        self.add_record_button.clicked.connect(self.manual_add_record)

        # 删除按钮
        self.delete_record_button.clicked.connect(self.delete_record)

        # 查询按钮
        self.search_record_button.clicked.connect(self.search_SQLTable)


    # 串口检测
    def port_check(self):
        # 检测所有存在的串口， 将信息存储在字典中
        self.Com_dict = {}
        port_list = list(serial.tools.list_ports.comports())
        self.s1__box_2.clear()
        for port in port_list:
            self.Com_dict["%s" % port[0]] = "%s" % port[1]
            self.s1__box_2.addItem(port[0])
        if len(self.Com_dict) == 0:
            self.state_label.setText(" 无串口")

    # 串口信息
    def port_imf(self):
        # 显示选定串口的详细信息
        imf_s = self.s1__box_2.currentText()
        if imf_s != "":
            self.state_label.setText(self.Com_dict[self.s1__box_2.currentText()])

    # 打开串口
    def port_open(self):
        self.ser.port = self.s1__box_2.currentText()
        print(self.ser.port)
        self.ser.baudrate = int(self.s1__box_3.currentText())
        self.ser.bytesize = int(self.s1__box_4.currentText())
        self.ser.stopbits = int(self.s1__box_6.currentText())
        self.ser.parity = self.s1__box_5.currentText()

        try:
            self.ser.open()
        except:
            QMessageBox.critical(self, "Port Error", "此串口不能被打开！")
            return None

        # 打开串口接收定时器, 周期2ms
        self.timer.start(1)

        if self.ser.isOpen():
            self.open_button.setEnabled(False)
            self.close_button.setEnabled(True)
            self.formGroupBox1.setTitle("串口状态（已开启）")

    # 关闭串口
    def port_close(self):
        self.timer.stop()
        self.timer_send.stop()
        try:
            self.ser.close()
        except:
            pass
        self.open_button.setEnabled(True)
        self.close_button.setEnabled(False)
        # 只有先把串口关了，才能设置定时发送功能
        self.lineEdit_3.setEnabled(True)

        # 接收数据和发送数据数目置零
        self.data_num_received = 0
        self.lineEdit.setText(str(self.data_num_received))
        self.data_num_sended = 0
        self.lineEdit_2.setText(str(self.data_num_sended))
        self.formGroupBox1.setTitle("串口状态（已关闭）")

    # 发送数据
    def data_send(self):
        # 判断串口是否打开
        if self.ser.isOpen():
            input_s = self.s3__send_text.toPlainText()
            # 非空字符串
            if self.hex_send.isChecked():
                # hex 发送
                input_s = input_s.strip()
                send_list = []
                while input_s != '':
                    try:
                        num = int(input_s[0:2], 16)
                    except ValueError:
                        QMessageBox.critical(self, 'wrong data', '请输入十六进制数据， 以空格分开')
                        return None
                    input_s = input_s[2:].strip()
                    send_list.append(num)
                input_s = bytes(send_list)
            else:
                # ascii 发送
                input_s = (input_s + '\r\n').encode('gb2312')

            num = self.ser.write(input_s)
            self.data_num_sended += num
            self.lineEdit_2.setText(str(self.data_num_sended))
        else:
            pass

    # 接收数据
    def data_receive(self):
        try:
            num = self.ser.inWaiting()
        except:
            self.port_close()
            return None
        if num > 0:
            self.getCurrentTimeString()

            data = self.ser.read(num)
            num = len(data)
            self.update_record(data.strip().decode('gb2312'))
            # hex 显示
            if self.hex_receive.checkState():
                out_s = ''
                for i in range(0, len(data)):
                    out_s = out_s + '{:02X}'.format(data[i]) + ' '
                self.s2__receive_text.insertPlainText(out_s)
            else:
                # 串口即受到的字符串为b'123', 要转成unicode字符串才能输出到窗口中
                try:
                    self.s2__receive_text.insertPlainText(data.decode('gb2312'))
                except UnicodeDecodeError:
                    pass

            # 统计接收字符的数量
            self.data_num_received += num
            self.lineEdit.setText(str(self.data_num_received))

            # 获取到text光标
            textCursor = self.s2__receive_text.textCursor()
            # 滚动到底部
            textCursor.movePosition(textCursor.End)
            # 设置光标到text中去
            self.s2__receive_text.setTextCursor(textCursor)
        else:
            pass

    # 定时发送数据
    def data_send_timer(self):
        if self.timer_send_cb.isChecked():
            self.timer_send.start(int(self.lineEdit_3.text()))
            self.lineEdit_3.setEnabled(False)
        else:
            self.timer_send.stop()
            self.lineEdit_3.setEnabled(True)


    # 清除显示
    def send_data_clear(self):
        self.s3__send_text.setText("")

    def receive_data_clear(self):
        self.s2__receive_text.setText("")

    def database_view_clear(self):
        self.s2_database_text.setText("")

    # 获取当前时间
    def getCurrentTimeString(self):
        time_stamp = time.time()  # 当前时间的时间戳
        local_time = time.localtime(time_stamp)
        # 因为文件名有符号限制，所以都用 '-' 隔开
        str_time = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
        self.currentTime = str(str_time)


    ######## 数据库操作  #########
    # 链接数据库
    def create_SQL(self):
        self.database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.database.setDatabaseName('test.db')
        self.database.open()

    # 删除数据库
    def remove_SQL(self):
        self.database.removeDatabase('test.db')

    # 创建表
    def create_SQLTable(self, tableName):
        q = QSqlQuery()
        sql_code = u"create table {} (id INTEGER primary key AUTOINCREMENT, name varchar(30), department varchar(30), time varchar(30))".format(tableName)
        print(sql_code)
        if q.exec_(sql_code):
            print("create a table")


    # 插入一条记录
    def insert_SQLTable(self, tableName, name, department):
        # self.getCurrentTimeString()
        # INSERT INTO tableName values(name, department, time)
        q = QSqlQuery()
        sql_code = u"insert into {0} values(NULL, \"{1}\", \"{2}\", NULL)".format(tableName, name, department)
        print(sql_code)
        if q.exec_(sql_code):
            print('succeed insert data')


    #### 按钮触发
    # 查找 √
    def search_SQLTable(self):
        # 每次查找先清除显示框内容
        self.s2__database_text.setText("")
        q = QSqlQuery()

        # 判断选择条件
        if self.s1__box_8.currentText() == "显示所有":
            sql_code = "select * from tbname"

        elif self.s1__box_8.currentText() == "通过 ID 查询":
            sql_code = "select * from tbname where id = {}".format(self.lineEdit_7.text())

        elif self.s1__box_8.currentText() == "通过名字查询":
            sql_code = "select * from tbname where name = \'{}\'".format(self.lineEdit_7.text())

        elif self.s1__box_8.currentText() == "通过部门查询":
            sql_code = "select * from tbname where department = \'{}\'".format(self.lineEdit_7.text())

        print(sql_code)

        if q.exec_(sql_code):
            id_index = q.record().indexOf('id')
            name_index = q.record().indexOf('name')
            department_index = q.record().indexOf('department')
            time_index = q.record().indexOf('time')
            self.s2__database_text.insertPlainText("| id | name | department | time |\r\n")
            self.s2__database_text.insertPlainText(" ————————————————\r\n")

            while q.next():
                id = q.value(id_index)
                name = q.value(name_index)
                department = q.value(department_index)
                time = q.value(time_index)
                print(id, name, department, time)
                self.s2__database_text.insertPlainText(str(id) + ' ' + str(name) + ' ' +
                                                       str(department) + ' ' + str(time) + '\r\n')

    # 手动添加 √
    def manual_add_record(self):
        self.insert_SQLTable("tbname", self.lineEdit_4.text(), self.lineEdit_5.text())

    # 删除记录 √
    def delete_record(self):
        sql_code = ""
        q = QSqlQuery()
        # 判断选择条件
        if self.s1__box_7.currentText() == "删除所有记录":
            sql_code = "delete from tbname"
        elif self.s1__box_7.currentText() == "通过 ID 删除":
            sql_code = "delete from tbname where id = {}".format(self.lineEdit_6.text())
        elif self.s1__box_7.currentText() == "通过名字删除":
            sql_code = "delete from tbname where name = \'{}\'".format(self.lineEdit_6.text())
        elif self.s1__box_7.currentText() == "通过部门删除":
            sql_code = "delete from tbname where department = \'{}\'".format(self.lineEdit_6.text())

        print(sql_code)
        if q.exec_(sql_code):
            print("delete succeed")

    # 更新打卡时间
    def update_record(self, name):
        q = QSqlQuery()
        sql_code = "update tbname set time = '{0}' where name = \'{1}\'".format(self.currentTime, name)
        print(sql_code)
        if q.exec_(sql_code):
            print("update succeed")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login = LoginUI()
    login.show()
    ex = Example()
    sys.exit(app.exec_())