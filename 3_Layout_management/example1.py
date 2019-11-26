# 布局管理
# 在一个GUI程序里，布局是一个很重要的方面。布局就是如何管理应用中的元素和窗口。
# 有两种方式可以搞定：绝对定位和PyQt5的layout类

# 1. 绝对定位
# · 元素不会随着我们更改窗口的位置和大小而变化。
# · 不能适用于不同的平台和不同分辨率的显示器
# · 更改应用字体大小会破坏布局
# · 如果我们决定重构这个应用，需要全部计算一下每个元素的位置和大小#

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lable1 = QLabel('fanleung', self)
        # 这个元素的左上角就在程序的左上角开始（15，10）的位置
        lable1.move(15, 10)

        lable2 = QLabel('code', self)
        lable2.move(35, 40)

        lable3 = QLabel('for programers', self)
        lable3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('绝对定位')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
