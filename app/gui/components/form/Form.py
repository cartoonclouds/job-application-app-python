# Framework imports
from typing import Any, List, Sequence, TypeVar
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QLabel,
    QWidget,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
)

# Application imports
from app.gui.components.EditableLabel.EditableLabel import EditableLabel
from app.gui.components.form.PayOptions import PayOptions
from app.gui.components.form.inputs.DateTimeInput import DateTimeInput
from app.gui.components.form.inputs.SelectBox import SelectBox
from app.gui.components.form.inputs.TextAreaInput import TextAreaInput
from app.gui.components.form.inputs.TextInput import TextInput
from app.gui.components.form.inputs.ToggleButtonSquare import ToggleButtonSquare
from PySide6.QtGui import QPalette, QColor, QPaintEvent
from app.storage import Storage

from app.types import TModel
from app.utils.mixins.ListMixin import ListMixin

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


class Form(QFrame, ListMixin):
    modified = Signal(bool, QFrame)

    def __init__(self, name: str, model: TModel, title: str) -> None:
        super(Form, self).__init__()

        self._name = name
        self._model = model
        self._title = title
        self._inputs: Sequence[TInput] = []
        self.setObjectName("Form")
        self.setContentsMargins(0, Storage.WIDGET_SPACING * 5, 0, 0)
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.setStyleSheet(
            """
            QFrame {
                background-color: #FFF
            }
        """
        )

        self._layout = QFormLayout()
        self._layout.setAlignment(Qt.AlignTop)
        self._layout.setSpacing(12)

        self.title = QLabel(self._title, self)
        self.title.setMinimumWidth(self.width())
        self.title.setContentsMargins(Storage.WIDGET_MARGINS)
        self.title.setStyleSheet(
            "background-color: #ababab; border-right:1px solid #333"
        )
        self.title.show()

        self.setLayout(self._layout)

    # https://stackoverflow.com/questions/19211828/using-any-and-all-to-check-if-a-list-contains-one-set-of-values-or-another
    def isModified(self):
        """Determines if any input element in the form has been modified"""
        return len(self.modifiedWidgets()) > 0

    def modifiedWidgets(self):
        """Returns any element in the form that has been modified"""
        return [w for w in self.inputs() if w.isModified()]

    def inputs(self) -> Sequence[TInput]:
        """Returns all form input elements"""
        return self._inputs

    def addRow(self, *fields: TInput | Sequence[TInput]):
        if len(fields) == 1:
            field = fields[0]

            self._addWidget(self._layout, field)
        else:
            hLayout = QHBoxLayout()
            hLayout.setContentsMargins(Storage.ZERO_MARGINS)

            row = QWidget()
            row.setLayout(hLayout)

            for field in fields:
                if not isinstance(field, QWidget):
                    continue

                layout = QFormLayout()
                self._addWidget(layout, field)
                hLayout.addLayout(layout)

            # Only set the first column's input's margin left to align all left most labels
            fields[0].getInput().setContentsMargins(Storage.WIDGET_SPACING, 0, 0, 0)
            fields[1].getLabel().setAlignment(Qt.AlignRight | Qt.AlignVCenter)

            self._layout.addRow(row)

    def _addWidget(self, layout: QFormLayout, field: TInput):
        if not isinstance(field, QWidget):
            return

        self._inputs.append(field)

        if hasattr(field, "modified"):
            field.modified.connect(lambda: self.modified.emit(self.isModified(), self))

        layout.addRow(field.getLabel(), field)

    def setTitle(self, title: str):
        self._title = title
        self.title.setText(title)

    def paintEvent(self, painter: QPaintEvent) -> None:
        maxWidth = 0

        for input in self.inputs():
            maxWidth = max(maxWidth, input.getLabel().width())

        for input in self.inputs():
            input.getLabel().setMinimumWidth(maxWidth)

        return super().paintEvent(painter)
