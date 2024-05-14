from PyQt5 import QtWidgets, QtCore
from dashboard_logic import MydashboardWindow # Import the MainWindow class from mainpage.py
from login import Ui_MainWindow

class LoginApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Assuming your UI class is Ui_MainWindow
        self.ui.setupUi(self)
        self.ui.SignInButton.clicked.connect(self.login)
        self.ui.close.clicked.connect(self.close) 

    def login(self):
        email = self.ui.Login.text()
        password = self.ui.password_edit.text()

        # Example of a simple login check
        if email == "" and password == "":
            print("Login successful")
            self.main_window = MydashboardWindow()
            self.main_window.show()
            self.close()  # Emit signal on successful login
        else:
            print("Login failed")
            # Show an error message or take other appropriate action
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid username or password")


    def close(self):
        print("Close")  # For demonstration purposes
        super().close()  # Correctly call the superclass's close method