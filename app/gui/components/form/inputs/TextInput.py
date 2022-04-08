# Standard Library
from enum import Enum, auto

# Framework imports
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPaintEvent
from PySide6.QtWidgets import QLabel, QLineEdit

# Application imports
from app.constants import WIDGET_SPACING
from app.gui.components.form.inputs.Input import Input
from app.models.Model import Model


class AffixLocation(Enum):
    PREFIX = auto()
    SUFFIX = auto()


class TextInput(Input[QLineEdit], QLineEdit):
    # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLineEdit.html

    def __init__(self, label: str | None = None):
        # https://stackoverflow.com/questions/222877/what-does-super-do-in-python-difference-between-super-init-and-expl/33469090#33469090
        # https://stackoverflow.com/questions/9575409/calling-parent-class-init-with-multiple-inheritance-whats-the-right-way
        # QLineEdit.__init__(self)
        super().__init__(label)

        self._prefix: QLabel | None = None
        self._suffix: QLabel | None = None

        self._autoRemoveAffix: bool = False

    def setBinding(
        self,
        object: Model,
        property: str,
        updateProperty: str | None = None,
    ):
        super().setBinding(object, property, updateProperty)

        self.setText(str(self.boundValue()))

        self.textEdited.connect(self._onTextChanged)

    @Slot(str)
    def _onTextChanged(self):
        assert self._boundObject is not None

        text = self.text()

        if self._autoRemoveAffix:
            text = self._removeAffixFromInput()

        self.updateBoundObject(text)

    def setAutoRemoveAffix(self, autoRemoveAffix: bool):
        self._autoRemoveAffix = autoRemoveAffix

    def setPrefix(self, text: str):
        self._prefix = self._setAffix(AffixLocation.PREFIX, text)

    def setSuffix(self, text: str):
        self._suffix = self._setAffix(AffixLocation.SUFFIX, text)

    def _setAffix(self, affix: AffixLocation, text: str):
        affixLabel = QLabel(text, self)
        affixLabel.setBuddy(self)
        affixLabel.setAlignment(Qt.AlignCenter)
        affixLabel.setStyleSheet(
            "background-color: #e9ecef; border-"
            + ("right" if affix == AffixLocation.PREFIX else "left")
            + ":1px solid #ababab"
        )

        if self._autoRemoveAffix:
            self._removeAffixFromInput()

        affixLabel.show()

        return affixLabel

    def _removeAffixFromInput(self) -> str:
        text = self.text()

        # If the prefix was entered, remove it
        if self._prefix is not None and text.startswith(self._prefix.text()):
            text = text.replace(self._prefix.text(), "")

        # If the suffix was entered, remove it
        if self._suffix is not None and text.endswith(self._suffix.text()):
            text = text.replace(self._suffix.text(), "")

        self.setText(text)

        return text

    def _updateAffix(self, affix: AffixLocation, affixLabel: QLabel | None):
        if affixLabel is None:
            return

        inputFont = self.font()
        affixLabel.setFont(inputFont)

        height = self.sizeHint().height() - 2
        width = max(
            affixLabel.sizeHint().width() + (WIDGET_SPACING * 2),
            height,
        )

        prefixPos = self.pos()
        prefixPosX = prefixPos.x() + 1

        if affix == AffixLocation.SUFFIX:
            prefixPosX = prefixPosX + self.width() - width - 2

        prefixPos.setX(prefixPosX)
        prefixPos.setY(prefixPos.y() + 1)

        affixLabel.setMaximumHeight(height)
        affixLabel.setMaximumWidth(width)
        affixLabel.move(prefixPos)

    def paintEvent(self, painter: QPaintEvent) -> None:  # type: ignore[override]
        self._updateAffix(AffixLocation.PREFIX, self._prefix)
        self._updateAffix(AffixLocation.SUFFIX, self._suffix)

        inputMargins = self.contentsMargins()
        if self._prefix is not None:
            inputMargins.setLeft(self._prefix.maximumWidth() + WIDGET_SPACING)

        if self._suffix is not None:
            inputMargins.setRight(self._suffix.maximumWidth() + WIDGET_SPACING)
        self.setTextMargins(inputMargins)

        return super().paintEvent(painter)
