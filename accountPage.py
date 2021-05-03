import os
from xml.etree import ElementTree
from PyQt5 import QtCore, QtGui, QtWidgets

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

class Ui_AccountPage(object):
    def setupUi(self, AccountPage):
        AccountPage.setObjectName("AccountPage")
        AccountPage.resize(1000, 750)
        AccountPage.setMinimumSize(QtCore.QSize(1000, 750))
        AccountPage.setMaximumSize(QtCore.QSize(1000, 750))
        
        self.tabWidget = QtWidgets.QTabWidget(AccountPage)
        self.tabWidget.setGeometry(QtCore.QRect(10, 140, 981, 601))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(50, 50))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        
        self.Cart = QtWidgets.QWidget()
        self.Cart.setEnabled(True)
        self.Cart.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Cart.setObjectName("Cart")
        self.ProductList = QtWidgets.QListWidget(self.Cart)
        self.ProductList.setGeometry(QtCore.QRect(0, 50, 651, 511))
        self.ProductList.setStyleSheet("font: 14pt \"Nirmala UI\";")
        self.ProductList.setObjectName("ProductList")
        try:
            for x in cartList:
                item = QtWidgets.QListWidgetItem()
                self.ProductList.addItem(item)
        except (AttributeError, TypeError):
            pass
        try:
             self.ProductList.clicked.connect(self.list_clicked)
        except (TypeError):
            pass       
        self.ItemImage = QtWidgets.QLabel(self.Cart)
        self.ItemImage.setGeometry(QtCore.QRect(660, 50, 311, 311))
        self.ItemImage.setText("")
        self.ItemImage.setPixmap(QtGui.QPixmap("Images/Item/default.jpg"))
        self.ItemImage.setScaledContents(True)
        self.ItemImage.setObjectName("ItemImage")
        self.RemoveFromList = QtWidgets.QPushButton(self.Cart)
        self.RemoveFromList.setGeometry(QtCore.QRect(660, 500, 311, 51))
        self.RemoveFromList.setObjectName("RemoveFromList")
        self.ItemPrice = QtWidgets.QLabel(self.Cart)
        self.ItemPrice.setGeometry(QtCore.QRect(660, 370, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ItemPrice.setFont(font)
        self.ItemPrice.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.ItemPrice.setObjectName("ItemPrice")
        self.Title = QtWidgets.QLabel(self.Cart)
        self.Title.setEnabled(True)
        self.Title.setGeometry(QtCore.QRect(0, 0, 971, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.Title.setObjectName("Title")
        self.ItemRating = QtWidgets.QLabel(self.Cart)
        self.ItemRating.setGeometry(QtCore.QRect(660, 0, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ItemRating.setFont(font)
        self.ItemRating.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.ItemRating.setObjectName("ItemRating")
        self.Checkout = QtWidgets.QPushButton(self.Cart)
        self.Checkout.setGeometry(QtCore.QRect(660, 440, 311, 51))
        self.Checkout.setObjectName("Checkout")
        self.tabWidget.addTab(self.Cart, "")
        
        self.History = QtWidgets.QWidget()
        self.History.setObjectName("History")
        self.Title_h = QtWidgets.QLabel(self.History)
        self.Title_h.setEnabled(True)
        self.Title_h.setGeometry(QtCore.QRect(0, 0, 971, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Title_h.setFont(font)
        self.Title_h.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.Title_h.setObjectName("Title_h")
        self.ProductList_h = QtWidgets.QListWidget(self.History)
        self.ProductList_h.setGeometry(QtCore.QRect(0, 50, 651, 511))
        self.ProductList_h.setStyleSheet("font: 14pt \"Nirmala UI\";")
        self.ProductList_h.setObjectName("ProductList_h")
        try:
            for x in historyList:
                item = QtWidgets.QListWidgetItem()
                self.ProductList_h.addItem(item)
        except (AttributeError, TypeError, NameError):
            pass
        try:
             self.ProductList_h.clicked.connect(self.list_h_clicked)
        except (TypeError):
            pass 
        self.ItemPrice_h = QtWidgets.QLabel(self.History)
        self.ItemPrice_h.setGeometry(QtCore.QRect(660, 370, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ItemPrice_h.setFont(font)
        self.ItemPrice_h.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.ItemPrice_h.setObjectName("ItemPrice_h")
        self.ItemImage_h = QtWidgets.QLabel(self.History)
        self.ItemImage_h.setGeometry(QtCore.QRect(660, 50, 311, 311))
        self.ItemImage_h.setText("")
        self.ItemImage_h.setPixmap(QtGui.QPixmap("Images/Item/default.jpg"))
        self.ItemImage_h.setScaledContents(True)
        self.ItemImage_h.setObjectName("ItemImage_h")
        self.BuyAgain = QtWidgets.QPushButton(self.History)
        self.BuyAgain.setGeometry(QtCore.QRect(660, 500, 311, 51))
        self.BuyAgain.setObjectName("BuyAgain")
        self.ReviewProduct = QtWidgets.QPushButton(self.History)
        self.ReviewProduct.setGeometry(QtCore.QRect(660, 440, 311, 51))
        self.ReviewProduct.setObjectName("ReviewProduct")
        self.tabWidget.addTab(self.History, "")
        
        self.Track = QtWidgets.QWidget()
        self.Track.setObjectName("Track")
        self.ProductList_t = QtWidgets.QListWidget(self.Track)
        self.ProductList_t.setGeometry(QtCore.QRect(0, 50, 651, 511))
        self.ProductList_t.setStyleSheet("font: 14pt \"Nirmala UI\";")
        self.ProductList_t.setObjectName("ProductList_t")
        try:
            for x in trackList:
                item = QtWidgets.QListWidgetItem()
                self.ProductList_t.addItem(item)
        except (AttributeError, TypeError, NameError):
            pass
        self.Title_t = QtWidgets.QLabel(self.Track)
        self.Title_t.setEnabled(True)
        self.Title_t.setGeometry(QtCore.QRect(0, 0, 971, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Title_t.setFont(font)
        self.Title_t.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.Title_t.setObjectName("Title_t")
        self.TextBox = QtWidgets.QLabel(self.Track)
        self.TextBox.setGeometry(QtCore.QRect(660, 50, 311, 311))
        self.TextBox.setScaledContents(True)
        self.TextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.TextBox.setWordWrap(True)
        self.TextBox.setObjectName("TextBox")
        self.CancelOrder = QtWidgets.QPushButton(self.Track)
        self.CancelOrder.setGeometry(QtCore.QRect(660, 500, 311, 51))
        self.CancelOrder.setObjectName("CancelOrder")
        self.tabWidget.addTab(self.Track, "")
        
        self.CustomerName = QtWidgets.QLabel(AccountPage)
        self.CustomerName.setGeometry(QtCore.QRect(140, 10, 691, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.CustomerName.setFont(font)
        self.CustomerName.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.CustomerName.setObjectName("CustomerName")

        self.BalanceData = QtWidgets.QLabel(AccountPage)
        self.BalanceData.setGeometry(QtCore.QRect(140, 100, 691, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(16)
        self.BalanceData.setFont(font)
        self.BalanceData.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.BalanceData.setObjectName("BalanceData")
        
        self.CustomerIcon = QtWidgets.QLabel(AccountPage)
        self.CustomerIcon.setGeometry(QtCore.QRect(10, 10, 121, 121))
        self.CustomerIcon.setText("")
        self.CustomerIcon.setPixmap(QtGui.QPixmap("Images/User/userIcon.png"))
        self.CustomerIcon.setScaledContents(True)
        self.CustomerIcon.setObjectName("CustomerIcon")
        
        self.CustomerInfo = QtWidgets.QLabel(AccountPage)
        self.CustomerInfo.setGeometry(QtCore.QRect(140, 60, 691, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(16)
        self.CustomerInfo.setFont(font)
        self.CustomerInfo.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.CustomerInfo.setObjectName("CustomerInfo")
        
        self.Logout = QtWidgets.QPushButton(AccountPage)
        self.Logout.setGeometry(QtCore.QRect(840, 10, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.Logout.setFont(font)
        self.Logout.setObjectName("Logout")
        
        self.CashIn = QtWidgets.QPushButton(AccountPage)
        self.CashIn.setGeometry(QtCore.QRect(750, 140, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.CashIn.setFont(font)
        self.CashIn.setObjectName("CashIn")
        self.CashOut = QtWidgets.QPushButton(AccountPage)
        self.CashOut.setGeometry(QtCore.QRect(870, 140, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.CashOut.setFont(font)
        self.CashOut.setObjectName("CashOut")
        self.BalanceOutput = QtWidgets.QLabel(AccountPage)
        self.BalanceOutput.setGeometry(QtCore.QRect(480, 100, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.BalanceOutput.setFont(font)
        self.BalanceOutput.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.BalanceOutput.setObjectName("BalanceOutput")
        self.BalanceInput = QtWidgets.QLineEdit(AccountPage)
        self.BalanceInput.setGeometry(QtCore.QRect(870, 110, 113, 22))
        self.BalanceInput.setObjectName("BalanceInput")

        self.retranslateUi(AccountPage)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AccountPage)

        self.RemoveFromList.clicked.connect(self.RemoveFromList_clicked)
        self.Checkout.clicked.connect(self.Checkout_clicked)
        self.CashIn.clicked.connect(self.CashIn_clicked)
        self.CashOut.clicked.connect(self.CashOut_clicked)
        self.ReviewProduct.clicked.connect(self.ReviewProduct_clicked)
        self.BuyAgain.clicked.connect(self.BuyAgain_clicked)
        self.CancelOrder.clicked.connect(self.CancelOrder_clicked)
        self.Logout.clicked.connect(self.Logout_clicked)

    def retranslateUi(self, AccountPage):
        _translate = QtCore.QCoreApplication.translate
        AccountPage.setWindowTitle(_translate("AccountPage", "Computer Store : Account Page : " + firstName + ' ' + lastName))
        AccountPage.setWindowIcon(QtGui.QIcon('Images/User/userIcon.png'))
        __sortingEnabled = self.ProductList.isSortingEnabled()
        self.ProductList.setSortingEnabled(False)
        try:
            i = 0
            for x in cartList:
                item = self.ProductList.item(0+i)
                for y in ItemData_Root.findall('Item'):
                    if(y.get('id') == x.text):
                        item.setText(_translate("AccountPage", x.text + ": " + y.find('item_name').text))
                i += 1
        except (AttributeError, TypeError):
            pass
        self.ProductList.setSortingEnabled(__sortingEnabled)
        self.RemoveFromList.setText(_translate("AccountPage", "Remove From List"))
        self.ItemPrice.setText(_translate("AccountPage", "$__.__"))
        self.Title.setText(_translate("AccountPage", "Products"))
        self.ItemRating.setText(_translate("AccountPage", "Rating: _/_"))
        self.Checkout.setText(_translate("AccountPage", "Checkout Cart Items"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Cart), _translate("AccountPage", "Cart"))
        self.Title_h.setText(_translate("AccountPage", "Products"))
        __sortingEnabled = self.ProductList_h.isSortingEnabled()
        self.ProductList_h.setSortingEnabled(False)
        try:
            i = 0
            for x in historyList:
                item = self.ProductList_h.item(0+i)
                for y in ItemData_Root.findall('Item'):
                    if(y.get('id') == x.text):
                        item.setText(_translate("AccountPage", x.text + ": " + y.find('item_name').text + ' - ' + x.get('date')))
                i += 1
        except (AttributeError, TypeError):
            pass
        self.ProductList_h.setSortingEnabled(__sortingEnabled)
        self.ItemPrice_h.setText(_translate("AccountPage", "$50.00"))
        self.BuyAgain.setText(_translate("AccountPage", "Buy Again"))
        self.ReviewProduct.setText(_translate("AccountPage", "Review Product"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.History), _translate("AccountPage", "History"))
        __sortingEnabled = self.ProductList_t.isSortingEnabled()
        self.ProductList_t.setSortingEnabled(False)
        try:
            i = 0
            for x in trackList:
                item = self.ProductList_t.item(0+i)
                for y in ItemData_Root.findall('Item'):
                    if(y.get('id') == x.text):
                        item.setText(_translate("AccountPage", x.text + ": " + y.find('item_name').text + ' - Estimated arrival date: ' + x.get('date')))
                i += 1
        except (AttributeError, TypeError):
            pass
        self.ProductList_t.setSortingEnabled(__sortingEnabled)
        self.Title_t.setText(_translate("AccountPage", "Products"))
        self.TextBox.setText(_translate("AccountPage", " "))
        if (trackList==None):
            self.TextBox.setText(_translate("AccountPage", "No Items Available"))
        self.CancelOrder.setText(_translate("AccountPage", "Cancel Order"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Track), _translate("AccountPage", "Track Order"))
        self.CustomerName.setText(_translate("AccountPage", firstName + ' ' + lastName))
        self.BalanceData.setText(_translate("AccountPage", "Balance: $" + userBalance + ' ' + bankName + 'Bank ' + bankNumber))
        self.CustomerInfo.setText(_translate("AccountPage", userEmail))
        self.Logout.setText(_translate("AccountPage", "Logout"))
        self.CashIn.setText(_translate("AccountPage", "Cash In"))
        self.CashOut.setText(_translate("AccountPage", "Cash Out"))
        self.BalanceOutput.setText(_translate("AccountPage", "Type in amount in $"))

    def list_clicked(self):
        item = self.ProductList.currentItem()
        product_num = item.text()[0:3]
        for x in ItemData_Root.findall('Item'):
            if(x.get('id') == product_num):
                self.ItemPrice.setText("$" + x.find('item_price').text)
                self.ItemRating.setText("Rating: " + x.find('item_rating').text)
                self.ItemImage.setPixmap(QtGui.QPixmap("Images/Item/" + product_num + ".jpg"))
                
    def list_h_clicked(self):
        item = self.ProductList_h.currentItem()
        product_num = item.text()[0:3]
        for x in ItemData_Root.findall('Item'):
            if(x.get('id') == product_num):
                self.ItemPrice_h.setText("$" + x.find('item_price').text)
                self.ItemImage_h.setPixmap(QtGui.QPixmap("Images/Item/" + product_num + ".jpg"))

    def RemoveFromList_clicked(self):
        item = self.ProductList.currentItem()
        if(item==None):
            self.ProductList.setCurrentRow(0)
            item = self.ProductList.currentItem()
        product_num = item.text()[0:3]
        for x in UserData_Root.find('Customers').findall('.//Customer'):
            if(x.get('id')==userEmail):
                for y in x.find('cart').findall('.//item'):
                    if(y.text == product_num):
                        x.find('cart').remove(y)
                        UserData_Tree.write('new.xml')
                        item = self.ProductList.currentItem()
                        self.ProductList.takeItem(self.ProductList.row(item))
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
        item = self.ProductList_h.currentItem()
        product_num = item.text()[0:3]
        #goto discussion page

    def BuyAgain_clicked(self):
        item = self.ProductList_h.currentItem()
        if(item==None):
            self.ProductList_h.setCurrentRow(0)
            item = self.ProductList_h.currentItem()
        product_num = item.text()[0:3]
        for x in UserData_Root.find('Customers').findall('.//Customer'):
            if(x.get('id')==userEmail):
                for y in x.find('purchases').findall('.//item'):
                    if(y.text == product_num):
                        _translate = QtCore.QCoreApplication.translate
                        product = ElementTree.SubElement(x.find('cart'), "item")
                        product.text = product_num
                        UserData_Tree.write('new.xml')
                        item = QtWidgets.QListWidgetItem()
                        self.ProductList.addItem(item)
                        item.setText(_translate("AccountPage", product_num + ": " + "name"))
                        print("item added to cart")
                        #goto transaction page

    def CancelOrder_clicked(self):
        item = self.ProductList_t.currentItem()
        if(item==None):
            self.ProductList_t.setCurrentRow(0)
            item = self.ProductList_t.currentItem()
        product_num = item.text()[0:3]
        for x in UserData_Root.find('Customers').findall('.//Customer'):
            if(x.get('id')==userEmail):
                for y in x.find('orders').findall('.//item'):
                    if(y.text == product_num):
                        x.find('orders').remove(y)
                        UserData_Tree.write('new.xml')
                        item = self.ProductList_t.currentItem()
                        self.ProductList_t.takeItem(self.ProductList_t.row(item))
                        print("order canceled")

    def Logout_clicked(self):
        sys.exit()
        #goto main page

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AccountPage = QtWidgets.QWidget()
    ui = Ui_AccountPage()
    ui.setupUi(AccountPage)
    AccountPage.show()
    sys.exit(app.exec_())
