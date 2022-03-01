from PySide6.QtWidgets import (
    QLabel,
    QFormLayout,
    QWidget,
    QFrame,
    QPlainTextEdit,
    QLayout,
    QVBoxLayout,
    QGroupBox,
    QPushButton,
    QCalendarWidget,
    QDateEdit,
    QGraphicsColorizeEffect,
    QHBoxLayout,
    QGridLayout,
)
from PySide6.QtGui import QFont, QPaintEvent, QFontMetrics
from PySide6.QtCore import Qt, QSize, QRect, QDateTime
from PySide6.QtWidgets import QSizePolicy, QLineEdit
from app.gui.components.form.inputs.SelectBox import SelectBox
from app.gui.components.form.inputs.TextAreaInput import TextAreaInput
from app.gui.components.form.inputs.TextInput import TextInput
from app.models import Model
import app.gui.components.form.inputs.TextInput

import ctypes
from app.models.Profession import Profession
from app.utilities.IconUtility import IconUtility


class Form(QFrame):
    def __init__(
        self, name: str, model: Model = None, title: str | None = None
    ) -> None:
        super(Form, self).__init__()

        self._model = model
        self._title = title
        self.setObjectName("Form:" + name)
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        # self.setContentsMargins(0, 0, 0, 0)

        self._layout = QGridLayout()
        self._layout.setAlignment(Qt.AlignTop)

        self.formTitle = QLabel(self._title)
        self.formTitle.move(0, -60)
        self.formTitle.setContentsMargins(0, 6, 0, 0)
        self.addRow(self.formTitle)

        # -------------------------- #
        # -- insert form elements -- #

        titleInput = TextInput("Title")
        titleInput.setBinding(self._model, "title")
        titleInput.setPlaceholderText("Job title")

        websiteInput = TextInput("Website")
        websiteInput.setBinding(self._model.job, "website")
        websiteInput.setPlaceholderText("www.job-application.com")

        professionInput = SelectBox("Profession")
        professionInput.addItems(sorted([p.profession for p in Profession.get().all()]))
        professionInput.setEditable(True)
        professionInput.setBinding(self._model.job.profession, "profession")
        professionInput.setPlaceholderText("Profession")

        commentsInput = TextAreaInput("Comments")
        commentsInput.setBinding(self._model.job, "comments")
        commentsInput.setPlaceholderText("Details about this job...")

        # self.calendar = QDateEdit(QDateTime.currentDateTime().date(), self)
        # self.calendar.setCalendarPopup(True)

        # textInput = "TextInput"
        # # y = getattr(app.gui.components.form.inputs.TextInput)
        # debug(globals()[textInput]())
        # debug(getattr(QLineEdit, 'QLineEdit'))

        self.addRow(titleInput)
        self.addRow(professionInput)
        self.addRow(websiteInput)
        self.addRow(professionInput)
        self.addRow(commentsInput)
        # -------------------------- #

        self.setLayout(self._layout)

    def addRow(self, *fields):
        newRowIndex = self.rowCount + 1
        newColIndex = 0

        if len(fields) == 1:
            field: TextInput = fields[0]
            self._layout.addWidget(field, newRowIndex, newColIndex, Qt.AlignTop)
        else:
            for field in fields:
                field: TextInput = field

                self._layout.addWidget(field, newRowIndex, newColIndex, Qt.AlignTop)
                newColIndex += 1

    @property
    def rowCount(self) -> int:
        return self._layout.rowCount()

    @property
    def columnCount(self) -> int:
        return self._layout.columnCount()

    def setTitle(self, title: str):
        self._title = title
        self.formTitle.setText(title)

    # def paintEvent(self, painter: QPaintEvent) -> None:
    #     # self.formTitle.move(painter.rect().x(), painter.rect().y() + 6)

    #     self.formTitle.raise_()
    #     self.stackUnder(jobForm.formTitle)

    #     return super().paintEvent(painter)
