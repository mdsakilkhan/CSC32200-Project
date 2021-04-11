import sys
from PyQt5 import QtWidgets as qtw
from PyQt5.uic import loadUi


class Login(qtw.QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = Login(windowTitle='hello world')
    app.exec_()
