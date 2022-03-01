# Standard Library
from typing import Any
import qtawesome as qta
from app.gui.components.form.form import Form

from app.gui.components.pages.Header import Header
from app.gui.components.tabs.Tab import Tab
from PySide6.QtWidgets import QFormLayout, QLineEdit, QVBoxLayout

# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabWidget.html
# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabBar.html


class JobApplicationTab(Tab):
    def __init__(self, label: str, **kwargs: Any) -> None:
        super().__init__(label=label, **kwargs)

        self.setObjectName("Tab:JobApplication")

        layout = QVBoxLayout(self)
        # *([10] * 4)
        self.setContentsMargins(10, 0, 10, 0)

        header = Header(f"Job Application - {self.model.title}")

        # QGroupBox to go around form
        # https://doc.qt.io/qtforpython/overviews/qtwidgets-widgets-groupbox-example.html#group-box-example

        jobForm = Form("JobInfo", self.model, "Job Information")

        layout.addWidget(header)
        layout.addWidget(jobForm)
