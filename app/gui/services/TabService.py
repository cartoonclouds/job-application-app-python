
from app import types
from app.gui.components.tabs.Tab import Tab
from app.gui.components.tabs.Tabs import Tabs
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QTabBar


class TabServiceProvider:
    def initTabs(self):
        self.tabs = Tabs()

    # def isTabOpen(self, tab: types.Tab):

    def openTab(self, tab: Tab, focus: bool = True) -> types.Tab:
        # if tab is already open, return

        # Add tab
        if isinstance(tab.icon, QIcon | QPixmap):
            tab.index = self.tabs.addTab(tab, tab.icon, tab.label)
        else:
            tab.index = self.tabs.addTab(tab, tab.label)

        # Remove the close button
        if not tab.closable:
            self.tabs.tabBar().setTabButton(tab.index, QTabBar.RightSide, None)

        tab.setParent(self.tabs)

        # Switch to new tab
        if focus:
            self.tabs.setCurrentIndex(tab.index)

        return tab

    def closeTab(self, tab: Tab | int):
        if isinstance(tab, Tab):
            tabIndex = tab.index
        else:
            tabIndex = tab

        self.tabs.removeTab(tabIndex)

    def tabCount(self) -> int:
        return self.tabs.count()


TabService = TabServiceProvider()
