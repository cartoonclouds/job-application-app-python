from PySide6.QtWidgets import (
    QLabel,
    QFrame,
    QGridLayout,
)
from app.gui.components.form.inputs.TextInput import TextInput
from app.models import Model
from PySide6.QtCore import Qt


class Form(QFrame):
    def __init__(self, name: str, model: Model, title: str) -> None:
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

        self.setLayout(self._layout)

    # TODO rowspan and colspan
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
