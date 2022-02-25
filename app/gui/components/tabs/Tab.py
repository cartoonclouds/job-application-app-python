

from typing import Optional
from PySide6.QtWidgets import QWidget, QTabWidget
from PySide6.QtGui import QIcon, QPixmap

from app.types import M


class Tab(QWidget):
    def __init__(self,
                 label: str,
                 model: Optional[M] = None,
                 tooltip: str | None = None,
                 whatsThis: str | None = None,
                 icon: Optional[QIcon | QPixmap] = None,
                 closable: bool = True,
                 movable: bool = True
                 ) -> None:
        super().__init__()

        self.model = model

        self._tooltip = tooltip
        self._whatsThis = whatsThis

        self.label = label
        self.icon = icon
        self.closable = closable
        self.movable = movable

        self._parent: QTabWidget | None

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
        if isinstance(self._parent, QTabWidget):
            return self._parent.indexOf(self)
        return -1

    def setTabIcon(self, icon: QIcon):
        if isinstance(self._parent, QTabWidget) and self.tabIndex():
            self._parent.setTabIcon(self.tabIndex(), icon)

    def setText(self, label: str):
        if isinstance(self._parent, QTabWidget) and self.tabIndex():
            self._parent.setTabText(self.tabIndex(), label)

    def setTooltip(self, tooltip: str):
        if isinstance(self._parent, QTabWidget) and self.tabIndex():
            self._parent.setTabToolTip(self.tabIndex(), tooltip)

    def setWhatsThis(self, tabWhatsThis: str):  # type: ignore
        if isinstance(self._parent, QTabWidget) and self.tabIndex():
            self._parent.setTabWhatsThis(self.tabIndex(), tabWhatsThis)

    def setActive(self):
        if isinstance(self._parent, QTabWidget) and self.tabIndex():
            self._parent.setCurrentWidget(self)
