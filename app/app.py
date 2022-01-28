import sys
from PySide6.QtWidgets import QApplication
from app.gui.window import MainWindow


class App():
    def __init__(self) -> None:
        app = QApplication(sys.argv)

        window = MainWindow()

        # https://docs.python.org/3/library/configparser.html

        sys.exit(app.exec())
