# Standard Library
from typing import Sequence, Type

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
        super(SelectBox, self).__init__(QComboBox(), label)

        self.baseWidgetModel = None
        self.baseWidget.setInsertPolicy(QComboBox.InsertAtTop)

        if dataModel:
            self.setModel(dataModel)

    def addItems(self, texts: Sequence[str]):
        self.baseWidget.addItems(texts)

    def setEditable(self, editable: bool):
        self.baseWidget.setEditable(editable)

    def findText(self, text: str, flags: Qt.MatchFlags) -> int:
        return self.baseWidget.findText(text, flags)

    def setBinding(
        self,
        object: Model,
        property: str,
        updateProperty: str | None = None,
    ) -> None:
        super().setBinding(object, property, updateProperty)

        propertyValue = self.boundValue()
        propertyIndex = self.baseWidget.findText(propertyValue)

        self.baseWidget.setCurrentText(propertyValue)
        self.baseWidget.setCurrentIndex(propertyIndex)

        self.baseWidget.currentIndexChanged.connect(self._onSelectionChanged)

    @Slot(int)
    def _onSelectionChanged(self, index: int):
        assert self._boundObject is not None

        if self.hasModel():
            assert self._updateProperty is not None

            indexModel = self.baseWidgetModel.getAt(index)

            self.updateBoundObject(
                indexModel,
                getattr(indexModel, self._updateProperty),
            )
        else:
            self.updateBoundObject(self.baseWidget.itemText(index))

    def hasModel(self) -> bool:
        return self.baseWidgetModel is not None

    def setModel(self, model):
        self.baseWidgetModel = model
        self.baseWidget.setModel(model)
