# Standard Library
from typing import Any, Optional

# Framework imports
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPaintEvent
from PySide6.QtWidgets import QLabel, QLineEdit

# Application imports
from app.Constants import WIDGET_SPACING, WIDGET_MARGINS, ZERO_MARGINS
from app.gui.components.form.inputs.Input import Input


class TextInput(Input[QLineEdit]):
    # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLineEdit.html
    def __init__(self, label: str | None = None):
        super(TextInput, self).__init__(QLineEdit())
        self.setObjectName("Input:TextInput:" + str(label))

        self._prefix: Optional[str] = None
        self._suffix: Optional[str] = None

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

        self._initialPropertyValue = str(
            getattr(self._boundObject, self._boundProperty)
        )

        self._input.setText(self._initialPropertyValue)

        self._input.editingFinished.connect(self._onTextChanged)
        self._input.editingFinished.connect(
            lambda: self.modified.emit(self.isModified())
        )

    @Slot(str)
    def _onTextChanged(self):
        self._removePreSuffixes()

        assert self._boundObject is not None
        self.updateBoundObject(self._boundObject, self._input.text())

    def isModified(self) -> bool:
        return self._input.displayText() != self._initialPropertyValue

    def _removePreSuffixes(self):
        # If the prefix was entered, remove it
        if self._prefix is not None and self._input.text().startswith(self._prefix):
            self._input.setText(self._input.text().replace(self._prefix, ""))

        # If the suffix was entered, remove it
        if self._suffix is not None and self._input.text().endswith(self._suffix):
            self._input.setText(self._input.text().replace(self._suffix, ""))

    def setPrefix(self, prefix: str):
        self._prefix = prefix

        self._prefixLabel = QLabel(self._prefix, self)
        self._prefixLabel.setBuddy(self._input)
        self._prefixLabel.setAlignment(Qt.AlignCenter)
        self._prefixLabel.setStyleSheet(
            "background-color: #e9ecef; border-right:1px solid #ababab"
        )

        self._removePreSuffixes()
        self._prefixLabel.show()

    def updatePrefix(self):
        if self._prefix is None:
            return

        inputFont = self._input.font()
        self._prefixLabel.setFont(inputFont)

        height = self._input.sizeHint().height() - 2
        width = max(
            self._prefixLabel.sizeHint().width() + (WIDGET_SPACING * 2),
            height,
        )

        prefixPos = self._input.pos()
        prefixPos.setX(prefixPos.x() + 1)
        prefixPos.setY(prefixPos.y() + 1)

        self._prefixLabel.setMaximumHeight(height)
        self._prefixLabel.setMaximumWidth(width)
        self._prefixLabel.move(prefixPos)

    def setSuffix(self, suffix: str):
        self._suffix = suffix

        self._suffixLabel = QLabel(self._suffix, self)
        self._suffixLabel.setAlignment(Qt.AlignCenter)
        self._suffixLabel.setStyleSheet(
            "background-color: #e9ecef; border-left:1px solid #ababab"
        )

        self._removePreSuffixes()
        self._suffixLabel.show()

    def updateSuffix(self):
        if self._suffix is None:
            return

        inputFont = self._input.font()
        self._suffixLabel.setFont(inputFont)

        height = self._input.sizeHint().height() - 2
        width = max(
            self._suffixLabel.sizeHint().width() + (WIDGET_SPACING * 2),
            height,
        )

        suffixPos = self._input.pos()
        suffixPos.setX(suffixPos.x() + self._input.width() - width - 1)
        suffixPos.setY(suffixPos.y() + 1)

        self._suffixLabel.setMaximumHeight(height)
        self._suffixLabel.setMaximumWidth(width)
        self._suffixLabel.move(suffixPos)

    def paintEvent(self, painter: QPaintEvent) -> None:
        self.updatePrefix()
        self.updateSuffix()

        inputMargins = self._input.contentsMargins()
        if self._prefix is not None:
            inputMargins.setLeft(self._prefixLabel.maximumWidth() + WIDGET_SPACING)

        if self._suffix is not None:
            inputMargins.setRight(self._suffixLabel.maximumWidth() + WIDGET_SPACING)
        self._input.setTextMargins(inputMargins)

        return super().paintEvent(painter)
