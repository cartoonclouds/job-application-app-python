

from PySide6.QtWidgets import QWidget, QTabWidget, QTabBar
from PySide6.QtGui import QIcon


class Tab(QWidget):
    def __init__(self):
        super(Tab, self).__init__()

        self.parent: QTabWidget = None

    def set_parent(self, parent: QTabWidget):
        self.parent = parent

    def set_tab_icon(self, icon: QIcon):
        self.parent.setTabIcon(self.index, icon)

    def set_text(self, label: str):
        self.parent.setTabText(self.index, label)

    def set_tooltip(self, tooltip: str):
        self.parent.setTabToolTip(self.index, tooltip)

    def set_whats_this(self, tabWhatsThis: str):
        self.parent.setTabWhatsThis(self.index, tabWhatsThis)

    def set_active(self):
        self.parent.setCurrentWidget(self)
