# Standard Library
from typing import Any, Optional

# Framework imports
from PySide6.QtCore import Slot, QPoint, Qt, QPropertyAnimation, QRect, QEasingCurve
from PySide6.QtWidgets import QCheckBox
from PySide6.QtGui import QPaintEvent, QPainter, QFont, QColor

# Application imports
from app.gui.components.form.inputs.Input import Input


class ToggleButton(Input[QCheckBox]):
    def __init__(self, text: str, uncheckedText: Optional[str] = None):
        super(ToggleButton, self).__init__(QCheckBox())
        self.setObjectName("Input:ToggleButton:" + str(text))

        self._input.setCheckable(True)
        self._input.setCursor(Qt.PointingHandCursor)
        self.animation = QPropertyAnimation(self, b"position")
        self.animation.setEasingCurve(QEasingCurve.OutBounce)
        self.animation.setDuration(500)

        # COLORS
        self._position = 3
        self._bg_color = "#777"
        self._circle_color = "#DDD"
        self._active_color = "#00BCFF"

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

        self._input.stateChanged.connect(self.setup_animation)
        self._input.stateChanged.connect(self._onButtonToggled)
        self._input.stateChanged.connect(lambda: self.modified.emit(self.isModified()))

    @Slot(bool)
    def _onButtonToggled(self, value: bool):
        assert self._boundObject is not None
        self.updateBoundObject(self._boundObject, value)

    # https://raw.githubusercontent.com/Wanderson-Magalhaes/PyOneDark_Qt_Widgets_Modern_GUI/master/gui/widgets/py_toggle/py_toggle.py
    @property
    def position(self) -> QPoint:
        return self._position

    @position.setter
    def position(self, pos: QPoint):
        self._position = pos
        self.update()

    # START STOP ANIMATION
    def setup_animation(self, value: bool):
        self.animation.stop()

        if value:
            self.animation.setEndValue(self.sizeHint().width() - 26)
        else:
            self.animation.setEndValue(4)

        self.animation.start()

    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)

    def paintEvent(self, painter: QPaintEvent):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.setFont(QFont("Segoe UI", 9))

        # SET PEN
        p.setPen(Qt.NoPen)

        # DRAW RECT
        rect = QRect(0, 0, self.sizeHint().width(), self.sizeHint().height())

        if not self._input.isChecked():
            p.setBrush(QColor(self._bg_color))
            p.drawRoundedRect(0, 0, rect.width(), 28, 14, 14)
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._position, 3, 22, 22)
        else:
            p.setBrush(QColor(self._active_color))
            p.drawRoundedRect(0, 0, rect.width(), 28, 14, 14)
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._position, 3, 22, 22)

        p.end()
