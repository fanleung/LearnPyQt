from ui_gym import Ui_Form
import sys, os
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtSql import QSqlQuery
from PyQt5 import QtWidgets, QtSql, QtCore

class Example(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 创建一个数据库
        self.setWindowTitle("健身系统")

        self.init()

        self.create_SQL()
        self.create_SQLTable('gym_table')

        # 实例化一个可编辑数据模型
        self.model = QtSql.QSqlTableModel()
        self.tableView.setModel(self.model)


    def init(self):
        # 链接按钮
        # 手动录入按钮
        self.pushButton_3.clicked.connect(self.manual_add_record)
        # 通过号码查找按钮
        self.pushButton.clicked.connect(self.search_record)
        # 打开图片
        self.pushButton_2.clicked.connect(self.search_by_picture)
        # 显示所有数据
        self.pushButton_4.clicked.connect(self.view_database)
        # 删除一行
        self.pushButton_6.clicked.connect(self.del_row_data)
        # 清空数据
        self.pushButton_7.clicked.connect(self.del_all_record)


    #### 数据库操作 #####
    # 创建数据库 gym_data.db 并打开
    def create_SQL(self):
        self.database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.database.setDatabaseName('gym_data.db')
        self.database.open()

    # 删除数据库
    def remove_SQL(self):
        self.database.removeDatabase('gym_data.db')

    # 创建表格
    def create_SQLTable(self, tableName):
        q = QSqlQuery()
        sql_code = u"create table {} (id int primary key, name varchar(30), sex varchar(10), age int, level varchar(100))".format(tableName)
        print(sql_code)
        if q.exec_(sql_code):
            print("create a table ")
        if q.exec_("insert into gym_table values(1234, 'fanleung', '男', 33, '普通会员')"):
            print("插入数据")

    # 插入一条记录
    def insert_SQLTable(self, tableName, id, name, sex, age, level):
        print('insert_SQLTable')
        q = QSqlQuery()
        sql_code = u"insert into {0} values({1}, \"{2}\", \"{3}\", {4}, \"{5}\")".format(
            tableName, id, name, sex, age, level
        )
        if q.exec_(sql_code):
            print('succeed insert record')
            # 录入完显示这一条
            self.query_record(id)
        else:
            QMessageBox.information(self, "Information",
                                    "该号码已存在，请检查")




    def search_by_picture(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file')
        if os.path.splitext(fname[0])[1] == '.png' or os.path.splitext(fname[0])[1] == '.jpg':
            print(fname)
            pic = QPixmap(fname[0])
            self.label_8.setPixmap(pic)
            self.label_8.setScaledContents(True)
        else:
            # 提示不支持此文件格式
            QMessageBox.information(self, "提示", "不支持此类型文件")

    # 通过卡号查找
    def query_record(self, id):
        self.model.setFilter(u"id = {0}".format(int(id)))
        self.model.select()

        ### 查询获取其他值
        q = QSqlQuery()
        sql_code = "select * from gym_table where id = {}".format(id)
        if q.exec(sql_code):
            id_index = q.record().indexOf('id')
            name_index = q.record().indexOf('name')
            sex_index = q.record().indexOf('sex')
            age_index = q.record().indexOf('age')
            level_index = q.record().indexOf('level')
            while q.next():
                id = q.value(id_index)
                name = q.value(name_index)
                sex = q.value(sex_index)
                age = q.value(age_index)
                level = q.value(level_index)
                print(id, name, sex, age, level)


    ### 按钮触发
    # 手动录入
    def manual_add_record(self):
        try:
            self.insert_SQLTable("gym_table", int(self.lineEdit_3.text()),
                             self.lineEdit_4.text(),
                             self.lineEdit_5.text(),
                             int(self.lineEdit_6.text()),
                             self.lineEdit_7.text())
        except Exception as e:
            print(e)

    # 通过条件查找
    def search_record(self):
        self.query_record(self.lineEdit.text())



    # 显示所有数据
    def view_database(self):
        # 设置数据模型的数据表
        self.model.setTable('gym_table')
        # 允许字段更改
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        # 显示全部
        self.model.setFilter('')
        # 选择所有数据
        self.model.select()
        # 设置表格头
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, '号码')
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, '姓名')
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, '性别')
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, '年龄')
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, '等级')

    # 添加一行数据
    def add_row_data(self):
        # 如果存在实例化的数据模型对象
        if self.model:
            self.model.insertRow(self.model.rowCount(), 1)
        else:
            self.create_SQLTable('gym_table')

    # 删除一行数据
    def del_row_data(self):
        if self.model:
            self.model.removeRow(self.tableView.currentIndex().row())
        else:
            self.create_SQLTable('gym_table')

    # 删除所有记录
    def del_all_record(self):
        reply = QMessageBox.question(self, '警告', "该操作不可恢复。确定要删除所有记录？",
                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            sql_code = "delete from gym_table"
            q = QSqlQuery()
            if q.exec_(sql_code):
                print("delete succeed")
                self.view_database()
            else:
                pass







if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())