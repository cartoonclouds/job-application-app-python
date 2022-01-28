import sys
import random
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QVBoxLayout
from app.gui.window import MainWindow


class App():
    def __init__(self) -> None:
        app = QApplication(sys.argv)

        window = MainWindow()

        # https://docs.python.org/3/library/configparser.html

        sys.exit(app.exec())
