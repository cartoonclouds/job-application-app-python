from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QTabBar, QTabWidget
from PySide6.QtCore import QPoint

from app.gui.components.tabs.Tab import Tab
from app.utils.Metaclasses.Singleton import Singleton


class TabServiceProvider(metaclass=Singleton):
    """
    URL: https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabWidget.html
    """

    _tabs: QTabWidget

    @classmethod
    def init(cls, tabBar: QTabBar):
        cls._tabs = QTabWidget()

        cls._tabs.setTabBar(tabBar)

    @classmethod
    @property
    def tabs(cls):
        return cls._tabs if hasattr(cls, "_tabs") else None

    @classmethod
    @property
    def tabBar(cls):
        return cls.tabs.tabBar()

    @classmethod
    def findTab(cls, tab: Tab | int | QPoint) -> None | Tab:
        """Searches for a tab either by another tab instance, the index or a cursor point.

        Args:
            tab (Tab | int | QPoint): The way to specifiy the tab to find

        Returns:
            None | Tab: The tab is returned if found, None otherwise
        """
        if isinstance(tab, Tab):
            tabIndex = cls.tabs.indexOf(tab)
        elif isinstance(tab, QPoint):
            tabIndex = cls.tabBar.tabAt(tab)
        elif isinstance(tab, int):  # type: ignore
            tabIndex = tab

        _tab = cls.tabs.widget(tabIndex)

        return _tab if isinstance(_tab, Tab) else None

    @classmethod
    def openTab(cls, tab: Tab | int | QPoint):
        """Opens a tab located by passing the tab instance, the index or a cursor point.

        If a tab instance is passed then it will be added to the group and set active.

        Args:
            tab (Tab | int | QPoint): The way to specifiy the tab to open

        Raises:
            Exception: If the tab cannot be found and a tab instance isn't passed an exception is thrown
        """
        _tab = tab if isinstance(tab, Tab) else cls.findTab(tab)

        if isinstance(_tab, Tab):
            cls.addTab(_tab)
        else:
            raise Exception(
                f"Unable to find or add tab to window. Error with tab {tab}"
            )

    @classmethod
    def addTab(cls, tab: Tab, focus: bool = True) -> Tab:
        """Adds a tab instance to the group of tabs.

        If an existing tab is passed it won't be added to prevent duplicate instances.

        Args:
            tab (Tab): The tab instance to add
            focus (bool, optional): Will set the tab as active. Defaults to True

        Returns:
            Tab: The newly added tab instance
        """
        isExistingTab = cls.findTab(tab)

        if isExistingTab is None:
            # Add tab
            if isinstance(tab.icon, QIcon | QPixmap):
                tabIndex = cls.tabs.addTab(tab, tab.icon, tab.label)
            else:
                tabIndex = cls.tabs.addTab(tab, tab.label)

            # Remove the close button
            if not tab.closable:
                cls.tabBar.setTabButton(tabIndex, QTabBar.RightSide, None)  # type: ignore

            tab.setParent(cls.tabs)

        # Switch to new tab
        if focus:
            tab.setActive()

        return tab

    @classmethod
    def closeTab(cls, tab: Tab | int | QPoint):
        """Closes a particular tab either by a tab instance, the index or a cursor point.

        Args:
            tab (Tab | int | QPoint): The way to specify the tab to be closed

        Raises:
            Exception: If the tab is not found an exception is thrown
        """
        closingTab = cls.findTab(tab)

        if not isinstance(closingTab, Tab):
            raise Exception(f"Unable to close tab. Tab not found.")

        if not closingTab.closable:
            return

        tabIndex = cls.tabs.indexOf(closingTab)

        cls.tabs.removeTab(tabIndex)

    @classmethod
    def tabCount(cls) -> int:
        """Returns the count of the number of tabs.

        Returns:
            int: The number of tabs in the group
        """
        return cls.tabs.count()
