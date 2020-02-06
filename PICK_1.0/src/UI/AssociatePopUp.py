# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AssociatePopUp.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class AssociateVectorScreen(object):
    def setupUi(self, Dialog):

        def closeCurrentWindow():
            Dialog.close()

        Dialog.setObjectName("Dialog")
        Dialog.resize(761, 350)
        self.AssociateTable = QtWidgets.QTableWidget(Dialog)
        self.AssociateTable.setGeometry(QtCore.QRect(20, 30, 391, 191))
        self.AssociateTable.setObjectName("AssociateTable")
        self.AssociateTable.setColumnCount(0)
        self.AssociateTable.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.AssociateTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.AssociateTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.AssociateTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.AssociateTable.setVerticalHeaderItem(3, item)
        self.AssociateScrollBar = QtWidgets.QScrollBar(Dialog)
        self.AssociateScrollBar.setGeometry(QtCore.QRect(400, 30, 20, 191))
        self.AssociateScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.AssociateScrollBar.setObjectName("AssociateScrollBar")
        self.AssociateSearchBar = QtWidgets.QLineEdit(Dialog)
        self.AssociateSearchBar.setGeometry(QtCore.QRect(20, 220, 113, 22))
        self.AssociateSearchBar.setObjectName("AssociateSearchBar")
        self.AssociateSelectVectBtn = QtWidgets.QPushButton(Dialog)
        self.AssociateSelectVectBtn.setGeometry(QtCore.QRect(310, 220, 93, 28))
        self.AssociateSelectVectBtn.setObjectName("AssociateSelectVectBtn")
        self.AssociateAddVectBtn = QtWidgets.QPushButton(Dialog)
        self.AssociateAddVectBtn.setGeometry(QtCore.QRect(20, 300, 311, 28))
        self.AssociateAddVectBtn.setObjectName("AssociateAddVectBtn")
        self.AssociateAddVectBtn.clicked.connect(closeCurrentWindow)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.AssociateTable.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Vector 1"))
        item = self.AssociateTable.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "Vector 2"))
        item = self.AssociateTable.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "Vector 3"))
        item = self.AssociateTable.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "Vector 4"))
        self.AssociateSearchBar.setText(_translate("Dialog", "Search"))
        self.AssociateSelectVectBtn.setText(_translate("Dialog", "Select Vector"))
        self.AssociateAddVectBtn.setText(_translate("Dialog", "Add Vector"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = AssociateVectorScreen()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
