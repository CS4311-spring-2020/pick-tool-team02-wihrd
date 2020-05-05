
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QInputDialog, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QTextEdit, QPushButton
from Models.EventConfiguration import EventConfiguration
from Models.Vector import vector

class addVectorDialog(object):

    def setUpDialogUI(self, QWidget):

        def closeDialogHelper():
            startDate = startTimeEdit.text()
            endDate = endTimeEdit.text()
            creator = rootDirectoryEditText.text()
            description = eventDescriptionEditText.toPlainText()
            name = eventNameEditText.text()
            newVector = vector(startDate, endDate, creator, description, name)
            eventConfig.addVector(newVector)
            QWidget.close()

        eventConfig = EventConfiguration.getinstance()
        QWidget.title = "Add A Vector"
        QWidget.resize(700, 500)
        mainLabel = QLabel("Add A New Vector")
        wrapperLayout = QVBoxLayout()
        wrapperLayout.addWidget(mainLabel)
        primaryGroupbox = QGroupBox()
        primaryLayout = QHBoxLayout()
        primaryLayout.setSpacing(0)
        eventDataLayout = QVBoxLayout()
        # eventDataLayout.setSpacing(0)
        # eventDataLayout.setContentsMargins(0,0,0,0)
        rootDirectoryLayout = QVBoxLayout()
        # rootDirectoryLayout.setSpacing(0)
        # rootDirectoryLayout.setContentsMargins(0,0,0,0)

        eventDataLabel = QLabel("General Vector Information")
        eventDataLayout.addWidget(eventDataLabel)

        eventNameLabel = QLabel("Vector Name")
        eventNameEditText = QLineEdit()
        eventNameEditText.setText(eventConfig.getName())
        eventNameEditText.displayText()
        eventDataLayout.addWidget(eventNameLabel)
        eventDataLayout.addWidget(eventNameEditText)

        eventDescriptionLable = QLabel("Vector Description")
        eventDescriptionEditText = QTextEdit()
        eventNameEditText.wordWrapMode = QTextEdit.WidgetWidth
        eventDescriptionEditText.setText(eventConfig.getDescription())
        eventDataLayout.addWidget(eventDescriptionLable)
        eventDataLayout.addWidget(eventDescriptionEditText)

        eventDescriptionGroup = QGroupBox()
        eventDescriptionGroup.setLayout(eventDataLayout)

        rootDirectoryLable = QLabel("Creator")
        rootDirectoryEditText = QLineEdit()
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
        rootDirectoryLayout.addWidget(rootDirectoryEditText)
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
        saveBtn = QPushButton("Add")
        saveBtn.clicked.connect(closeDialogHelper)
        wrapperLayout.addWidget(saveBtn)

        QWidget.setLayout(wrapperLayout)

        QWidget.show()
