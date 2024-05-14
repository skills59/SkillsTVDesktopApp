from PyQt5 import QtWidgets
from PyQt5 import QtCore
from dashboard import Ui_dashboardWindow  # Import the MainWindow class from dashboard.py
from login import Ui_MainWindow
from PyQt5.QtCore import QTimer, QDateTime, pyqtSlot
import sys

class MydashboardWindow(QtWidgets.QMainWindow, Ui_dashboardWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Call setupUi from the auto-generated class
        self.pushButton_15.clicked.connect(self.logout)  # Connect the clicked signal of pushButton_15 to logout function
        self.pushButton_18.clicked.connect(self.minimize)
        self.pushButton_19.clicked.connect(self.maximize)
        self.pushButton_17.clicked.connect(self.close)  


        self.LiveTv_Button.clicked.connect(self.switch_to_LiveTv)
        self.Movies_Button.clicked.connect(self.switch_to_Movies)
        self.Series_Button.clicked.connect(self.switch_to_Series)

        # Variables for dragging
        self.draggable = True
        self.offset = None


    def logout(self):
        # Perform logout actions here, such as clearing session data
        print("Logout")  # For demonstration purposes
        # Show login window
        login_window = MydashboardWindow()  # Instantiate your subclass
        login_window.show()
        self.close()  # Close the current dashboard window
        
    def close(self):
        print("Close")  # For demonstration purposes
        super().close()  # Correctly call the superclass's close method

    def minimize(self):
        self.showMinimized()

    def maximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

     # Reimplement mouse events to make the window draggable
    def mousePressEvent(self, event):
       if event.button() == QtCore.Qt.LeftButton and self.draggable:
           self.offset = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        if self.offset is not None and self.draggable:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event):
        self.offset = None




    def switch_to_LiveTv(self):
        self.stackedWidget.setCurrentIndex(0)  # Switch to dashboard page
        
    def switch_to_Movies(self):
        self.stackedWidget.setCurrentIndex(1)  # Switch to dashboard page
        
    def switch_to_Series(self):
        self.stackedWidget.setCurrentIndex(2)  # Switch to dashboard page
