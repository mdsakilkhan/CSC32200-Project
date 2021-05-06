import sys
from lxml import etree
from lxml import objectify
from PyQt5 import QtWidgets as qtw
from PyQt5.uic import loadUi

import Users
import Utilities as Utils

from LoginForm import Ui_LoginForm


class Main(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loginForm = LoginForm()

class Homepage(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = loadUI("Homepage.ui")

        # EDIT HERE**************************************************************************
        # Connect signals with slots (custom-defined methods)
        # Nana START





        # Nana END
        # Joshua START





        # Joshua END
        # Huihong START





        # Huihong END
        # Sakil START





        # Sakil END
        # EDIT HERE**************************************************************************

        self.ui.show()

    
    # EDIT HERE**************************************************************************

    # Define custom methods here. 
    # Nana START





    # Nana END
    # Joshua START





    # Joshua END
    # Huihong START





    # Huihong END
    # Sakil START





    # Sakil END
    # EDIT HERE**************************************************************************


class LoginForm(qtw.QDialog):
    def __init__(self):
        super().__init__()
        # Miscellaneous setup
        self.customer_dict = {} # Used to keep track of existing customers. Crucial for checking for existing users!
        self.ui = loadUi("LoginForm.ui")
        self.newUserForm = None

        # Connect signals and slots
        self.load_customers()
        self.ui.pButton_newUser.clicked.connect(self.__show_new_user_form)

        self.ui.show()

    def __show_new_user_form(self):
        self.newUserForm = NewUserForm(self)

    def load_customers(self):
    
        try:
            with open("Customers.xml") as file:
                xml = file.read()
                root_xml = objectify.fromstring(xml)
        except:
            print('No users exist')
            return

        customers_xml = root_xml.getchildren()
        self.cust_attrs = {}
        for customer in customers_xml:
            for attribute in customer.iter(): # Iterate through customer's attributes
                self.cust_attrs.update({attribute.tag: attribute.text})
            # Instantiate customer object
            incoming_cust = Users.Customer(first_name=self.cust_attrs.get('first_name'), 
                                           last_name=self.cust_attrs.get('last_name'), 
                                           date_of_birth=self.cust_attrs.get('date_of_birth'), 
                                           contact_num=self.cust_attrs.get('contact_num'), 
                                           email_address=self.cust_attrs.get('email_address'), 
                                           password=self.cust_attrs.get('password'),
                                           address=self.cust_attrs.get('address'),
                                           card_number=self.cust_attrs.get('card_number'), 
                                           bank=self.cust_attrs.get('bank'), 
                                           security_num=self.cust_attrs.get('security_num'), 
                                           balance=self.cust_attrs.get('balance'), 
                                           purchases=self.cust_attrs.get('purchases'), 
                                           cart=self.cust_attrs.get('cart'), 
                                           orders=self.cust_attrs.get('orders'))
            self.customer_dict.update({incoming_cust.id : incoming_cust})
        
        self.StoreClerks = []
        self.Vendors = []
        self.DeliveryCompanies = []


class NewUserForm(qtw.QDialog):
    def __init__(self, loginForm):
        super().__init__()
        # Save local reference to loginForm object
        self.loginForm = loginForm
        self.loginForm.ui.hide()
        self.ui = loadUi("newUserForm.ui")
        self.ui.pButton_create.setEnabled(False)
        # Connect signals and slots
        self.ui.lineEdit_emailAddress.textChanged.connect(self.__enable_create_button)
        self.ui.lineEdit_password.textChanged.connect(self.__enable_create_button)
        self.ui.lineEdit_confirmPassword.textChanged.connect(self.__enable_create_button)
        self.ui.lineEdit_firstName.textChanged.connect(self.__enable_create_button)
        self.ui.lineEdit_lastName.textChanged.connect(self.__enable_create_button)
        self.ui.lineEdit_DOB.textChanged.connect(self.__enable_create_button)
        self.ui.lineEdit_contactNumber.textChanged.connect(self.__enable_create_button)
        self.ui.lineEdit_address.textChanged.connect(self.__enable_create_button)
        self.ui.lineEdit_cardNumber.textChanged.connect(self.__enable_create_button)
        self.ui.lineEdit_bankName.textChanged.connect(self.__enable_create_button)
        self.ui.lineEdit_cvv.textChanged.connect(self.__enable_create_button)

        self.ui.pButton_create.clicked.connect(self.__create_customer)
        
        self.ui.show()

    def __enable_create_button(self):
        if (len(self.ui.lineEdit_emailAddress.text())
            and len(self.ui.lineEdit_password.text())
            and len(self.ui.lineEdit_confirmPassword.text())
            and len(self.ui.lineEdit_firstName.text())
            and len(self.ui.lineEdit_lastName.text())
            and len(self.ui.lineEdit_DOB.text())
            and len(self.ui.lineEdit_contactNumber.text())
            and len(self.ui.lineEdit_address.text())
            and len(self.ui.lineEdit_cardNumber.text())
            and len(self.ui.lineEdit_bankName.text())
            and len(self.ui.lineEdit_cvv.text())):
            self.ui.pButton_create.setEnabled(True)
        else:
            self.ui.pButton_create.setEnabled(False)

    def __create_customer(self):
        # Prepare popup message
        msg = qtw.QMessageBox()
        msg.setWindowTitle("Message")
        # Check if user already exists
        customer_already_exists = self.ui.lineEdit_emailAddress.text() in self.loginForm.customer_dict
        if (customer_already_exists):
            msg.setText("A customer has already been created with this email.")
            msg.setIcon(qtw.QMessageBox.Warning)
            x = msg.exec_()
            return
        # Check if password.text matches confirmPassowrd.text
        password_confirmed = self.ui.lineEdit_password.text() == self.ui.lineEdit_confirmPassword.text()
        if (not password_confirmed):
            msg.setText("Please make sure that password and confirm password match.")
            msg.setIcon(qtw.QMessageBox.Warning)
            x = msg.exec_()
            return                   
        else:
            # Prepare success message
            msg.setText("Account registration successful!")
            msg.setIcon(qtw.QMessageBox.Information)
            # Create root tag
            root = objectify.Element("Customers")
            # Append existing users 
            for c in self.loginForm.customer_dict.values():
                root.append(Utils.serialize_object(c))
            # Construct customer object
            customer = Users.Customer(email_address=self.ui.lineEdit_emailAddress.text(),
                                    password=self.ui.lineEdit_password.text(),
                                    first_name=self.ui.lineEdit_lastName.text(),
                                    last_name=self.ui.lineEdit_lastName.text(),
                                    date_of_birth=self.ui.lineEdit_DOB.text(),
                                    contact_num=self.ui.lineEdit_contactNumber.text(),
                                    address=self.ui.lineEdit_address.text(),
                                    card_number=self.ui.lineEdit_cardNumber.text(),
                                    bank=self.ui.lineEdit_bankName.text(),
                                    security_num=self.ui.lineEdit_cvv.text())
            root.append(Utils.serialize_object(customer))
            # remove lxml annotation
            objectify.deannotate(root)
            etree.cleanup_namespaces(root)
            # create the xml string
            obj_xml = etree.tostring(root, pretty_print=True, xml_declaration=True)
            try:
                with open("CustomersTemp.xml", "wb") as xml_writer:
                    xml_writer.write(obj_xml)
            except IOError:
                pass
            # Remove encoding declaration--was such a b*&%ch... 
            # The encoding declaration renders the lxml module unable to read it. Hence it had to be removed.
            Utils.remove_encoding_dec("CustomersTemp.xml","Customers.xml")
            # Refresh customers
            self.loginForm.load_customers()
            # Show success message
            x = msg.exec_()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = Main(windowTitle='Login')
    app.exec_()
