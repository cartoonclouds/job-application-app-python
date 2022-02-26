# Standard Library
from typing import Any

from app.gui.components.pages.Header import Header
from app.gui.components.tabs.Tab import Tab
from PySide6.QtWidgets import QFormLayout, QLineEdit, QVBoxLayout

# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabWidget.html
# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabBar.html


class JobApplicationTab(Tab):
    def __init__(self, label: str, **kwargs: Any) -> None:
        super().__init__(label=label, **kwargs)

        layout = QVBoxLayout()
        # *([10] * 4)
        self.setContentsMargins(10, 0, 10, 0)
        self.setLayout(layout)

        header = Header(f"Job Application - {self.model.title}")

        nameInput = QLineEdit()

        if self.model:
            nameInput.setText(self.model.title)

        layout.setStretchFactor(header, 0)

        # QGroupBox to go around form
        # https://doc.qt.io/qtforpython/overviews/qtwidgets-widgets-groupbox-example.html#group-box-example

        layout.addWidget(header)
        layout.addWidget(nameInput)

        self.setLayout(layout)
