import sys
import random
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QVBoxLayout
from gui.window import Window

if __name__ == "__main__":
    app = QApplication([])

    window = Window()
    window.resize(800, 600)
    window.show()

    sys.exit(app.exec())
