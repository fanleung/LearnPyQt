# 根据输入的输入参数
# 点击按钮
# 生成文本

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QLabel, QApplication, QGridLayout, QMessageBox)
import sys
import os

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建三个输入框
        self.nameLabel = QLabel("姓名")
        self.nameLineEdit = QLineEdit(self)
        self.sexLabel = QLabel("性别")
        self.sexLineEdit = QLineEdit(self)
        self.ageLabel = QLabel("年龄")
        self.ageLineEdit = QLineEdit(self)

        self.mainLayout = QGridLayout(self)
        self.mainLayout.addWidget(self.nameLabel, 0, 0)  # 控件名，行，列，占用行数，占用列数，对齐方式
        self.mainLayout.addWidget(self.nameLineEdit, 0, 1, 1, 1)
        self.mainLayout.addWidget(self.sexLabel, 1, 0)
        self.mainLayout.addWidget(self.sexLineEdit, 1, 1, 1, 1)
        self.mainLayout.addWidget(self.ageLabel, 2, 0)
        self.mainLayout.addWidget(self.ageLineEdit, 2, 1, 1, 1)

        self.btn = QPushButton('生成', self)
        self.btn.move(100, 220)
        self.btn.clicked.connect(self.generateText)

        # 窗口大小设置
        self.setGeometry(300, 300, 300, 260)
        self.setWindowTitle('生成文本')
        self.show()

    def generateText(self):
        # text, ok = QInputDialog.getText(self, 'Input Dialog',
        #     'Enter your name:')
        #
        # if ok:
        #     self.le.setText(str(text))

        # 这里生成文件
        if os.path.exists("Text.txt"):
            os.remove("Text.txt")
        file = open("Text.txt", 'w')

        file.write("your name: %s\r\n" % self.nameLineEdit.text())
        file.write("your age: %s\r\n" % self.ageLineEdit.text())
        file.write("your sex: %s\r\n" % self.sexLineEdit.text())

        file.close()

        # todo 跳出提示框，完成
        QMessageBox.information(self, "Information",
                            "已生成文本")

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())