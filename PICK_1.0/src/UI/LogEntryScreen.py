#LogEntryScreen
import time
import os
import re
import datetime
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QGroupBox, QApplication, QWidget, QTableWidget, QListWidget, QListWidgetItem, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QRect

from UI.Models.LogEntry import logEntry
from UI.AssociateToVectorPopup import AssociateToVector
from UI.splunkAuth import *


class LogEntryScreen(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        def showAddVectorPopup(self, logEntryTable, logEntryList):

            try:
                indexes = logEntryTable.selectionModel().selectedRows()
                index = indexes[0].row()
                logEntry = logEntryList[index]
                AssociateToVector.logentry = logEntry
                self.popup = QWidget()
                self.avDialog = AssociateToVector()
                self.avDialog.setUpDialogUI(self.popup)
                self.popup.show()

            except Exception as e:
                print('error associate:')
                print(str(e))


        def showFilterDialog(self, logEntryTable, logEntryList):

            try:
                FilterPopup.tablewidget = logEntryTable
                FilterPopup.logEntryList = logEntryList
                self.popup = QWidget()
                self.avDialog = FilterPopup()
                self.avDialog.setUpDialogUI(self.popup)
                self.popup.show()

            except Exception as e:
                print('error filter')
                print(str(e))

        
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

        self.refreshTable(logEntryTable, splunkExport())


        filterbtn = QPushButton("Filter")
        filterbtn.clicked.connect(lambda: showFilterDialog(self, logEntryTable, splunkExport()))
        markSigbtn = QPushButton("Mark As Significant")
        associatebtn = QPushButton("Associate")
        associatebtn.clicked.connect(lambda: showAddVectorPopup(self, logEntryTable, splunkExport()))
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


class FilterPopup(object):

    tablewidget : QTableWidget
    logEntryList : []

    def setUpDialogUI(self, QWidget):

        def get_dir(logEntry):
            dir = os.path.dirname(logEntry.get_path()).lower()
            return dir

        def time_split(logEntry):
            pattern = "\d{2}[/]\d{2}[/]\d{2}"
            d = re.findall(pattern, logEntry.get_timestamp())
            date = d.pop()
            date = date.split("/")
            return date

        def name_sort(logEntryList):
            li = sorted(logEntryList, key=lambda x: x.get_name().lower())
            LogEntryScreen.refreshTable(self.tablewidget, li)
            QWidget.close()

        def des_sort(logEntryList):
            li = sorted(logEntryList, key= lambda x: x.get_description().lower())
            LogEntryScreen.refreshTable(self.tablewidget, li)
            QWidget.close()


        def time_sort(logEntryList):
            logEntryList.sort(key=lambda date: time.strptime(date.get_timestamp(), "%H:%M %m/%d/%y %p"))
            LogEntryScreen.refreshTable(self.tablewidget, logEntryList)
            QWidget.close()

        def source_sort(logEntryList):
            li = sorted(logEntryList, key= lambda x: x.get_path().lower())
            LogEntryScreen.refreshTable(self.tablewidget, li)
            QWidget.close()

        def only_white(logEntryList):
            nl = time_sort(logEntryList)
            li= []
            team = "white"
            for x in nl:
                d = get_dir(x)
                if (d.endswith(team)):
                    li.append(x)
            LogEntryScreen.refreshTable(self.tablewidget, li)
            QWidget.close()

        def only_red(logEntryList):
            nl = time_sort(logEntryList)
            li = []
            team = "red"
            for x in nl:
                d = get_dir(x)
                if (d.endswith(team)):
                    li.append(x)
            LogEntryScreen.refreshTable(self.tablewidget, li)
            QWidget.close()

        def only_blue(logEntryList):
            nl = time_sort(logEntryList)
            li = []
            team = "blue"
            for x in nl:
                d = get_dir(x)
                if (d.endswith(team)):
                    li.append(x)
            LogEntryScreen.refreshTable(self.tablewidget, li)
            QWidget.close()

        def date_range(logEntryList, sd, ed):
            li = time_sort(logEntryList)
            nl = []
            sd = sd.split("/")
            ed = ed.split("/")
            s = datetime.date(int(sd[2]), int(sd[0]), int(sd[1]))
            e = datetime.date(int(ed[2]), int(ed[0]), int(ed[1]))

            for x in li:
                d = time_split(x)
                ld = datetime.date(int(d[2]), int(d[0]), int(d[1]))
                if((ld  >= s) and (ld <= e)):
                    nl.append(x)
            return nl

        def search(logEntryList, item):
            nl = time_sort(logEntryList)
            li=[]
            try:
                item = item.lower()
            except:
                item = item

            for x in nl:
                l = x.get_timestamp().split("/")
                l1 = x.get_name().lower().split()
                l2 = x.get_description().lower().split()
                l3 = x.get_path().lower().split("\\")
                newList = l + l1+ l2 + l3
                for i in newList:
                    if(i == item):
                        li.append(x)
            LogEntryScreen.refreshTable(self.tablewidget, li)
            QWidget.close()

        primaryLayout = QVBoxLayout()
        mainLabel = QLabel("Filter:")
        nameFilterBtn = QPushButton("Filter by Name")
        nameFilterBtn.clicked.connect(lambda: name_sort(self, self.logEntryList))
        timeFilterBtn = QPushButton("Filter by Time")
        timeFilterBtn.clicked.connect(lambda: time_sort(self, self.logEntryList))
        descriptionFilterBtn = QPushButton("Filter by Description")
        descriptionFilterBtn.clicked.connect(lambda: des_sort(self, self.logEntryList))
        blueFilterButton = QPushButton("Filter by Blue Team")
        blueFilterButton.clicked.connect(lambda: only_blue(self, self.logEntryList))
        redFilterButton = QPushButton("Filter by Red Team")
        redFilterButton.clicked.connect(lambda: only_red(self, self.logEntryList))
        whiteFilterButton = QPushButton("Filter by White Team")
        whiteFilterButton.clicked.connect(lambda: only_white(self, self.logEntryList))
        searchLabel = QLabel("Search:")
        searchText = QLineEdit()
        searchBtn = QPushButton("Search")
        searchBtn.clicked.connect(lambda: search(self, self.logEntryList, searchText.text()))

        primaryLayout.addWidget(mainLabel)
        primaryLayout.addWidget(nameFilterBtn)
        primaryLayout.addWidget(timeFilterBtn)
        primaryLayout.addWidget(descriptionFilterBtn)
        primaryLayout.addWidget(blueFilterButton)
        primaryLayout.addWidget(redFilterButton)
        primaryLayout.addWidget(whiteFilterButton)
        primaryLayout.addWidget(searchLabel)
        primaryLayout.addWidget(searchText)
        primaryLayout.addWidget(searchBtn)

        QWidget.setLayout(primaryLayout)

        QWidget.show()







if __name__ == "__main__":
    app = QApplication(sys.argv)
    #ex = LogIngestionScreen()
    sys.exit(app.exec_())
