# 例2，带窗口图标
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

# 窗口图标通常是显示在窗口的左上角，标题栏的最左边。下面的例子就是怎么用PyQt5创建一个这样的窗口

# Example 这个类继承父类 QWidget, 做了初始化，且调用了 super初始化了父类的构建函数，
# 那么 Example 类会继承父类 QWidget 的方法，使得initUI() 可以用父类的方法
# 类似 c 语言的声明

class Example(QWidget):
    def __init__(self):
        super().__init__() # 因为重新初始化了，如果没调用 super().__init__(), 就不能使用父类的方法
        self.initUI()

    def initUI(self):
        # setGeometry() 有两个作用：把窗口放到屏幕上并且设置窗口大小
        # 参数分别表示x,y,w,h,也就是说是 resize() 和 move() 的合体
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())

