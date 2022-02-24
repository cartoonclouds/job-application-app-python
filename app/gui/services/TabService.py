
from app import types
from app.gui.components.tabs.Tab import Tab
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QTabBar, QTabWidget
from PySide6.QtCore import QModelIndex, QPersistentModelIndex

# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabWidget.html


class TabServiceProvider:
    tabs: QTabWidget

    def initTabs(self, tabBar: QTabBar):
        self.tabs = QTabWidget()
        self.tabs.setTabBar(tabBar)

    # def isTabOpen(self, tab: types.Tab):

    def openTab(self, tab: Tab, focus: bool = True) -> types.Tab:
        # if tab is already open, return

        # Add tab
        if isinstance(tab.icon, QIcon | QPixmap):
            tabIndex = self.tabs.addTab(tab, tab.icon, tab.label)
        else:
            tabIndex = self.tabs.addTab(tab, tab.label)

        # Remove the close button
        if not tab.closable:
            self.tabs.tabBar().setTabButton(tabIndex, QTabBar.RightSide, None)  # type: ignore

        tab.setParent(self.tabs)

        # Switch to new tab
        if focus:
            tab.setActive()

        return tab

    def closeTab(self, tab: Tab | int):
        closingTab: Tab
        tabIndex: int

        if isinstance(tab, Tab):
            closingTab = tab
        else:
            closingTab = self.tabs.widget(tab)  # type: ignore

        if not closingTab.closable:
            return

        tabIndex = self.tabs.indexOf(closingTab)

        self.tabs.removeTab(tabIndex)

    def tabCount(self) -> int:
        return self.tabs.count()


TabService = TabServiceProvider()
