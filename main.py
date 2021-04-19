import sys
import Users
from PyQt5 import QtWidgets as qtw
from PyQt5.uic import loadUi

from LoginForm import Ui_LoginForm


class StartUp(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)
        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = StartUp(windowTitle='Login')
    app.exec_()
