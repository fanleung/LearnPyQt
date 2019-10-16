# 例3, 提示框
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个提示框，使用 10px 的 SansSerif 字体
        QToolTip.setFont(QFont('SansSerif', 10))

        # 调用setTooltip() 创建提示框可以使用富文本格式的内容
        self.setToolTip('This is a <b>QWidget</b> widget')

        # 创建一个按钮，并为按钮添加提示框
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QpushButton</b> widget')
        # sizeHint() 方法提供一个默认按钮的大小
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())