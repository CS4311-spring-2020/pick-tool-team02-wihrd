import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from LogIngestionScreen import LogIngestionScreen

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
        
        self.home_page = HomePage(self)
        self.setCentralWidget(self.home_page)
        
        self.show()


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
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()
        self.tab7 = QWidget()

        self.tabs.resize(300,200)

        self.tabs.addTab(self.tab1, "Log Ingestion")
        self.tabs.addTab(self.tab2, "Tab 2")
        self.tabs.addTab(self.tab3, "Tab 3")
        self.tabs.addTab(self.tab4, "Tab 4")
        self.tabs.addTab(self.tab5, "Tab 5")
        self.tabs.addTab(self.tab6, "Tab 6")
        self.tabs.addTab(self.tab7, "Tab 7")

        self.layout.addWidget(self.tabs)


    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())