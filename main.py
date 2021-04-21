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

        # Member variables
        self.ui = loadUi("LoginForm.ui")
        self.newUserForm = None

        # Connect signals and slots
        self.ui.pButton_newUser.clicked.connect(self.show_new_user_form)

        self.ui.show()

    def show_new_user_form(self):
        self.newUserForm = NewUserForm(self.ui)


class NewUserForm(qtw.QDialog):
    def __init__(self, loginForm):
        super().__init__()

        loginForm.hide()
        self.ui = loadUi("newUserForm.ui")
        self.ui.pButton_create.setEnabled(False)
        # Connect signals and slots
        self.ui.lineEdit_firstName.textChanged.connect(self.enable_create_button)
        self.ui.lineEdit_lastName.textChanged.connect(self.enable_create_button)
        self.ui.lineEdit_DOB.textChanged.connect(self.enable_create_button)
        self.ui.lineEdit_contactNumber.textChanged.connect(self.enable_create_button)
        self.ui.lineEdit_emailAddress.textChanged.connect(self.enable_create_button)
        self.ui.lineEdit_address.textChanged.connect(self.enable_create_button)
        self.ui.lineEdit_cardNumber.textChanged.connect(self.enable_create_button)
        self.ui.lineEdit_bankName.textChanged.connect(self.enable_create_button)
        self.ui.lineEdit_cvv.textChanged.connect(self.enable_create_button)
        
        self.ui.show()

    def enable_create_button(self):
        if (not self.ui.lineEdit_firstName.text()
            and not self.ui.lineEdit_lastName.text()
            and not self.ui.lineEdit_DOB.text()
            and not self.ui.lineEdit_contactNumber.text()
            and not self.ui.lineEdit_emailAddress.text()
            and not self.ui.lineEdit_address.text()
            and not self.ui.lineEdit_cardNumber.text()
            and not self.ui.lineEdit_bankName.text()
            and not self.ui.lineEdit_cvv.text()):
            self.ui.pButton_create.setEnabled(True)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = Main(windowTitle='Login')
    app.exec_()
