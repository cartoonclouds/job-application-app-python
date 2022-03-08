import sys
from PySide6.QtWidgets import QApplication, QStyleFactory
from window import MainWindow
import logging


class App:
    def __init__(self) -> None:
        app = QApplication(sys.argv)
        # app.setStyle("Plastique")
        # https://stackoverflow.com/questions/63442415/changing-font-size-of-all-qlabel-objects-pyqt5
        # custom_font = QFont()
        # custom_font.setWeight(18);
        # QApplication.setFont(custom_font, "QLabel")

        # QApplication.setStyle(QStyleFactory.create("QPlastiqueStyle"))
        # QApplication.setStyle(QStyleFactory.create("Cleanlooks"))
        window = MainWindow()

        window.setWindowModified(True)

        # QScreen to get Window information

        # https://webgradients.com/

        # https://docs.python.org/3/library/configparser.html

        sys.exit(app.exec())
