from functools import partial
from app.gui.components.form.inputs.Input import Input, UpdateEvent
from PySide6.QtWidgets import QPlainTextEdit
from PySide6.QtCore import Slot
from typing import Any


class TextAreaInput(Input):
    def __init__(self, label: str | None = None):
        super(TextAreaInput, self).__init__(QPlainTextEdit)

        if label:
            self.setLabel(label)

    def setBinding(
        self,
        object: Any,
        property: str,
        updateEvent: UpdateEvent = UpdateEvent.ON_CHANGE,
    ):
        self._boundObject = object
        self._boundProperty = property
        self._updateEvent = updateEvent

        self._input.insertPlainText(getattr(self._boundObject, self._boundProperty))

        if self._updateEvent == UpdateEvent.ON_CHANGE:
            self._input.textChanged.connect(self._onTextChanged)

    @Slot(str)
    def _onTextChanged(self):
        setattr(self._boundObject, self._boundProperty, self._input.document().toPlainText())
