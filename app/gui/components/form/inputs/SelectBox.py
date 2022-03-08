from typing import Any, Sequence, cast

from parted import Alignment
from app.gui.components.form.inputs.Input import Input
from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import (
    QAbstractListModel,
    Qt,
    Slot,
)


class SelectBox(Input[QComboBox]):
    # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QComboBox.html
    def __init__(
        self, label: str | None = None, model: QAbstractListModel | None = None
    ):
        super(SelectBox, self).__init__(QComboBox())
        self.setObjectName("Input:SelectBox:" + str(label))

        self._isModified: bool = False
        self._input.setInsertPolicy(QComboBox.InsertAtTop)

        if label:
            self.setLabel(label)

        if model:
            self.setModel(model)

    def addItems(self, texts: Sequence[str]):
        self._input.addItems(texts)

    def setEditable(self, editable: bool):
        self._input.setEditable(editable)

    def findText(self, text: str, flags: Qt.MatchFlags) -> int:
        return self._input.findText(text, flags)

    def setBinding(
        self,
        object: Any,
        property: str,
        updateProperty: str | None = None,
    ) -> None:
        self._boundObject = object
        self._boundProperty = property
        self._updateProperty = updateProperty

        propertyValue = getattr(self._boundObject, self._boundProperty)
        propertyIndex = self._input.findText(propertyValue)

        # TODO listen on self._boundObject for save eveny

        self._input.setCurrentText(propertyValue)
        self._input.setCurrentIndex(propertyIndex)

        self._input.currentIndexChanged.connect(self._onSelectionChanged)

    @Slot(int)
    def _onSelectionChanged(self, index: int):
        if self.hasModel():
            indexModel = self.dataModel.getAt(index)

            self.updateBoundObject(
                indexModel,
                getattr(indexModel, self._updateProperty),
            )
        else:
            self.updateBoundObject(self._boundObject, self._input.itemText(index))

        self._isModified = True

    def isModified(self) -> bool:
        return self._isModified
