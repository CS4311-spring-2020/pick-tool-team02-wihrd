# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImportLoadinScreen.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class ImportDirLoadingScreen(object):
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.CheckRootDirLabel = QtWidgets.QLabel(Dialog)
        self.CheckRootDirLabel.setGeometry(QtCore.QRect(120, 70, 141, 16))
        self.CheckRootDirLabel.setObjectName("CheckRootDirLabel")
        self.CheckRootDirPBar = QtWidgets.QProgressBar(Dialog)
        self.CheckRootDirPBar.setGeometry(QtCore.QRect(100, 90, 211, 23))
        self.CheckRootDirPBar.setProperty("value", 24)
        self.CheckRootDirPBar.setObjectName("CheckRootDirPBar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.CheckRootDirLabel.setText(_translate("Dialog", "Checking Root Directory"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = ImportDirLoadingScreen()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
