from PyQt6.QtWidgets import QMainWindow
import random

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        from baitap24 import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.on_random_click)
        self.ui.pushButton_2.clicked.connect(self.on_new_game_click)
        self.ui.pushButton_3.clicked.connect(self.close)

    def on_random_click(self):
        random_numbers = [random.randint(1, 9) for _ in range(3)]
        self.ui.label.setText(str(random_numbers[0]))
        self.ui.label_2.setText(str(random_numbers[1]))
        self.ui.label_3.setText(str(random_numbers[2]))

    def on_new_game_click(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.label.setText("3")
        self.ui.label_2.setText("4")
        self.ui.label_3.setText("6")
