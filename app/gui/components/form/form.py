from PySide6.QtWidgets import (
    QLabel,
    QFormLayout,
    QWidget,
    QFrame,
    QPlainTextEdit,
    QLayout,
    QVBoxLayout,
    QGroupBox,
    QPushButton,
    QCalendarWidget,
    QDateEdit,
    QGraphicsColorizeEffect,
)
from PySide6.QtGui import QFont, QPaintEvent
from PySide6.QtCore import Qt, QSize, QRect, QDateTime
from PySide6.QtWidgets import QSizePolicy, QLineEdit
from app.gui.components.textinput.TextInput import TextInput
from app.models import Model

from app.utilities.IconUtility import IconUtility


class Form(QWidget):
    def __init__(self, model: Model = None, title: str | None = None) -> None:
        super(Form, self).__init__()

        self._model = model
        self._title = title
        self.setObjectName("Form:Job")

        layout = QVBoxLayout()

        frame = QFrame(self)
        frame.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)

        frameLayout = QFormLayout()
        frameLayout.setRowWrapPolicy(QFormLayout.WrapAllRows)
        # layout.setContentsMargins(0, 0, 0, 0)
        # layout.setVerticalSpacing(10)
        # layout.setLabelAlignment(Qt.AlignCenter)

        frame.setLayout(frameLayout)

        self.formTitle = QLabel(self._title)
        self.formTitle.setMaximumHeight(12)
        self.formTitle.move(0, 6)
        self.formTitle.setContentsMargins(0, 6, 0, 0)

        titleInput = TextInput()
        titleInput.setBinding(self._model, "title")
        titleInput.setPlaceholderText("Job title")

        professionInput = TextInput()
        # professionInput.setBinding(self._model, "title")
        professionInput.setPlaceholderText("Profession")

        # creating a QDateEdit object
        self.calendar = QDateEdit(QDateTime.currentDateTime().date(), self)
        self.calendar.setCalendarPopup(True)

        frameLayout.addRow(self.formTitle)
        frameLayout.addRow("Title", titleInput)
        frameLayout.addRow("Profession", professionInput)
        frameLayout.addRow(self.calendar)

        self.setLayout(layout)
        layout.addWidget(self.formTitle)
        layout.addWidget(frame)

    def setTitle(self, title: str):
        self._title = title
        # update label

    def paintEvent(self, painter: QPaintEvent) -> None:
        # self.formTitle.move(painter.rect().x(), painter.rect().y() + 6)

        self.formTitle.raise_()
        self.stackUnder(jobForm.formTitle)

        return super().paintEvent(painter)
