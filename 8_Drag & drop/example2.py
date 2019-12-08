# 拖放按钮组件
# 这个例子展示怎么拖放一个button组件

from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag
import sys

class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

    # 重构，mouseMoveEvent 是拖拽开始的事件
    # 我们只修改右键的事件，左键的操作还是默认
    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.RightButton:
            return

        # 创建一个 QDrag 对象，用来传输 MIME-based 数据
        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        # 拖放事件开始时，用到的处理函数式start().
        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):
        # 注意，我们在父级上也调用了mousePressEvent()方法，
        # 不然的话，我们是看不到按钮按下的效果的。
        super().mousePressEvent(e)
        if e.button() == Qt.LeftButton:
            print('press')

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 激活组件的拖拽事件
        self.setAcceptDrops(True)

        self.button = Button('Button', self)
        self.button.move(100, 65)

        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 200, 150)
        self.show()

    def dragEnterEvent(self, e):
        e.accept()

    # 在dropEvent()方法里，我们定义了按钮按下后和释放后的行为，
    # 获得鼠标移动的位置，然后把按钮放到这个地方。
    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)
        
        # 指定放下的动作类型为moveAction
        e.setDropAction(Qt.MoveAction)
        e.accept()

# 这个例子，左键点击按钮，控制台输出 press
# 右键可以点击然后拖动按钮
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
