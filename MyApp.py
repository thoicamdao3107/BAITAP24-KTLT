import sys
from PyQt6.QtWidgets import QApplication
from baitap24Ext import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
