from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QTabBar, QTabWidget
from PySide6.QtCore import QPoint

from app.gui.components.tabs.Tab import Tab


class _TabServiceProvider:
    """
    URL: https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabWidget.html
    """

    tabs: QTabWidget

    def init(self, tabBar: QTabBar):
        self.tabs = QTabWidget()

        self.tabs.setTabBar(tabBar)

    def tabBar(self):
        return self.tabs.tabBar()

    def findTab(self, tab: Tab | int | QPoint) -> None | Tab:
        """Searches for a tab either by another tab instance, the index or a cursor point.

        Args:
            tab (Tab | int | QPoint): The way to specifiy the tab to find

        Returns:
            None | Tab: The tab is returned if found, None otherwise
        """
        if isinstance(tab, Tab):
            tabIndex = self.tabs.indexOf(tab)
        elif isinstance(tab, QPoint):
            tabIndex = self.tabBar().tabAt(tab)
        elif isinstance(tab, int):  # type: ignore
            tabIndex = tab

        _tab = self.tabs.widget(tabIndex)

        return _tab if isinstance(_tab, Tab) else None

    def openTab(self, tab: Tab | int | QPoint):
        """Opens a tab located by passing the tab instance, the index or a cursor point.

        If a tab instance is passed then it will be added to the group and set active.

        Args:
            tab (Tab | int | QPoint): The way to specifiy the tab to open

        Raises:
            Exception: If the tab cannot be found and a tab instance isn't passed an exception is thrown
        """
        _tab = tab if isinstance(tab, Tab) else self.findTab(tab)

        if isinstance(_tab, Tab):
            self.addTab(_tab)
        else:
            raise Exception(
                f"Unable to find or add tab to window. Error with tab {tab}"
            )

    def addTab(self, tab: Tab, focus: bool = True) -> Tab:
        """Adds a tab instance to the group of tabs.

        If an existing tab is passed it won't be added to prevent duplicate instances.

        Args:
            tab (Tab): The tab instance to add
            focus (bool, optional): Will set the tab as active. Defaults to True

        Returns:
            Tab: The newly added tab instance
        """
        isExistingTab = self.findTab(tab)

        if isExistingTab is None:
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

    def closeTab(self, tab: Tab | int | QPoint):
        """Closes a particular tab either by a tab instance, the index or a cursor point.

        Args:
            tab (Tab | int | QPoint): The way to specify the tab to be closed

        Raises:
            Exception: If the tab is not found an exception is thrown
        """
        closingTab = self.findTab(tab)

        if not isinstance(closingTab, Tab):
            raise Exception(f"Unable to close tab. Tab not found.")

        if not closingTab.closable:
            return

        tabIndex = self.tabs.indexOf(closingTab)

        self.tabs.removeTab(tabIndex)

    def tabCount(self) -> int:
        """Returns the count of the number of tabs.

        Returns:
            int: The number of tabs in the group
        """
        return self.tabs.count()


TabServiceProvider = _TabServiceProvider()
