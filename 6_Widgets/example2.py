# 切换按钮
# 切换按钮就是QPushButton的一种特殊模式。 它只有两种状态：按下和未按下。
# 我们再点击的时候切换两种状态，有很多场景会使用到这个功能。


from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, QApplication)
from PyQt5.QtGui import QColor
import sys

# 我们创建了一个切换按钮和一个QWidget，并把QWidget的背景设置为黑色。
# 点击不同的切换按钮，背景色会在红、绿、蓝之间切换（而且能看到颜色合成的效果，而不是单纯的颜色覆盖）。
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置颜色为黑色
        self.col = QColor(0, 0, 0)

        # 创建一个QPushButton，然后调用它的setCheckable()的方法就把这个按钮编程了切换按钮。
        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10, 10)
        # 把点击信号和我们定义好的函数关联起来，这里是把点击事件转换成布尔值。
        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)
        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)
        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet('QWidget { background-color: %s }' % self.col.name())

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle button')
        self.show()

    def setColor(self, pressed):
        # sender 返回点击了哪个按键
        source = self.sender()
        print(source.text())
        if pressed:
            val = 255
        else:
            val = 0

        # 对应按钮 QPushButton 第一个参数
        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet('QWidget { background-color: %s }' % self.col.name())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())