# Standard Library
from typing import Sequence

# Framework imports
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QComboBox

# Application imports
from app.gui.components.form.inputs.Input import Input

# from app.gui.components.models.ListModel import ListModel TODO Type dataModel
from app.models.Model import Model
from app.typings.types import M


class SelectBox(Input[QComboBox]):
    # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QComboBox.html
    def __init__(
        self,
        label: str | None = None,
        dataModel=None,
    ):
        super(SelectBox, self).__init__(QComboBox(), str(label or ""))

        self._inputModel = None
        self._input.setInsertPolicy(QComboBox.InsertAtTop)

        if label:
            self.setLabel(label)

        if dataModel:
            self.setModel(dataModel)

    def addItems(self, texts: Sequence[str]):
        self._input.addItems(texts)

    def setEditable(self, editable: bool):
        self._input.setEditable(editable)

    def findText(self, text: str, flags: Qt.MatchFlags) -> int:
        return self._input.findText(text, flags)

    def setBinding(
        self,
        object: Model,
        property: str,
        updateProperty: str | None = None,
    ) -> None:
        self._boundObject = object
        self._boundProperty = property
        self._updateProperty = updateProperty

        propertyValue = getattr(self._boundObject, self._boundProperty)
        self._initialPropertyIndex = self._input.findText(propertyValue)

        self._input.setCurrentText(propertyValue)
        self._input.setCurrentIndex(self._initialPropertyIndex)

        self._input.currentIndexChanged.connect(self._onSelectionChanged)
        self._input.currentIndexChanged.connect(
            lambda: self.modified.emit(self.isModified())
        )

    @Slot(int)
    def _onSelectionChanged(self, index: int):
        assert self._boundObject is not None

        if self.hasModel():
            assert self._updateProperty is not None

            indexModel = self._inputModel.getAt(index)

            self.updateBoundObject(
                indexModel,
                getattr(indexModel, self._updateProperty),
            )
        else:
            self.updateBoundObject(self._boundObject, self._input.itemText(index))

    def hasModel(self) -> bool:
        return self._inputModel is not None

    def setModel(self, model):
        self._inputModel = model
        self._input.setModel(model)
