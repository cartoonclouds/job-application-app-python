

from PySide6.QtWidgets import QWidget, QTabWidget, QTabBar
from PySide6.QtGui import QIcon


class Tab(QWidget):
    def __init__(self):
        super(Tab, self).__init__()

        self.parent: QTabWidget = None

    def setParent(self, parent: QTabWidget):
        self.parent = parent

    def setTabIcon(self, icon: QIcon):
        self.parent.setTabIcon(self.index, icon)

    def setText(self, label: str):
        self.parent.setTabText(self.index, label)

    def setTooltip(self, tooltip: str):
        self.parent.setTabToolTip(self.index, tooltip)

    def setWhatsThis(self, tabWhatsThis: str):
        self.parent.setTabWhatsThis(self.index, tabWhatsThis)

    def setActive(self):
        self.parent.setCurrentWidget(self)
