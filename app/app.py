import sys
from PySide6.QtWidgets import QApplication
from window import MainWindow


class App:
    def __init__(self) -> None:
        app = QApplication(sys.argv)

        # https://stackoverflow.com/questions/63442415/changing-font-size-of-all-qlabel-objects-pyqt5
        # custom_font = QFont()
        # custom_font.setWeight(18);
        # QApplication.setFont(custom_font, "QLabel")

        window = MainWindow()

        # https://docs.python.org/3/library/configparser.html

        sys.exit(app.exec())
