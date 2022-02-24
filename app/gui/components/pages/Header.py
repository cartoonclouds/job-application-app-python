

from PySide6.QtWidgets import QLabel, QHBoxLayout, QWidget
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

from app.utilities.IconUtility import IconUtility


class Header(QWidget):
    def __init__(self, text: str) -> None:
        super().__init__()

        self._text = text
        self._icon = IconUtility.getFileIcon("gear")

        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setLayout(layout)

        label = QLabel(text)
        label.setFont(QFont(['Helvetica', 'SansSerif'], 18))

        icon = QLabel("")
        icon.setPixmap(self._icon)

        layout.addWidget(icon)
        layout.addWidget(label)
