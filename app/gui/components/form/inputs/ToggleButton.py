# Framework imports
from typing import overload
from PySide6.QtCore import (
    QEasingCurve,
    QPoint,
    QPropertyAnimation,
    QRect,
    Qt,
    Slot,
    QSize,
)
from PySide6.QtGui import QColor, QFont, QPainter, QResizeEvent, QPaintEvent
from PySide6.QtWidgets import QAbstractButton

# Application imports
from app.gui.components.form.inputs.Input import Input
from app.gui.components.form.inputs.SwitchPrivate import SwitchPrivate
from app.models.Model import Model


class ToggleButton(Input[QAbstractButton], QAbstractButton):
    def __init__(self, checkedText: str, uncheckedText: str | None = None):
        super().__init__()

        self._checkedText: str = checkedText
        self._uncheckedText: str = checkedText

        self.setSize(84, 42)

        if uncheckedText is not None:
            self._uncheckedText = uncheckedText

        self.switch = SwitchPrivate(self)
        self.setCheckable(True)
        self.setCursor(Qt.PointingHandCursor)

        self.clicked.connect(self.switch.animate)

    def setBinding(
        self,
        object: Model,
        property: str,
        updateProperty: str | None = None,
    ):
        super().setBinding(object, property, updateProperty)

        self.setChecked(self.boundValue())

        self.clicked.connect(self._onButtonToggled)

    @Slot(bool)
    def _onButtonToggled(self, value: bool):
        assert self._boundObject is not None

        self.updateBoundObject(value)

    def setChecked(self, checked: bool) -> None:  # type: ignore[override]
        self.switch.animate(checked)
        return super().setChecked(checked)

    @overload
    def setSize(self, width: int, height: int):
        pass

    @overload
    def setSize(self, width: QSize):
        pass

    def setSize(self, width: int | QSize, height: None | int = None):
        if isinstance(width, QSize):
            height = width.height()
            width = width.width()

        self._width = width
        self._height = height

    def sizeHint(self):
        return QSize(self._width, self._height)

    def paintEvent(self, event: QPaintEvent):  # type: ignore[override]
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        self.switch.draw(painter)

    def resizeEvent(self, event: QResizeEvent):
        self.update()

    def __del__(self):
        del self.switch
