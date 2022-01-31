
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from app.gui.components.tabs.Tab import Tab
from app import types


class Tabs(QTabWidget):
    """A collection of tabs.

    URL:
        https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabWidget.html
        https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabBar.html
    """

    def __init__(self) -> None:
        super().__init__()

        self.setTabsClosable(True)
        self.setDocumentMode(True)
        self.setMovable(True)

        self.tabCloseRequested.connect(self.closeTab)
        self.tabBarDoubleClicked.connect(self.tabOpenDoubleClick)

    def addNewTab(self, tab: types.Tab) -> types.Tab:
        # Add tab
        if isinstance(tab.icon, QIcon | QPixmap):
            tab.index = self.addTab(tab, tab.icon, tab.label)
        else:
            tab.index = self.addTab(tab, tab.label)

        # Remove the close button
        if not tab.closable:
            self.tabBar().setTabButton(tab.index, QTabBar.RightSide, None)

        tab.setParent(self)

        return tab

    def addNewEmptyTab(self):
        pass

    def tabOpenDoubleClick(self, i: int):
        if i == -1:  # No tab under the click
            self.addNewEmptyTab()

    def closeTab(self, tabIndex: int):
        tab: Tab = self.widget(tabIndex)  # type: ignore

        if not tab.closable:
            return

        self.removeTab(tabIndex)
