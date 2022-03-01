from typing import Any, Sequence
from app.gui.components.form.inputs.Input import Input, UpdateEvent
from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import Slot


class SelectBox(Input):
    def __init__(self, label: str | None = None, list: Sequence[str] | None = None):
        super(SelectBox, self).__init__(QComboBox)

        if label:
            self.setLabel(label)

        if list:
            self.addItems(list)

    def addItems(self, list: Sequence[str]):
        self._input.addItems(list)

    def setEditable(self, editable: bool):
        self._input.setEditable(editable)

    def setBinding(
        self,
        object: Any,
        property: str,
        updateEvent: UpdateEvent = UpdateEvent.ON_CHANGE,
    ):
        self._boundObject = object
        self._boundProperty = property
        self._updateEvent = updateEvent

        self._input.setCurrentText(getattr(self._boundObject, self._boundProperty))

        if self._updateEvent == UpdateEvent.ON_CHANGE:
            self._input.currentIndexChanged.connect(self._onSelectionChanged)

    @Slot(str)
    def _onSelectionChanged(self, index: int):
        setattr(self._boundObject, self._boundProperty, self._input.currentText())
