# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ExportGraph.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class ExportGraphScreen(object):
    def setupUi(self, ExportGraph):

        def closeCurrentScreen():
            ExportGraph.close()

        ExportGraph.setObjectName("ExportGraph")
        ExportGraph.resize(398, 341)
        self.ExportGraphExportButton = QtWidgets.QPushButton(ExportGraph)
        self.ExportGraphExportButton.setGeometry(QtCore.QRect(30, 260, 81, 31))
        self.ExportGraphExportButton.setObjectName("ExportGraphExportButton")
        self.ExportGraphExportButton.clicked.connect(closeCurrentScreen)
        self.ExportGraphJPNGButton = QtWidgets.QPushButton(ExportGraph)
        self.ExportGraphJPNGButton.setGeometry(QtCore.QRect(110, 80, 81, 31))
        self.ExportGraphJPNGButton.setObjectName("ExportGraphJPNGButton")
        self.ExportGraphPNGButton = QtWidgets.QPushButton(ExportGraph)
        self.ExportGraphPNGButton.setGeometry(QtCore.QRect(30, 80, 81, 31))
        self.ExportGraphPNGButton.setObjectName("ExportGraphPNGButton")
        self.ExportGraphNameText = QtWidgets.QTextEdit(ExportGraph)
        self.ExportGraphNameText.setGeometry(QtCore.QRect(30, 10, 101, 31))
        self.ExportGraphNameText.setObjectName("ExportGraphNameText")
        self.ExportGraphNameTextBox = QtWidgets.QPlainTextEdit(ExportGraph)
        self.ExportGraphNameTextBox.setGeometry(QtCore.QRect(30, 50, 131, 31))
        self.ExportGraphNameTextBox.setObjectName("ExportGraphNameTextBox")

        self.retranslateUi(ExportGraph)
        QtCore.QMetaObject.connectSlotsByName(ExportGraph)

    def retranslateUi(self, ExportGraph):
        _translate = QtCore.QCoreApplication.translate
        ExportGraph.setWindowTitle(_translate("ExportGraph", "Dialog"))
        self.ExportGraphExportButton.setText(_translate("ExportGraph", "Export"))
        self.ExportGraphJPNGButton.setText(_translate("ExportGraph", "JPEG"))
        self.ExportGraphPNGButton.setText(_translate("ExportGraph", "PNG"))
        self.ExportGraphNameText.setHtml(_translate("ExportGraph", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.875pt;\">Name</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.875pt;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ExportGraph = QtWidgets.QDialog()
    ui = ExportGraphScreen()
    ui.setupUi(ExportGraph)
    ExportGraph.show()
    sys.exit(app.exec_())
