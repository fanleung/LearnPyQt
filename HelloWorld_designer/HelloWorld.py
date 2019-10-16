import sys
from PyQt5 import QtWidgets
from HelloWorld_designer import Ui_From

## Ui_From 是ui文件生成的py文件的类名
## 这里新建一个子类 MyPyQT_Form 来继承 HelloWorld_designer.py 中的 父类 Ui_From

class MyPyQT_Form(QtWidgets.QWidget,Ui_From):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())