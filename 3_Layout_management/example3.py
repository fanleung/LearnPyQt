# 栅格布局
# 最常用的还是栅格布局了。这种布局是把窗口分为行和列。
# 创建和使用栅格布局，需要使用QGridLayout模块。

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['clear', 'Back', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            # *可以把元组拆分， 变成两个参数，类似**可以拆分字典
            # 等同于
            # grid.addWidget(button, position[0], position[1])
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('计算器')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())