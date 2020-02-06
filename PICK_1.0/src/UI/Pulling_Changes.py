# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pulling Changes.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class PullingChangesScreen(object):
    def setupUi(self, Dialog):

        def closeCurrentScreen():
            self.syncedAlert()
            Dialog.close()

        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.PullingChangesProgressBar = QtWidgets.QProgressBar(Dialog)
        self.PullingChangesProgressBar.setGeometry(QtCore.QRect(130, 130, 118, 23))
        self.PullingChangesProgressBar.setProperty("value", 50)
        self.PullingChangesProgressBar.setTextVisible(True)
        self.PullingChangesProgressBar.setObjectName("PullingChangesProgressBar")
        self.PullingChangesLabel = QtWidgets.QLabel(Dialog)
        self.PullingChangesLabel.setGeometry(QtCore.QRect(130, 110, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PullingChangesLabel.setFont(font)
        self.PullingChangesLabel.setObjectName("PullingChangesLabel")
        self.DemoBtn = QtWidgets.QPushButton(Dialog)
        self.DemoBtn.setGeometry(QtCore.QRect(340, 260, 51, 32))
        self.DemoBtn.setObjectName("DemoBtn")
        self.DemoBtn.clicked.connect(closeCurrentScreen)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.PullingChangesLabel.setText(_translate("Dialog", "PULLING CHANGES..."))
        self.DemoBtn.setText(_translate("Dialog", "DemoBtn"))

    def syncedAlert(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alert!")
        msg.setText("Synced")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = PullingChangesScreen()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
