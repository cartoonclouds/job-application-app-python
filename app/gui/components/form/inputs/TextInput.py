from typing import Any
from app.gui.components.form.inputs.Input import Input, UpdateEvent
from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Slot


class TextInput(Input[QLineEdit]):
    def __init__(self, label: str | None = None):
        super(TextInput, self).__init__(QLineEdit())

        if label:
            self.setLabel(label)

    def setBinding(
        self,
        object: Any,
        property: str,
        updatePropery: str | None = None,
        updateEvent: UpdateEvent = UpdateEvent.Change,
    ):
        self._boundObject = object
        self._boundProperty = property
        self._updateEvent = updateEvent

        self._input.setText(str(getattr(self._boundObject, self._boundProperty)))

        if self._updateEvent == UpdateEvent.Change:
            self._input.textChanged.connect(self._onTextChanged)
        else:
            self._input.returnPressed.connect(self._onReturnedPressed)

    @Slot(str)
    def _onTextChanged(self, text: str):
        self.updateBoundObject(text)

    @Slot(str)
    def _onReturnedPressed(self, text: str):
        self.updateBoundObject(text)
