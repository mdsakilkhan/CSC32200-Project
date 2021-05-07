# Native and pip modules
import sys
from lxml import etree
from lxml import objectify
from PyQt5 import QtWidgets as qtw
from PyQt5.uic import loadUi
# Custom modules 
import Users
import Utilities as Utils
from LoginForm import Ui_LoginForm


class Main(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.homepage = Homepage()

class Homepage(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # EDIT HERE**************************************************************************
        
        # INITILIAZE MEMBER VAIRABLES
        self.ui = loadUi("Homepage.ui")
        # Nana START
        
        # Nana END
        # Joshua START
        self.customer_logged_in = False 
        self.current_customer = None # Current customer that is logged in
        self.customer_dict = {} # Key: Username | Value: Password. Crucial for checking for login!
        self.customer_list = [] # Used to keep track of existing customers.
        self.load_customers() # Populates customer_dict
        self.newUserForm = None
        # Joshua END

        # Huihong START
        self.loginForm = None

        # Huihong END
        # Sakil START

        # Sakil End
        




        # CONNECT SIGNALS AND SLOTS (CUSTOM DEFINED METHODS)
        # Nana START





        # Nana END
        # Joshua START
        self.ui.pButton_logIn.clicked.connect(self.goto_login_form)
        self.ui.pButton_register.clicked.connect(self.goto_new_user_form)


        # Joshua END
        # Huihong START





        # Huihong END
        # Sakil START





        # Sakil END
        # EDIT HERE**************************************************************************
        self.ui.show()    
    # EDIT HERE**************************************************************************

    # DEFINE CUSTOM METHODS HERE
    # Nana START





    # Nana END
    # Joshua START
    def goto_new_user_form(self):
        self.newUserForm = NewUserForm(self) # Pass in current instance of homepage

    def goto_login_form(self):
        self.loginForm = LoginForm(self.customer_dict)

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
            for attribute in customer.getchildren() : # Iterate through customer's attributes
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
            self.customer_dict.update({incoming_cust.id : incoming_cust.password})   
            self.customer_list.append(incoming_cust)  



    # Joshua END
    # Huihong START





    # Huihong END
    # Sakil START





    # Sakil END
    # EDIT HERE**************************************************************************


class LoginForm(qtw.QDialog):
    def __init__(self, customer_dict):
        super().__init__()
        # Initialize member variables       
        self.ui = loadUi("LoginForm.ui")
        self.customer_dict = customer_dict        
        self.username = None
        self.password = None

        # Connect signals and slots
        self.ui.pButton_login.clicked.connect(self.verify_login)
        self.ui.lineEdit_username.textChanged.connect(self.get_username)
        self.ui.lineEdit_password.textChanged.connect(self.get_password)

        self.ui.show()

    def get_username(self):
        self.username = self.ui.lineEdit_username.text()

    def get_password(self):
        self.password = self.ui.lineEdit_password.text()

    def verify_login(self):
        if (self.username in self.customer_dict.keys() 
            and self.password == self.customer_dict.get(self.username)):
            msg = qtw.QMessageBox.information(self, '', 'Login Successful')
        else:
            msg = qtw.QMessageBox.warning(self, '', 'Invalid Credentials')

class NewUserForm(qtw.QDialog):
    def __init__(self, homepage):
        super().__init__()
        # Save local reference to homepage object
        self.homepage = homepage
        self.homepage.ui.hide()
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
        self.ui.pButton_cancel.clicked.connect(self.__return_to_homepage)
        
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
        customer_already_exists = self.ui.lineEdit_emailAddress.text() in self.homepage.customer_dict
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
            for existing_customer in self.homepage.customer_list:
                root.append(Utils.serialize_object(existing_customer))
            # Construct customer object
            new_customer = Users.Customer(email_address=self.ui.lineEdit_emailAddress.text(),
                                    password=self.ui.lineEdit_password.text(),
                                    first_name=self.ui.lineEdit_lastName.text(),
                                    last_name=self.ui.lineEdit_lastName.text(),
                                    date_of_birth=self.ui.lineEdit_DOB.text(),
                                    contact_num=self.ui.lineEdit_contactNumber.text(),
                                    address=self.ui.lineEdit_address.text(),
                                    card_number=self.ui.lineEdit_cardNumber.text(),
                                    bank=self.ui.lineEdit_bankName.text(),
                                    security_num=self.ui.lineEdit_cvv.text())
            root.append(Utils.serialize_object(new_customer))
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
            self.homepage.load_customers()
            # Show success message
            x = msg.exec_()
            self.__return_to_homepage()

    def __return_to_homepage(self):
        self.homepage.ui.show()
        self.ui.close()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = Main(windowTitle='Computer Store')
    app.exec_()
