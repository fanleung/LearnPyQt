# 下拉选框
# QComboBox组件能让用户在多个选择项中选择一个。

from PyQt5.QtWidgets import (QWidget, QLabel,
    QComboBox, QApplication)
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.lb1 = QLabel("Ubuntu", self)

        self.combo = QComboBox(self)
        self.combo.addItem("Ubuntu")
        self.combo.addItem("Mandriva")
        self.combo.addItem("Fedora")
        self.combo.addItem("Arch")
        self.combo.addItem("Gentoo")

        self.combo.move(50, 50)
        self.lb1.move(50, 150)

        self.combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 30, 300, 200)
        self.setWindowTitle('QComboBox')
        self.show()

    def onActivated(self, text):
        # 在方法内部，设置标签内容为选定的字符串，然后设置自适应文本大小
        self.lb1.setText(text)
        self.lb1.adjustSize()
        # 通过 currnetText 获取下拉菜单内容
        print('当前下拉菜单内容:' + self.combo.currentText())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
