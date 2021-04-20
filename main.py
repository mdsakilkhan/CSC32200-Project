import sys
import Users
from PyQt5 import QtWidgets as qtw
from PyQt5.uic import loadUi

from LoginForm import Ui_LoginForm


class Main(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loginForm = LoginForm()


class LoginForm(qtw.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = loadUi("LoginForm.ui")

        # Connect signals and slots
        self.ui.pButton_newUser.clicked.connect(self.show_new_user_form)

        self.ui.show()

    def show_new_user_form(self):
        newUserForm = NewUserForm()


class NewUserForm(qtw.QDialog):
    def __init__(self):
        super().__init__()
        page1 = loadUi("newUserForm.ui")
        page1.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = Main(windowTitle='Login')
    app.exec_()
