# Native and pip modules
import os
import sys
from xml.etree import ElementTree
from lxml import etree
from lxml import objectify
from PyQt5 import QtCore as qtc, QtGui, QtWidgets as qtw
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
        self.ui = loadUi("UiFiles/Homepage.ui")
        # Nana START
        self.componentPic = ["100.jpg","101.jpg","102.jpg","103.jpg","104.jpg","105.jpg","106.jpg","107.jpg","108.jpg","109.jpg","110.jpg","111.jpg","112.jpg","113.jpg","114.jpg","115.jpg","116.jpg","117.jpg","118.jpg","119.jpg","120.jpg","121.jpg","122.jpg","123.jpg","124.jpg","125.jpg","126.jpg","127.jpg","128.jpg","129.jpg","130.jpg",]
        self.items_path = os.path.abspath("Data/Items.xml")
        self.pathOfCommentsXML = os.path.abspath("Data/comments.xml")
        self.listOfDicts = self.parse(self.items_path)

        self.listofCommentsDicts = self.parseXMLforComments(self.pathOfCommentsXML)
        self.commentsAboutItems = self.returnlistOfCertainComments('item')
        
        
        self.commentsAboutCompanies = self.returnlistOfCertainComments('company')
        self.commentsaboutClerks = self.returnlistOfCertainComments('clerk')
      
        listOfItemCategories = self.returnItemCategories(self.listOfDicts)
        
       
        for itemName in listOfItemCategories:
            self.ui.listWidget_2.addItem(itemName)
            self.ui.ItemCategory.addItem(itemName)

        self.ui.listWidget_2.itemClicked.connect(self.showItemsInListView)

        self.ui.listWidget_3.itemClicked.connect(self.showImagesandDescription)
        
        self.ui.ItemCategory.itemClicked.connect(self.showItemsInSecondListView)

        self.ui.PartList.itemClicked.connect(self.showItemComment)
        # Nana END
        # Joshua START
        self.clerk_logged_in = False
        self.manager_logged_in = False
        self.customer_logged_in = False 
        self.current_customer = None # Current customer that is logged in 
        # self.current_customer = self.id_customer_dict.get("sakil@gmail.com") # to test account page
        self.id_pword_dict = {} # Key: id | Value: Password. Crucial for checking for login!
        self.id_customer_dict = {} # Key: id | Value: Customer. Used to keep track of existing customers.
        self.load_customers() # Populates id_pword_dict and id_customer_dict
        self.newUserForm = None
        self.ui.pButton_logOut.setDisabled(True)
        self.ui.pButton_account.setDisabled(True)
        self.avoidList = None
        # Joshua END

        


   
        # Huihong START
        self.loginForm = None

        # Huihong END     




        # CONNECT SIGNALS AND SLOTS (CUSTOM DEFINED METHODS)
        # Nana START





        # Nana END
        # Joshua START
        self.ui.pButton_logIn.clicked.connect(self.goto_login_form)
        self.ui.pButton_register.clicked.connect(self.goto_new_user_form)
        self.ui.pButton_logOut.clicked.connect(self.logout)
        self.ui.pButton_deliverySystem.clicked.connect(self.test)
        self.ui.pButton_avoidList.clicked.connect(self.goto_avoid_list)
        # Joshua END
        # Huihong START





        # Huihong END
        # Sakil START
        
        self.UserData_fileName = 'Customers.xml'
        self.UserData_filePath = os.path.abspath(os.path.join('Data', self.UserData_fileName))
        self.UserData_Tree = ElementTree.parse(self.UserData_filePath)
        self.UserData_Root = self.UserData_Tree.getroot()

        self.ItemData_fileName = 'Items.xml'
        self.ItemData_filePath = os.path.abspath(os.path.join('Data', self.ItemData_fileName))
        self.ItemData_Tree = ElementTree.parse("Data/Items.xml")
        self.ItemData_Root = self.ItemData_Tree.getroot()

        self.cartList = None
        self.historyList = None
        self.trackList = None
        
        tempArr = []
        for x in self.ItemData_Root:
            tempArr.append(int(x.find('item_sold').text))
        tempArr.sort()

        self.mostPop = []
        for x in self.ItemData_Root:
            if(x.find('item_sold').text == str(tempArr[len(tempArr)-1])):
                self.mostPop.append(x.get('id'))
        for x in self.ItemData_Root:
            if(x.find('item_sold').text == str(tempArr[len(tempArr)-2])):
                self.mostPop.append(x.get('id'))
        for x in self.ItemData_Root:
            if(x.find('item_sold').text == str(tempArr[len(tempArr)-3])):
                self.mostPop.append(x.get('id'))
        self.adminRec = ["116","104","127"]

        for y in self.ItemData_Root.findall('Item'):
            if(y.get('id') == self.mostPop[0]):
                self.ui.ItemInfo.setText("$ " + y.find('item_price').text + "   " + y.find('item_name').text)
        self.ui.ItemImage.setPixmap(QtGui.QPixmap("Images/Item/" + self.mostPop[0] + ".jpg"))
        for y in self.ItemData_Root.findall('Item'):
            if(y.get('id') == self.mostPop[1]):
                self.ui.ItemInfo_2.setText("$ " + y.find('item_price').text + "   " + y.find('item_name').text)
        self.ui.ItemImage_2.setPixmap(QtGui.QPixmap("Images/Item/" + self.mostPop[1] + ".jpg"))
        for y in self.ItemData_Root.findall('Item'):
            if(y.get('id') == self.mostPop[2]):
                self.ui.ItemInfo_3.setText("$ " + y.find('item_price').text + "   " + y.find('item_name').text)
        self.ui.ItemImage_3.setPixmap(QtGui.QPixmap("Images/Item/" + self.mostPop[2] + ".jpg"))
        for y in self.ItemData_Root.findall('Item'):
            if(y.get('id') == self.adminRec[0]):
                self.ui.ItemInfo_4.setText("$ " + y.find('item_price').text + "   " + y.find('item_name').text)
        self.ui.ItemImage_4.setPixmap(QtGui.QPixmap("Images/Item/" + self.adminRec[0] + ".jpg"))
        for y in self.ItemData_Root.findall('Item'):
            if(y.get('id') == self.adminRec[1]):
                self.ui.ItemInfo_5.setText("$ " + y.find('item_price').text + "   " + y.find('item_name').text)
        self.ui.ItemImage_5.setPixmap(QtGui.QPixmap("Images/Item/" + self.adminRec[1] + ".jpg"))
        for y in self.ItemData_Root.findall('Item'):
            if(y.get('id') == self.adminRec[2]):
                self.ui.ItemInfo_6.setText("$ " + y.find('item_price').text + "   " + y.find('item_name').text)
        self.ui.ItemImage_6.setPixmap(QtGui.QPixmap("Images/Item/" + self.adminRec[2] + ".jpg"))

        self.ui.pButton_account.clicked.connect(self.goto_account_page)
        self.ui.pushButton.clicked.connect(self.buy_1)
        self.ui.pushButton_2.clicked.connect(self.buy_2)
        self.ui.pushButton_3.clicked.connect(self.buy_3)
        self.ui.pushButton_4.clicked.connect(self.buy_4)
        self.ui.pushButton_5.clicked.connect(self.buy_5)
        self.ui.pushButton_6.clicked.connect(self.buy_6)

        self.ui.pushButton_9.clicked.connect(self.AddCart_Parts)
        self.ui.pushButton_7.clicked.connect(self.AddCart_PreBuild)

        # Sakil END
        # EDIT HERE**************************************************************************
        self.ui.show()    
    # EDIT HERE**************************************************************************

    # DEFINE CUSTOM METHODS HERE

    # Sakil START
    def buy_1(self):
        try:
            self.UserData_fileName = 'Customers.xml'
            self.UserData_filePath = os.path.abspath(os.path.join('Data', self.UserData_fileName))
            self.UserData_Tree = ElementTree.parse(self.UserData_filePath)
            self.UserData_Root = self.UserData_Tree.getroot()
            product_num = self.mostPop[0]
            for x in self.UserData_Root.findall('.//Customer'):
                if(x.find('id').text==self.current_customer.email_address):
                    product = ElementTree.SubElement(x.find('cart'), "item")
                    product.text = product_num
                    self.UserData_Tree.write('Data/Customers.xml') 
                    self.ui.label_17.setText("Item added to cart")
        except (AttributeError):
            self.ui.label_17.setText("You need to login to buy")
                
    def buy_2(self):
        try:
            self.UserData_fileName = 'Customers.xml'
            self.UserData_filePath = os.path.abspath(os.path.join('Data', self.UserData_fileName))
            self.UserData_Tree = ElementTree.parse(self.UserData_filePath)
            self.UserData_Root = self.UserData_Tree.getroot()
            product_num = self.mostPop[1]
            for x in self.UserData_Root.findall('.//Customer'):
                if(x.find('id').text==self.current_customer.email_address):
                    product = ElementTree.SubElement(x.find('cart'), "item")
                    product.text = product_num
                    self.UserData_Tree.write('Data/Customers.xml') 
                    self.ui.label_17.setText("Item added to cart")
        except (AttributeError):
            self.ui.label_17.setText("You need to login to buy")
                
    def buy_3(self):
        try:
            self.UserData_fileName = 'Customers.xml'
            self.UserData_filePath = os.path.abspath(os.path.join('Data', self.UserData_fileName))
            self.UserData_Tree = ElementTree.parse(self.UserData_filePath)
            self.UserData_Root = self.UserData_Tree.getroot()
            product_num = self.mostPop[2]
            for x in self.UserData_Root.findall('.//Customer'):
                if(x.find('id').text==self.current_customer.email_address):
                    product = ElementTree.SubElement(x.find('cart'), "item")
                    product.text = product_num
                    self.UserData_Tree.write('Data/Customers.xml') 
                    self.ui.label_17.setText("Item added to cart")
        except (AttributeError):
            self.ui.label_17.setText("You need to login to buy")
                
    def buy_4(self):
        try:
            self.UserData_fileName = 'Customers.xml'
            self.UserData_filePath = os.path.abspath(os.path.join('Data', self.UserData_fileName))
            self.UserData_Tree = ElementTree.parse(self.UserData_filePath)
            self.UserData_Root = self.UserData_Tree.getroot()
            product_num = self.adminRec[0]
            for x in self.UserData_Root.findall('.//Customer'):
                if(x.find('id').text==self.current_customer.email_address):
                    product = ElementTree.SubElement(x.find('cart'), "item")
                    product.text = product_num
                    self.UserData_Tree.write('Data/Customers.xml') 
                    self.ui.label_17.setText("Item added to cart")
        except (AttributeError):
            self.ui.label_17.setText("You need to login to buy")
                
    def buy_5(self):
        try:
            self.UserData_fileName = 'Customers.xml'
            self.UserData_filePath = os.path.abspath(os.path.join('Data', self.UserData_fileName))
            self.UserData_Tree = ElementTree.parse(self.UserData_filePath)
            self.UserData_Root = self.UserData_Tree.getroot()
            product_num = self.adminRec[1]
            for x in self.UserData_Root.findall('.//Customer'):
                if(x.find('id').text==self.current_customer.email_address):
                    product = ElementTree.SubElement(x.find('cart'), "item")
                    product.text = product_num
                    self.UserData_Tree.write('Data/Customers.xml') 
                    self.ui.label_17.setText("Item added to cart")
        except (AttributeError):
            self.ui.label_17.setText("You need to login to buy")
                
    def buy_6(self):
        try:
            self.UserData_fileName = 'Customers.xml'
            self.UserData_filePath = os.path.abspath(os.path.join('Data', self.UserData_fileName))
            self.UserData_Tree = ElementTree.parse(self.UserData_filePath)
            self.UserData_Root = self.UserData_Tree.getroot()
            product_num = self.adminRec[2]
            for x in self.UserData_Root.findall('.//Customer'):
                if(x.find('id').text==self.current_customer.email_address):
                    product = ElementTree.SubElement(x.find('cart'), "item")
                    product.text = product_num
                    self.UserData_Tree.write('Data/Customers.xml') 
                    self.ui.label_17.setText("Item added to cart")
        except (AttributeError):
            self.ui.label_17.setText("You need to login to buy")

    def AddCart_Parts(self):
        try:
            self.UserData_fileName = 'Customers.xml'
            self.UserData_filePath = os.path.abspath(os.path.join('Data', self.UserData_fileName))
            self.UserData_Tree = ElementTree.parse(self.UserData_filePath)
            self.UserData_Root = self.UserData_Tree.getroot()
            product_num = None
            for x in self.ItemData_Root:
                if(x.find('item_name').text == self.ui.listWidget_3.currentItem().text()):
                    product_num = x.get('id')
            for x in self.UserData_Root.findall('.//Customer'):
                if(x.find('id').text == self.current_customer.email_address):
                    product = ElementTree.SubElement(x.find('cart'), "item")
                    product.text = product_num
                    self.UserData_Tree.write('Data/Customers.xml') 
                    self.ui.label_17.setText("Item added to cart")
        except (AttributeError):
            print("You need to login to buy")
            
    def AddCart_PreBuild(self):
        try:
            self.UserData_fileName = 'Customers.xml'
            self.UserData_filePath = os.path.abspath(os.path.join('Data', self.UserData_fileName))
            self.UserData_Tree = ElementTree.parse(self.UserData_filePath)
            self.UserData_Root = self.UserData_Tree.getroot()
            product_num = None
            for x in self.ItemData_Root:
                if(x.find('item_name').text == self.ui.listWidget.currentItem().text()):
                    product_num = x.get('id')
            for x in self.UserData_Root.findall('.//Customer'):
                if(x.find('id').text == self.current_customer.email_address):
                    product = ElementTree.SubElement(x.find('cart'), "item")
                    product.text = product_num
                    self.UserData_Tree.write('Data/Customers.xml') 
                    self.ui.label_17.setText("Item added to cart")
        except (AttributeError):
            print("You need to login to buy")
                
    # Sakil END

    # Nana START
    def showItemsInListView(self):
        itemName = self.ui.listWidget_2.currentItem().text()
        listofItems = self.returnListOfDictItems(itemName,self.listOfDicts)
        self.ui.listWidget_3.clear()
        for item in listofItems:
            self.ui.listWidget_3.addItem(item['item_name'])

    def showItemsInSecondListView(self):
        itemName = self.ui.ItemCategory.currentItem().text()
        listofItems = self.returnListOfDictItems(itemName,self.listOfDicts)
        self.ui.PartList.clear()
        for item in listofItems:
            self.ui.PartList.addItem(item['item_name'])

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
            items_dict['id'] = item.attrib['id']
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
    
    #returns list of items that matches category
    def returnListOfDictItems(self,itemCategory,itemDictList):
        listOfItems = []
        for items in itemDictList:
            if items['item_type'] == itemCategory:
                listOfItems.append(items)
        return listOfItems
    
    #want to return dictionary of that item
    def returnSpecificItemByName(self,itemName):
        itemdict = {}
        for item in self.listOfDicts:
            if (item['item_name'] == itemName):
                itemdict = item
        return itemdict

    def showImagesandDescription(self):
        itemPicked = self.ui.listWidget_3.currentItem().text()
        specificItem = self.returnSpecificItemByName(itemPicked) # will be that item

        itemId = specificItem['id'] # the itemItem
        targetImage = ""
        for pic in self.componentPic:
            if itemId in pic:
                targetImage = pic
        
        pixString = "Images/Item/" + targetImage
        pixImage = QtGui.QPixmap(pixString)
        scaledPix = pixImage.scaled(150,150)
        self.ui.label_11.setPixmap(scaledPix)

        #now descriptuonn..
        for item in self.listOfDicts:
            if (item['item_name'] == itemPicked):
                    itemPrice = item['item_price']
                    itemRating = item['item_rating']
        
        DescriptionString = "Price: " + itemPrice +  "\n Rating: " + itemRating
        self.ui.plainTextEdit_2.clear()
        self.ui.plainTextEdit_2.appendPlainText(DescriptionString)

        #find the id of that item?
    def parseXMLforComments(self,xmlFile):
        with open(xmlFile) as opedml:
            xml = opedml.read().encode()
        
        root = etree.fromstring(xml)
        comment_dict = {}
        commentsgotten = []
        for item in root.getchildren():
            for elem in item.getchildren():
                if elem.text:
                    text = elem.text
                comment_dict[elem.tag] = text
            if item.tag == "Comment":
                commentsgotten.append(comment_dict)
                comment_dict = {}
        return commentsgotten

    def returnlistOfCertainComments(self,identifier):

        listofCertainComments = []
        for comment in self.listofCommentsDicts:
            if identifier in comment:
                listofCertainComments.append(comment)
        return listofCertainComments


    def showItemComment(self):
        itemSelected = self.ui.PartList.currentItem().text()
        userName = ""
        commentString = ""
        self.ui.commentList.clear()
        for comment in self.commentsAboutItems:
            if itemSelected in comment.values():
                userName = comment["customer_name"]
                commentString = comment["description"]
                fullString = "Name: " + userName + "\nComment " + commentString
                #print(fullString)
                self.ui.commentList.addItem(fullString)
                userName = ""
                commentStirng = ""
        

    # Nana END
    # Joshua START
    def test(self, event):
        self.transactionPage = TransactionPage(self)

    def goto_new_user_form(self):
        self.newUserForm = NewUserForm(self) # Pass in current instance of homepage

    def goto_login_form(self):
        self.loginForm = LoginForm(self)

    def goto_avoid_list(self):
        self.avoidList = AvoidList()

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
                purchases = []
                cart = []
                orders = []
                if attribute.tag == "purchases" and len(attribute):
                    for item in attribute.getchildren():
                        itemWithDate = Users.ItemWithDate()
                        itemWithDate.id = item.text
                        itemWithDate.date = item.get('date')
                        purchases.append(itemWithDate)
                    self.cust_attrs.update({attribute.tag: purchases})
                elif attribute.tag == "cart" and len(attribute):
                    for item in attribute.getchildren():
                        itemWithDate = Users.ItemWithDate()
                        itemWithDate.id = item.text
                        cart.append(itemWithDate)
                    self.cust_attrs.update({attribute.tag: cart})
                elif attribute.tag == "orders" and len(attribute):
                    for item in attribute.getchildren():
                        itemWithDate = Users.ItemWithDate()
                        itemWithDate.id = item.text
                        itemWithDate.date = item.get('date')
                        orders.append(itemWithDate)
                    self.cust_attrs.update({attribute.tag: orders})
                else:
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
        self.ui.pButton_account.setEnabled(False)
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

class SelectUserForm(qtw.QWidget):
    def __init__(self, homepage):
        super().__init__()
        # Initialize member variables       
        self.ui = loadUi("UiFiles/SelectUserForm.ui")
        # Save reference to hompage object
        self.homepage = homepage

        # Connect signals and slots
        
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
            self.homepage.ui.pButton_account.setDisabled(False)
            self.homepage.enable_or_diable_register()
            msg = qtw.QMessageBox.information(self, '', 'Login Successful')
            '''
            for x in self.homepage.UserData_Root.findall('Customer'):
                if(x.get('id') == self.homepage.current_customer.id):
                    if(len(x.find('cart').findall('item'))>0):
                        self.cartList = x.find('cart').findall('item')
                    if(len(x.find('purchases').findall('item'))>0):
                        self.self.historyList = x.find('purchases').findall('item')
                    if(len(x.find('orders').findall('item'))>0):
                        trackList = x.find('orders').findall('item')
            '''            
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
        # Check avoid list
        avoid_dict = self.check_avoid_dict()
        email = self.ui.lineEdit_emailAddress.text() 
        if (avoid_dict.get(email) != None):
            msg = qtw.QMessageBox.information(self, '', 'This email has been suspended. Please contact a manager.')
            return
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

    def check_avoid_dict(self):
        AvoidList_fileName = 'AvoidList.xml'
        AvoidList_filePath = os.path.abspath(os.path.join('Data', AvoidList_fileName))
        AvoidList_Tree = ElementTree.parse(AvoidList_filePath)
        AvoidList_Root = AvoidList_Tree.getroot()
        avoid_dict = {}
        for child in AvoidList_Root:
            avoid_dict.update({child.get("email"): child.get("email")})
        return avoid_dict

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
        
        _translate = qtc.QCoreApplication.translate
        
        self.UserData_fileName = 'Customers.xml'
        self.UserData_filePath = os.path.abspath(os.path.join('Data', self.UserData_fileName))
        self.UserData_Tree = ElementTree.parse(self.UserData_filePath)
        self.UserData_Root = self.UserData_Tree.getroot()

        self.ItemData_fileName = 'Items.xml'
        self.ItemData_filePath = os.path.abspath(os.path.join('Data', self.ItemData_fileName))
        self.ItemData_Tree = ElementTree.parse(self.ItemData_filePath)
        self.ItemData_Root = self.ItemData_Tree.getroot()

        self.login_email = homepage.current_customer.email_address

        self.firstName = homepage.current_customer.first_name
        self.lastName = homepage.current_customer.last_name
        self.userEmail = homepage.current_customer.email_address
        self.userBalance = homepage.current_customer.balance
        self.bankName = homepage.current_customer.bank
        self.bankNumber = homepage.current_customer.card_number

        self.cartList = None
        self.historyList = None
        self.trackList = None

        for x in self.UserData_Root.findall('Customer'):
            if(x.find('id').text == self.login_email):
                if(len(x.find('cart').findall('item'))>0):
                    self.cartList = x.find('cart').findall('item')
                if(len(x.find('purchases').findall('item'))>0):
                    self.historyList = x.find('purchases').findall('item')
                if(len(x.find('orders').findall('item'))>0):
                    self.trackList = x.find('orders').findall('item')
        
        try:
            for x in self.cartList:
                item = qtw.QListWidgetItem()
                self.ui.ProductList.addItem(item)
        except (AttributeError, TypeError):
            pass
        try:
             self.ui.ProductList.clicked.connect(self.list_clicked)
        except (TypeError):
            pass  
        try:
            i = 0
            for x in self.cartList:
                item = self.ui.ProductList.item(0+i)
                for y in self.ItemData_Root.findall('Item'):
                    if(y.get('id') == x.text):
                        item.setText(_translate("AccountPage", x.text + ": " + y.find('item_name').text))
                i += 1
        except (AttributeError, TypeError):
            pass

        try:
            for x in self.historyList:
                item = qtw.QListWidgetItem()
                self.ui.ProductList_h.addItem(item)
        except (AttributeError, TypeError, NameError):
            pass
        try:
             self.ui.ProductList_h.clicked.connect(self.list_h_clicked)
        except (TypeError):
            pass 
        try:
            i = 0
            for x in self.historyList:
                item = self.ui.ProductList_h.item(0+i)
                for y in self.ItemData_Root.findall('Item'):
                    if(y.get('id') == x.text):
                        item.setText(_translate("AccountPage", x.text + ": " + y.find('item_name').text + " - " + x.get('date')))
                i += 1
        except (AttributeError, TypeError):
            pass

        try:
            for x in self.trackList:
                item = qtw.QListWidgetItem()
                self.ui.ProductList_t.addItem(item)
        except (AttributeError, TypeError, NameError):
            pass
        try:
             self.ui.ProductList_t.clicked.connect(self.list_t_clicked)
        except (TypeError):
            pass 
        try:
            i = 0
            for x in self.trackList:
                item = self.ui.ProductList_t.item(0+i)
                for y in self.ItemData_Root.findall('Item'):
                    if(y.get('id') == x.text):
                        item.setText(_translate("AccountPage", x.text + ": " + y.find('item_name').text))
                i += 1
        except (AttributeError, TypeError):
            pass

        # From retranslateui 
        self.ui.setWindowTitle(_translate("AccountPage", "Computer Store : Account Page : " + self.firstName + ' ' + self.lastName))
        self.ui.setWindowIcon(QtGui.QIcon('Images/User/userIcon.png'))        
        self.ui.CustomerName.setText(_translate("AccountPage", self.firstName + ' ' + self.lastName))
        self.ui.BalanceData.setText(_translate("AccountPage", "Balance: $" + self.userBalance))
        self.ui.CustomerInfo.setText(_translate("AccountPage", self.login_email))
        self.ui.CustomerIcon.setPixmap(QtGui.QPixmap("Images/User/userIcon.png"))
        self.ui.ItemImage.setText(_translate("AccountPage", "Select Item"))
        self.ui.ItemImage_h.setText(_translate("AccountPage", "Select Item"))
        self.ui.TextBox.setText(_translate("AccountPage", "Select Item"))
        
        if (self.cartList==None):
            self.ui.ItemImage.setText(_translate("AccountPage", "No Items Available"))
        if (self.historyList==None):
            self.ui.ItemImage_h.setText(_translate("AccountPage", "No Items Available"))
        if (self.trackList==None):
            self.ui.TextBox.setText(_translate("AccountPage", "No Items Available"))
        
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
        for x in self.ItemData_Root.findall('Item'):
            if(x.get('id') == product_num):
                self.ui.ItemPrice.setText("$" + x.find('item_price').text)
                self.ui.ItemRating.setText("Rating: " + x.find('item_rating').text)
                self.ui.ItemImage.setPixmap(QtGui.QPixmap("Images/Item/" + product_num + ".jpg"))
    
    def list_h_clicked(self):
        item = self.ui.ProductList_h.currentItem()
        product_num = item.text()[0:3]
        for x in self.ItemData_Root.findall('Item'):
            if(x.get('id') == product_num):
                self.ui.ItemPrice_h.setText("$" + x.find('item_price').text)
                self.ui.ItemImage_h.setPixmap(QtGui.QPixmap("Images/Item/" + product_num + ".jpg"))

    def list_t_clicked(self):
        _translate = qtc.QCoreApplication.translate
        item = self.ui.ProductList_t.currentItem()
        product_num = item.text()[0:3]
        for x in self.trackList:
            if(x.text == product_num):
                self.ui.TextBox.setText(_translate("AccountPage", "Estimated arrival date: " + x.get('date')))

    def CashIn_clicked(self):
        self.UserData_fileName = 'Customers.xml'
        self.UserData_filePath = os.path.abspath(os.path.join('Data', self.UserData_fileName))
        self.UserData_Tree = ElementTree.parse(self.UserData_filePath)
        self.UserData_Root = self.UserData_Tree.getroot()
        balance = float(self.userBalance)
        try:
            user_input = float(self.ui.BalanceInput.text())
        except (ValueError):
            user_input = 0.0
        if(user_input>20000):
            self.ui.BalanceOutput.setText("Unsucessful: Not enough balance in " + self.bankName + ' Bank ' + self.bankNumber[0:4] + '*')
        else:
            self.userBalance = str(round((balance+user_input), 2))
            self.ui.BalanceData.setText("Balance: $" + self.userBalance)
            self.ui.BalanceOutput.setText("Sucessful: $" + str(user_input) + ' added from ' + self.bankName + ' Bank ' + self.bankNumber[0:4] + '*')
            for x in self.UserData_Root.findall('.//Customer'):
                if(x.find('id').text==self.login_email):
                    x.find('balance').text = self.userBalance
                    self.UserData_Tree.write('Data/Customers.xml') 

    def CashOut_clicked(self):
        self.UserData_fileName = 'Customers.xml'
        self.UserData_filePath = os.path.abspath(os.path.join('Data', self.UserData_fileName))
        self.UserData_Tree = ElementTree.parse(self.UserData_filePath)
        self.UserData_Root = self.UserData_Tree.getroot()
        balance = float(self.userBalance)
        try:
            user_input = float(self.ui.BalanceInput.text())
        except (ValueError):
            user_input = 0.0
        if(user_input>balance):
            self.ui.BalanceOutput.setText("Unsucessful: Not enough balance in account")
        else:
            self.userBalance = str(round((balance-user_input), 2))
            self.ui.BalanceData.setText("Balance: $" + self.userBalance)
            self.ui.BalanceOutput.setText("Sucessful: $" + str(user_input) + ' sent to ' + self.bankName + ' Bank ' + self.bankNumber[0:4] + '*')
            for x in self.UserData_Root.findall('.//Customer'):
                if(x.find('id').text==self.login_email):
                    x.find('balance').text = self.userBalance
                    self.UserData_Tree.write('Data/Customers.xml') 

    def Checkout_clicked(self):
        #self.ui.hide()
        self.homepage.test(self.homepage)
        #goto transaction page

    def ReviewProduct_clicked(self):
        self.ui.hide()
        self.homepage.ui.tabWidget.setCurrentIndex(3)
        self.homepage.ui.show()
    
    def RemoveFromList_clicked(self):
        self.UserData_fileName = 'Customers.xml'
        self.UserData_filePath = os.path.abspath(os.path.join('Data', self.UserData_fileName))
        self.UserData_Tree = ElementTree.parse(self.UserData_filePath)
        self.UserData_Root = self.UserData_Tree.getroot()
        try:
            item = self.ui.ProductList.currentItem()
            if(item==None):
                self.ui.ProductList.setCurrentRow(0)
                item = self.ui.ProductList.currentItem()
            product_num = item.text()[0:3]
            for x in self.UserData_Root.findall('.//Customer'):
                if(x.find('id').text==self.login_email):
                    for y in x.find('cart').findall('item'):
                        if(y.text == product_num):
                            x.find('cart').remove(y)
                            self.UserData_Tree.write('Data/Customers.xml') 
                            item = self.ui.ProductList.currentItem()
                            self.ui.ProductList.takeItem(self.ui.ProductList.row(item))
                            self.ui.ItemImage.setText("Item removed from cart")
                            return
        except (AttributeError):
            pass

    def BuyAgain_clicked(self):
        self.UserData_fileName = 'Customers.xml'
        self.UserData_filePath = os.path.abspath(os.path.join('Data', self.UserData_fileName))
        self.UserData_Tree = ElementTree.parse(self.UserData_filePath)
        self.UserData_Root = self.UserData_Tree.getroot()
        try:
            item = self.ui.ProductList_h.currentItem()
            if(item==None):
                self.ui.ProductList_h.setCurrentRow(0)
                item = self.ui.ProductList_h.currentItem()
            product_num = item.text()[0:3]
            for x in self.UserData_Root.findall('.//Customer'):
                if(x.find('id').text==self.login_email):
                    for y in x.find('purchases').findall('.//item'):
                        if(y.text == product_num):
                            _translate = qtc.QCoreApplication.translate
                            product = ElementTree.SubElement(x.find('cart'), "item")
                            product.text = product_num
                            self.UserData_Tree.write('Data/Customers.xml') 
                            item = qtw.QListWidgetItem()
                            self.ui.ProductList.addItem(item)
                            item.setText(_translate("AccountPage", product_num + ": " + "name"))
                            for z in self.ItemData_Root.findall('Item'):
                                if(z.get('id') == y.text):
                                    item.setText(_translate("AccountPage", y.text + ": " + z.find('item_name').text))
                            self.ui.ItemImage_h.setText(_translate("AccountPage", "Item added to cart"))
        except (AttributeError):
            pass

    def CancelOrder_clicked(self):
        self.UserData_fileName = 'Customers.xml'
        self.UserData_filePath = os.path.abspath(os.path.join('Data', self.UserData_fileName))
        self.UserData_Tree = ElementTree.parse(self.UserData_filePath)
        self.UserData_Root = self.UserData_Tree.getroot()
        try:
            item = self.ui.ProductList_t.currentItem()
            if(item==None):
                self.ui.ProductList_t.setCurrentRow(0)
                item = self.ui.ProductList_t.currentItem()
            product_num = item.text()[0:3]
            for x in self.UserData_Root.findall('.//Customer'):
                if(x.find('id').text==self.login_email):
                    for y in x.find('orders').findall('.//item'):
                        if(y.text == product_num):
                            x.find('orders').remove(y)
                            self.UserData_Tree.write('Data/Customers.xml') 
                            item = self.ui.ProductList_t.currentItem()
                            self.ui.ProductList_t.takeItem(self.ui.ProductList_t.row(item))
                            self.ui.TextBox.setText("Order canceled, money will be added to your account balance in 3-5 business days")
                            return
        except (AttributeError):
            pass

    def Logout_clicked(self):
        self.ui.hide()
        self.homepage.ui.tabWidget.setCurrentIndex(0)
        self.homepage.ui.show()

class TransactionPage(qtw.QWidget):
    def __init__(self, homepage):
        super().__init__()
        self.homepage= homepage
        self.customer = self.homepage.current_customer
        self.ui = loadUi("UiFiles/TransactionPage.ui")

        self.ItemData_fileName = 'Items.xml'
        self.ItemData_filePath = os.path.abspath(os.path.join('Data', self.ItemData_fileName))
        self.ItemData_Tree = ElementTree.parse(self.ItemData_filePath)
        self.ItemData_Root = self.ItemData_Tree.getroot()

        self.ui.pButton_close.clicked.connect(self.ui.close)
        self.generate_transaction()

        self.ui.show()

        # itemWithDate = Users.ItemWithDate()
        # itemWithDate.id = x.text
        # homepage.current_customer.cart.append(itemWithDate)

    def generate_transaction(self):
        self.ui.lineEdit_orderNumber.setText(None)
        self.ui.lineEdit_datePurchased.setText(self.customer.cart[0].date) 
        self.ui.lineEdit_fullName.setText(self.customer.first_name + " " + self.customer.last_name) 
        self.ui.lineEdit_contactNumber.setText(self.customer.contact_num)
        self.ui.lineEdit_address.setText(self.customer.address)
        self.ui.lineEdit_email.setText(self.customer.email_address)
        self.ui.lineEdit_cardNum.setText(self.customer.contact_num[-4:])

        self.ui.tableWidget_items.setRowCount(len(self.customer.cart)+1)
        self.ui.tableWidget_items.setColumnCount(3)

        total = 0
        i = 0
        for x in self.customer.cart:
            for y in self.ItemData_Root.findall('Item'):
                if(y.get('id') == x.id):
                    total += float(y.find('item_price').text)
                    self.ui.tableWidget_items.setItem(i, 0, qtw.QTableWidgetItem(y.find('item_name').text))
                    self.ui.tableWidget_items.setItem(i, 1, qtw.QTableWidgetItem(y.find('item_type').text))
                    self.ui.tableWidget_items.setItem(i, 2, qtw.QTableWidgetItem(y.find('item_price').text))
            i += 1
        
        self.ui.label_totalCost.setText(str(total))
    
class AvoidList(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = loadUi("UiFiles/AvoidList.ui")
        self.AvoidList_fileName = 'AvoidList.xml'
        self.AvoidList_filePath = os.path.abspath(os.path.join('Data', self.AvoidList_fileName))
        self.AvoidList_Tree = ElementTree.parse(self.AvoidList_filePath)
        self.AvoidList_Root = self.AvoidList_Tree.getroot()
        self.avoid_dict = {}
        self.refresh_avoid_list()
        self.current_selection = None

        # Connect signals and slots
        self.ui.listWidget_avoidList.itemClicked.connect(self.get_current_selection)
        self.ui.pButton_add.clicked.connect(self.add_email)
        self.ui.pButton_remove.clicked.connect(self.remove_email)

        self.ui.show()

    def get_current_selection(self, item):
        self.current_selection = item.text()

    def remove_email(self):
        if self.current_selection == None:
            msg = qtw.QMessageBox.information(self, '', 'Please select an email to remove.')
            return
        for child in self.AvoidList_Root:
            if child.get("email") == self.current_selection:
                self.AvoidList_Root.remove(child)
        # Update tree 
        self.AvoidList_Tree._setroot(self.AvoidList_Root)
        # Use updated tree to write xml
        self.AvoidList_Tree.write("Data/AvoidList.xml")
        # Update dictionary
        self.avoid_dict.pop(self.current_selection)
        self.refresh_avoid_list()
        self.current_selection = None
        msg = qtw.QMessageBox.information(self, '', 'Email removed successfully.')

    def refresh_avoid_list(self):
        # clear items
        self.ui.listWidget_avoidList.clear()
        # Populate from xml file
        for child in self.AvoidList_Root:
            self.avoid_dict.update({child.get("email"): child.get("email")})
            self.ui.listWidget_avoidList.addItem(qtw.QListWidgetItem(child.get("email")))

    def add_email(self):
        new_email = self.ui.lineEdit_add.text()
        if len(new_email) > 0 and self.avoid_dict.get(new_email) == None:
            ElementTree.SubElement(self.AvoidList_Root, "email", email=new_email)
            # self.AvoidList_Tree._setroot(self.AvoidList_Root)
            self.AvoidList_Tree.write("Data/AvoidList.xml")
            self.avoid_dict.update({new_email: new_email})
            msg = qtw.QMessageBox.information(self, '', 'Email added to avoid list.')
            self.refresh_avoid_list()
            self.ui.lineEdit_add.clear()
        elif self.avoid_dict.get(new_email) != None:
            msg = qtw.QMessageBox.information(self, '', 'Email is already in the list.')
        else:
            msg = qtw.QMessageBox.information(self, '', 'Please provide an email.')
            
class CustomerListModel(qtc.QAbstractListModel):
    def __init__(self, customer):
        super.__init__(self)
        self.customer = customer

    def rowCount(self, parent):
        return len(self.customer.__dict__)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = Main(windowTitle='Computer Store')
    app.exec_()
