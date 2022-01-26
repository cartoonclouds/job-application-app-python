
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabWidget.html
# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabBar.html


class JobApplicationTab(QWidget):
    def __init__(self,
                 label: str,
                 tabs: QTabWidget,
                 autoAddToTabs: bool = True,
                 tooltip: str = None,
                 whatsThis: str = None,
                 icon: QIcon = None
                 ):
        
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
            self.add_to_tabs()

    def set_tab_icon(self, icon: QIcon):
        self.icon = icon
        self.tabs.setTabIcon(self.index, icon)

    def set_tab_text(self, label: str):
        self.label = label
        self.tabs.setTabText(self.index, label)

    def set_tab_tooltip(self, tooltip: str):
        self.tooltip = tooltip
        self.tabs.setTabToolTip(self.index, tooltip)

    def set_tab_whatsthis(self, tabWhatsThis: str):
        self.tabWhatsThis = tabWhatsThis
        self.tabs.setTabWhatsThis(self.index, tabWhatsThis)

    def set_active(self):
        self.error_if_not_inserted(
            "Tab must be inserted before setting as active")

        self.tabs.setCurrentWidget(self)

    def add_to_tabs(self):
        self.error_if_inserted("A tab cannot be inserted more than once")

        self.index = self.tabs.addTab(self, self.label)
        self.set_tab_text(self.label)
        self.set_tab_tooltip(self.tooltip)
        self.set_tab_whatsthis(self.tabWhatsThis)

        if (isinstance(self.icon, QIcon)):
            self.set_tab_icon(self.icon)

    def error_if_inserted(self, error):
        if self.index >= 0:
            raise Exception(error)
            # throw exception already added

    def error_if_not_inserted(self, error):
        if self.index == -1:
            raise Exception(error)
            # throw exception already added
