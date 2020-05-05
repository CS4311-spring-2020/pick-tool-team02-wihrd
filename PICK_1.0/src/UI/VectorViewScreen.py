import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QGroupBox, QApplication, QWidget, QTableWidget, QListWidget, QListWidgetItem, QPushButton, QComboBox, QTabWidget
from graph.graph_editor import GraphEditor
from graph.graph_editor_view import GraphEditorView
from AddNewVectorDialog import addVectorDialog
from Models.EventConfiguration import EventConfiguration

class VectorScreen(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        def showAddVectorPopup(self, vectorComboBox):
            self.popup = QWidget()
            self.avDialog = addVectorDialog()
            self.avDialog.setUpDialogUI(self.popup)
            self.updateVectorComboBox(vectorComboBox)
            self.popup.show()


        primaryLayout = QVBoxLayout(self)
        mainlabel = QLabel("Vector View")

        vectorselectLayout = QHBoxLayout()
        vectorComboBox = QComboBox()
        self.updateVectorComboBox(vectorComboBox)
        vectorComboBox.currentIndexChanged.connect(lambda: self.selectionchanged(vectorComboBox.currentIndex(), vectorTable))
        vectorAddButton = QPushButton("Add New Vector")
        vectorAddButton.clicked.connect(lambda: showAddVectorPopup(self, vectorComboBox))
        spacerlabel = QLabel()
        spacerlabel1 = QLabel()
        spacerlabel2 = QLabel()
        spacerlabel3 = QLabel()
        spacerlabel4 = QLabel()
        vectorselectGroupBox = QGroupBox()
        vectorselectLayout.addWidget(vectorComboBox)
        vectorselectLayout.addWidget(vectorAddButton)
        vectorselectLayout.addWidget(spacerlabel)
        vectorselectLayout.addWidget(spacerlabel1)
        vectorselectLayout.addWidget(spacerlabel2)
        vectorselectLayout.addWidget(spacerlabel3)
        vectorselectLayout.addWidget(spacerlabel4)
        vectorselectGroupBox.setLayout(vectorselectLayout)

        tabs = QTabWidget()
        vectorTableHeaders = ["Log ID", "Log Name", "TimeStamp", "Description", "Reporter", "Artifact", "Team"]
        vectorTable = QTableWidget(1, 7)
        vectorTable.setHorizontalHeaderLabels(vectorTableHeaders)
        header = vectorTable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        tabletab = vectorTable
        tabs.addTab(tabletab, "Table")

        graphEditor = GraphEditor()
        graphEditorScene = graphEditor.graph_editor_scene
        graphEditorView = GraphEditorView(graphEditorScene, tabs)
        graphTab = graphEditorView
        tabs.addTab(graphTab, "Graph")

        primaryLayout.addWidget(mainlabel)
        primaryLayout.addWidget(vectorselectGroupBox)
        primaryLayout.addWidget(tabs)

        self.show()



    def updateVectorComboBox(self, vectorComboBox):
        eventconfig = EventConfiguration.getinstance()
        vectorComboBox.clear()
        for vector in eventconfig.getVectorList():
            vectorComboBox.addItem(vector.get_name())

    def selectionchanged(self, i, vectorTable):
        eventconfig = EventConfiguration.getinstance()
        vectorList = eventconfig.getVectorList()
        vector = vectorList[i]
        logEntryList = vector.get_logentrys()
        print("firstloop")
        if (logEntryList and vectorTable):
            print("secondloop")
            rowcount = vectorTable.rowCount()
            for logEntry in logEntryList:
                print("thirdloop")
                vectorTable.insertRow(rowcount)
                vectorTable.setItem(rowcount, 0, QtWidgets.QTableWidgetItem(rowcount))
                vectorTable.setItem(rowcount, 1, QtWidgets.QTableWidgetItem(logEntry.get_name()))
                vectorTable.setItem(rowcount, 2, QtWidgets.QTableWidgetItem(logEntry.get_timestamp()))
                vectorTable.setItem(rowcount, 3, QtWidgets.QTableWidgetItem(logEntry.get_description()))
                vectorTable.setItem(rowcount, 4, QtWidgets.QTableWidgetItem(""))
                vectorTable.setItem(rowcount, 5, QtWidgets.QTableWidgetItem(logEntry.get_path()))
                vectorTable.setItem(rowcount, 6, QtWidgets.QTableWidgetItem(""))
                rowcount = rowcount + 1







if __name__ == "__main__":
    app = QApplication(sys.argv)
    #ex = LogIngestionScreen()
    sys.exit(app.exec_())




