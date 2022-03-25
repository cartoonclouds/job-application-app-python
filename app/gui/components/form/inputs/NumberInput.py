# Framework imports
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDoubleSpinBox

# Application imports
from app.gui.components.form.inputs.Input import Input
from app.models.Model import Model


class NumberInput(Input[QDoubleSpinBox]):
    # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QDoubleSpinBox.html
    def __init__(self, label: str | None = None):
        super(NumberInput, self).__init__(QDoubleSpinBox(), str(label))

        self._prefix: str | None = None
        self._suffix: str | None = None

        if label is not None:
            self.setLabel(label)

    def setBinding(
        self,
        object: Model,
        property: str,
        updateProperty: str | None = None,
    ):
        self._boundObject = object
        self._boundProperty = property
        self._updateProperty = updateProperty

        self._input.setValue(float(getattr(self._boundObject, self._boundProperty)))

        self._input.valueChanged.connect(self._onValueChanged)
        self._input.valueChanged.connect(lambda: self.modified.emit(self.isModified()))

    @Slot(str)
    def _onValueChanged(self):
        assert self._boundObject is not None
        self.updateBoundObject(self._boundObject, self._input.value())

    def setMinimum(self, val: float):
        self._input.setMinimum(val)

    def setMaximum(self, val: float):
        self._input.setMaximum(val)

    def setRange(self, min: float, max: float):
        self._input.setRange(min, max)

    def setDecimals(self, prec: int):
        self._input.setDecimals(prec)

    def setSingleStep(self, step: float):
        self._input.setSingleStep(step)
