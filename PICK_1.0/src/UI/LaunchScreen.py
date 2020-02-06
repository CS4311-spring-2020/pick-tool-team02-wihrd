# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LaunchScreen.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from SecondLaunchScreen import SecondLaunchScreen


class Ui_Dialog(object):
    def setupUi(self, Dialog):

        def openSecondLaunchScreenHelper():
            Dialog.close()
            self.openSecondLaunchScreen()

        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.LaunchScreenlabel = QtWidgets.QLabel(Dialog)
        self.LaunchScreenlabel.setGeometry(QtCore.QRect(80, 30, 271, 16))
        self.LaunchScreenlabel.setObjectName("LaunchScreenlabel")
        self.LaunchPageBtn = QtWidgets.QPushButton(Dialog)
        self.LaunchPageBtn.setGeometry(QtCore.QRect(140, 210, 113, 32))
        self.LaunchPageBtn.setObjectName("LaunchPageBtn")
        self.LaunchPageBtn.clicked.connect(openSecondLaunchScreenHelper)
        self.LaunchScreenImageView = QtWidgets.QGraphicsView(Dialog)
        self.LaunchScreenImageView.setGeometry(QtCore.QRect(100, 70, 191, 121))
        self.LaunchScreenImageView.setObjectName("LaunchScreenImageView")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.LaunchScreenlabel.setText(_translate("Dialog", "PMR Insight Collective Knowledge Tool"))
        self.LaunchPageBtn.setText(_translate("Dialog", "Start"))

    def openSecondLaunchScreen(self):
        self.window = QtWidgets.QDialog()
        self.ui = SecondLaunchScreen()
        self.ui.setupUi(self.window)
        self.window.show()






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
