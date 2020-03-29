import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QGroupBox, QApplication, QWidget, QTableWidget, QListWidget, QListWidgetItem, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QRect

class LogIngestionScreen(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.top = parent.top
        self.left = parent.left
        self.height = parent.height
        self.width = parent.width
        dimen = QRect(0,0,self.height/2,self.width/3)

        # Declaring Layouts 
        mainLayout = QVBoxLayout(self)
        mainLayout.setGeometry(dimen)
        validationLayout = QHBoxLayout()
        #validationLayout.setGeometry(dimen)
        bottomLayout = QHBoxLayout()
        validationTableLayout = QVBoxLayout()
        cleansingLayout = QVBoxLayout()
        enforcementTableLayout = QVBoxLayout()
        validationTableButtonsLayout = QHBoxLayout()

        #ValidationTableLayout Content Definitions
        validationTableLabels = ["Log File", "Time", "Description", "Team", "Progress", "Status"]
        validationTable = QTableWidget(3, 6)
        validationTable.setHorizontalHeaderLabels(validationTableLabels)
        header = validationTable.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        validationTableGroupBox = QGroupBox("Validation")
        validationTableLayout.addWidget(validationTable)
        validationTableGroupBox.setLayout(validationTableLayout)
        importLogsBtn = QPushButton("Import Logs")
        ingestLogsBtn = QPushButton("Ingest Logs")
        spacerlabel = QLabel()
        spacerlabel3 = QLabel()
        spacerlabel4 = QLabel()
        spacerlabel5 = QLabel()
        spacerlabel6 = QLabel()
        validationBtnGroupBox = QGroupBox()
        validationTableButtonsLayout.addWidget(spacerlabel, alignment = QtCore.Qt.AlignRight)
        validationTableButtonsLayout.addWidget(spacerlabel3, alignment = QtCore.Qt.AlignRight)
        validationTableButtonsLayout.addWidget(spacerlabel4, alignment = QtCore.Qt.AlignRight)
        validationTableButtonsLayout.addWidget(spacerlabel5, alignment = QtCore.Qt.AlignRight)
        validationTableButtonsLayout.addWidget(spacerlabel6, alignment = QtCore.Qt.AlignRight)
        validationTableButtonsLayout.addWidget(importLogsBtn, alignment = QtCore.Qt.AlignRight)
        validationTableButtonsLayout.addWidget(ingestLogsBtn, alignment = QtCore.Qt.AlignRight)
        validationBtnGroupBox.setLayout(validationTableButtonsLayout)
        validationTableLayout.addWidget(validationBtnGroupBox)

        #Validation Settings
        validationGroupBox = QGroupBox()
        validationGroupBox.setLayout(validationLayout)



        #Enforcement Action Table Layout
        enfrocementTableHeaders = ["Log File", "Time", "Description", "Team", "Error"]
        enforcementTable = QTableWidget(4, 5)
        enforcementTable.setHorizontalHeaderLabels(enfrocementTableHeaders)
        enforcementTableGroupBox = QGroupBox("Enforcement Action Reports")
        enforcementTableLayout.addWidget(enforcementTable)
        enforcementTableGroupBox.setLayout(enforcementTableLayout)
        ignoreEARbtn = QPushButton("Ignore")
        confirmEARbtn = QPushButton("Confirm")
        spacerlabel7 = QLabel()
        spacerlabel8 = QLabel()
        enforcementbtnGroupBox = QGroupBox()
        enforcementbtnLayout = QHBoxLayout()
        enforcementbtnLayout.addWidget(spacerlabel7)
        enforcementbtnLayout.addWidget(spacerlabel8)
        enforcementbtnLayout.addWidget(ignoreEARbtn)
        enforcementbtnLayout.addWidget(confirmEARbtn)
        enforcementbtnGroupBox.setLayout(enforcementbtnLayout)
        enforcementTableLayout.addWidget(enforcementbtnGroupBox)

        #cleansing layout content definitions
        cleansingList = QListWidget()
        listItem1 = QListWidgetItem("Log A")
        listItem2 = QListWidgetItem("Log B")
        listItem3 = QListWidgetItem("Log C")
        cleansingList.addItem(listItem1)
        cleansingList.addItem(listItem2)
        cleansingList.addItem(listItem3)
        cleansingGroupBox = QGroupBox("Cleansed Files")
        cleansingLayout.addWidget(cleansingList)
        cleansingGroupBox.setLayout(cleansingLayout)
        #validationLayout.addWidget(cleansingGroupBox)


        bottomLayout.addWidget(enforcementTableGroupBox)
        bottomLayout.addWidget(cleansingGroupBox)
        enforcementGroupBox = QGroupBox()
        enforcementGroupBox.setLayout(bottomLayout)

        mainLayout.addWidget(validationTableGroupBox)
        mainLayout.addWidget(enforcementGroupBox)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    #ex = LogIngestionScreen()
    sys.exit(app.exec_())
