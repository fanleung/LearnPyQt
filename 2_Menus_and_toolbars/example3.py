# 子菜单
# 子菜单是嵌套在菜单里面的二级或者三级等的菜单

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QMenu, qApp

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建菜单栏 File
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        # 使用 QMenu 添加一个新菜单 Import
        impMenu = QMenu('Import', self)
        # 使用 QAction 添加一个动作
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)

        # 创建 new 标签
        newAct = QAction('new', self)

        # 创建 exit 标签, 参考 example2
        exitAct = QAction('Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        # 如果点击 exit 就退出
        exitAct.triggered.connect(qApp.quit)


        # 先建 new
        fileMenu.addAction(newAct)
        # 后加 import
        fileMenu.addMenu(impMenu)
        # 最后 exit
        fileMenu.addAction(exitAct)


        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('submenu')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())