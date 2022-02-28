from PySide6.QtWidgets import (
    QLabel,
    QHBoxLayout,
    QWidget,
    QFrame,
    QPlainTextEdit,
    QLayout,
)
from PySide6.QtGui import QFont, QFontMetrics
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QSizePolicy

from app.utilities.IconUtility import IconUtility


class Header(QFrame):
    def __init__(self, text: str) -> None:
        super().__init__()

        self._text = text
        self._icon = IconUtility.getFileIconAsPixmap("gear")

        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)

        label = QLabel(text)
        label.setFont(QFont(["Helvetica", "SansSerif"], 18))

        icon = QLabel("")
        icon.setPixmap(self._icon)

        fontMetrics: QFontMetrics = label.fontMetrics()
        textSize: QSize = fontMetrics.size(0, label.text())
        self.setMaximumHeight(textSize.height())

        layout.addWidget(icon)
        layout.addWidget(label)
