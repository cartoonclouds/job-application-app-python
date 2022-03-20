# Standard Library
from typing import Any, Optional

# Framework imports
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPushButton

# Application imports
from app.gui.components.form.inputs.Input import Input


class ToggleButtonSquare(Input[QPushButton]):
    _checkedStyles = "background-color: lightblue"
    _uncheckedStyles = "background-color: lightgrey"

    def __init__(self, text: str, uncheckedText: Optional[str] = None):
        super(ToggleButtonSquare, self).__init__(QPushButton())
        self.setObjectName("Input:ToggleButtonSquare:" + str(text))

        self._checkedText = text
        self._uncheckedText = uncheckedText

        self._input.setCheckable(True)
        self._input.setText(text)
        self._input.setStyleSheet(ToggleButtonSquare._uncheckedStyles)

    def setBinding(
        self,
        object: Any,
        property: str,
        updateProperty: str | None = None,
    ):
        self._boundObject = object
        self._boundProperty = property
        self._updateProperty = updateProperty

        self._initialPropertyValue = bool(
            getattr(self._boundObject, self._boundProperty)
        )

        self._input.setChecked(self._initialPropertyValue)
        self._updateButton()

        self._input.clicked.connect(self._onButtonToggled)
        self._input.clicked.connect(lambda: self.modified.emit(self.isModified()))

    def isModified(self) -> bool:
        return self._input.isChecked() == self._initialPropertyValue

    def _hasUpdatingText(self) -> bool:
        return self._uncheckedText is not None

    @Slot(str)
    def _onButtonToggled(self):
        assert self._boundObject is not None
        self.updateBoundObject(self._boundObject, self._input.isChecked())

        if self._hasUpdatingText():
            self._updateButton()

    def _updateButton(self):
        if self._input.isChecked():
            self._input.setText(self._checkedText)
            self._input.setStyleSheet(ToggleButtonSquare._checkedStyles)
        else:
            self._input.setText(self._uncheckedText)
            self._input.setStyleSheet(ToggleButtonSquare._uncheckedStyles)
