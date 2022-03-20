from typing import Type
from typing_extensions import Self
from PySide6.QtWidgets import QMainWindow, QStatusBar
from pendulum import Pendulum


class StatusBarServiceProvider:
    statusBar: QStatusBar

    @classmethod
    def init(cls, window: QMainWindow) -> Type["StatusBarServiceProvider"]:
        cls.statusBar = window.statusBar()

        # Adding a temporary message
        cls.statusBar.showMessage("Status Bar service initiated")

        # Adding a permanent message
        # cls.wcLabel = QLabel(f"100 Words")
        # statusbar.addPermanentWidget(cls.wcLabel)

        return cls

    @classmethod
    def message(cls, message: str, withTimeStamp: bool = True):
        message = (
            Pendulum.now().to_time_string() + " " + message
            if withTimeStamp
            else message
        )

        cls.statusBar.showMessage(message)
