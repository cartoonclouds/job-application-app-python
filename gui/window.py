import sys
import random
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QVBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Instance variables
        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        # GUI setup
        self.button = QPushButton("Click me!")
        self.text = QLabel(
            "Hello World", alignment=Qt.AlignCenter)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))