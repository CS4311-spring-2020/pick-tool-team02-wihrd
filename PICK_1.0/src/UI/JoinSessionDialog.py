# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JoinSessionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Main_Screen_UI import MainScreen


class JoinSessionDialog(object):
    def setupUi(self, JoinSessionDialog):

        def launchMainScreenHelper():
            JoinSessionDialog.close()
            self.launchMainScreen()

        JoinSessionDialog.setObjectName("JoinSessionDialog")
        JoinSessionDialog.resize(438, 359)
        self.JoinSessionDialogJoinSessionLabel = QtWidgets.QLabel(JoinSessionDialog)
        self.JoinSessionDialogJoinSessionLabel.setGeometry(QtCore.QRect(10, 20, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.JoinSessionDialogJoinSessionLabel.setFont(font)
        self.JoinSessionDialogJoinSessionLabel.setObjectName("JoinSessionDialogJoinSessionLabel")
        self.JoinSessionDialogJoinSessionLabel_2 = QtWidgets.QLabel(JoinSessionDialog)
        self.JoinSessionDialogJoinSessionLabel_2.setGeometry(QtCore.QRect(10, 80, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.JoinSessionDialogJoinSessionLabel_2.setFont(font)
        self.JoinSessionDialogJoinSessionLabel_2.setObjectName("JoinSessionDialogJoinSessionLabel_2")
        self.JoinSessionIPAddressEdit = QtWidgets.QLineEdit(JoinSessionDialog)
        self.JoinSessionIPAddressEdit.setGeometry(QtCore.QRect(10, 100, 151, 21))
        self.JoinSessionIPAddressEdit.setObjectName("JoinSessionIPAddressEdit")
        self.JoinSessionLeadLabel = QtWidgets.QLabel(JoinSessionDialog)
        self.JoinSessionLeadLabel.setGeometry(QtCore.QRect(10, 160, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.JoinSessionLeadLabel.setFont(font)
        self.JoinSessionLeadLabel.setObjectName("JoinSessionLeadLabel")
        self.LeadCheckboxYes = QtWidgets.QCheckBox(JoinSessionDialog)
        self.LeadCheckboxYes.setGeometry(QtCore.QRect(10, 190, 51, 20))
        self.LeadCheckboxYes.setObjectName("LeadCheckboxYes")
        self.LeadCheckboxNo = QtWidgets.QCheckBox(JoinSessionDialog)
        self.LeadCheckboxNo.setGeometry(QtCore.QRect(70, 190, 51, 20))
        self.LeadCheckboxNo.setObjectName("LeadCheckboxNo")
        self.JoinSessionBtn = QtWidgets.QPushButton(JoinSessionDialog)
        self.JoinSessionBtn.setGeometry(QtCore.QRect(290, 300, 113, 32))
        self.JoinSessionBtn.setObjectName("JoinSessionBtn")
        self.JoinSessionBtn.clicked.connect(launchMainScreenHelper)

        self.retranslateUi(JoinSessionDialog)
        QtCore.QMetaObject.connectSlotsByName(JoinSessionDialog)

    def retranslateUi(self, JoinSessionDialog):
        _translate = QtCore.QCoreApplication.translate
        JoinSessionDialog.setWindowTitle(_translate("JoinSessionDialog", "Dialog"))
        self.JoinSessionDialogJoinSessionLabel.setText(_translate("JoinSessionDialog", "Join Session"))
        self.JoinSessionDialogJoinSessionLabel_2.setText(_translate("JoinSessionDialog", "Enter Session IP Address:"))
        self.JoinSessionIPAddressEdit.setText(_translate("JoinSessionDialog", "192.168.1.1"))
        self.JoinSessionLeadLabel.setText(_translate("JoinSessionDialog", "Are you a lead:"))
        self.LeadCheckboxYes.setText(_translate("JoinSessionDialog", "Yes"))
        self.LeadCheckboxNo.setText(_translate("JoinSessionDialog", "No"))
        self.JoinSessionBtn.setText(_translate("JoinSessionDialog", "Join Session"))


    def launchMainScreen(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = MainScreen()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JoinSessionDialog = QtWidgets.QDialog()
    ui = JoinSessionDialog()
    ui.setupUi(JoinSessionDialog)
    JoinSessionDialog.show()
    sys.exit(app.exec_())
