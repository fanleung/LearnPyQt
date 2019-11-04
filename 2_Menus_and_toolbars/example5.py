# 右键菜单

import sys
from PyQt5.QtWidgets import QMainWindow, qApp, QMenu, QApplication

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('右键菜单')
        self.show()

    def contextMenuEvent(self, QContextMenuEvent):
        cmenu = QMenu(self)

        newAct = cmenu.addAction("new")
        openAct = cmenu.addAction("open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(QContextMenuEvent.pos()))

        if action == quitAct:
            qApp.quit()
        elif action == openAct:
            print("你右键open了")
        elif action == newAct:
            print("你右键new了")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())