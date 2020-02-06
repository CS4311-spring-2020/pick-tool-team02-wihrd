# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Denied.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Pulling_Changes import PullingChangesScreen


class DeniedScreen(object):
    def setupUi(self, Dialog):

        def closeCurrentScreen():
            self.dbChangesAlertPopup()
            Dialog.close()

        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.DeniedPopupOkBtn = QtWidgets.QDialogButtonBox(Dialog)
        self.DeniedPopupOkBtn.setGeometry(QtCore.QRect(230, 240, 141, 32))
        self.DeniedPopupOkBtn.setOrientation(QtCore.Qt.Horizontal)
        self.DeniedPopupOkBtn.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.DeniedPopupOkBtn.setObjectName("DeniedPopupOkBtn")
        self.CorrectResyncTextField = QtWidgets.QTextBrowser(Dialog)
        self.CorrectResyncTextField.setGeometry(QtCore.QRect(30, 230, 161, 41))
        self.CorrectResyncTextField.setObjectName("CorrectResyncTextField")
        self.ReasonDenialTextField = QtWidgets.QTextBrowser(Dialog)
        self.ReasonDenialTextField.setGeometry(QtCore.QRect(30, 40, 341, 192))
        self.ReasonDenialTextField.setObjectName("ReasonDenialTextField")
        self.DeniedLabel = QtWidgets.QLabel(Dialog)
        self.DeniedLabel.setGeometry(QtCore.QRect(160, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DeniedLabel.setFont(font)
        self.DeniedLabel.setObjectName("DeniedLabel")

        self.retranslateUi(Dialog)
        self.DeniedPopupOkBtn.accepted.connect(closeCurrentScreen)
        self.DeniedPopupOkBtn.rejected.connect(closeCurrentScreen)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.CorrectResyncTextField.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Correct to resync changes.</span></p></body></html>"))
        self.ReasonDenialTextField.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">Reason for denial.</span></p></body></html>"))
        self.DeniedLabel.setText(_translate("Dialog", "DENIED"))

    def dbChangesAlertPopup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alert!")
        msg.setText("New Changes to Pull")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.Ignore)
        msg.buttonClicked.connect(self.showPullingChangesScreen)
        x = msg.exec_()

    def showPullingChangesScreen(self, i):
        self.window = QtWidgets.QDialog()
        self.ui = PullingChangesScreen()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = DeniedScreen()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
