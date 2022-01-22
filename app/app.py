import sys
import random
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QVBoxLayout
from gui.window import Window


class App:
    def __init__(self):
        app = QApplication([])

        # https://docs.python.org/3/library/configparser.html
        window = Window()
        window.resize(800, 600)
        window.show()

        sys.exit(app.exec())
