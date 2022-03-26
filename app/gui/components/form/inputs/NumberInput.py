# Framework imports
from typing import Type
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDoubleSpinBox

# Application imports
from app.gui.components.form.inputs.Input import Input
from app.models.Model import Model


class NumberInput(Input[QDoubleSpinBox]):
    # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QDoubleSpinBox.html
    def __init__(self, label: str | None = None):
        super(NumberInput, self).__init__(QDoubleSpinBox(), label)

        self._prefix: str | None = None
        self._suffix: str | None = None

    def setBinding(
        self,
        object: Model,
        property: str,
        updateProperty: str | None = None,
    ):
        super().setBinding(object, property, updateProperty)

        self.baseWidget.setValue(self.boundValue())

        self.baseWidget.valueChanged.connect(self._onValueChanged)

    @Slot(str)
    def _onValueChanged(self):
        assert self._boundObject is not None
        self.updateBoundObject(self.baseWidget.value())

    def setMinimum(self, val: float):
        self.baseWidget.setMinimum(val)

    def setMaximum(self, val: float):
        self.baseWidget.setMaximum(val)

    def setRange(self, min: float, max: float):
        self.baseWidget.setRange(min, max)

    def setDecimals(self, prec: int):
        self.baseWidget.setDecimals(prec)

    def setSingleStep(self, step: float):
        self.baseWidget.setSingleStep(step)
