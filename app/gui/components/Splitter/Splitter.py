from typing import Optional
from PySide6.QtWidgets import (
    QVBoxLayout,
    QSplitter,
    QFrame,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QSplitterHandle,
    QWidget,
)

from PySide6.QtGui import QPaintEvent
from PySide6.QtCore import Qt

from app.gui.components.Splitter.SplitterHandle import SplitterHandle


class Splitter(QSplitter):
    def __init__(
        self, orientation: Qt.Orientation, parent: Optional[QWidget] = None
    ) -> None:
        super(Splitter, self).__init__(orientation, parent)

        #     background-color: #f8f8f8;
        #     background-color: #bebebe;
        self.setHandleWidth(8)
        self.setStyleSheet(
            """
            QSplitter::handle { 
                background-color: #bebebe;
            } 
        """
        )
        self.setChildrenCollapsible(False)

    def createHandle(self) -> QSplitterHandle:
        return SplitterHandle(self.orientation(), self)
