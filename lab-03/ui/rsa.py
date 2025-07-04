# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/rsa.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1108, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 130, 47, 13))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 270, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 30, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.label_4.setObjectName("label_4")
        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(60, 380, 75, 23))
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(180, 380, 75, 23))
        self.btn_decrypt.setObjectName("btn_decrypt")
        self.txt_cipher_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_cipher_text.setGeometry(QtCore.QRect(70, 260, 281, 71))
        self.txt_cipher_text.setObjectName("txt_cipher_text")
        self.txt_plain_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_plain_text.setGeometry(QtCore.QRect(70, 120, 281, 71))
        self.txt_plain_text.setObjectName("txt_plain_text")
        self.txt_sign = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_sign.setGeometry(QtCore.QRect(540, 260, 281, 71))
        self.txt_sign.setObjectName("txt_sign")
        self.txt_infor = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_infor.setGeometry(QtCore.QRect(540, 120, 281, 71))
        self.txt_infor.setObjectName("txt_infor")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(466, 130, 61, 20))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(470, 270, 71, 20))
        self.label_5.setObjectName("label_5")
        self.btn_gen_key = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen_key.setGeometry(QtCore.QRect(520, 40, 75, 23))
        self.btn_gen_key.setObjectName("btn_gen_key")
        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(670, 390, 75, 23))
        self.btn_verify.setObjectName("btn_verify")
        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(550, 390, 75, 23))
        self.btn_sign.setObjectName("btn_sign")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1108, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Plain Text"))
        self.label_3.setText(_translate("MainWindow", "CipherText"))
        self.label_4.setText(_translate("MainWindow", "RSA cipher"))
        self.btn_encrypt.setText(_translate("MainWindow", "encrypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "decrypt"))
        self.label_2.setText(_translate("MainWindow", "Information"))
        self.label_5.setText(_translate("MainWindow", "Signature"))
        self.btn_gen_key.setText(_translate("MainWindow", "Tạo Khoá"))
        self.btn_verify.setText(_translate("MainWindow", "Verify"))
        self.btn_sign.setText(_translate("MainWindow", "Sign"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
