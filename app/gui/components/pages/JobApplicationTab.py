# Standard Library
from typing import Any

from app.gui.components.pages.Header import Header
from app.gui.components.tabs.Tab import Tab
from PySide6.QtWidgets import QFormLayout, QLineEdit

# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabWidget.html
# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabBar.html


class JobApplicationTab(Tab):
    def __init__(self, label: str, **kwargs: Any) -> None:
        super().__init__(label=label, **kwargs)

        layout = QFormLayout()
        nameInput = QLineEdit()

        if self.model:
            nameInput.setText(self.model.title)

        layout.addRow(Header(f"Job Application - {self.model.title}"))
        layout.addRow("Name", nameInput)
        layout.addRow("Address", QLineEdit())

        self.setLayout(layout)
