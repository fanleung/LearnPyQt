# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_server.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(724, 492)
        self.formGroupBox = QtWidgets.QGroupBox(Form)
        self.formGroupBox.setGeometry(QtCore.QRect(10, 10, 291, 151))
        self.formGroupBox.setObjectName("formGroupBox")
        self.layoutWidget = QtWidgets.QWidget(self.formGroupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(7, 21, 281, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.s1__lb_1 = QtWidgets.QLabel(self.layoutWidget)
        self.s1__lb_1.setObjectName("s1__lb_1")
        self.horizontalLayout.addWidget(self.s1__lb_1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.socket_connect_button_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.socket_connect_button_2.setObjectName("socket_connect_button_2")
        self.horizontalLayout.addWidget(self.socket_connect_button_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.s1__lb_2 = QtWidgets.QLabel(self.layoutWidget)
        self.s1__lb_2.setObjectName("s1__lb_2")
        self.horizontalLayout_2.addWidget(self.s1__lb_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.socket_connect_button = QtWidgets.QPushButton(self.layoutWidget)
        self.socket_connect_button.setObjectName("socket_connect_button")
        self.horizontalLayout_3.addWidget(self.socket_connect_button)
        self.socket_disconnect_button = QtWidgets.QPushButton(self.layoutWidget)
        self.socket_disconnect_button.setObjectName("socket_disconnect_button")
        self.horizontalLayout_3.addWidget(self.socket_disconnect_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalGroupBox = QtWidgets.QGroupBox(Form)
        self.verticalGroupBox.setGeometry(QtCore.QRect(310, 10, 401, 471))
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.s2__receive_text = QtWidgets.QTextBrowser(self.verticalGroupBox)
        self.s2__receive_text.setGeometry(QtCore.QRect(11, 49, 379, 411))
        self.s2__receive_text.setObjectName("s2__receive_text")
        self.widget = QtWidgets.QWidget(self.verticalGroupBox)
        self.widget.setGeometry(QtCore.QRect(11, 20, 229, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.hex_receive = QtWidgets.QCheckBox(self.widget)
        self.hex_receive.setObjectName("hex_receive")
        self.horizontalLayout_5.addWidget(self.hex_receive)
        self.rece_clear_button = QtWidgets.QPushButton(self.widget)
        self.rece_clear_button.setObjectName("rece_clear_button")
        self.horizontalLayout_5.addWidget(self.rece_clear_button)
        self.rece_clear_button_2 = QtWidgets.QPushButton(self.widget)
        self.rece_clear_button_2.setObjectName("rece_clear_button_2")
        self.horizontalLayout_5.addWidget(self.rece_clear_button_2)
        self.verticalGroupBox_2 = QtWidgets.QGroupBox(Form)
        self.verticalGroupBox_2.setGeometry(QtCore.QRect(10, 170, 291, 231))
        self.verticalGroupBox_2.setObjectName("verticalGroupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.s3__send_text = QtWidgets.QTextEdit(self.verticalGroupBox_2)
        self.s3__send_text.setObjectName("s3__send_text")
        self.verticalLayout_2.addWidget(self.s3__send_text)
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(70, 450, 161, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.hex_send_2 = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.hex_send_2.setObjectName("hex_send_2")
        self.horizontalLayout_7.addWidget(self.hex_send_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_7.addWidget(self.lineEdit_3)
        self.dw = QtWidgets.QLabel(self.layoutWidget_2)
        self.dw.setObjectName("dw")
        self.horizontalLayout_7.addWidget(self.dw)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(20, 410, 281, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.hex_send = QtWidgets.QCheckBox(self.widget1)
        self.hex_send.setObjectName("hex_send")
        self.horizontalLayout_4.addWidget(self.hex_send)
        self.data_send_button = QtWidgets.QPushButton(self.widget1)
        self.data_send_button.setObjectName("data_send_button")
        self.horizontalLayout_4.addWidget(self.data_send_button)
        self.send_clear_button_2 = QtWidgets.QPushButton(self.widget1)
        self.send_clear_button_2.setObjectName("send_clear_button_2")
        self.horizontalLayout_4.addWidget(self.send_clear_button_2)
        self.send_clear_button = QtWidgets.QPushButton(self.widget1)
        self.send_clear_button.setObjectName("send_clear_button")
        self.horizontalLayout_4.addWidget(self.send_clear_button)
        self.verticalGroupBox.raise_()
        self.verticalGroupBox_2.raise_()
        self.formGroupBox.raise_()
        self.data_send_button.raise_()
        self.send_clear_button.raise_()
        self.hex_send.raise_()
        self.send_clear_button_2.raise_()
        self.layoutWidget_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.formGroupBox.setTitle(_translate("Form", "TCP 服务端配置"))
        self.s1__lb_1.setText(_translate("Form", "本地 IP"))
        self.socket_connect_button_2.setText(_translate("Form", "获取"))
        self.s1__lb_2.setText(_translate("Form", "监听端口："))
        self.socket_connect_button.setText(_translate("Form", "开启服务器"))
        self.socket_disconnect_button.setText(_translate("Form", "关闭服务器"))
        self.verticalGroupBox.setTitle(_translate("Form", "接受区"))
        self.hex_receive.setText(_translate("Form", "Hex接收"))
        self.rece_clear_button.setText(_translate("Form", "清除"))
        self.rece_clear_button_2.setText(_translate("Form", "保存文件"))
        self.verticalGroupBox_2.setTitle(_translate("Form", "发送区"))
        self.s3__send_text.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.hex_send_2.setText(_translate("Form", "定时发送"))
        self.lineEdit_3.setText(_translate("Form", "1000"))
        self.dw.setText(_translate("Form", "ms/次"))
        self.hex_send.setText(_translate("Form", "Hex发送"))
        self.data_send_button.setText(_translate("Form", "发送"))
        self.send_clear_button_2.setText(_translate("Form", "打开文本"))
        self.send_clear_button.setText(_translate("Form", "清除"))

