# 例4, 关闭窗口

""""
关闭一个窗口最直观的方式就是点击标题栏的那个叉，这个例子里，
我们展示的是如何用程序关闭一个窗口。
这里我们将接触到一点single和slots的知识。
"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # QPushButton(string text, QWidget parent = None)
        # text参数是想要显示的按钮名称，parent参数是放在按钮上的组件
        # 这个例子中，父级组件就是我们创建的继承自 Qwidget 的 Example 类
        qbtn = QPushButton('Quit', self)
        # 事件传递系统在PyQt5内建的single和slot机制里面。
        # 点击按钮之后，信号会被捕捉并给出既定的反应。
        # QCoreApplication包含了事件的主循环，它能添加和删除所有的事件，instance()创建了一个它的实例。
        # QCoreApplication是在QApplication里创建的。
        # 点击事件和能终止进程并退出应用的quit函数绑定在了一起。
        # 在发送者和接受者之间建立了通讯，发送者就是按钮，接受者就是应用对象。
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())