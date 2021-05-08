# Native and pip modules
import os
import sys
from xml.etree import ElementTree
from lxml import etree
from lxml import objectify
from PyQt5 import QtCore, QtGui, QtWidgets as qtw
from PyQt5.uic import loadUi
# Custom modules 
import Users
import Utilities as Utils
from LoginForm import Ui_LoginForm

UserData_fileName = 'Users3.xml'
UserData_filePath = os.path.abspath(os.path.join('Data', UserData_fileName))
UserData_Tree = ElementTree.parse(UserData_filePath)
UserData_Root = UserData_Tree.getroot()

ItemData_fileName = 'Items.xml'
ItemData_filePath = os.path.abspath(os.path.join('Data', ItemData_fileName))
ItemData_Tree = ElementTree.parse(ItemData_filePath)
ItemData_Root = ItemData_Tree.getroot()

login_email = "email2"

firstName = ''
lastName = ''
userEmail = ''
userBalance = ''
bankName = ''
bankNumber = ''

cartList = None
historyList = None
trackList = None

for x in UserData_Root.find('Customers').findall('Customer'):
    if(x.get('id') == login_email):
        firstName = x.find('first_name').text
        lastName = x.find('last_name').text
        userEmail = x.find('email_address').text
        userBalance = x.find('balance').text
        bankName = x.find('bank').text
        bankNumber = x.find('card_number').text
        if(len(x.find('cart').findall('item'))>0):
            cartList = x.find('cart').findall('item')
        if(len(x.find('purchases').findall('item'))>0):
            historyList = x.find('purchases').findall('item')
        if(len(x.find('orders').findall('item'))>0):
            trackList = x.find('orders').findall('item')
class Main(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.homepage = Homepage()

class Homepage(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # EDIT HERE**************************************************************************
        
        # INITILIAZE MEMBER VAIRABLES
        self.ui = loadUi("UiFiles/Homepage.ui")
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

        listOfDicts = self.parse("Data/Items.xml")
       # print(listOfDicts)
        listOfItemCategories = self.returnItemCategories(listOfDicts)
        
        for itemName in listOfItemCategories:
            self.ui.listWidget_2.addItem(itemName)

       # self.ui.listWidget_2.item(0).connect(self.print)

        def print(self):
            print("Item 1 clicked")
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
        self.ui.label_currentlyVisiting.mouseReleaseEvent = self.test
        # Joshua END
        # Huihong START





        # Huihong END
        # Sakil START
        self.ui.pButton_account.clicked.connect(self.goto_account_page)




        # Sakil END
        # EDIT HERE**************************************************************************
        self.ui.show()    
    # EDIT HERE**************************************************************************

    # DEFINE CUSTOM METHODS HERE
    # Nana START
    def parse(self,xmlFile):

        with open(xmlFile) as opedml:
            xml = opedml.read().encode()
    
        root = etree.fromstring(xml)
        items_dict = {}
        itemsgotten = []
        for item in root.getchildren():
            for elem in item.getchildren():
                if elem.text:
                    text = elem.text
                items_dict[elem.tag] = text
            if item.tag == "Item":
                itemsgotten.append(items_dict)
                items_dict = {}
        return itemsgotten

    def returnItemCategories(self,itemsDict):
        listOfCategories = []
        for item in itemsDict:
            if (listOfCategories.count(item['item_type']) == 0):
                listOfCategories.append(item['item_type'])
        return listOfCategories

    # Nana END
    # Joshua START
    def test(self, event):
        print("label clicked")

    def goto_new_user_form(self):
        self.newUserForm = NewUserForm(self) # Pass in current instance of homepage

    def goto_login_form(self):
        self.loginForm = LoginForm(self)

    def load_customers(self):
        try:
            with open("Data/Customers.xml") as file:
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
        self.ui.label_currentlyVisiting.show()

    def enable_or_diable_register(self):
        if self.customer_logged_in == False:
            self.ui.pButton_register.setEnabled(True)
        else:
            self.ui.pButton_register.setEnabled(False)
    # Joshua END
    # Huihong START





    # Huihong END
    # Sakil START
    def goto_account_page(self):
        self.accountPage = AccountPage(self)




    # Sakil END
    # EDIT HERE**************************************************************************

class LoginForm(qtw.QDialog):
    def __init__(self, homepage):
        super().__init__()
        # Initialize member variables       
        self.ui = loadUi("UiFiles/LoginForm.ui")
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
            self.homepage.ui.label_currentlyVisiting.hide()
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
        self.ui = loadUi("UiFiles/newUserForm.ui")
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
                root.append(Utils.serialize_object(existing_customer, "Customer"))
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
            root.append(Utils.serialize_object(new_customer, "Customer"))
            # remove lxml annotation
            objectify.deannotate(root)
            etree.cleanup_namespaces(root)
            # create the xml string
            obj_xml = etree.tostring(root, pretty_print=True, xml_declaration=True)
            try:
                with open("Data/CustomersTemp.xml", "wb") as xml_writer:
                    xml_writer.write(obj_xml)
            except IOError:
                pass
            # Remove encoding declaration--was such a b*&%ch... 
            # The encoding declaration renders the lxml module unable to read it. Hence it had to be removed.
            Utils.remove_encoding_dec("Data/CustomersTemp.xml","Data/Customers.xml")
            # Refresh customers
            self.homepage.load_customers()
            # Show success message
            msg = qtw.QMessageBox.information(self, '', 'User registration successful')
            self.return_to_homepage()

    def return_to_homepage(self):
        self.homepage.ui.show()
        self.ui.close()

class AccountPage(qtw.QWidget):
    def __init__(self, homepage):
        super().__init__()
        # Create reference to homepage instance
        self.homepage = homepage
        self.homepage.ui.hide()
        self.ui = loadUi("UiFiles/accountPage.ui")
        
        try:
            for x in cartList:
                item = qtw.QListWidgetItem()
                self.ui.ProductList.addItem(item)
        except (AttributeError, TypeError):
            pass
        try:
             self.ui.ProductList.clicked.connect(self.list_clicked)
        except (TypeError):
            pass  
        # second try-catch
        try:
            for x in historyList:
                item = qtw.QListWidgetItem()
                self.ui.ProductList_h.addItem(item)
        except (AttributeError, TypeError, NameError):
            pass
        try:
             self.ui.ProductList_h.clicked.connect(self.list_h_clicked)
        except (TypeError):
            pass 
        # third try catch
        try:
            for x in trackList:
                item = qtw.QListWidgetItem()
                self.ui.ProductList_t.addItem(item)
        except (AttributeError, TypeError, NameError):
            pass


        # From retranslateui 
        _translate = QtCore.QCoreApplication.translate
        # self.setWindowTitle(_translate("AccountPage", "Computer Store : Account Page : " + firstName + ' ' + lastName))
        # self.setWindowIcon(QtGui.QIcon('Images/User/userIcon.png'))
        # 1st try- catch
        try:
            i = 0
            for x in cartList:
                item = self.ui.ProductList.item(0+i)
                for y in ItemData_Root.findall('Item'):
                    if(y.get('id') == x.text):
                        item.setText(_translate("AccountPage", x.text + ": " + y.find('item_name').text))
                i += 1
        except (AttributeError, TypeError):
            pass
        # second try catch
        try:
            i = 0
            for x in historyList:
                item = self.ui.ProductList_h.item(0+i)
                for y in ItemData_Root.findall('Item'):
                    if(y.get('id') == x.text):
                        item.setText(_translate("AccountPage", x.text + ": " + y.find('item_name').text + ' - ' + x.get('date')))
                i += 1
        except (AttributeError, TypeError):
            pass
        # third try catch
        try:
            i = 0
            for x in trackList:
                item = self.ui.ProductList_t.item(0+i)
                for y in ItemData_Root.findall('Item'):
                    if(y.get('id') == x.text):
                        item.setText(_translate("AccountPage", x.text + ": " + y.find('item_name').text + ' - Estimated arrival date: ' + x.get('date')))
                i += 1
        except (AttributeError, TypeError):
            pass
        if (trackList==None):
            self.TextBox.setText(_translate("AccountPage", "No Items Available"))
        self.ui.CustomerName.setText(_translate("AccountPage", firstName + ' ' + lastName))
        self.ui.BalanceData.setText(_translate("AccountPage", "Balance: $" + userBalance + ' ' + bankName + 'Bank ' + bankNumber))
        self.ui.CustomerInfo.setText(_translate("AccountPage", userEmail))


        # Connect signals and slots
        self.ui.RemoveFromList.clicked.connect(self.RemoveFromList_clicked)
        self.ui.Checkout.clicked.connect(self.Checkout_clicked)
        self.ui.CashIn.clicked.connect(self.CashIn_clicked)
        self.ui.CashOut.clicked.connect(self.CashOut_clicked)
        self.ui.ReviewProduct.clicked.connect(self.ReviewProduct_clicked)
        self.ui.BuyAgain.clicked.connect(self.BuyAgain_clicked)
        self.ui.CancelOrder.clicked.connect(self.CancelOrder_clicked)
        self.ui.Logout.clicked.connect(self.Logout_clicked)
    
        self.ui.show()

    # Slots go here
    def list_clicked(self):
        item = self.ui.ProductList.currentItem()
        product_num = item.text()[0:3]
        for x in ItemData_Root.findall('Item'):
            if(x.get('id') == product_num):
                self.ItemPrice.setText("$" + x.find('item_price').text)
                self.ItemRating.setText("Rating: " + x.find('item_rating').text)
                self.ItemImage.setPixmap(QtGui.QPixmap("Images/Item/" + product_num + ".jpg"))
                
    def list_h_clicked(self):
        item = self.ui.ProductList_h.currentItem()
        product_num = item.text()[0:3]
        for x in ItemData_Root.findall('Item'):
            if(x.get('id') == product_num):
                self.ItemPrice_h.setText("$" + x.find('item_price').text)
                self.ItemImage_h.setPixmap(QtGui.QPixmap("Images/Item/" + product_num + ".jpg"))

    def RemoveFromList_clicked(self):
        item = self.ui.ProductList.currentItem()
        if(item==None):
            self.ui.ProductList.setCurrentRow(0)
            item = self.ui.ProductList.currentItem()
        product_num = item.text()[0:3]
        for x in UserData_Root.find('Customers').findall('.//Customer'):
            if(x.get('id')==userEmail):
                for y in x.find('cart').findall('.//item'):
                    if(y.text == product_num):
                        x.find('cart').remove(y)
                        UserData_Tree.write('new.xml')
                        item = self.ui.ProductList.currentItem()
                        self.ui.ProductList.takeItem(self.ui.ProductList.row(item))
                        print("item removed")

    def CashIn_clicked(self):
        user_input = self.BalanceInput.text()
        if(user_input==""):
            user_input = "0"
        num = bankNumber[0:4]+"*"
        self.BalanceOutput.setText("$" + user_input + ' added from ' + bankName + ' Bank ' + num)

    def CashOut_clicked(self):
        user_input = self.BalanceInput.text()
        if(user_input==""):
            user_input = "0"
        num = bankNumber[0:4]+"*"
        self.BalanceOutput.setText("$" + user_input + ' sent to ' + bankName + ' Bank ' + num)

    def Checkout_clicked(self):
        pass
        #goto transaction page

    def ReviewProduct_clicked(self):
        item = self.ui.ProductList_h.currentItem()
        product_num = item.text()[0:3]
        #goto discussion page

    def BuyAgain_clicked(self):
        item = self.ui.ProductList_h.currentItem()
        if(item==None):
            self.ui.ProductList_h.setCurrentRow(0)
            item = self.ui.ProductList_h.currentItem()
        product_num = item.text()[0:3]
        for x in UserData_Root.find('Customers').findall('.//Customer'):
            if(x.get('id')==userEmail):
                for y in x.find('purchases').findall('.//item'):
                    if(y.text == product_num):
                        _translate = QtCore.QCoreApplication.translate
                        product = ElementTree.SubElement(x.find('cart'), "item")
                        product.text = product_num
                        UserData_Tree.write('new.xml')
                        item = qtw.QListWidgetItem()
                        self.ui.ProductList.addItem(item)
                        item.setText(_translate("AccountPage", product_num + ": " + "name"))
                        print("item added to cart")
                        #goto transaction page

    def CancelOrder_clicked(self):
        item = self.ui.ProductList_t.currentItem()
        if(item==None):
            self.ui.ProductList_t.setCurrentRow(0)
            item = self.ui.ProductList_t.currentItem()
        product_num = item.text()[0:3]
        for x in UserData_Root.find('Customers').findall('.//Customer'):
            if(x.get('id')==userEmail):
                for y in x.find('orders').findall('.//item'):
                    if(y.text == product_num):
                        x.find('orders').remove(y)
                        UserData_Tree.write('new.xml')
                        item = self.ui.ProductList_t.currentItem()
                        self.ui.ProductList_t.takeItem(self.ui.ProductList_t.row(item))
                        print("order canceled")

    def Logout_clicked(self):
        self.ui.hide()
        self.homepage.ui.show()
        #goto main page

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = Main(windowTitle='Computer Store')
    app.exec_()
