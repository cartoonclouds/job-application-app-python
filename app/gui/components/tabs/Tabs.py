
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from app.gui.components.tabs.Tab import Tab

# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabWidget.html
# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabBar.html


class Tabs(QTabWidget):
    def __init__(self):
        super(Tabs, self).__init__()

        self.setTabsClosable(True)
        self.setDocumentMode(True)
        self.setMovable(True)

        self.tabCloseRequested.connect(self.close_tab)
        self.tabBarDoubleClicked.connect(self.tab_open_doubleclick)

    def add_tab(self, tab: Tab) -> Tab:
        tab.set_parent(self)

        # Add tab
        if isinstance(tab.icon, QIcon):
            tab.index = self.addTab(tab, tab.icon, tab.label)
        else:
            tab.index = self.addTab(tab, tab.label)

        tab.set_text(tab.label)
        tab.set_tooltip(tab.tooltip)
        tab.set_whats_this(tab.tab_whatsThis)

        # Remove the close button
        if not tab.closable:
            self.tabBar().setTabButton(tab.index, QTabBar.RightSide, None)

        return tab

    def add_new_tab(self):
        pass

    def tab_open_doubleclick(self, i):
        if i == -1:  # No tab under the click
            self.add_new_tab()

    def close_tab(self, tabIndex):
        tab: Tab = self.widget(tabIndex)

        if not tab.closable:
            return

        self.removeTab(tabIndex)
