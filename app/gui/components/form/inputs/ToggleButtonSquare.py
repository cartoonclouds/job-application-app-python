from typing import Any, Optional
from app.gui.components.form.inputs.Input import Input
from PySide6.QtWidgets import QPushButton, QLabel
from PySide6.QtCore import Slot, QPoint, Qt
from PySide6.QtGui import QResizeEvent


class ToggleButtonSquare(Input[QPushButton]):
    # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLineEdit.html

    _checkedStyles = "background-color: lightblue"
    _uncheckedStyles = "background-color: lightgrey"

    def __init__(self, text: str, uncheckedText: Optional[str] = None):
        super(ToggleButtonSquare, self).__init__(QPushButton())
        self.setObjectName("Input:ToggleButtonSquare:" + str(text))

        self._checkedText = text
        self._uncheckedText = uncheckedText
        self._isModified: bool = False

        self._input.setCheckable(True)
        self._input.setText(text)
        self._input.setStyleSheet(ToggleButtonSquare._uncheckedStyles)
        self._input.clicked.connect(lambda: self.modified.emit(True))

    def setBinding(
        self,
        object: Any,
        property: str,
        updateProperty: str | None = None,
    ):
        self._boundObject = object
        self._boundProperty = property
        self._updateProperty = updateProperty

        propertyValue = bool(getattr(self._boundObject, self._boundProperty))

        self._input.setChecked(propertyValue)
        self._updateButton()

        self._input.clicked.connect(self._onButtonToggled)

    def _hasUpdatingText(self) -> bool:
        return self._uncheckedText is not None

    @Slot(str)
    def _onButtonToggled(self):
        self.updateBoundObject(self._boundObject, self._input.isChecked())

        self._isModified = True

        if self._hasUpdatingText():
            self._updateButton()

    def isModified(self) -> bool:
        return self._isModified

    def _updateButton(self):
        if self._input.isChecked():
            self._input.setText(self._checkedText)
            self._input.setStyleSheet(ToggleButtonSquare._checkedStyles)
        else:
            self._input.setText(self._uncheckedText)
            self._input.setStyleSheet(ToggleButtonSquare._uncheckedStyles)
