import sys, math
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
import random

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 600)
        self.setWindowTitle('Register')
        self.label_tp = QLabel(self)
        self.label_tp.setFixedSize(200, 80)
        self.label_tp.move(0, 0)
        self.label_tp.setStyleSheet("QLabel{background:rgb(300,300,300,120,0.3);}"
                                    "QLabel{color:rgb(300,300,300,120,0.3);font-size:20px;font-weight:bold;font-family:Times New Roman;}"
                                    )



        label_bj = 'border-width:1px;border-style:solid;font-size:25px;border-color:rgb(255,255,255,0.5);background-color:rgb(255,255,255,0.3);'
        self.label = QLabel(self)
        self.label.setText("Register")

        self.label.move(100, 100)
        self.label.setFixedSize(600, 50)
        self.label.setStyleSheet(label_bj)
        self.label.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)

        label_wzbj = 'border-width:1px;border-style:solid;font-size:12px;border-color:rgb(0,0,0,0.5);background-color:rgb(255,255,255,0.3);'

        self.label_zh = QLabel(self)
        self.label_zh.setText("UserId :")
        self.label_zh.move(100, 170)
        self.label_zh.setFixedSize(100, 30)
        self.label_zh.setStyleSheet(label_wzbj)
        self.label_zh.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)

        self.label_xm = QLabel(self)
        self.label_xm.setText("UserName :")
        self.label_xm.move(100, 210)
        self.label_xm.setFixedSize(100, 30)
        self.label_xm.setStyleSheet(label_wzbj)
        self.label_xm.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)

        self.label_mm = QLabel(self)
        self.label_mm.setText("Password :")
        self.label_mm.move(100, 250)
        self.label_mm.setFixedSize(100, 30)
        self.label_mm.setStyleSheet(label_wzbj)
        self.label_mm.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)

        self.label_qmm = QLabel(self)
        self.label_qmm.setText(" ConfirmPassword:")
        self.label_qmm.move(100, 290)
        self.label_qmm.setFixedSize(100, 30)
        self.label_qmm.setStyleSheet(label_wzbj)
        self.label_qmm.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)

        self.label_lxdh = QLabel(self)
        self.label_lxdh.setText(" PhoneNumber:")
        self.label_lxdh.move(100, 330)
        self.label_lxdh.setFixedSize(100, 30)
        self.label_lxdh.setStyleSheet(label_wzbj)
        self.label_lxdh.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)

        self.label_emil = QLabel(self)
        self.label_emil.setText("Email :")
        self.label_emil.move(100, 370)
        self.label_emil.setFixedSize(100, 30)
        self.label_emil.setStyleSheet(label_wzbj)
        self.label_emil.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)

        self.sr_zh = QLineEdit(self)

        self.sr_zh.setPlaceholderText("Enter UserId")
        self.sr_zh.move(210, 170)
        self.sr_zh.setFixedSize(400, 30)
        self.sr_zh.setStyleSheet(label_wzbj)

        self.sr_xm = QLineEdit(self)
        self.sr_xm.setPlaceholderText("Enter User Name")
        self.sr_xm.move(210, 210)
        self.sr_xm.setFixedSize(400, 30)
        self.sr_xm.setStyleSheet(label_wzbj)

        self.sr_mm = QLineEdit(self)
        self.sr_mm.setPlaceholderText("Enter Password")
        self.sr_mm.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.sr_mm.move(210, 250)
        self.sr_mm.setFixedSize(400, 30)
        self.sr_mm.setStyleSheet(label_wzbj)

        self.sr_qmm = QLineEdit(self)
        self.sr_qmm.setPlaceholderText("Confirm Password")
        self.sr_qmm.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.sr_qmm.move(210, 290)
        self.sr_qmm.setFixedSize(400, 30)
        self.sr_qmm.setStyleSheet(label_wzbj)

        self.sr_lxdh = QLineEdit(self)
        self.sr_lxdh.setPlaceholderText("Enter Phone Number")
        self.sr_lxdh.move(210, 330)
        self.sr_lxdh.setFixedSize(400, 30)
        self.sr_lxdh.setStyleSheet(label_wzbj)

        self.sr_emil = QLineEdit(self)
        self.sr_emil.setPlaceholderText("Enter Email")
        self.sr_emil.move(210, 370)
        self.sr_emil.setFixedSize(400, 30)
        self.sr_emil.setStyleSheet(label_wzbj)


        self.label_zh_qr = QLabel(self)
        self.label_zh_qr.setText("*")
        self.label_zh_qr.move(620, 170)
        self.label_zh_qr.setFixedSize(100, 30)

        self.label_xm_qr = QLabel(self)
        self.label_xm_qr.setText("*")
        self.label_xm_qr.move(620, 210)
        self.label_xm_qr.setFixedSize(100, 30)

        self.label_mm_qr = QLabel(self)
        self.label_mm_qr.setText("*")
        self.label_mm_qr.move(620, 250)
        self.label_mm_qr.setFixedSize(100, 30)

        self.label_qmm_qr = QLabel(self)
        self.label_qmm_qr.setText("*")
        self.label_qmm_qr.move(620, 290)
        self.label_qmm_qr.setFixedSize(100, 30)

        self.label_lxdh_qr = QLabel(self)
        self.label_lxdh_qr.setText("")
        self.label_lxdh_qr.move(620, 330)
        self.label_lxdh_qr.setFixedSize(100, 30)

        self.label_emil_qr = QLabel(self)
        self.label_emil_qr.setText("")
        self.label_emil_qr.move(620, 370)
        self.label_emil_qr.setFixedSize(100, 30)



        self.bt1 = QPushButton('identityode', self)
        self.bt1.move(100, 450)
        self.bt1.setFixedSize(100, 30)

        self.count = 30
        self.bt1.clicked.connect(self.Action)
        self.time = QtCore.QTimer(self)

        self.time.setInterval(1000)

        self.time.timeout.connect(self.Refresh)


        self.label_sjm = QLabel(self)
        self.label_sjm.setText("")
        self.label_sjm.move(210, 450)
        self.label_sjm.setFixedSize(60, 30)
        self.label_sjm.setStyleSheet(label_wzbj)
        self.label_sjm.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)


        self.sr_yzm = QLineEdit(self)
        self.sr_yzm.setPlaceholderText(" Enter identity Code")
        self.sr_yzm.move(280, 450)
        self.sr_yzm.setFixedSize(200, 30)
        self.sr_yzm.setStyleSheet(label_wzbj)


        self.bt2 = QPushButton('Agree', self)
        self.bt2.move(490, 450)
        self.bt2.setFixedSize(120, 30)
        self.bt2.clicked.connect(self.register)

        self.label_zctg_qr = QLabel(self)
        self.label_zctg_qr.setText("")
        self.label_zctg_qr.move(620, 450)
        self.label_zctg_qr.setFixedSize(100, 30)



        self.show()

    def Action(self):
        if self.bt1.isEnabled():
            self.time.start()
            self.bt1.setEnabled(False)
            sjs = str(random.randint(0, 9999))
            if len(sjs) < 4:
                sjs = '0' * (4 - len(sjs)) + sjs
            self.label_sjm.setText(sjs)



    def Refresh(self):
        if self.count > 0:
            self.bt1.setText(str(self.count) + 'Re-sent')
            self.count -= 1
        else:
            self.time.stop()
            self.bt1.setText('Get a random verification code')
            self.bt1.setEnabled(True)

            self.count = 30

    def register(self):

        self.label_zh_qr.setText('*')
        self.label_xm_qr.setText('*')
        self.label_mm_qr.setText('*')
        self.label_qmm_qr.setText('*')

        if len(self.sr_zh.text()) == 0:
            self.label_zh_qr.setText('PassWord Required')

        elif len(self.sr_xm.text()) == 0:
            self.label_xm_qr.setText('name Required')

        elif len(self.sr_mm.text()) == 0:
            self.label_mm_qr.setText('Pa')

        elif len(self.sr_qmm.text()) == 0:
            self.label_qmm_qr.setText('Password Required')

        elif self.sr_qmm.text() != self.sr_mm.text():
            self.label_qmm_qr.setText('Inconsistent passwords')

        elif len(self.sr_yzm.text()) == 0:
            self.label_zctg_qr.setText('Verification Required')

        elif self.label_sjm.text() != self.sr_yzm.text():
            self.label_zctg_qr.setText('Inconsistent Verification  ')
        else:
            self.label_zctg_qr.setText('Welcome')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
