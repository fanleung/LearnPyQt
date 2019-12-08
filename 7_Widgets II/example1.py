# 控件2
# 继续介绍PyQt5控件。这次的有QPixmap，QLineEdit，QSplitter，和QComboBox。

# 图片
# QPixmap是处理图片的组件。本例中，我们使用QPixmap在窗口里显示一张图片


from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
                             QLabel, QApplication)
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)

        # 创建一个 Qpixmap 对象，接收一个文件作为参数
        pixmap = QPixmap('open.png')

        lb1 = QLabel(self)
        # 把 QPixmap 实例放到 QLabel 组件里面
        lb1.setPixmap(pixmap)

        hbox.addWidget(lb1)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Picmap')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

