from PySide6.QtWidgets import (
    QVBoxLayout,
    QSplitter,
    QFrame,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QSplitterHandle,
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QPaintEvent, QPainter, QBrush, QGradient


class SplitterHandle(QSplitterHandle):
    def __init__(self, orientation: Qt.Orientation, parent: QSplitter) -> None:
        super(SplitterHandle, self).__init__(orientation, parent)

    def paintEvent(self, event: QPaintEvent) -> None: # type: ignore[override]
        return super().paintEvent(event)
      
        # painter = QPainter(self)
        # gradient = QGradient(QGradient.WarmFlame)

        # debug(gradient)

        # if self.orientation() == Qt.Horizontal:
        #     gradient.setStart(event.rect().left(), event.rect().height() / 2)
        #     gradient.setFinalStop(event.rect().right(), event.rect().height() / 2)
        # else:
        #     gradient.setStart(event.rect().width() / 2, event.rect().top())
        #     gradient.setFinalStop(event.rect().width() / 2, event.rect().bottom())

        # painter.fillRect(event.rect(), QBrush(gradient))
