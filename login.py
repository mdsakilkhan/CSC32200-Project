from PyQt5.Qt import *
import sys
from xml.etree import ElementTree
import os
import math

UserData_fileName = 'Customers.xml'
UserData_filePath = os.path.abspath(os.path.join('Data', UserData_fileName))
UserData_Tree = ElementTree.parse(UserData_filePath)
UserData_Root = UserData_Tree.getroot()

login_email = "email2"

firstName = ''
lastName = ''
userEmail = ''
userBalance = ''
bankName = ''
bankNumber = ''
password=''
for x in UserData_Root.find('Customers').findall('Customer'):
    if(x.get('id') == login_email):
        firstName = x.find('first_name').text
        lastName = x.find('last_name').text
        userEmail = x.find('email_address').text
        userBalance = x.find('balance').text
        bankName = x.find('bank').text
        bankNumber = x.find('card_number').text


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon("C:/Users/hughy/Downloads/sky.jpeg"))
        self.resize(600, 300)
        self.Co_Width = 80
        self.Co_Heigth = 60
        self.setup_ui()

    def setup_ui(self):
        self.lab_l = QLabel("UserName:", self)  # Account label
        self.Lin_l = QLineEdit(self)  # Account entry box
        self.Lin_l.setPlaceholderText('Enter UserName')
        self.lab_p = QLabel("Password :", self)  # Password tab
        self.Lin_p = QLineEdit(self)  # Password entry box
        self.Lin_p.setPlaceholderText('Enter Password')
        self.Lin_p.setEchoMode(QLineEdit.Password)  # Set ciphertext display
        self.Pu_l = QPushButton("login", self)  # Login button
        self.Pu_l.clicked.connect(self.Login)
        self.exit_button = QPushButton("cancel", self)
        self.exit_button.clicked.connect(self.close)





    def resizeEvent(self, evt):  # Reset the control coordinate event
        # Account label

        self.lab_l.resize(self.Co_Width, self.Co_Heigth / 2)
        self.lab_l.move(self.width() / 3, self.height() / 5)
        # username entry box
        self.Lin_l.move(self.lab_l.x() + self.lab_l.width(), self.lab_l.y())
        # Password tab
        self.lab_p.resize(self.Co_Width, self.Co_Heigth / 2)
        self.lab_p.move(self.lab_l.x(), self.lab_l.y() + self.lab_l.height())
        # Password entry box
        self.Lin_p.move(self.lab_p.x() + self.lab_p.width(), self.lab_p.y())
        # Login button
        self.Pu_l.move(self.Lin_p.x() + self.Lin_p.width() / 20, self.lab_p.y() + self.lab_p.width())
        self.exit_button.move(self.Lin_p.x() + self.Lin_p.width() , self.lab_p.y() + self.lab_p.width())

    def Login(self):

        if (self.Lin_l.text() == login_email and self.Lin_p.text() == password):
            QMessageBox.information(self, '', 'login successful!')
            self.close()
        elif (self.Lin_l.text() != login_email):
            self.Lin_l.setText("")
            self.Lin_p.setText("")
            QMessageBox.warning(self, '', 'wrong user name!')
        elif (self.Lin_p.text() != password):
            self.Lin_p.setText("")
            QMessageBox.warning(self, '', 'wrong password')






if __name__ == '__main__':
    App = QApplication(sys.argv)
    Win = Window()
    Win.show()
    sys.exit(App.exec_())
