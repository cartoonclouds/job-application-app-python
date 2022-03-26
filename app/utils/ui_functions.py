from itertools import islice
from typing import Callable, Any
from PySide6.QtWidgets import QApplication, QMainWindow, QMenuBar
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtCore import QKeyCombination
from app.utils.iter_functions import first_where

from app.utils.object_functions import formatObjectName
from inflection import parameterize

# from main import MainWindow


class UIFunctions:
    @classmethod
    def findMainWindow(cls) -> QMainWindow | None:
        # Global function to find the (open) QMainWindow in application
        app: QApplication | None = QApplication.instance()
        if app is None:
            return None

        return first_where(app.topLevelWidgets(), lambda w: isinstance(w, QMainWindow))

    @classmethod
    def create_new_action(
        cls,
        name: str,
        tooltip: str,
        statusTip: str,
        shortcut: QKeySequence | QKeyCombination | QKeySequence.StandardKey | str | int,
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
