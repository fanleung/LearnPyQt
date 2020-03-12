
# 导入一些用到的包
from ui_student import Ui_Form
import sys, os
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtSql import QSqlQuery
from PyQt5 import QtWidgets, QtSql, QtCore
from aip import AipOcr
import re


class Example(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 设置窗口名
        self.setWindowTitle("学生信息管理系统")

        self.init()

        # 设置 百度ai 接口的 APPID,API_KEY,Secre_Key, 调用百度Ai 接口的时候要用到
        self.APP_ID = '17126510'  # 百度ai中心应用管理里获取
        self.API_Key = 'dBFwmo4uWyufwbpGXirCriAe'  # 百度ai中心应用管理里获取
        self.Secret_Key = 'nj3go0oFWqqNXZCxkmtOpuQ7AGgsStf4'  # 百度ai中心应用管理里获取

        # 创建一个数据库
        self.create_SQL()
        # 创建匹配数据表 list_table
        self.create_CheckTable()
        # 创建晚归数据表 record_table
        self.create_SQLTable()

        # 实例化一个可编辑数据模型
        self.model = QtSql.QSqlTableModel()
        self.tableView.setModel(self.model)



    def init(self):
        # 链接按钮，即触发按钮，执行对应的函数
        # 手动录入按钮
        self.pushButton_3.clicked.connect(self.manual_add_record)
        # 通过号码查找按钮
        self.pushButton_5.clicked.connect(self.search_record)
        # 打开图片
        self.pushButton_2.clicked.connect(self.search_by_picture)
        # 显示所有数据
        self.pushButton_4.clicked.connect(self.view_database)
        # 删除一行
        self.pushButton_6.clicked.connect(self.del_row_data)
        # 清空数据
        self.pushButton_7.clicked.connect(self.del_all_record)


    #### 数据库操作 #####
    # 创建数据库 student.db 并打开
    def create_SQL(self):
        self.database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.database.setDatabaseName('student.db')
        self.database.open()

    # 删除数据库
    def remove_SQL(self):
        self.database.removeDatabase('student.db')

    # 创建录入表格
    def create_CheckTable(self):
        q = QSqlQuery()
        sql_code = u"create table list_table (name varchar(30), department varchar(40), grade varchar(40),\
        id varchar(20) primary key, sex varchar(10), room varchar(20))"
        print(sql_code)
        if q.exec_(sql_code):
            print("create a table ")

    # 新增一条录入数据
    def insert_CheckTable(self, name, department, grade, id, sex, room):
        print('insert_SQLTable')
        q = QSqlQuery()
        sql_code = u"insert into list_table values(\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\", \"{5}\")".format(
         name, department, grade, id, sex, room
        )
        if q.exec_(sql_code):
            print('succeed insert record')
            # 录入完显示这一条
            QMessageBox.information(self, "Information",
                                    "已录入该信息")
        else:
            QMessageBox.information(self, "Information",
                                    "该学号已存在，请检查")

    # 创建晚归记录的表格
    def create_SQLTable(self):
        q = QSqlQuery()
        sql_code = u"create table record_table (name varchar(30), department varchar(40), grade varchar(40),\
        id varchar(20), sex varchar(10), room varchar(20), time varchar(30), reason varchar(200))"
        print(sql_code)
        if q.exec_(sql_code):
            print("create a table ")

    # 插入一条晚归记录
    def insert_SQLTable(self, name, department, grade, id, sex, room):
        print('insert_SQLTable')
        q = QSqlQuery()
        sql_code = u"insert into record_table values(\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\", \"{5}\", NULL, NULL)".format(
         name, department, grade, id, sex, room
        )
        if q.exec_(sql_code):
            print('succeed insert record')
            # 录入完刷新
            self.view_database()
        else:
            QMessageBox.information(self, "Information",
                                    "新增晚归记录不成功，请检查")

    # 通过图片识别，来识别出学号。
    # 再利用这个学号，从匹配数据表中找到对应的其他信息，写入晚归数据表
    def search_by_picture(self):
        # 打开图片，并显示缩略图
        fname = QFileDialog.getOpenFileName(self, 'Open file')
        # 图片格式仅支持 png 或 jpg
        if os.path.splitext(fname[0])[1] == '.png' or os.path.splitext(fname[0])[1] == '.jpg':
            print(fname)
            pic = QPixmap(fname[0])
            self.label_8.setPixmap(pic)
            self.label_8.setScaledContents(True)

            # 调用百度ai 接口，识别出文字
            # 利用正则表达式，提取出学号
            cardID = self.baiduOCR(self.APP_ID, fname[0], self.API_Key, self.Secret_Key)
            # 打印识别出来的学号
            print(cardID)

            # 利用这个学号，从匹配数据表中找到对应的其他信息
            # 把找到的其他信息，往晚归数据表插入一条记录
            q = QSqlQuery()
            sql_code = "select * from list_table where id = \"{}\"".format(cardID)
            if q.exec(sql_code):
                name_index = q.record().indexOf('name')
                department_index = q.record().indexOf('department')
                grade_index = q.record().indexOf('grade')
                id_index = q.record().indexOf('id')
                sex_index = q.record().indexOf('sex')
                room_index = q.record().indexOf('room')
                while q.next():
                    name = q.value(name_index)
                    department = q.value(department_index)
                    grade = q.value(grade_index)
                    id = q.value(id_index)
                    sex = q.value(sex_index)
                    room = q.value(room_index)
                    # 插入
                    self.insert_SQLTable(name, department, grade, id, sex, room)

        else:
            # 提示不支持此文件格式
            QMessageBox.information(self, "提示", "不支持此类型文件")
        # 刷新 晚归数据表
        self.view_database()

    # 通过某个学号，查找这个人的所有晚归记录
    def query_record(self, id):
        self.model.setFilter(u"id = \"{0}\"".format(id))
        self.model.select()

    ### 按钮触发
    # 录入数据到匹配数据表
    def manual_add_record(self):
        try:
            self.insert_CheckTable(self.lineEdit_3.text(),
                             self.lineEdit_4.text(),
                             self.lineEdit_5.text(),
                             self.lineEdit_6.text(),
                             self.lineEdit_8.text(),
                             self.lineEdit_9.text())
        except Exception as e:
            print(e)

    # 通过条件查找
    def search_record(self):
        self.query_record(self.lineEdit_10.text())

    # 显示所有数据
    def view_database(self):
        # 设置数据模型的数据表
        self.model.setTable('record_table')
        # 允许字段更改
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        # 显示全部
        self.model.setFilter('')
        # 选择所有数据
        self.model.select()
        # 设置表格头
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, '姓名')
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, '院系')
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, '班级')
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, '学号')
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, '性别')
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, '宿舍')
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, '晚归时间')
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, '晚归原因')

    # 添加一行数据
    # def add_row_data(self):
    #     # 如果存在实例化的数据模型对象
    #     if self.model:
    #         self.model.insertRow(self.model.rowCount(), 1)
    #     else:
    #         self.create_SQLTable('record_table')

    # 删除一行数据
    def del_row_data(self):
        if self.model:
            self.model.removeRow(self.tableView.currentIndex().row())
        else:
            self.create_SQLTable('record_table')

    # 删除所有记录
    def del_all_record(self):
        reply = QMessageBox.question(self, '警告', "该操作不可恢复。确定要删除所有记录？",
                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            sql_code = "delete from record_table"
            q = QSqlQuery()
            if q.exec_(sql_code):
                print("delete succeed")
                self.view_database()
            else:
                pass
            pass
        else:
            pass

    def baiduOCR(self, appid, filename, API_Key, Secret_Key):
        # 识别图片
        string = ""
        client = AipOcr(appid, API_Key, Secret_Key)
        i = open(filename, 'rb')
        print('正在识别: %s' % filename)
        message = client.basicAccurate(i.read())
        print("识别成功")
        i.close()
        # 正则表达式，识别出学号后面的数字
        reg = re.compile(r"(?<=学号:)\d+")
        for i in message.get('words_result'):
            string += i.get('words')
        # print(string)
        match = reg.search(string)
        return match.group(0)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())





