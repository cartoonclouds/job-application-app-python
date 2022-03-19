import typing
from PySide6.QtWidgets import QApplication, QMainWindow


class GUIUtilities:
    @classmethod
    def findMainWindow(cls) -> typing.Union[QMainWindow, None]:
        # Global function to find the (open) QMainWindow in application
        app = QApplication.instance()
        for widget in app.topLevelWidgets():
            if isinstance(widget, QMainWindow):
                return widget
        return None
