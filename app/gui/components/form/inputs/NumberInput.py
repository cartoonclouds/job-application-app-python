# Framework imports
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDoubleSpinBox

# Application imports
from app.gui.components.form.inputs.Input import Input
from app.models.Model import Model


class NumberInput(Input[QDoubleSpinBox], QDoubleSpinBox):
    # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QDoubleSpinBox.html
    def __init__(self, label: str | None = None):
        super().__init__(label)

        self._prefix: str | None = None
        self._suffix: str | None = None

    def setBinding(
        self,
        object: Model,
        property: str,
        updateProperty: str | None = None,
    ):
        super().setBinding(object, property, updateProperty)

        self.setValue(self.boundValue())

        self.valueChanged.connect(self._onValueChanged)

    @Slot(str)
    def _onValueChanged(self):
        assert self._boundObject is not None

        self.updateBoundObject(self.value())
