#LogEntryScreen
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QGroupBox, QApplication, QWidget, QTableWidget, QListWidget, QListWidgetItem, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QRect
from Models.LogEntry import logEntry

class LogEntryScreen(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.top = parent.top
        self.left = parent.left
        self.height = parent.height
        self.width = parent.width
        dimen = QRect(0,0,self.height/2,self.width/3)

        primaryLayout = QVBoxLayout(self)
        buttonlayout = QHBoxLayout()

        log1 = logEntry("bleh","sdf","asd","sa")
        log2 = logEntry("asdfasdf","sasdfasdfdf","aasdfsasd","asdfsdfsa")
        log3 = logEntry("123123","1323132","12321","113223")

        list = []
        list.append(log1)
        list.append(log2)
        list.append(log3)


        logEntryTableLable = QLabel("Log Entries")
        logEntryTableLabels = ["Log ID", "Log Name", "TimeStamp", "Description", "Reporter", "Artifact", "Team"]
        logEntryTable = QTableWidget(1, 7)
        logEntryTable.setHorizontalHeaderLabels(logEntryTableLabels)
        header = logEntryTable.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        primaryLayout.addWidget(logEntryTableLable)
        primaryLayout.addWidget(logEntryTable)

        self.refreshTable(logEntryTable, list)


        filterbtn = QPushButton("Filter")
        markSigbtn = QPushButton("Mark As Significant")
        associatebtn = QPushButton("Associate")
        spacerlabel1 = QLabel()
        spacerlabel2 = QLabel()
        spacerlabel3 = QLabel()
        buttonlayout.addWidget(spacerlabel1)
        buttonlayout.addWidget(spacerlabel2)
        buttonlayout.addWidget(spacerlabel3)
        buttonlayout.addWidget(associatebtn)
        buttonlayout.addWidget(markSigbtn)
        buttonlayout.addWidget(filterbtn)
        buttonGroupBox = QGroupBox()
        buttonGroupBox.setLayout(buttonlayout)

        primaryLayout.addWidget(buttonGroupBox)

        self.show()



    def refreshTable(self, tableWidget, logEntryList):
        print("firstloop")
        if(logEntryList and tableWidget):
            print("secondloop")
            rowcount = tableWidget.rowCount()
            for logEntry in logEntryList:
                print("thirdloop")
                tableWidget.insertRow(rowcount)
                tableWidget.setItem(rowcount, 0, QtWidgets.QTableWidgetItem(rowcount))
                tableWidget.setItem(rowcount, 1, QtWidgets.QTableWidgetItem(logEntry.get_name()))
                tableWidget.setItem(rowcount, 2, QtWidgets.QTableWidgetItem(logEntry.get_timestamp()))
                tableWidget.setItem(rowcount, 3, QtWidgets.QTableWidgetItem(logEntry.get_description()))
                tableWidget.setItem(rowcount, 4, QtWidgets.QTableWidgetItem(""))
                tableWidget.setItem(rowcount, 5, QtWidgets.QTableWidgetItem(logEntry.get_path()))
                tableWidget.setItem(rowcount, 6, QtWidgets.QTableWidgetItem(""))
                rowcount = rowcount+1
            #tableWidget.Repaint()






if __name__ == "__main__":
    app = QApplication(sys.argv)
    #ex = LogIngestionScreen()
    sys.exit(app.exec_())
