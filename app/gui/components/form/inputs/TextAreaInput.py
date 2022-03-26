# Framework imports
from typing import Type
from PySide6.QtCore import QMargins, Slot
from PySide6.QtGui import QFontMetrics, QTextDocument
from PySide6.QtWidgets import QPlainTextEdit

# Application imports
from app.gui.components.form.inputs.Input import Input
from app.models.Model import Model


class TextAreaInput(Input[QPlainTextEdit]):
    def __init__(self, label: str | None = None):
        super(TextAreaInput, self).__init__(QPlainTextEdit(), label)

    def setBinding(
        self,
        object: Model,
        property: str,
        updateProperty: str | None = None,
    ):
        super().setBinding(object, property, updateProperty)

        self.baseWidget.insertPlainText(self.boundValue())
        self.baseWidget.document().setModified(False)

        self.baseWidget.textChanged.connect(self._onTextChanged)

    @Slot(str)
    def _onTextChanged(self):
        assert self._boundObject is not None

        self.updateBoundObject(self.baseWidget.document().toPlainText())

    def setHeight(self, rows: int):
        document: QTextDocument = self.baseWidget.document()
        fontMetrics: QFontMetrics = self.baseWidget.fontMetrics()
        margins: QMargins = self.baseWidget.contentsMargins()

        height = (
            fontMetrics.lineSpacing() * rows
            + (document.documentMargin() + self.baseWidget.frameWidth()) * 2
            + margins.top()
            + margins.bottom()
        )

        self.baseWidget.setFixedHeight(int(height))
