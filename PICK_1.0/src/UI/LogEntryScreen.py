#LogEntryScreen
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QGroupBox, QApplication, QWidget, QTableWidget, QListWidget, QListWidgetItem, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QRect

class LogEntryScreen(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.top = parent.top
        self.left = parent.left
        self.height = parent.height
        self.width = parent.width
        dimen = QRect(0,0,self.height/2,self.width/3)







if __name__ == "__main__":
    app = QApplication(sys.argv)
    #ex = LogIngestionScreen()
    sys.exit(app.exec_())
