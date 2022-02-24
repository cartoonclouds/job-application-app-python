

from PySide6.QtWidgets import QMainWindow, QStatusBar


class StatusBarServiceProvider:
    statusBar: QStatusBar

    def init(self, window: QMainWindow) -> None:
        self.statusBar: QStatusBar = window.statusBar()

        # Adding a temporary message
        self.statusBar.showMessage("Status Bar service initiated")

        # Adding a permanent message
        # self.wcLabel = QLabel(f"100 Words")
        # statusbar.addPermanentWidget(self.wcLabel)

    def showMessage(self, message: str):
        self.statusBar.showMessage(message)


StatusBarService = StatusBarServiceProvider()
