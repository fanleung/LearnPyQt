# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(252, 164)
        self.label = QtWidgets.QLabel(login)
        self.label.setGeometry(QtCore.QRect(30, 30, 54, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(login)
        self.label_2.setGeometry(QtCore.QRect(30, 72, 54, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(login)
        self.lineEdit.setGeometry(QtCore.QRect(80, 30, 141, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(login)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 70, 141, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(login)
        self.pushButton.setGeometry(QtCore.QRect(30, 120, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(login)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 120, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Form"))
        self.label.setText(_translate("login", "账号："))
        self.label_2.setText(_translate("login", "密码："))
        self.pushButton.setText(_translate("login", "确定"))
        self.pushButton_2.setText(_translate("login", "取消"))

