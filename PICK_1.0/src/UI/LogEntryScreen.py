#LogEntryScreen
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QGroupBox, QApplication, QWidget, QTableWidget, QListWidget, QListWidgetItem, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QRect

class LogEntryScreen(QWidget):

    def __init__(self):
        super().__init__()
