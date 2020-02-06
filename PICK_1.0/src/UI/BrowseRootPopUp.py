# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BrowseRootPopUp.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from ImportLoadinScreen import ImportDirLoadingScreen


class BrowseScreen(object):
    def setupUi(self, Dialog):

        def closeBrowseScreen():
            Dialog.close()
            self.showImportLoadingScreen()

        Dialog.setObjectName("Dialog")
        Dialog.resize(536, 334)
        self.BrowseRootPopUpBtn = QtWidgets.QDialogButtonBox(Dialog)
        self.BrowseRootPopUpBtn.setGeometry(QtCore.QRect(160, 290, 341, 32))
        self.BrowseRootPopUpBtn.setOrientation(QtCore.Qt.Horizontal)
        self.BrowseRootPopUpBtn.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.BrowseRootPopUpBtn.setObjectName("BrowseRootPopUpBtn")
        self.BrowseRootPopUpLabel = QtWidgets.QLabel(Dialog)
        self.BrowseRootPopUpLabel.setGeometry(QtCore.QRect(10, 10, 151, 16))
        self.BrowseRootPopUpLabel.setObjectName("BrowseRootPopUpLabel")
        self.BrowseRootInput = QtWidgets.QLineEdit(Dialog)
        self.BrowseRootInput.setGeometry(QtCore.QRect(10, 30, 271, 22))
        self.BrowseRootInput.setObjectName("BrowseRootInput")
        self.BrowseRootPopUpTable = QtWidgets.QTableWidget(Dialog)
        self.BrowseRootPopUpTable.setGeometry(QtCore.QRect(10, 60, 256, 192))
        self.BrowseRootPopUpTable.setObjectName("BrowseRootPopUpTable")
        self.BrowseRootPopUpTable.setColumnCount(0)
        self.BrowseRootPopUpTable.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.BrowseRootPopUpTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.BrowseRootPopUpTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.BrowseRootPopUpTable.setVerticalHeaderItem(2, item)
        self.verticalScrollBar = QtWidgets.QScrollBar(Dialog)
        self.verticalScrollBar.setGeometry(QtCore.QRect(260, 60, 16, 191))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")

        self.retranslateUi(Dialog)
        self.BrowseRootPopUpBtn.accepted.connect(closeBrowseScreen)
        self.BrowseRootPopUpBtn.rejected.connect(closeBrowseScreen)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.BrowseRootPopUpLabel.setText(_translate("Dialog", "Search for Root Directory"))
        self.BrowseRootInput.setText(_translate("Dialog", "C:/Users/AAFolder01_31_2020"))
        item = self.BrowseRootPopUpTable.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Blue Team"))
        item = self.BrowseRootPopUpTable.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "Red Team"))
        item = self.BrowseRootPopUpTable.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "White Team"))

    def showImportLoadingScreen(self):
        self.window = QtWidgets.QDialog()
        self.ui = ImportDirLoadingScreen()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = BrowseScreen()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
