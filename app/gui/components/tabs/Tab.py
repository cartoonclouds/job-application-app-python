from typing import Optional
from PySide6.QtWidgets import QWidget, QTabWidget
from PySide6.QtGui import QIcon, QPixmap

from app.types import M


class Tab(QWidget):
    # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabWidget.html
    def __init__(
        self,
        label: str,
        model: Optional[M] = None,
        tooltip: str | None = None,
        whatsThis: str | None = None,
        icon: Optional[QIcon | QPixmap] = None,
        closable: bool = True,
        movable: bool = True,
    ) -> None:
        super().__init__()

        self.model = model

        self._tooltip = tooltip
        self._whatsThis = whatsThis

        self.label = label
        self.icon = icon
        self.closable = closable
        self.movable = movable

        self._parent: QTabWidget

    def setParent(self, parent: QTabWidget):  # type: ignore
        self._parent = parent

        if isinstance(self._tooltip, str):
            self.setTooltip(self._tooltip)

        if isinstance(self._whatsThis, str):
            self.setWhatsThis(self._whatsThis)

        if isinstance(self._tooltip, str):
            self.setText(self._tooltip)

        if isinstance(self.icon, QIcon):
            self.setTabIcon(self.icon)

    def tabIndex(self) -> int:
        if self._parent:
            return self._parent.indexOf(self)
        return -1

    def setTabIcon(self, icon: QIcon):
        if self._parent and self.tabIndex():
            self._parent.setTabIcon(self.tabIndex(), icon)

    def setText(self, label: str):
        if self._parent and self.tabIndex():
            self._parent.setTabText(self.tabIndex(), label)

    def setTooltip(self, tooltip: str):
        if self._parent and self.tabIndex():
            self._parent.setTabToolTip(self.tabIndex(), tooltip)

    def setWhatsThis(self, tabWhatsThis: str):  # type: ignore
        if self._parent and self.tabIndex():
            self._parent.setTabWhatsThis(self.tabIndex(), tabWhatsThis)

    def setActive(self):
        if self._parent and self.tabIndex():
            self._parent.setCurrentWidget(self)
