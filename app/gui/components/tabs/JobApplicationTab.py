
from PySide6.QtWidgets import QFormLayout, QLineEdit

from app.gui.components.tabs.Tab import Tab
from app import types

# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabWidget.html
# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabBar.html


class JobApplicationTab(Tab):
    def __init__(self, label: str, **kwargs: types.TabDetails) -> None:
        super().__init__(label=label, **kwargs)

        layout = QFormLayout()
        nameInput = QLineEdit()

        if self.model:
            nameInput.setText(self.model.title)

        layout.addRow("Name", nameInput)
        layout.addRow("Address", QLineEdit())

        self.setLayout(layout)
