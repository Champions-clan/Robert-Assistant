# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'css.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("QLineEdit{\n"
"padding: 6px 12px;\n"
"font-size: 14px;\n"
"color: #555;\n"
"background-color:#fff;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border-color: #56afe9;\n"
"}")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 411, 80))
        self.frame.setStyleSheet("QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(250, 250, 250, 90), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom: 1px solid darkgrey;\n"
"}\n"
"\n"
"QToolButton {\n"
"background-color: transparent;\n"
"border: none;\n"
"}\n"
"\n"
"QToolButton:checked, QToolButton:pressed {\n"
"background-color: rgb(193,210,238);\n"
"border: 1px solid rgb(60,127,177);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"background-color : rgb(224,232,246);\n"
"}\n"
"\n"
"QToolButton:checked:hover {\n"
"background-color : rgb(193,210,238);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.facebook = QtWidgets.QToolButton(self.frame)
        self.facebook.setGeometry(QtCore.QRect(60, 20, 51, 41))
        self.facebook.setCheckable(True)
        self.facebook.setAutoExclusive(True)
        self.facebook.setObjectName("facebook")
        self.twitter = QtWidgets.QToolButton(self.frame)
        self.twitter.setGeometry(QtCore.QRect(170, 20, 51, 41))
        self.twitter.setCheckable(True)
        self.twitter.setAutoExclusive(True)
        self.twitter.setObjectName("twitter")
        self.googleplus = QtWidgets.QToolButton(self.frame)
        self.googleplus.setGeometry(QtCore.QRect(280, 20, 51, 41))
        self.googleplus.setCheckable(True)
        self.googleplus.setAutoExclusive(True)
        self.googleplus.setObjectName("googleplus")
        self.username = QtWidgets.QLineEdit(Dialog)
        self.username.setGeometry(QtCore.QRect(130, 110, 131, 31))
        self.username.setText("")
        self.username.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.username.setObjectName("username")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(130, 190, 131, 23))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"border: 2px solid grey;\n"
"border-radius: 5px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QProgressBar:chunk{\n"
"background-color: #3366ff;\n"
"width: 10px;\n"
"margin: 1px;\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.Login = QtWidgets.QPushButton(Dialog)
        self.Login.setGeometry(QtCore.QRect(158, 230, 75, 23))
        self.Login.setStyleSheet("QPushButton {\n"
"font-size: 14px;\n"
"border: 1px solid transparent;\n"
"border-radius: 4px;\n"
"color: #fff;\n"
"background-color: #428bca;\n"
"border-color: #357ebd;\n"
"}\n"
"\n"
"QPushButtonHover {\n"
"color: #fff;\n"
"background-color: #3071a9;\n"
"border-color: #285e8e;\n"
"}")
        self.Login.setObjectName("Login")
        self.username_2 = QtWidgets.QLineEdit(Dialog)
        self.username_2.setGeometry(QtCore.QRect(130, 150, 131, 31))
        self.username_2.setText("")
        self.username_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.username_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.username_2.setObjectName("username_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.facebook.setText(_translate("Dialog", "Facebook"))
        self.twitter.setText(_translate("Dialog", "Twitter"))
        self.googleplus.setText(_translate("Dialog", "Google+"))
        self.username.setPlaceholderText(_translate("Dialog", "Username"))
        self.Login.setText(_translate("Dialog", "Login"))
        self.username_2.setPlaceholderText(_translate("Dialog", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
