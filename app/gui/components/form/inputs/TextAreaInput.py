# Framework imports
from PySide6.QtCore import Slot
from PySide6.QtGui import QFontMetrics, QTextDocument
from PySide6.QtWidgets import QPlainTextEdit

# Application imports
from app.gui.components.form.inputs.Input import Input
from app.models.Model import Model


class TextAreaInput(Input[QPlainTextEdit], QPlainTextEdit):
    def __init__(self, label: str | None = None):
        super().__init__(label)
        

    def setBinding(
        self,
        object: Model,
        property: str,
        updateProperty: str | None = None,
    ):
        super().setBinding(object, property, updateProperty)

        self.insertPlainText(self.boundValue())
        self.document().setModified(False)

        self.textChanged.connect(self._onTextChanged)

    @Slot(str)
    def _onTextChanged(self):
        assert self._boundObject is not None

        self.updateBoundObject(self.document().toPlainText())

    def setHeight(self, rows: int):
        document: QTextDocument = self.document()
        fontMetrics: QFontMetrics = self.fontMetrics()
        # margins: QMargins = self.contentsMargins()
        # + margins.top()
        # + margins.bottom()

        height = (
            fontMetrics.lineSpacing() * rows
            + (document.documentMargin() + self.frameWidth()) * 2
        )

        self.setFixedHeight(int(height))
