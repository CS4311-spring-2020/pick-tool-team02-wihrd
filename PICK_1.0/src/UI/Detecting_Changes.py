# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Detecting Changes.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Pushing_Changes import PushingChangesScreen


class DetectingChangesScreen(object):
    def setupUi(self, Dialog):

        def moveToPushingChanges():
            Dialog.close()
            self.showPushingChangesScreen()

        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.DetectingChangesProgressBar = QtWidgets.QProgressBar(Dialog)
        self.DetectingChangesProgressBar.setGeometry(QtCore.QRect(140, 120, 118, 23))
        self.DetectingChangesProgressBar.setProperty("value", 88)
        self.DetectingChangesProgressBar.setObjectName("DetectingChangesProgressBar")
        self.DetectingChangesLabel = QtWidgets.QLabel(Dialog)
        self.DetectingChangesLabel.setGeometry(QtCore.QRect(134, 100, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DetectingChangesLabel.setFont(font)
        self.DetectingChangesLabel.setObjectName("DetectingChangesLabel")
        self.DemoBtn = QtWidgets.QPushButton(Dialog)
        self.DemoBtn.setGeometry(QtCore.QRect(330, 260, 61, 32))
        self.DemoBtn.setObjectName("DemoBtn")
        self.DemoBtn.clicked.connect(moveToPushingChanges)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.DetectingChangesLabel.setText(_translate("Dialog", "DETECTING CHANGES..."))
        self.DemoBtn.setText(_translate("Dialog", "Demo Btn"))

    def showPushingChangesScreen(self):
        self.window = QtWidgets.QDialog()
        self.ui = PushingChangesScreen()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = DetectingChangesScreen()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
