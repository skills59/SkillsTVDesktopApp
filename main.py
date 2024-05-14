import sys
from PyQt5.QtWidgets import QApplication
from login_logic import LoginApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginApp()  # Instantiate your subclass
    login_window.show()
    sys.exit(app.exec_())
