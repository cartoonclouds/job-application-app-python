# Framework imports
from typing import Sequence, TypeVar
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QGridLayout, QLabel, QWidget

# Application imports
from app.gui.components.EditableLabel.EditableLabel import EditableLabel
from app.gui.components.form.PayOptions import PayOptions
from app.gui.components.form.inputs.DateTimeInput import DateTimeInput
from app.gui.components.form.inputs.SelectBox import SelectBox
from app.gui.components.form.inputs.TextAreaInput import TextAreaInput
from app.gui.components.form.inputs.TextInput import TextInput
from app.gui.components.form.inputs.ToggleButtonSquare import ToggleButtonSquare
from PySide6.QtCore import Signal

from app.types import TModel

TInput = TypeVar(
    "TInput",
    EditableLabel,
    DateTimeInput,
    SelectBox,
    TextAreaInput,
    TextInput,
    ToggleButtonSquare,
    PayOptions,
    QLabel,
)


# Validator https://docs.python-cerberus.org/en/stable/


class Form(QFrame):
    modified = Signal(bool)

    def __init__(self, name: str, model: TModel, title: str) -> None:
        super(Form, self).__init__()

        self._name = name
        self._model = model
        self._title = title
        self.setObjectName("Form")
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.setStyleSheet(
            """
            QFrame {
                background-color: #FFF
            }
        """
        )

        self._layout = QGridLayout()
        self._layout.setAlignment(Qt.AlignTop)
        self._layout.setSpacing(12)

        self.formTitle = QLabel(self._title, self)
        # self.formTitle.move(0, -15)
        # self.formTitle.raise_()
        # self.formTitle.setContentsMargins(0, 6, 0, 0)

        self.addRow(self.formTitle)

        self.setLayout(self._layout)

    # https://stackoverflow.com/questions/19211828/using-any-and-all-to-check-if-a-list-contains-one-set-of-values-or-another
    def isModified(self):
        """Determines if any input element in the form has been modified"""
        return len(self.modifiedWidgets()) > 0

    def modifiedWidgets(self):
        """Returns any element in the form that has been modified"""
        return [w for w in self.inputWidgets() if w.isModified()]

    def inputWidgets(self) -> Sequence[TInput]:
        """Returns all form input elements"""
        return [w for w in self.children() if isinstance(w, TInput)]

    def addRow(
        self, *fields: TInput | Sequence[TInput], **cellSpan: dict[str, int] | int
    ):
        newRowIndex = self.rowCount + 1
        newColIndex = 0

        colspan: int = cellSpan.get("columnSpan", 1)
        rowspan: int = cellSpan.get("rowSpan", 1)

        if len(fields) == 1:
            field = fields[0]

            if hasattr(field, "modified"):
                field.modified.connect(lambda: self.modified.emit(True))

            self._layout.addWidget(
                field, newRowIndex, newColIndex, rowspan, colspan, Qt.AlignTop
            )
        else:
            for field in fields:
                if not isinstance(field, QWidget):
                    continue

                if hasattr(field, "modified"):
                    field.modified.connect(lambda: self.modified.emit(True))

                self._layout.addWidget(
                    field, newRowIndex, newColIndex, rowspan, colspan, Qt.AlignTop
                )
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
