from abc import abstractmethod
import abc
from typing import Any
from enum import Enum, unique, auto
from PySide6.QtGui import QPixmap, QMovie, QFont
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout, QPlainTextEdit
from app.models.Model import Model


@unique
class UpdateEvent(Enum):
    ON_CHANGE = auto()
    ON_ENTER = auto()


# https://stackoverflow.com/questions/4821104/dynamic-instantiation-from-string-name-of-a-class-in-dynamically-imported-module
class Input(QWidget):
    def __init__(self, input):
        super(Input, self).__init__()

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)

        self._input = input()
        self._label = QLabel()
        self._label.setBuddy(self._input)
        labelFont = self._label.font()
        labelFont.setPointSize(11)
        labelFont.setCapitalization(QFont.SmallCaps)
        self._label.setFont(labelFont)
        self._label.hide()

        self._layout.addWidget(self._label)
        self._layout.addWidget(self._input)

        self.setLayout(self._layout)

    def setLabel(self, label: str):
        self._label.setText(label)
        self._label.show()

    def getLabel(self) -> QLabel | None:
        return self._label

    def setPlaceholderText(self, text: str):
        self._input.setPlaceholderText(text)

    def setBinding(
        self,
        object: Any,
        property: str,
        updateEvent: UpdateEvent = UpdateEvent.ON_CHANGE,
    ) -> None:
        raise NotImplementedError
