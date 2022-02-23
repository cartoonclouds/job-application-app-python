
from app.gui.components.tabs.Tab import Tab
from PySide6.QtWidgets import QTabWidget


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

    def tabOpenDoubleClick(self, i: int):
        pass
        # if i == -1:  # No tab under the click
        #     self.addNewEmptyTab()

    def closeTab(self, tabIndex: int):
        tab: Tab = self.widget(tabIndex)  # type: ignore

        if not tab.closable:
            return

        self.removeTab(tabIndex)
