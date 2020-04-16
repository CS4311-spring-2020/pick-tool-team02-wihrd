
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QInputDialog, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QTextEdit, QPushButton
from Models.EventConfiguration import EventConfiguration

class EventConfigDialog(object):
    def setUpDialogUI(self, QWidget):


        def closeDialogHelper():
            eventConfig.setName(eventNameEditText.text())
            eventConfig.setDescription(eventDescriptionEditText.toPlainText())
            eventConfig.setRootDirectory(rootDirectoryEditText.text())
            eventConfig.setStartDate(startTimeEdit.text())
            eventConfig.setEndDate(endTimeEdit.text())
            QWidget.close()
        
        eventConfig =  EventConfiguration.getinstance()
        QWidget.title = "Event Configuration"
        QWidget.resize(700,500)
        mainLabel = QLabel("Event Configuration Settings")
        wrapperLayout = QVBoxLayout()
        wrapperLayout.addWidget(mainLabel)
        primaryGroupbox = QGroupBox()
        primaryLayout = QHBoxLayout()
        primaryLayout.setSpacing(0)
        eventDataLayout = QVBoxLayout()
        #eventDataLayout.setSpacing(0)
        #eventDataLayout.setContentsMargins(0,0,0,0)
        rootDirectoryLayout = QVBoxLayout()
        #rootDirectoryLayout.setSpacing(0)
        #rootDirectoryLayout.setContentsMargins(0,0,0,0)

        eventDataLabel = QLabel("General Event Information")
        eventDataLayout.addWidget(eventDataLabel)
        
        eventNameLabel = QLabel("Event Name")
        eventNameEditText = QLineEdit()
        eventNameEditText.setText(eventConfig.getName())
        eventNameEditText.displayText()
        eventDataLayout.addWidget(eventNameLabel)
        eventDataLayout.addWidget(eventNameEditText)

        eventDescriptionLable = QLabel ("Event Description")
        eventDescriptionEditText = QTextEdit()
        eventNameEditText.wordWrapMode = QTextEdit.WidgetWidth
        eventDescriptionEditText.setText(eventConfig.getDescription())
        eventDataLayout.addWidget(eventDescriptionLable)
        eventDataLayout.addWidget(eventDescriptionEditText)

        eventDescriptionGroup = QGroupBox()
        eventDescriptionGroup.setLayout(eventDataLayout)

        rootDirectoryLable = QLabel("Root Directory Information")
        rootDirectoryCurrentLable = QLabel("Current Root Directory")
        rootDirectoryEditText = QLineEdit()
        rootDirectoryEditText.setText(eventConfig.getRootDirectory())
        rootDirectoryEditText.displayText()
        rootDirectoryBrowseButton = QPushButton("Browse")
        dateLabel = QLabel("Start and End Dates")
        startTimeLable = QLabel("Start Date")
        startTimeEdit = QLineEdit()
        startTimeEdit.setText(eventConfig.getStartDate())
        startTimeEdit.displayText()
        endTimeLable = QLabel("End Date")
        endTimeEdit = QLineEdit()
        endTimeEdit.setText(eventConfig.getEndDate())
        endTimeEdit.displayText()
        spacerlable = QLabel()
        spacerlable2 = QLabel()
        rootDirectoryLayout.addWidget(rootDirectoryLable)
        rootDirectoryLayout.addWidget(rootDirectoryCurrentLable)
        rootDirectoryLayout.addWidget(rootDirectoryEditText)
        rootDirectoryLayout.addWidget(rootDirectoryBrowseButton)
        rootDirectoryLayout.addWidget(spacerlable)
        rootDirectoryLayout.addWidget(spacerlable2)
        rootDirectoryLayout.addWidget(dateLabel)
        rootDirectoryLayout.addWidget(startTimeLable)
        rootDirectoryLayout.addWidget(startTimeEdit)
        rootDirectoryLayout.addWidget(endTimeLable)
        rootDirectoryLayout.addWidget(endTimeEdit)

        rootDirectoryGroupBox = QGroupBox()
        rootDirectoryGroupBox.setLayout(rootDirectoryLayout)

        primaryLayout.addWidget(eventDescriptionGroup)
        primaryLayout.addWidget(rootDirectoryGroupBox)
        primaryGroupbox.setLayout(primaryLayout)

        wrapperLayout.addWidget(primaryGroupbox)
        saveBtn = QPushButton("Save")
        saveBtn.clicked.connect(closeDialogHelper)
        wrapperLayout.addWidget(saveBtn)

        QWidget.setLayout(wrapperLayout)
        
        QWidget.show()


        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog  = QWidget()
    ui = EventConfigDialog()
    ui.setUpDialogUI(dialog)
    dialog.show()
    sys.exit(app.exec_())