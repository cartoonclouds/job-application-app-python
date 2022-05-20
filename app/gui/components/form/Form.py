# Standard Library
from typing import Type, TypeAlias, overload

# Framework imports
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPaintEvent
from PySide6.QtWidgets import (
    QFormLayout,
    QFrame,
    QHBoxLayout,
    QLabel,
    QWidget,
    QSpacerItem,
    QSizePolicy,
)

# Application imports
from app.constants import WIDGET_MARGINS, WIDGET_SPACING, ZERO_MARGINS
from app.gui.components.EditableLabel.EditableLabel import EditableLabel
from app.gui.components.form.inputs.DateTimeInput import DateTimeInput
from app.gui.components.form.inputs.SelectBox import SelectBox
from app.gui.components.form.inputs.TextAreaInput import TextAreaInput
from app.gui.components.form.inputs.TextInput import TextInput
from app.gui.components.form.inputs.ToggleButtonSquare import ToggleButtonSquare
from app.gui.components.form.PayOptions import PayOptions
from app.models.Model import Model
from app.typings.types import InputT
from app.utils.object_functions import format_object_name

# Third party imports
from inflection import parameterize

# Validator https://docs.python-cerberus.org/en/stable/


class Form(QFrame):
    modified = Signal(bool, QFrame)

    def __init__(self, name: str, model: Model, title: str) -> None:
        super().__init__()

        self.setObjectName(
            format_object_name(
                __class__.__name__,
                type(self).__name__,
                parameterize(title or "", "_").lower(),
            )
        )
        self.setContentsMargins(0, WIDGET_SPACING * 5, 0, 0)
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)

        # self.setStyleSheet(
        #     """
        #     QFrame {
        #         background-color: #FFF
        #     }
        # """
        # )

        self._name = name
        self._model = model
        self._title = title
        self._inputs: list[InputT] = []

        self._layout = QFormLayout()
        self._layout.setAlignment(Qt.AlignTop)
        # self._layout.setSpacing(WIDGET_SPACING * 2)

        self.title = QLabel(self._title, self)
        self.title.setContentsMargins(WIDGET_MARGINS)
        self.title.setStyleSheet(
            "background-color: #fff; border:1px solid #999; border-width: 1px 1px 0 1px;"
        )
        self.title.show()

        self.setLayout(self._layout)

    # https://stackoverflow.com/questions/19211828/using-any-and-all-to-check-if-a-list-contains-one-set-of-values-or-another
    def isModified(self) -> bool:
        """Determines if any input element in the form has been modified"""
        return len(self.modifiedWidgets()) > 0

    def modifiedWidgets(self):
        """Returns any element in the form that has been modified"""
        return [w for w in self.inputs() if w.isModified()]

    def inputs(self) -> list[InputT]:
        """Returns all form input elements"""
        return self._inputs

    def addVerticalExpander(self):
        spacer = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self._layout.addItem(spacer)

    def addRow(self, *fields: InputT | list[InputT]):
        if len(fields) == 1:
            field = fields[0]
            assert not isinstance(field, list)

            self._addWidget(self._layout, field)
        else:
            hLayout = QHBoxLayout()
            hLayout.setContentsMargins(ZERO_MARGINS)

            row = QWidget()
            row.setLayout(hLayout)
            row.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

            for index, field in enumerate(fields):
                if not isinstance(field, QWidget):
                    continue

                layout = QFormLayout()
                layout.setContentsMargins(ZERO_MARGINS)
                self._addWidget(layout, field)
                hLayout.addLayout(layout)

                # Set columns > 1 label right aligned
                if index > 0:
                    field.get_label().setAlignment(Qt.AlignRight | Qt.AlignVCenter)

            self._layout.addRow(row)

    def _addWidget(self, layout: QFormLayout, field: InputT):
        self._inputs.append(field)

        if hasattr(field, "modified"):
            field.modified.connect(lambda: self.modified.emit(self.isModified(), self))

        layout.addRow(field.get_label(), field)

    def setTitle(self, title: str):
        self._title = title
        self.title.setText(title)

    def paintEvent(self, painter: QPaintEvent) -> None:  # type: ignore[override]
        maxWidth = 0

        for input in self.inputs():
            maxWidth = max(maxWidth, input.get_label().width())

        for input in self.inputs():
            input.get_label().setMinimumWidth(maxWidth)

        return super().paintEvent(painter)
