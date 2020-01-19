# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HelloWorld_designer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_From(object):
    def setupUi(self, From):
        From.setObjectName("From")
        From.resize(250, 150)
        self.label = QtWidgets.QLabel(From)
        self.label.setGeometry(QtCore.QRect(90, 50, 71, 16))
        # self.label.setObjectName("label")

        self.retranslateUi(From)
        # QtCore.QMetaObject.connectSlotsByName(From)

    def retranslateUi(self, From):
        _translate = QtCore.QCoreApplication.translate
        From.setWindowTitle(_translate("From", "Simple"))
        self.label.setText(_translate("From", "hello world"))
        pass
