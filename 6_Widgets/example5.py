# 日历
# QCalendarWidget提供了基于月份的日历插件，十分简易而且直观

from PyQt5.QtWidgets import (QWidget, QCalendarWidget,
                             QLabel, QApplication, QVBoxLayout)

from PyQt5.QtCore import QDate
import sys

# 这个例子有日期组件和标签组件组成，标签显示被选中的日期
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout(self)
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        # 选择一个日期时，QDate的点击信号就触发了，
        # 把这个信号和我们自己定义的 showDate() 方法关联起来
        cal.clicked[QDate].connect(self.showDate)

        vbox.addWidget(cal)
        self.lb1 = QLabel(self)
        # 使用selectedDate()方法获取选中的日期，然后把日期对象转成字符串，在标签里面显示出来
        date = cal.selectedDate()
        print(date)
        self.lb1.setText(date.toString())

        vbox.addWidget(self.lb1)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):
        self.lb1.setText(date.toString())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
