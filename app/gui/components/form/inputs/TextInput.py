from typing import Any
from app.gui.components.form.inputs.Input import Input
from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Slot


class TextInput(Input[QLineEdit]):
    # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLineEdit.html
    def __init__(self, label: str | None = None):
        super(TextInput, self).__init__(QLineEdit())
        self.setObjectName("Input:TextInput:" + str(label))

        self._prefix = None
        self._suffix = None

        if label:
            self.setLabel(label)

    def setBinding(
        self,
        object: Any,
        property: str,
        updateProperty: str | None = None,
    ):
        self._boundObject = object
        self._boundProperty = property
        self._updateProperty = updateProperty

        propertyValue = str(getattr(self._boundObject, self._boundProperty))

        self._input.setText(propertyValue)

        self._input.textChanged.connect(self._updatePrefixSuffix)
        self._input.editingFinished.connect(self._onTextChanged)

    @Slot(str)
    def _onTextChanged(self):
        self.updateBoundObject(self._boundObject, self._input.text())

    def _updatePrefixSuffix(self):
        # line_edit = self.sender() # A reference to which QLineEdit triggered the method.
        text = self._input.text()

        if self._prefix and not text.startswith(self._prefix):
            self._input.blockSignals(True)  # Prevent recursive calls to this method.
            self._input.setText(self._prefix + text)
            self._input.blockSignals(False)

        if self._suffix and not text.endswith(self._suffix):
            self._input.blockSignals(True)  # Prevent recursive calls to this method.
            self._input.setText(text + self._suffix)
            self._input.blockSignals(False)

    def setPrefix(self, prefix: str):
        self._prefix = prefix

    def setSuffix(self, suffix: str):
        self._suffix = suffix

    def isModified(self) -> bool:
        return self._input.isModified()