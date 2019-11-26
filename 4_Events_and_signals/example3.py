# 事件对象
# 事件对象是用python来描述一系列的事件自身属性的对象。

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        self.text = "x: {0}, y: {1}".format(x, y)

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        # 事件追踪默认没有开启，当开启后才会追踪鼠标的点击事件
        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()

    def mouseMoveEvent(self, QMouseEvent):
        # QMouseEvent 代表了事件对象。里面有我们触发事件（鼠标移动）的事件对象
        # 获取 x, y 的坐标
        x = QMouseEvent.x()
        y = QMouseEvent.y()

        # text = "x: {0},  y: {1}".format(x, y)
        text = "x: %s, y: %s" % (x, y)
        self.label.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())