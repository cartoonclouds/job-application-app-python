# Standard Library
from typing import Any
import qtawesome as qta
from app.gui.components.Splitter.Splitter import Splitter
from app.gui.components.datatable.Datatable import Datatable
from app.gui.components.form.CompanyForm import CompanyForm
from app.gui.components.form.Form import Form
from app.gui.components.form.JobForm import JobForm
from app.gui.components.form.inputs.TextInput import TextInput
from app.gui.components.form.inputs.ToggleButtonSquare import ToggleButtonSquare
from app.gui.components.models.ActionDatatableModel import ActionDatatableModel

from app.gui.components.pages.Header import Header
from app.gui.components.tabs.Tab import Tab
from PySide6.QtWidgets import (
    QVBoxLayout,
    QSplitter,
    QFrame,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QSplitterHandle,
)
from PySide6.QtCore import Qt, QSize, Slot
from PySide6.QtGui import QPaintEvent, QFontMetrics
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

        # Setup frames
        header = self._setupHeader()
        leftFrame = self._setupLeftFrame()

        rightFrame = self._setupRightFrame()

        # Setup Layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # line = QFrame(handle)
        # line.setFrameShape(QFrame.HLine)
        # line.setFrameShadow(QFrame.Sunken)
        # handleLayout.addWidget(handle)

        splitter = Splitter(Qt.Horizontal)
        splitter.addWidget(leftFrame)
        splitter.addWidget(rightFrame)

        # Add components to tab
        layout.addWidget(header)
        layout.addWidget(splitter)

    def _setupLeftFrame(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, Storage.WIDGET_SPACING * 3, 0)
        layout.setSpacing(20)
        frame = QFrame()
        frame.setLayout(layout)

        frame.setMinimumWidth(650)
        frame.setMaximumWidth(650)

        jobForm = JobForm(self.model.job)
        companyForm = CompanyForm(self.model.company)

        jobForm.modified.connect(self._formModified)
        companyForm.modified.connect(self._formModified)
        # -------------------------- #

        layout.addWidget(jobForm)
        layout.addWidget(companyForm)

        return frame

    def _setupHeader(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(Storage.ZERO_MARGINS)
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

        # Set header's max height
        fontMetrics: QFontMetrics = header.label.fontMetrics()
        textSize: QSize = fontMetrics.size(0, header.label.text())
        layoutMargins = layout.contentsMargins()
        frame.setMaximumHeight(
            textSize.height() + layoutMargins.top() + layoutMargins.bottom()
        )

        saveButton = QPushButton("Save")

        # Toggle buttons
        pinButton = ToggleButtonSquare("Pinned", "Pin")
        pinButton.setBinding(self.model, "pinned")

        requiredFollowupButton = ToggleButtonSquare(
            "Requires Followup", "Require Followup"
        )
        requiredFollowupButton.setBinding(self.model, "requires_followup")

        layout.addWidget(header)
        layout.addWidget(saveButton)
        layout.addWidget(pinButton)
        layout.addWidget(requiredFollowupButton)

        header.resize(header.sizeHint())

        return frame

    def _setupRightFrame(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(Storage.WIDGET_SPACING * 3, 0, 0, 0)
        frame = QFrame()
        frame.setLayout(layout)

        datatableModel = ActionDatatableModel()
        datatable = Datatable(datatableModel)

        layout.addWidget(datatable)
        layout.addWidget(QLabel("Right Hand Side File Dropzone"))

        return frame

    def _updateJobApplicationTitle(self, text: str):
        setattr(self.model, "title", text)

        debug(self.model, dict(zip(["title"], [text])))

    @Slot(bool, Form)
    def _formModified(self, modified: bool, form: Form):
        debug(form, "Modified? " + str(modified))

        # window.setWindowModified(False)
