from typing import Any, Optional
from app.gui.components.form.inputs.Input import Input
from PySide6.QtWidgets import QLineEdit, QLabel
from PySide6.QtCore import Slot, QPoint, Qt
from PySide6.QtGui import QResizeEvent


class TextInput(Input[QLineEdit]):
    # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLineEdit.html
    def __init__(self, label: str | None = None):
        super(TextInput, self).__init__(QLineEdit())
        self.setObjectName("Input:TextInput:" + str(label))

        self._prefix: Optional[str] = None
        self._suffix: Optional[str] = None
        self._input.editingFinished.connect(lambda: self.modified.emit(True))

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

        self._input.editingFinished.connect(self._onTextChanged)

    @Slot(str)
    def _onTextChanged(self):
        self.updateBoundObject(self._boundObject, self._input.text())

    def isModified(self) -> bool:
        return self._input.isModified()

    def setPrefix(self, prefix: str):
        self._prefix = prefix

        self._prefixLabel = QLabel(self._prefix, self)
        self._prefixLabel.setBuddy(self._input)
        self._prefixLabel.setAlignment(Qt.AlignCenter)
        self._prefixLabel.setStyleSheet(
            "background-color: #e9ecef; border-right:1px solid #ababab"
        )

    def updatePrefix(self):
        if self._prefix is None:
            return

        inputFont = self._input.font()
        self._prefixLabel.setFont(inputFont)

        inputMargins = self._input.contentsMargins()

        prefixLabelPos = self._input.pos()
        prefixLabelPos.setX(prefixLabelPos.x() + 1)
        prefixLabelPos.setY(prefixLabelPos.y() + 1)

        height = self._input.sizeHint().height() - 2
        width = max(self._prefixLabel.sizeHint().width() + 8, height)
        self._prefixLabel.setMaximumHeight(height)
        self._prefixLabel.setMaximumWidth(width)
        self._prefixLabel.move(prefixLabelPos)

        inputMargins.setLeft(width + 2)
        self._input.setTextMargins(inputMargins)

    def setSuffix(self, suffix: str):
        self._suffix = suffix

        self._suffixLabel = QLabel(self._suffix, self)
        self._suffixLabel.setAlignment(Qt.AlignCenter)
        self._suffixLabel.setStyleSheet(
            "background-color: #e9ecef; border-left:1px solid #ababab"
        )

    def updateSuffix(self):
        if self._suffix is None:
            return

        inputFont = self._input.font()
        self._suffixLabel.setFont(inputFont)

        inputMargins = self._input.contentsMargins()

        height = self._input.sizeHint().height() - 2
        width = max(self._suffixLabel.sizeHint().width() + 8, height)
        self._suffixLabel.setMaximumHeight(height)
        self._suffixLabel.setMaximumWidth(width)

        suffixLabelPos = self._input.pos()
        suffixLabelPos.setX(suffixLabelPos.x() + self._input.width() - width - 1)
        suffixLabelPos.setY(suffixLabelPos.y() + 1)

        self._suffixLabel.move(suffixLabelPos)

        inputMargins.setRight(width + 2)
        self._input.setTextMargins(inputMargins)

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.updatePrefix()
        self.updateSuffix()

        return super().resizeEvent(event)
