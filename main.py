import sys
import Users
from PyQt5 import QtWidgets as qtw
from PyQt5.uic import loadUi

from lxml import etree
from lxml import objectify

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

        self.ui.pButton_create.clicked.connect(self.create_user)
        
        self.ui.show()

    def enable_create_button(self):
        if (len(self.ui.lineEdit_firstName.text())
            and len(self.ui.lineEdit_lastName.text())
            and len(self.ui.lineEdit_DOB.text())
            and len(self.ui.lineEdit_contactNumber.text())
            and len(self.ui.lineEdit_emailAddress.text())
            and len(self.ui.lineEdit_address.text())
            and len(self.ui.lineEdit_cardNumber.text())
            and len(self.ui.lineEdit_bankName.text())
            and len(self.ui.lineEdit_cvv.text())):
            self.ui.pButton_create.setEnabled(True)
        else:
            self.ui.pButton_create.setEnabled(False)

    def create_user(self):
        root = objectify.Element("Users")
        Customers = objectify.SubElement(root,"Customers")
        customer = Users.Customer(first_name="Joshua")
        Customers.append(Users.Utilities.create_xml(customer))
        StoreClerks = []
        Vendors = []
        DeliveryCompanies = []

        # remove lxml annotation
        objectify.deannotate(root)
        etree.cleanup_namespaces(root)

        # create the xml string
        obj_xml = etree.tostring(root,
                                 pretty_print=True,
                                 xml_declaration=True)

        try:
            with open("test.xml", "wb") as xml_writer:
                xml_writer.write(obj_xml)
        except IOError:
            pass


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = Main(windowTitle='Login')
    app.exec_()
