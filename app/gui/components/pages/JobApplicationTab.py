# Standard Library
from typing import Any
import qtawesome as qta
from app.gui.components.Splitter.Splitter import Splitter
from app.gui.components.datatable.Datatable import Datatable
from app.gui.components.form.CompanyForm import CompanyForm
from app.gui.components.form.Form import Form
from app.gui.components.form.JobForm import JobForm
from app.gui.components.form.inputs.ToggleButton import ToggleButton
from app.gui.components.form.inputs.ToggleButtonSquare import ToggleButtonSquare
from app.gui.components.models.ActionDatatableModel import ActionDatatableModel

from app.gui.components.pages.TabHeader import TabHeader
from app.gui.components.tabs.Tab import Tab
from PySide6.QtWidgets import (
    QVBoxLayout,
    QSplitter,
    QFrame,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QSplitterHandle,
    QMainWindow,
)
from PySide6.QtCore import Qt, QSize, Slot
from PySide6.QtGui import QFontMetrics
from app.constants import WIDGET_SPACING, WIDGET_MARGINS, ZERO_MARGINS
from app.models.JobApplication import JobApplication
from app.utils.ui_functions import UIFunctions

from app.utils.icon_utility import IconUtility

# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabWidget.html
# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabBar.html


class JobApplicationTab(Tab):
    def __init__(self, label: str, model: JobApplication, **kwargs: Any) -> None:
        super().__init__(label=label, **kwargs)

        self.model = model

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

        widget = splitter.widget(1)
        policy = widget.sizePolicy()
        policy.setHorizontalStretch(10)
        widget.setSizePolicy(policy)

        # Add components to tab
        layout.addWidget(header)
        layout.addWidget(splitter)

    def _setupHeader(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(ZERO_MARGINS)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        frame = QFrame()
        frame.setLayout(layout)
        frame.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)

        header = TabHeader(
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
            textSize.height() + layoutMargins.top() + layoutMargins.bottom() + 2
        )

        saveButton = QPushButton("Save")
        saveButton.clicked.connect(self.model.push)
        # TODO Refresh model/clear "modified"

        # Toggle buttons
        pinButton = ToggleButton("Pinned", "Pin")
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

    def _setupLeftFrame(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(ZERO_MARGINS)
        frame = QFrame()
        frame.setLayout(layout)

        # frame.setMinimumWidth(650)
        # frame.setMaximumWidth(650)

        self.model

        jobForm = JobForm(self.model.job)
        companyForm = CompanyForm(self.model.company)

        metaObject = companyForm.metaObject()
        properties = [
            metaObject.property(i).name()
            for i in range(metaObject.propertyOffset(), metaObject.propertyCount())
        ]
        methods = [
            metaObject.method(i).signature()
            for i in range(metaObject.methodOffset(), metaObject.methodCount())
        ]
        # debug(metaObject.methodCount())

        jobForm.modified.connect(self._formModified)
        companyForm.modified.connect(self._formModified)
        # -------------------------- #

        layout.addWidget(jobForm)
        layout.addWidget(companyForm)

        return frame

    def _setupRightFrame(self):
        layout = QVBoxLayout()
        frame = QFrame()
        frame.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        frame.setLayout(layout)

        datatableModel = ActionDatatableModel()
        datatable = Datatable(datatableModel)

        dropzone = QLabel("Right Hand Side File Dropzone")

        splitter = Splitter(Qt.Vertical)
        splitter.addWidget(datatable)
        splitter.addWidget(dropzone)

        layout.addWidget(splitter)

        # datatable.setStyleSheet("border:3px solid green")
        # dropzone.setStyleSheet("border:1px solid blue")
        # frame.setStyleSheet("border:1px solid red")

        return frame

    @Slot(str)
    def _updateJobApplicationTitle(self, text: str):
        setattr(self.model, "title", text)

        debug(self.model, dict(zip(["title"], [text])))

    @Slot(bool, Form)
    def _formModified(self, modified: bool, form: Form):
        window = UIFunctions.findMainWindow()

        if isinstance(window, QMainWindow):
            window.setWindowModified(modified)
