# Standard Library
from typing import Any
import qtawesome as qta
from app.gui.components.form.CompanyForm import CompanyForm
from app.gui.components.form.JobForm import JobForm
from app.gui.components.form.inputs.TextInput import TextInput

from app.gui.components.pages.Header import Header
from app.gui.components.tabs.Tab import Tab
from PySide6.QtWidgets import (
    QVBoxLayout,
    QSplitter,
    QFrame,
    QLabel,
    QPushButton,
    QHBoxLayout,
)
from PySide6.QtCore import Qt
from app.storage import Storage

from app.utils.IconUtility import IconUtility

# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabWidget.html
# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabBar.html


class JobApplicationTab(Tab):
    def __init__(self, label: str, **kwargs: Any) -> None:
        super().__init__(label=label, **kwargs)

        self.setObjectName("Tab:JobApplication")
        self.setContentsMargins(
            Storage.WIDGET_SPACING * 2, 0, Storage.WIDGET_SPACING * 2, 0
        )

        # Header
        header = self._setupHeader()

        # Setup Layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        splitter = QSplitter(Qt.Horizontal)
        splitter.setSizes([80, 800])
        # splitter.setSizes([500, 500])
        # splitter.setStretchFactor(1, 500)

        # splitter.setHandleWidth(100)
        # splitter.setSizes([500, 500])
        # splitter.setStretchFactor(1, 500)

        # Splitter handle
        # handle: QSplitterHandle = splitter.handle(1)
        # handleLayout = QVBoxLayout(handle)
        # handleLayout.setSpacing(0)
        # # handleLayout.setContentsMargins(10, 0, 10, 0)

        # line = QFrame(handle)
        # line.setFrameShape(QFrame.HLine)
        # line.setFrameShadow(QFrame.Sunken)
        # handleLayout.addWidget(handle)

        # splitter.createHandle()
        splitter.setStyleSheet("QSplitter::handle { background-color: gray }")

        leftLayout = QVBoxLayout()
        leftLayout.setContentsMargins(0, 0, Storage.WIDGET_SPACING * 3, 0)
        leftLayout.setSpacing(20)
        leftFrame = QFrame()
        leftFrame.setLayout(leftLayout)
        leftFrame.setMaximumWidth(600)

        rightLayout = QVBoxLayout()
        rightLayout.setContentsMargins(Storage.WIDGET_SPACING * 3, 0, 0, 0)
        rightFrame = QFrame()
        rightFrame.setLayout(rightLayout)

        # *([10] * 4)
        # QGroupBox to go around form
        # https://doc.qt.io/qtforpython/overviews/qtwidgets-widgets-groupbox-example.html#group-box-example

        # Setup LHS components
        jobForm = JobForm(self.model.job)
        companyForm = CompanyForm(self.model.company)

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

    def _setupHeader(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(
            0, Storage.WIDGET_SPACING * 2, 0, Storage.WIDGET_SPACING * 2
        )
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        frame = QFrame()
        frame.setLayout(layout)
        frame.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)

        header = Header(
            f"Job Application - {self.model.title}",
            IconUtility.getFileIconAsPixmap("gear"),
            True,
        )
        header.textChanged.connect(self._updateJobApplicationTitle)

        saveButton = QPushButton("Save")
        # Toggle buttons
        pinButton = QPushButton("Pin")
        requiredFollowupButton = QPushButton("Required Followup")

        layout.addWidget(header)
        layout.addWidget(saveButton)
        layout.addWidget(pinButton)
        layout.addWidget(requiredFollowupButton)

        header.resize(header.sizeHint())

        return frame

    def _updateJobApplicationTitle(self, text: str):
        setattr(self.model, "title", text)
