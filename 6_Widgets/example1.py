# 控件1
# PyQt5有很多的控件，比如按钮，单选框，滑动条，复选框等等
# 在本章，我们将介绍一些很有用的控件：QCheckBox，ToggleButton，QSlider，QProgressBar和QCalendarWidget。

# QcheckBox
# QCheckBox组件有俩状态：开和关。通常跟标签一起使用，用在激活和关闭一些选项的场景

from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt
import sys

# 这个例子中，有一个能切换窗口标题的单选框。
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 这个是QCheckBox的构造器， 第一个参数为标题
        cb = QCheckBox('show title', self)
        cb.move(20, 20)

        # 要设置窗口标题，我们就要检查单选框的状态。默认情况下，窗口没有标题，单选框未选中。
        cb.toggle()

        # 把单选框的状态和 changeTitle 关联起来
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QcheckBox')
            print("打勾了")
        else:
            self.setWindowTitle(' ')
            print("去勾了")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())