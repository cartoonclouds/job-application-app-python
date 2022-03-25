from typing import Union, Callable, Any
from PySide6.QtWidgets import QApplication, QMainWindow, QMenuBar
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtCore import QKeyCombination

from app.utils.object_functions import formatObjectName
from inflection import parameterize

# from main import MainWindow


class UIFunctions:
    @classmethod
    def findMainWindow(cls) -> Union[QMainWindow, None]:
        # Global function to find the (open) QMainWindow in application
        app = QApplication.instance()
        for widget in app.topLevelWidgets():
            if isinstance(widget, QMainWindow):
                return widget
        return None

    @classmethod
    def createNewAction(
        cls,
        name: str,
        tooltip: str,
        statusTip: str,
        shortcut: Union[
            QKeySequence, QKeyCombination, QKeySequence.StandardKey, str, int
        ],
        slot: Callable[..., Any],
        menubar: QMenuBar,
    ):
        action = QAction(name, menubar)

        action.setObjectName(
            formatObjectName(
                "Action",
                parameterize(name or "", "_").lower(),
            )
        )
        action.setToolTip(tooltip)
        action.setStatusTip(statusTip)
        action.setShortcut(shortcut)
        action.triggered.connect(slot)

        return action
