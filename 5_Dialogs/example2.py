# 选取颜色
# QColorDialog 提供颜色的选择

from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame,
    QColorDialog, QApplication)
from PyQt5.QtGui import QColor
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

# 创建一个按钮和一个 frame, 默认的背景颜色为黑色，我们可以使用 QcolorDialog 改变背景颜色
    def initUI(self):
        # 初始化 QtGui.QFrame 的背景颜色
        col = QColor(0, 0, 0)

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s}" % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('color dialog')
        self.show()

    def showDialog(self):
        # 弹出一个 QColorDialog 对话框
        col = QColorDialog.getColor()

        # 预览颜色，点击取消按钮则返回，如果颜色是选择的，则从取色框里选择这个颜色
        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s}" % col.name())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

