from typing import Type
from PySide6.QtCore import (
    QObject,
    QSize,
    QPointF,
    QPropertyAnimation,
    QEasingCurve,
    Qt,
    Slot,
    Property,
    QRect,
)
from PySide6.QtGui import QPainter, QPalette, QLinearGradient, QGradient, QColor, QBrush
from PySide6.QtWidgets import (
    QAbstractButton,
    QApplication,
    QWidget,
    QHBoxLayout,
    QLabel,
)
from pygments import highlight


class SwitchPrivate(QObject):
    """

    URL: https://www.pythonguis.com/tutorials/pyside6-animated-widgets/
         https://github.com/eyllanesc/RaspberryPi/blob/master/pyqt/lib/GUI/Switch.pys
    """

    def __init__(self, parentWidget: QWidget, parent: None | QObject = None):
        QObject.__init__(self, parent=parent)

        self.parentWidget = parentWidget

        self._position = 0.0

        self.gradient = QLinearGradient()
        self.gradient.setSpread(QGradient.PadSpread)

        self.animation = QPropertyAnimation(self, b"position")
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.setDuration(400)
        self.animation.setEasingCurve(QEasingCurve.InOutExpo)

        self.animation.finished.connect(self.parentWidget.update)

    @Property(float)  # type: ignore
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value
        self.parentWidget.update()

    @Slot(bool, name="animate")
    def animate(self, checked: bool):
        self.animation.setDirection(
            QPropertyAnimation.Forward if checked else QPropertyAnimation.Backward
        )
        self.animation.start()

    def __del__(self):
        del self.animation

    def draw(self, painter: QPainter):
        # COLORS
        # self._position = 3
        # self._bg_color = "#777"
        # self._circle_color = "#DDD"
        # self._active_color = "#00BCFF"

        widgetRect: QRect = self.parentWidget.rect()
        widgetWidth = widgetRect.width()
        widgetHeight = widgetRect.height()

        margin = int(widgetHeight / 10)
        shadow = self.parentWidget.palette().color(QPalette.Dark)
        light = self.parentWidget.palette().color(QPalette.Light)
        button = self.parentWidget.palette().color(QPalette.Button)

        painter.setPen(Qt.NoPen)

        solidColor = True

        if solidColor:
            # Solid color
            solidBrush = QBrush(QColor(13, 110, 253))
            whiteBrush = QBrush(Qt.white)

            painter.setBrush(solidBrush)
            painter.drawRoundedRect(widgetRect, widgetHeight / 2, widgetHeight / 2)

            painter.setBrush(whiteBrush)
            x: float = widgetHeight / 2.0 + self._position * (
                widgetWidth - widgetHeight
            )

            painter.drawEllipse(
                QPointF(x, widgetHeight / 2),
                widgetHeight / 2 - margin,
                widgetHeight / 2 - margin,
            )

        else:
            # Draw background
            self.gradient.setColorAt(0, shadow.darker(130))
            self.gradient.setColorAt(1, light.darker(130))
            self.gradient.setStart(0, widgetHeight)
            self.gradient.setFinalStop(0, 0)

            painter.setBrush(self.gradient)
            painter.drawRoundedRect(widgetRect, widgetHeight / 2, widgetHeight / 2)

            # # Draw border
            self.gradient.setColorAt(0, shadow.darker(140))
            self.gradient.setColorAt(1, light.darker(160))
            self.gradient.setStart(0, 0)
            self.gradient.setFinalStop(0, widgetHeight)

            painter.setBrush(self.gradient)
            painter.drawRoundedRect(
                widgetRect.adjusted(margin, margin, -margin, -margin),
                widgetHeight / 2,
                widgetHeight / 2,
            )

            # Draw handle
            self.gradient.setColorAt(0, button.darker(130))
            self.gradient.setColorAt(1, button)

            painter.setBrush(self.gradient)

            x: float = widgetHeight / 2.0 + self._position * (
                widgetWidth - widgetHeight
            )

            painter.drawEllipse(
                QPointF(x, widgetHeight / 2),
                widgetHeight / 2 - margin,
                widgetHeight / 2 - margin,
            )
