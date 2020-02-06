# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Filter.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class FilterScreen(object):
    def setupUi(self, Filter):

        def closeFilterScreen():
            Filter.close()

        Filter.setObjectName("Filter")
        Filter.resize(402, 340)
        self.FilterButton = QtWidgets.QPushButton(Filter)
        self.FilterButton.setGeometry(QtCore.QRect(30, 300, 121, 23))
        self.FilterButton.setObjectName("FilterButton")
        self.FilterButton.clicked.connect(closeFilterScreen)
        self.FilterSelectAttributeListWidgetBox = QtWidgets.QListWidget(Filter)
        self.FilterSelectAttributeListWidgetBox.setGeometry(QtCore.QRect(20, 100, 141, 161))
        self.FilterSelectAttributeListWidgetBox.setObjectName("FilterSelectAttributeListWidgetBox")
        item = QtWidgets.QListWidgetItem()
        self.FilterSelectAttributeListWidgetBox.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.FilterSelectAttributeListWidgetBox.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.FilterSelectAttributeListWidgetBox.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.FilterSelectAttributeListWidgetBox.addItem(item)
        self.FilterSelectKeywordListWidgetBox = QtWidgets.QListWidget(Filter)
        self.FilterSelectKeywordListWidgetBox.setGeometry(QtCore.QRect(200, 100, 151, 161))
        self.FilterSelectKeywordListWidgetBox.setObjectName("FilterSelectKeywordListWidgetBox")
        item = QtWidgets.QListWidgetItem()
        self.FilterSelectKeywordListWidgetBox.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.FilterSelectKeywordListWidgetBox.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.FilterSelectKeywordListWidgetBox.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.FilterSelectKeywordListWidgetBox.addItem(item)
        self.FilterSelectAttributeSearchBox = QtWidgets.QPlainTextEdit(Filter)
        self.FilterSelectAttributeSearchBox.setGeometry(QtCore.QRect(20, 50, 141, 31))
        self.FilterSelectAttributeSearchBox.setObjectName("FilterSelectAttributeSearchBox")
        self.FilterSelectKeywordSearchBox = QtWidgets.QPlainTextEdit(Filter)
        self.FilterSelectKeywordSearchBox.setGeometry(QtCore.QRect(200, 50, 151, 31))
        self.FilterSelectKeywordSearchBox.setObjectName("FilterSelectKeywordSearchBox")
        self.FilterSelectAttributeText = QtWidgets.QTextEdit(Filter)
        self.FilterSelectAttributeText.setGeometry(QtCore.QRect(20, 10, 111, 31))
        self.FilterSelectAttributeText.setObjectName("FilterSelectAttributeText")
        self.FilterSelectKeywordText = QtWidgets.QTextEdit(Filter)
        self.FilterSelectKeywordText.setGeometry(QtCore.QRect(200, 10, 111, 31))
        self.FilterSelectKeywordText.setObjectName("FilterSelectKeywordText")
        self.verticalScrollBar = QtWidgets.QScrollBar(Filter)
        self.verticalScrollBar.setGeometry(QtCore.QRect(160, 100, 16, 160))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(Filter)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(350, 100, 16, 160))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")

        self.retranslateUi(Filter)
        QtCore.QMetaObject.connectSlotsByName(Filter)

    def retranslateUi(self, Filter):
        _translate = QtCore.QCoreApplication.translate
        Filter.setWindowTitle(_translate("Filter", "Dialog"))
        self.FilterButton.setText(_translate("Filter", "Filter"))
        __sortingEnabled = self.FilterSelectAttributeListWidgetBox.isSortingEnabled()
        self.FilterSelectAttributeListWidgetBox.setSortingEnabled(False)
        item = self.FilterSelectAttributeListWidgetBox.item(0)
        item.setText(_translate("Filter", "Name"))
        item = self.FilterSelectAttributeListWidgetBox.item(1)
        item.setText(_translate("Filter", "ID"))
        item = self.FilterSelectAttributeListWidgetBox.item(2)
        item.setText(_translate("Filter", "Time Stamp"))
        item = self.FilterSelectAttributeListWidgetBox.item(3)
        item.setText(_translate("Filter", "Team"))
        self.FilterSelectAttributeListWidgetBox.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.FilterSelectKeywordListWidgetBox.isSortingEnabled()
        self.FilterSelectKeywordListWidgetBox.setSortingEnabled(False)
        item = self.FilterSelectKeywordListWidgetBox.item(0)
        item.setText(_translate("Filter", "White"))
        item = self.FilterSelectKeywordListWidgetBox.item(2)
        item.setText(_translate("Filter", "Attack"))
        item = self.FilterSelectKeywordListWidgetBox.item(3)
        item.setText(_translate("Filter", "11:40"))
        self.FilterSelectKeywordListWidgetBox.setSortingEnabled(__sortingEnabled)
        self.FilterSelectAttributeSearchBox.setPlainText(_translate("Filter", "Search\n"
""))
        self.FilterSelectKeywordSearchBox.setPlainText(_translate("Filter", "Search\n"
""))
        self.FilterSelectAttributeText.setHtml(_translate("Filter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select Attribute</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.FilterSelectKeywordText.setHtml(_translate("Filter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select Keyword</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Filter = QtWidgets.QDialog()
    ui = FilterScreen()
    ui.setupUi(Filter)
    Filter.show()
    sys.exit(app.exec_())
