# 行编辑
# QLineEdit组件提供了编辑文本的功能，自带了撤销、重做、剪切、粘贴、拖拽等功能。

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.lb1 = QLabel(self)
        self.lb2 = QLabel(self)
        qle = QLineEdit(self)


        qle.move(60, 100)
        self.lb1.move(60, 40)
        self.lb2.move(60, 60)

        # 如果输入框的值有变化，就调用 onChanged 方法
        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()

    # test 是当前 lineEdit 的内容
    def onChanged(self, text):
        self.lb1.setText(text)
        self.lb2.setText(len(text))
        self.lb1.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())