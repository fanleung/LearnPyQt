# 进度条
# 进度条是用来展示任务进度的（我也不想这样说话）。它的滚动能让用户了解到任务的进度。
# QProgressBar组件提供了水平和垂直两种进度条，进度条可以设置最大值和最小值，默认情况是0~99。

from PyQt5.QtWidgets import (QWidget, QProgressBar,
                             QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer
import sys

# 我们创建了一个水平的进度条和一个按钮，这个按钮控制进度条的开始和停止。
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 新建一个 QProcessBar 构造器
        self.pbar = QProgressBar(self)
        # x, y, w, h
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        # 用时间控制进度条
        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProcessBar')
        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        self.step = self.step + 1
        self.pbar.setValue(self.step)

    # 用来控制和暂停的
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            # 调用 start 方法加载一个时间事件，两个参数：过期时间 和 事件接收者
            self.timer.start(100, self)
            self.btn.setText('Stop')
            # 如果满 100 就置零
            if self.step >= 100:
                self.step = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

