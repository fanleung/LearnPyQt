from PyQt5.QtSql import QSqlQuery
from PyQt5 import QtGui, QtCore, QtWidgets, QtSql
import sys

# 1. 链接数据库
# 没有test.db这个文件的时候则会在当前目录新建一个test.db文件
# 打开数据库，打开成功返回True
database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
database.setDatabaseName('test.db')
database.open()

# 2. 新建表
# 创建表, ID为主键
q = QSqlQuery()
sql_code = 'create table tbname (id int primary key, name varchar(30), age int)'
if q.exec_(sql_code):
    print("create a table")

# 3、插入数据
q = QSqlQuery()
sql_code = 'insert into tbname values(4, "fanleung", 15)'
if q.exec_(sql_code):
    print('succeed insert data')

# 4. 查询
# q = QSqlQuery()
# sql_code = 'select id,name,age from tbname'
# if q.exec(sql_code):
#     id_index = q.record().indexOf('id')
#     name_index = q.record().indexOf('name')
#     age_index = q.record().indexOf('age')
#     while q.next():
#         id = q.value(id_index)
#         name = q.value(name_index)
#         age = q.value(age_index)
#         print(id, name, age)

# Q = QSqlQuery()
# sql_code = 'select * from tbname where id = \'3\''
# if q.exec(sql_code):
#     id_index = q.record().indexOf('id')
#     name_index = q.record().indexOf('name')
#     age_index = q.record().indexOf('age')
#     print("| id | name | age |")
#     print("-------------------")
#     while q.next():
#         id = q.value(id_index)
#         name = q.value(name_index)
#         age = q.value(age_index)
#         print(id, name, age)

Q = QSqlQuery()
sql_code = 'select * from tbname where name = \'fanleung\''
if q.exec(sql_code):
    id_index = q.record().indexOf('id')
    name_index = q.record().indexOf('name')
    age_index = q.record().indexOf('age')
    print("| id | name | age |")
    print("-------------------")
    while q.next():
        id = q.value(id_index)
        name = q.value(name_index)
        age = q.value(age_index)
        print(id, name, age)



def create_SQL(sqlname):
    '''
    创建数据库
    :param sqlname: 数据库目录名称
    '''
    database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    database.setDatabaseName(sqlname)
    database.open()

def create_SQLtable(tbname):
    '''
    创建通用数据表，默认第一列为主键，名称:ID，类型:INTEGER, 自增
    :param tbname: 数据表名称
    '''
    # CREATE TABLE if not exists 表名 (ID INTEGER PRIMARY KEY AUTOINCREMENT);
    q = QSqlQuery()
    command = u"CREATE TABLE if not exists {} (ID INTEGER PRIMARY KEY AUTOINCREMENT);".format(tbname)
    q.exec_(command)

def add_SQLtable_cloumn(tbname, column_name, genre):
    '''
    指定数据表添加列
    :param tbname: 表名
    :param column_name: 列名
    :param genre: 添加列类型
    '''
    # ALTER TABLE 表名 ADD 列名 列类型;
    q = QSqlQuery()
    command = u"ALTER TABLE {} ADD {} {};".format(tbname, column_name, genre)
    q.exec_(command)

def add_SQLtable_row(tbname, row_num):
    '''
    指定数据表添加行
    :param tbname: 表格名称
    :param row_num: 行数
    '''
    # INSERT INTO 表名 (ID) VALUES (行);
    q = QSqlQuery()
    for row in range(1, row_num + 1):
        command = "INSERT INTO {} (ID) VALUES ({});".format(tbname, str(row))
        q.exec_(command)

def set_SQLtable_value(tbname, column, row, value):
    '''
    更新数据表指定位置的值
    :param tbname: 数据表名称
    :param row: 行数
    :param column: 列数
    :param value: 值
    '''
    # UPDATE 表名 SET 列名=值 WHERE ID=行;
    q = QSqlQuery()
    command = u"UPDATE {} SET {}='{}' WHERE ID={};".format(tbname, column, value, str(row))
    q.exec_(command)

def get_SQLtable_value(tbname, column, row):
    '''
    读取指定数据表的指定列行数据
    :param tbname: 数据表名称
    :param row: 数据表行
    :param column: 数据表列
    :return 返回查询到的值
    '''
    # SELECT 列名 FROM 表名 WHERE ID = 行号;
    q = QSqlQuery()
    command = "SELECT {} FROM {} WHERE ID={};".format(column, tbname, str(row))
    q.exec_(command)
    if q.next():
        result = q.value(0)
        return result

def get_SQLtable_column(tbname, column):
    '''
    读取数据表指定列的所有数据
    :param tbname: 数据表名称
    :param column: 列名称
    :return 返回查询到的值列表
    '''
    # SELECT 列名 FROM 表名;
    q = QSqlQuery()
    command = "SELECT {} FROM {};".format(column, tbname)
    value_list = []
    if q.exec_(command):
        column_index = q.record().indexOf(column)  # 获取列索引值
        while q.next():
            value = q.value(column_index)
            value_list.append(value)
    return value_list

def get_SQLtable_column_name(tbname):
    '''
    获取数据表字段名字
    :param tbname: 数据表名称
    :return: 返回字段(列)名称列表
    '''
    q = QSqlQuery()
    command = "pragma table_info({})".format(tbname)
    name_list = []
    if q.exec_(command):
        while q.next():
            column_name = q.value(1)
            name_list.append(column_name)
    return name_list

def get_SQLtable_row(tbname, row):
    '''
    读取数据表指定行的所有数据
    :param tbname: 数据表名称
    :param column: 行名称
    :return 返回查询到的值列表
    '''
    # SELECT * FROM 表名 WHERE ID = 行号;
    name_list = get_SQLtable_column_name(tbname)
    num = len(name_list) - 1
    q = QSqlQuery()
    command = "SELECT * FROM {} WHERE ID={};".format(tbname, str(row))
    value_list = []
    if q.exec_(command):
        while q.next():
            for i in range(1, num):
                value = q.value(i)
                value_list.append(value)
    return value_list

def delete_SQLtable_value(tbname):
    '''
    清空指定数据表
    :param tbname: 表名
    '''
    # DELETE FROM table_name WHERE[condition];
    q = QSqlQuery()
    command = "DELETE FROM " + tbname + ";"
    q.exec_(command)


