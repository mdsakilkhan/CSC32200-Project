from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AccountPage(object):
    def setupUi(self, AccountPage):
        #------------------------------
        name = "Sakil Khan"
        #------------------------------
        AccountPage.setObjectName("AccountPage")
        AccountPage.setWindowTitle("Computer Store : Account Page : " + name)
        AccountPage.resize(1000, 750)
        AccountPage.setMinimumSize(QtCore.QSize(1000, 750))
        AccountPage.setMaximumSize(QtCore.QSize(1000, 750))
        self.tabWidget = QtWidgets.QTabWidget(AccountPage)
        self.tabWidget.setGeometry(QtCore.QRect(10, 60, 981, 681))
        self.tabWidget.setAutoFillBackground(False)
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
        self.tabWidget.addTab(self.Cart, "")
        self.History = QtWidgets.QWidget()
        self.History.setObjectName("History")
        self.tabWidget.addTab(self.History, "")
        self.Track = QtWidgets.QWidget()
        self.Track.setObjectName("Track")
        self.tabWidget.addTab(self.Track, "")
        self.Logout = QtWidgets.QPushButton(AccountPage)
        self.Logout.setGeometry(QtCore.QRect(870, 10, 111, 31))
        self.Logout.setObjectName("Logout")
        self.CustomerIcon = QtWidgets.QLabel(AccountPage)
        self.CustomerIcon.setGeometry(QtCore.QRect(14, 15, 31, 31))
        self.CustomerIcon.setText("")
        self.CustomerIcon.setPixmap(QtGui.QPixmap("../../../Desktop/laptop-user-1-1179329.png"))
        self.CustomerIcon.setScaledContents(True)
        self.CustomerIcon.setObjectName("CustomerIcon")
        self.CustomerName = QtWidgets.QLabel(AccountPage)
        self.CustomerName.setGeometry(QtCore.QRect(54, 15, 801, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(22)
        self.CustomerName.setFont(font)
        self.CustomerName.setObjectName("CustomerName")

        self.retranslateUi(AccountPage)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AccountPage)

    def retranslateUi(self, AccountPage):
        #------------------------------
        name = "Sakil Khan"
        #------------------------------
        _translate = QtCore.QCoreApplication.translate
        AccountPage.setWindowTitle(_translate("AccountPage", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Cart), _translate("AccountPage", "Cart"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.History), _translate("AccountPage", "History"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Track), _translate("AccountPage", "Track Order"))
        self.Logout.setText(_translate("AccountPage", "Logout"))
        self.CustomerName.setText(_translate("AccountPage", name))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AccountPage = QtWidgets.QWidget()
    ui = Ui_AccountPage()
    ui.setupUi(AccountPage)
    AccountPage.show()
    sys.exit(app.exec_())