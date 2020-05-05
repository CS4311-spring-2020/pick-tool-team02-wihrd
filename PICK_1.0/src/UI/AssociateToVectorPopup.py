import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QInputDialog, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QTextEdit, QPushButton, QComboBox
from Models.EventConfiguration import EventConfiguration
from UI.Models.LogEntry import logEntry

class AssociateToVector(object):

    logentry : logEntry

    def setUpDialogUI(self, QWidget):


        def closeDialogHelper(self, vectorComboBox):

            try:
                eventConfig = EventConfiguration.getinstance()
                vectorList = eventConfig.getVectorList()
                vector = vectorList[vectorComboBox.currentIndex()]
                vector.addLogEntry(self.logentry)
                QWidget.close()
            except Exception as e:
                print('error close dialog:')
                print(str(e))

        
        primaryLayout = QVBoxLayout()
        mainLabel = QLabel("Associate to Vector")
        logentryLabel = QLabel("Log Entry" + self.logentry.get_path())
        vectorComboBox = QComboBox()
        self.updateVectorComboBox(vectorComboBox)
        savebutton = QPushButton("Associate")
        try:
            savebutton.clicked.connect(lambda: closeDialogHelper(self, vectorComboBox))
        except Exception as e:
            print('error close dialog:')
            print(str(e))
        primaryLayout.addWidget(mainLabel)
        primaryLayout.addWidget(logentryLabel)
        primaryLayout.addWidget(vectorComboBox)
        primaryLayout.addWidget(savebutton)

        QWidget.setLayout(primaryLayout)
        QWidget.show()


    def updateVectorComboBox(self, vectorComboBox):
        eventConfig = EventConfiguration.getinstance()
        vectorlist = eventConfig.getVectorList()
        for vector in vectorlist:
            vectorComboBox.addItem(vector.get_name())






if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = QWidget()
    ui = AssociateToVector()
    ui.setUpDialogUI(dialog)
    dialog.show()
    sys.exit(app.exec_())