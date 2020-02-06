# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pushing Changes.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Denied import DeniedScreen

class PushingChangesScreen(object):
    def setupUi(self, Dialog):

        def closeCurrentScreen():
            self.scanCompletePopup()
            Dialog.close()

        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        self.PushingChangesProgressBar = QtWidgets.QProgressBar(Dialog)
        self.PushingChangesProgressBar.setGeometry(QtCore.QRect(130, 140, 118, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.PushingChangesProgressBar.setFont(font)
        self.PushingChangesProgressBar.setProperty("value", 24)
        self.PushingChangesProgressBar.setObjectName("PushingChangesProgressBar")
        self.PushingChangesLabel = QtWidgets.QLabel(Dialog)
        self.PushingChangesLabel.setGeometry(QtCore.QRect(120, 110, 141, 21))
        self.PushingChangesLabel.setObjectName("PushingChangesLabel")
        self.DemoBtn = QtWidgets.QPushButton(Dialog)
        self.DemoBtn.setGeometry(QtCore.QRect(340, 260, 51, 32))
        self.DemoBtn.setObjectName("DemoBtn")
        self.DemoBtn.clicked.connect(closeCurrentScreen)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.PushingChangesLabel.setText(_translate("Dialog", "PUSHING CHANGES..."))
        self.DemoBtn.setText(_translate("Dialog", "Demo Btn"))

    def scanCompletePopup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Scan Complete")
        msg.setText("Awaiting Lead Approval")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(self.showDeniedScreen)
        x = msg.exec_()

    def showDeniedScreen(self):
        self.window = QtWidgets.QDialog()
        self.ui = DeniedScreen()
        self.ui.setupUi(self.window)
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = PushingChangesScreen()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
