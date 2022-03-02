from typing import Any
from app.gui.components.form.inputs.Input import Input, UpdateEvent
from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import (
    QAbstractListModel,
    Qt,
    Slot,
)


class SelectBox(Input[QComboBox]):
    def __init__(
        self, label: str | None = None, model: QAbstractListModel | None = None
    ):
        super(SelectBox, self).__init__(QComboBox())

        self._input.setInsertPolicy(QComboBox.InsertAtTop)

        if label:
            self.setLabel(label)

        if model:
            self.setModel(model)

    def setEditable(self, editable: bool):
        self._input.setEditable(editable)

    def findText(self, text: str, flags: Qt.MatchFlags) -> int:
        return self._input.findText(text, flags)

    def setBinding(
        self,
        object: Any,
        property: str,
        updatePropery: str,
        updateEvent: UpdateEvent = UpdateEvent.Change,
    ) -> None:
        self._boundObject = object
        self._boundProperty = property
        self._updatePropery = updatePropery
        self._updateEvent = updateEvent

        propertyValue = getattr(self._boundObject, self._boundProperty)
        propertyIndex = self.dataModel.findIndex(propertyValue)

        self._input.setCurrentText(propertyValue)
        self._input.setCurrentIndex(propertyIndex)

        if self._updateEvent == UpdateEvent.Change:
            self._input.currentIndexChanged.connect(self._onSelectionChanged)

    @Slot(str)
    def _onSelectionChanged(self, index: int):
        self.updateBoundObject(getattr(self.dataModel[index], self._updatePropery))
