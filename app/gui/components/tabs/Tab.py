

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.gui.components.tabs.Tabs import Tabs


class Tab(QWidget):
    def __init__(self,
                 label: str,
                 tooltip: str | None = None,
                 whatsThis: str | None = None,
                 icon: QIcon | None = None,
                 closable: bool = True
                 ) -> None:
        super().__init__()

        self._tooltip = tooltip
        self._whatsThis = whatsThis

        self.label = label
        self.index = 0
        self.icon = icon
        self.closable = closable

    def setParent(self, parent: 'Tabs'):  # type: ignore
        self.parent: 'Tabs' = parent

        if isinstance(self._tooltip, str):
            self.setTooltip(self._tooltip)

        if isinstance(self._whatsThis, str):
            self.setWhatsThis(self._whatsThis)

        if isinstance(self._tooltip, str):
            self.setText(self._tooltip)

        if isinstance(self.icon, QIcon):
            self.setTabIcon(self.icon)

    def setTabIcon(self, icon: QIcon):
        self.parent.setTabIcon(self.index, icon)

    def setText(self, label: str):
        self.parent.setTabText(self.index, label)

    def setTooltip(self, tooltip: str):
        self.parent.setTabToolTip(self.index, tooltip)

    def setWhatsThis(self, tabWhatsThis: str):  # type: ignore
        self.parent.setTabWhatsThis(self.index, tabWhatsThis)

    def setActive(self):
        self.parent.setCurrentWidget(self)
