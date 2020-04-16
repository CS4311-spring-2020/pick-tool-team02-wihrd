import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout, qApp, QAction, QToolBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from LogIngestionScreen import LogIngestionScreen
from EventConfigDialog import EventConfigDialog
from LogEntryScreen import LogEntryScreen

class App(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.title = 'PICK 1.0'
        self.left = 0
        self.top = 0
        self.width = 1000
        self.height = 700
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        exitAct = QAction(QIcon('exit.png'), '&Exit', self)        
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        button_action = QAction("Event Configuration", self)
        button_action.setStatusTip("Click this button to edit the details and key information about the current Event!")
        button_action.triggered.connect(self.showEventConfigScreen)
        toolbar.addAction(button_action)

        self.home_page = HomePage(self)
        self.setCentralWidget(self.home_page)
        
        self.show()

    def onMyToolBarButtonClick(self, s):
        print("click", s)

    def showEventConfigScreen(self):
        self.popup = QWidget()
        self.ecDialog = EventConfigDialog()
        self.ecDialog.setUpDialogUI(self.popup)
        self.popup.show()


class HomePage(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.left = parent.left
        self.top = parent.top
        self.width = parent.width
        self.height = parent.height
        self.layout = QVBoxLayout(self)

        self.tabs = QTabWidget()
        self.tab1 = LogIngestionScreen(self)
        self.tab2 = LogEntryScreen(self)
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()

        self.tabs.resize(300,200)

        self.tabs.addTab(self.tab1, "Log Ingestion")
        self.tabs.addTab(self.tab2, "Log Entries")
        self.tabs.addTab(self.tab3, "Vector View")
        self.tabs.addTab(self.tab4, "History")
        self.tabs.addTab(self.tab5, "Lead")

        self.layout.addWidget(self.tabs)


    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())