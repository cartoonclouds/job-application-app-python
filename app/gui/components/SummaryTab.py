
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabWidget.html
# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabBar.html


class SummaryTab(QWidget):
    def __init__(self, tabs: QTabWidget, label: str, autoAddToTabs: bool = True, tooltip: str = None, whatsThis: str = None, icon: QIcon = None):
        super().__init__()

        self.tabs = tabs
        self.label = label
        self.index = -1
        self.autoAddToTabs = autoAddToTabs
        self.tooltip = tooltip
        self.tabWhatsThis = whatsThis
        self.icon = icon

        layout = QFormLayout()
        layout.addRow("Name", QLineEdit())
        layout.addRow("Address", QLineEdit())

        self.setLayout(layout)

        if (autoAddToTabs):
            self.addToTabs()

    def setTabIcon(self, icon: QIcon):
        self.icon = icon
        self.tabs.setTabIcon(self.index, icon)

    def setTabText(self, label: str):
        self.label = label
        self.tabs.setTabText(self.index, label)

    def setTabToolTip(self, tooltip: str):
        self.tooltip = tooltip
        self.tabs.setTabToolTip(self.index, tooltip)

    def setTabWhatsThis(self, tabWhatsThis: str):
        self.tabWhatsThis = tabWhatsThis
        self.tabs.setTabWhatsThis(self.index, tabWhatsThis)

    def setActive(self):
        self.errorIfNotInserted(
            "Tab must be inserted before setting as active")

        self.tabs.setCurrentWidget(self)

    def addToTabs(self):
        self.errorIfInserted("A tab cannot be inserted more than once")

        self.index = self.tabs.addTab(self, self.label)
        self.setTabText(self.label)
        self.setTabToolTip(self.tooltip)
        self.setTabWhatsThis(self.tabWhatsThis)

        if (isinstance(self.icon, QIcon)):
            self.setTabIcon(self.icon)

        # Remove the close button
        self.tabs.tabBar().setTabButton(self.index, QTabBar.RightSide, None)

    def errorIfInserted(self, error):
        if self.index >= 0:
            raise Exception(error)
            # throw exception already added

    def errorIfNotInserted(self, error):
        if self.index == -1:
            raise Exception(error)
            # throw exception already added
