# Standard Library
from typing import Any
import qtawesome as qta
from app.gui.components.form.CompanyForm import CompanyForm
from app.gui.components.form.JobForm import JobForm

from app.gui.components.pages.Header import Header
from app.gui.components.tabs.Tab import Tab
from PySide6.QtWidgets import QVBoxLayout, QSplitter, QFrame, QLabel
from PySide6.QtCore import Qt

# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabWidget.html
# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabBar.html


class JobApplicationTab(Tab):
    def __init__(self, label: str, **kwargs: Any) -> None:
        super().__init__(label=label, **kwargs)

        self.setObjectName("Tab:JobApplication")
        self.setContentsMargins(10, 0, 10, 0)

        # Setup Layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        splitter = QSplitter(Qt.Horizontal)
        splitter.setSizes([80, 800])
        splitter.setHandleWidth(100)

        leftLayout = QVBoxLayout()
        leftLayout.setContentsMargins(0, 0, 0, 0)
        leftLayout.setSpacing(20)
        leftFrame = QFrame()
        leftFrame.setLayout(leftLayout)

        rightLayout = QVBoxLayout()
        rightLayout.setContentsMargins(0, 0, 0, 0)
        rightFrame = QFrame()
        rightFrame.setLayout(rightLayout)

        # *([10] * 4)
        # QGroupBox to go around form
        # https://doc.qt.io/qtforpython/overviews/qtwidgets-widgets-groupbox-example.html#group-box-example

        # Setup LHS components
        header = Header(f"Job Application - {self.model.title}")
        jobForm = JobForm(self.model.job)
        companyForm = CompanyForm(self.model.company)

        leftLayout.addWidget(header)
        leftLayout.addWidget(jobForm)
        leftLayout.addWidget(companyForm)

        # Setup RHS components
        label = QLabel("Right Hand Side Frame")
        rightLayout.addWidget(label)

        splitter.addWidget(leftFrame)
        splitter.addWidget(rightFrame)

        # Add components to tab
        layout.addWidget(header)
        layout.addWidget(splitter)
