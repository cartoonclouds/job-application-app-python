# Framework imports
from PySide6.QtCore import QEasingCurve, QPoint, QPropertyAnimation, QRect, Qt, Slot
from PySide6.QtGui import QColor, QFont, QPainter, QPaintEvent
from PySide6.QtWidgets import QCheckBox

# Application imports
from app.gui.components.form.inputs.Input import Input
from app.models.Model import Model


class ToggleButton(Input[QCheckBox], QCheckBox):
    def __init__(self, checkedText: str, uncheckedText: str | None = None):
        super().__init__(checkedText)

        self._checkedText: str = checkedText
        self._uncheckedText: str = checkedText

        if uncheckedText is not None:
            self._uncheckedText = uncheckedText

        self.setCheckable(True)
        self.setCursor(Qt.PointingHandCursor)
        self.setText(checkedText)

        # COLORS
        self._position = 3
        self._bg_color = "#777"
        self._circle_color = "#DDD"
        self._active_color = "#00BCFF"

        self.animation = QPropertyAnimation(self, b"position")
        self.animation.setEasingCurve(QEasingCurve.OutBounce)
        self.animation.setDuration(500)

        self.stateChanged.connect(self.setup_animation)

    def setBinding(
        self,
        object: Model,
        property: str,
        updateProperty: str | None = None,
    ):
        super().setBinding(object, property, updateProperty)

        self.setChecked(self.boundValue())

        self.stateChanged.connect(self._onButtonToggled)

    @Slot(bool)
    def _onButtonToggled(self, value: bool):
        assert self._boundObject is not None

        self.updateBoundObject(value)

    # https://raw.githubusercontent.com/Wanderson-Magalhaes/PyOneDark_Qt_Widgets_Modern_GUI/master/gui/widgets/py_toggle/py_toggle.py
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, pos):
        self._position = pos
        self.update()

    # START STOP ANIMATION
    def setup_animation(self, value: bool):
        self.animation.stop()

        if value:
            self.animation.setEndValue(self.width() - 26)
        else:
            self.animation.setEndValue(4)

        self.animation.start()

    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)

    def paintEvent(self, painter: QPaintEvent):  # type: ignore[override]
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.setFont(QFont("Segoe UI", 9))

        # SET PEN
        p.setPen(Qt.NoPen)

        # DRAW RECT
        rect = QRect(0, 0, self.width(), self.height())

        if not self.isChecked():
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
