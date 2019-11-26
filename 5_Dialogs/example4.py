# 选择文件
# QFileDialog给用户提供文件或者文件夹选择的功能。能打开和保存文件

from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction,
                             QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
import sys

# 这里设置了一个文本编辑框，文本编辑框是基于QMainWindow组件的。
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl + O')
        openFile.setStatusTip('Open new file')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File Dialog')
        self.show()
    # 弹出QFileDialog窗口。getOpenFileName()方法的第一个参数是说明文字，第二个参数是默认打开的文件夹路径。
    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())