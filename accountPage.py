import os
from xml.etree import ElementTree
from PyQt5 import QtCore, QtGui, QtWidgets

UserData_fileName = 'Users.xml'
UserData_filePath = os.path.abspath(os.path.join('Data', UserData_fileName))
UserData_Tree = ElementTree.parse(UserData_filePath)
UserData_Root = UserData_Tree.getroot()

for x in UserData_Root.findall('Customer'):
    firstName = x.find('FirstName').text
    lastName = x.find('LastName').text
    userEmail = x.find('Email').text
    userBalance = x.find('Balance').text
    bankName = x.find('PaymentInfo').find('Bank').text
    bankNumber = x.find('PaymentInfo').find('CardNum').text
    
    cartList = x.find('Cart').findall('ItemNum')
    historyList = x.find('PurchaseHistory').findall('Item')
    trackList = x.find('TrackInfo').findall('ItemNum')
    """
    try:
        cartList = x.find('Cart').findall('ItemNum')
    except AttributeError:
        pass
    try:
        historyList = x.find('PurchaseHistory').findall('Item')
    except AttributeError:
        pass
    try:
        trackList = x.find('TrackInfo').findall('ItemNum')
    except AttributeError:
        pass
    """

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
        self.ItemRating.setGeometry(QtCore.QRect(660, 430, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ItemRating.setFont(font)
        self.ItemRating.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.ItemRating.setObjectName("ItemRating")
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
                self.ProductList.addItem(item)
        except (AttributeError, TypeError):
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
                self.ProductList.addItem(item)
        except (AttributeError, TypeError):
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

        self.retranslateUi(AccountPage)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AccountPage)

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
                item.setText(_translate("AccountPage", x.text))
                i += 1
        except (AttributeError, TypeError):
            pass
        self.ProductList.setSortingEnabled(__sortingEnabled)
        self.RemoveFromList.setText(_translate("AccountPage", "Remove From List"))
        self.ItemPrice.setText(_translate("AccountPage", "$50.00"))
        self.Title.setText(_translate("AccountPage", "Products"))
        self.ItemRating.setText(_translate("AccountPage", "Rating: 4/5"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Cart), _translate("AccountPage", "Cart"))
        self.Title_h.setText(_translate("AccountPage", "Products"))
        __sortingEnabled = self.ProductList_h.isSortingEnabled()
        self.ProductList_h.setSortingEnabled(False)
        try:
            i = 0
            for x in historyList:
                item = self.ProductList_h.item(0+i)
                item.setText(_translate("AccountPage", x.find('ItemNum').text + ' - ' + x.find('Date').text))
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
                item.setText(_translate("AccountPage", x.find('ItemNum').text + ' - ' + x.find('Date').text))
                i += 1
        except (AttributeError, TypeError):
            pass
        self.ProductList_t.setSortingEnabled(__sortingEnabled)
        self.Title_t.setText(_translate("AccountPage", "Products"))
        self.TextBox.setText(_translate("AccountPage", " "))
        if (trackList==0):
            self.TextBox.setText(_translate("AccountPage", "No Items Available"))
        self.CancelOrder.setText(_translate("AccountPage", "Cancel Order"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Track), _translate("AccountPage", "Track Order"))
        self.CustomerName.setText(_translate("AccountPage", firstName + ' ' + lastName))
        self.BalanceData.setText(_translate("AccountPage", "Balance: $" + userBalance + ' ' + bankName + 'Bank ' + bankNumber))
        self.CustomerInfo.setText(_translate("AccountPage", userEmail))
        self.Logout.setText(_translate("AccountPage", "Logout"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AccountPage = QtWidgets.QWidget()
    ui = Ui_AccountPage()
    ui.setupUi(AccountPage)
    AccountPage.show()
    sys.exit(app.exec_())
