# Framework imports
from PySide6.QtCore import (
    QEvent,
    QModelIndex,
    QObject,
    QPersistentModelIndex,
    QPoint,
    Qt,
)
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QApplication, QTabBar, QTabWidget, QWidget
from typing import Any


# Application imports
from app.gui.components.tabs.Tab import Tab
from app.gui.services.tab_service import TabServiceProvider
from app.utils.object_functions import format_object_name


class TabBar(QTabBar):
    """A collection of tabs.

    URL:
        https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabBar.html
    """

    def __init__(self) -> None:
        super(TabBar, self).__init__()
        self.setObjectName(format_object_name(__class__.__name__))
        self.setTabsClosable(True)
        self.setDocumentMode(True)
        self.setMovable(True)

        self.tabCloseRequested.connect(TabServiceProvider.closeTab)

        self.installEventFilter(self)

    def currentTab(self) -> Tab:
        return self.parentWidget().currentWidget()  # type: ignore

    # def mousePressEvent(self, arg__1: QMouseEvent) -> None:
    #     # all tabs movable except first
    #     self.setMovable(self.tabAt(arg__1.pos()) != 0)

    #     return super().mousePressEvent(arg__1)

    def eventFilter(self, source: "TabBar", event: QEvent) -> bool:

        if event.type() == QEvent.Type.MouseMove:

            if not source.currentTab().movable:  # Block MouseMove for first tab.
                return True

            else:  # For remaining tabs:

                # block MouseMove if the left edge of the moving tab goes
                # farther to the left than the right edge of first tab.

                moving_leftEdge = event.pos().x() - self.edge_offset
                fixed_rightEdge = self.tabRect(0).width()

                if moving_leftEdge < fixed_rightEdge:
                    return True

        elif event.type() == QEvent.Type.MouseButtonPress:
            event: QMouseEvent = event

            if event.button() == Qt.MouseButton.MiddleButton:
                TabServiceProvider.closeTab(event.pos())

            # Get mouse click horizontal position.
            xclick = event.pos().x()

            # Get the left edge horizontal position of the targeted tab.
            xleft = self.tabRect(self.tabAt(event.pos())).x()

            # Compute and store offset between mouse click horizontal
            # position and the left edge of the targeted tab
            self.edge_offset = xclick - xleft

        return QWidget.eventFilter(self, source, event)
