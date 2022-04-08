# Standard Library
from typing import Sequence

# Framework imports
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QComboBox

# Application imports
from app.gui.components.form.inputs.Input import Input

# from app.gui.components.models.ListModel import ListModel TODO Type dataModel
from app.models.Model import Model


class SelectBox(Input[QComboBox], QComboBox):
    # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QComboBox.html
    def __init__(self, label: str | None = None):
        super().__init__(label)

        self.baseWidgetModel = None
        self.setInsertPolicy(QComboBox.InsertAtTop)

    def setBinding(
        self,
        object: Model,
        property: str,
        updateProperty: str | None = None,
    ) -> None:
        super().setBinding(object, property, updateProperty)

        propertyValue = self.boundValue()
        propertyIndex = self.findText(propertyValue)

        self.setCurrentText(propertyValue)
        self.setCurrentIndex(propertyIndex)

        self.currentIndexChanged.connect(self._onSelectionChanged)

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
            self.updateBoundObject(self.itemText(index))

    def hasModel(self) -> bool:
        return self.baseWidgetModel is not None

    def setModel(self, model):
        self.baseWidgetModel = model
        super().setModel(model)
