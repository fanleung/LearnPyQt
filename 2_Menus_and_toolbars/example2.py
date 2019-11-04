# 菜单栏
# 菜单栏是非常常用的。
# 是一组命令的集合（Mac OS下状态栏的显示不一样，为了得到最相似的外观，
# 我们增加了一句menubar.setNativeMenuBar(False))。

import sys
from PyQt5.QtWidgets import qApp, QAction, QMainWindow, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建图标、exit 标签
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        # 创建快捷键组合
        exitAct.setShortcut('Ctrl+Q')
        # 创建状态栏，当鼠标悬停在菜单栏的时候，能显示当前状态
        exitAct.setStatusTip('Exit application')
        # 指定执行这个动作时，触发退出应用事件
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        # 创建菜单栏 File
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        # 在File 中添加标签 Exit 标签
        fileMenu.addAction(exitAct)

        # 创建菜单栏 Edit
        # EditMenu = menubar.addMenu('&Edit')
        # EditMenu.addAction(exitAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

