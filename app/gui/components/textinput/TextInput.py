from typing import Any
from enum import Enum, unique, auto
from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap, QMovie
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout
from app.models.Model import Model


@unique
class UpdateEvent(Enum):
    ON_CHANGE = auto()
    ON_ENTER = auto()


Label = QPixmap | QMovie | str | int | float | None


class TextInput(QWidget):
    def __init__(self, labelText: Label = None):
        super().__init__()

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(10, 0, 10, 0)
        self.setLayout(self._layout)

        self._label = QLabel(self)
        self._input = QLineEdit(self)

        self._label.setBuddy(self._input)

        self._layout.addWidget(self._label)
        self._layout.addWidget(self._input)

        if isinstance(labelText, str):
            self.setLabelText(labelText)

    def setLabelText(self, text: str):
        self._label.setText(text)

    def setBinding(
        self,
        object: Any,
        property: str,
        updateEvent: UpdateEvent = UpdateEvent.ON_CHANGE,
    ):
        self._boundObject = object
        self._boundProperty = property
        self._updateEvent = updateEvent

        self._input.setText(getattr(self._boundObject, self._boundProperty))

        if self._updateEvent == UpdateEvent.ON_CHANGE:
            self._input.textChanged.connect(self._onTextChanged)
        else:
            self._input.returnPressed.connect(self._onReturnedPressed)

        # self._boundObject.updatedEvent.connect(self._onBoundObjectUpdated)

    # TODO Write setBindingChangeEvent()

    @Slot(Model)
    def _onBoundObjectUpdated(self, object: Model):
        debug(object)

    @Slot(str)
    def _onTextChanged(self, text: str):
        setattr(self._boundObject, self._boundProperty, text)

    @Slot(str)
    def _onReturnedPressed(self, text: str):
        setattr(self._boundObject, self._boundProperty, text)
