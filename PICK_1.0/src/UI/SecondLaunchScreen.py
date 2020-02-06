# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SecondLaunchScreen.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Main_Screen_UI import MainScreen


class SecondLaunchScreen(object):
    def setupUi(self, Dialog):

        def launchMainScreenHelper():
            Dialog.close()
            self.launchMainScreen()

        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.SecondLaunchLabel = QtWidgets.QLabel(Dialog)
        self.SecondLaunchLabel.setGeometry(QtCore.QRect(110, 40, 161, 16))
        self.SecondLaunchLabel.setObjectName("SecondLaunchLabel")
        self.SecondLaunchJoinBtn = QtWidgets.QPushButton(Dialog)
        self.SecondLaunchJoinBtn.setGeometry(QtCore.QRect(130, 120, 113, 32))
        self.SecondLaunchJoinBtn.setObjectName("SecondLaunchJoinBtn")
        self.SecondLaunchJoinBtn.clicked.connect(launchMainScreenHelper)
        self.SecondLaunchStartbtn = QtWidgets.QPushButton(Dialog)
        self.SecondLaunchStartbtn.setGeometry(QtCore.QRect(130, 200, 113, 32))
        self.SecondLaunchStartbtn.setObjectName("SecondLaunchStartbtn")
        self.SecondLaunchStartbtn.clicked.connect(launchMainScreenHelper)
        self.SecondLaunchInProgLabel = QtWidgets.QLabel(Dialog)
        self.SecondLaunchInProgLabel.setGeometry(QtCore.QRect(130, 100, 121, 20))
        self.SecondLaunchInProgLabel.setObjectName("SecondLaunchInProgLabel")
        self.SecondLaunchNoSessionLabel = QtWidgets.QLabel(Dialog)
        self.SecondLaunchNoSessionLabel.setGeometry(QtCore.QRect(120, 180, 151, 20))
        self.SecondLaunchNoSessionLabel.setObjectName("SecondLaunchNoSessionLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.SecondLaunchLabel.setText(_translate("Dialog", "Checking for Assignment"))
        self.SecondLaunchJoinBtn.setText(_translate("Dialog", "Join Session"))
        self.SecondLaunchStartbtn.setText(_translate("Dialog", "Start Session"))
        self.SecondLaunchInProgLabel.setText(_translate("Dialog", "Session in Progress"))
        self.SecondLaunchNoSessionLabel.setText(_translate("Dialog", "No Session in Progress"))

    def launchMainScreen(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = MainScreen()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = SecondLaunchScreen()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
