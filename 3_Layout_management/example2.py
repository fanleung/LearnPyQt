# 布局盒
# 使用盒布局能让程序具有更强的适应性。这个才是布局一个应用的更合适的方式。
# QHBoxLayout和QVBoxLayout是基本的布局类，分别是水平布局和垂直布局。

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout,
                             QVBoxLayout, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        # 创建一个水平布局，增加两个按钮和弹性空间。
        # stretch函数在两个按钮前面增        hbox.addStretch(1)加了一些弹性空间, 把空白部分平分，所以按钮都是往右靠
        # 如果 stretch 放中间，则按钮会布局在两边
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        # 为了布局需要，需要把水平布局放到一个垂直布局盒
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # 设置布局，要执行这句，才会生效
        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('布局盒')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
