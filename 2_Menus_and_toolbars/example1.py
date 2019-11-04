# 状态栏
# 状态栏是用来显示应用的状态信息的组件。
# QMainWindow提供了主窗口的功能，使用它能创建一些简单的状态栏、工具栏和菜单栏

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('statusbar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())