

from PySide6.QtWidgets import QWidget, QTabWidget
from PySide6.QtGui import QIcon


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

    def setParent(self, parent: QTabWidget):
        self.parent = parent

        self.setTooltip(self._tooltip)
        self.setWhatsThis(self._whatsThis)
        self.setText(self.label)

        self.setTabIcon(self.icon)

    def setTabIcon(self, icon: QIcon):
        if not icon:
            return
        self.parent.setTabIcon(self.index, icon)

    def setText(self, label: str):
        self.parent.setTabText(self.index, label)

    def setTooltip(self, tooltip: str):
        self.parent.setTabToolTip(self.index, tooltip)

    def setWhatsThis(self, tabWhatsThis: str):
        self.parent.setTabWhatsThis(self.index, tabWhatsThis)

    def setActive(self):
        self.parent.setCurrentWidget(self)
