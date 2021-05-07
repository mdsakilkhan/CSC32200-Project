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
        self.id_pword_dict = {} # Key: id | Value: Password. Crucial for checking for login!
        self.id_customer_dict = {} # Used to keep track of existing customers.
        self.load_customers() # Populates id_pword_dict and id_customer_dict
        
        self.newUserForm = None
        self.ui.pButton_logOut.setDisabled(True)
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
        self.ui.pButton_logOut.clicked.connect(self.logout)

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
        self.loginForm = LoginForm(self)

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
            self.id_pword_dict.update({incoming_cust.id : incoming_cust.password})   
            self.id_customer_dict.update({incoming_cust.id : incoming_cust})
        return

    def logout(self):
        self.current_customer = None
        self.customer_logged_in = False
        self.ui.pButton_logIn.setEnabled(True)
        self.ui.pButton_logOut.setEnabled(False)
        self.enable_or_diable_register()
        msg = qtw.QMessageBox.information(self, '', 'Log out successful')

    def enable_or_diable_register(self):
        if self.customer_logged_in == False:
            self.ui.pButton_register.setEnabled(True)
        else:
            self.ui.pButton_register.setEnabled(False)
    # Joshua END
    # Huihong START





    # Huihong END
    # Sakil START





    # Sakil END
    # EDIT HERE**************************************************************************


class LoginForm(qtw.QDialog):
    def __init__(self, homepage):
        super().__init__()
        # Initialize member variables       
        self.ui = loadUi("LoginForm.ui")
        # Save reference to hompage object
        self.homepage = homepage        
        self.id = None
        self.password = None

        # Connect signals and slots
        self.ui.pButton_login.clicked.connect(self.verify_login)
        self.ui.lineEdit_username.textChanged.connect(self.get_username)
        self.ui.lineEdit_password.textChanged.connect(self.get_password)

        self.ui.show()

    def verify_login(self):
        if (self.id in self.homepage.id_pword_dict.keys() and self.password == self.homepage.id_pword_dict.get(self.id)):
            self.homepage.customer_logged_in = True
            self.homepage.current_customer = self.homepage.id_customer_dict.get(self.id)
            self.homepage.ui.pButton_logIn.setDisabled(True)
            self.homepage.ui.pButton_logOut.setDisabled(False)
            self.homepage.enable_or_diable_register()
            msg = qtw.QMessageBox.information(self, '', 'Login Successful')
            self.ui.close()
        else:
            msg = qtw.QMessageBox.warning(self, '', 'Invalid credentials, please try again.')

    def get_username(self):
        self.id = self.ui.lineEdit_username.text()

    def get_password(self):
        self.password = self.ui.lineEdit_password.text()

    

class NewUserForm(qtw.QDialog):
    def __init__(self, homepage):
        super().__init__()
        # Save local reference to homepage object
        self.homepage = homepage
        self.homepage.ui.hide()
        self.ui = loadUi("newUserForm.ui")
        self.ui.pButton_create.setEnabled(False)
        # Connect signals and slots
        self.ui.lineEdit_emailAddress.textChanged.connect(self.enable_create_button)
        self.ui.lineEdit_password.textChanged.connect(self.enable_create_button)
        self.ui.lineEdit_confirmPassword.textChanged.connect(self.enable_create_button)
        self.ui.lineEdit_firstName.textChanged.connect(self.enable_create_button)
        self.ui.lineEdit_lastName.textChanged.connect(self.enable_create_button)
        self.ui.lineEdit_DOB.textChanged.connect(self.enable_create_button)
        self.ui.lineEdit_contactNumber.textChanged.connect(self.enable_create_button)
        self.ui.lineEdit_address.textChanged.connect(self.enable_create_button)
        self.ui.lineEdit_cardNumber.textChanged.connect(self.enable_create_button)
        self.ui.lineEdit_bankName.textChanged.connect(self.enable_create_button)
        self.ui.lineEdit_cvv.textChanged.connect(self.enable_create_button)

        self.ui.pButton_create.clicked.connect(self.create_customer)
        self.ui.pButton_cancel.clicked.connect(self.return_to_homepage)
        
        self.ui.show()

    def enable_create_button(self):
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

    def create_customer(self):
        # Check if user already exists
        customer_already_exists = self.ui.lineEdit_emailAddress.text() in self.homepage.id_pword_dict
        if (customer_already_exists):
            msg = qtw.QMessageBox.information(self, '', 'A customer has already been created with this email.')
            return
        # Check if password.text matches confirmPassowrd.text
        password_confirmed = self.ui.lineEdit_password.text() == self.ui.lineEdit_confirmPassword.text()
        if (not password_confirmed):
            msg = qtw.QMessageBox.warning(self, '', 'Password and confirm password do not match.')
            return                   
        else:
            # Create root tag
            root = objectify.Element("Customers")
            # Append existing users 
            for existing_customer in self.homepage.id_customer_dict.values():
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
            msg = qtw.QMessageBox.information(self, '', 'User registration successful')
            self.return_to_homepage()

    def return_to_homepage(self):
        self.homepage.ui.show()
        self.ui.close()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = Main(windowTitle='Computer Store')
    app.exec_()
