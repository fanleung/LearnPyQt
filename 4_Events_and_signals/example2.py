# 重构事件处理器
# 在 pyqt5 中，事件处理器经常被重写

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 300)
        self.setWindowTitle('Event handler')
        self.show()

    # 这个例子中，我们替换了事件处理函数 KeyPressEvent()
    # 按下 ESC 键就退出程序
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())