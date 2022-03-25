
# Framework imports
from PySide6.QtCore import QMargins, Slot
from PySide6.QtGui import QFontMetrics, QTextDocument
from PySide6.QtWidgets import QPlainTextEdit

# Application imports
from app.gui.components.form.inputs.Input import Input
from app.models.Model import Model


class TextAreaInput(Input[QPlainTextEdit]):
    def __init__(self, label: str | None = None):
        super(TextAreaInput, self).__init__(QPlainTextEdit(), str(label))

        if label is not None:
            self.setLabel(label)

    def setBinding(
        self,
        object: Model,
        property: str,
        updateProperty: str | None = None,
    ):
        self._boundObject = object
        self._boundProperty = property

        self._input.insertPlainText(getattr(self._boundObject, self._boundProperty))
        self._input.document().setModified(False)

        self._input.textChanged.connect(self._onTextChanged)

    @Slot(str)
    def _onTextChanged(self):
        assert self._boundObject is not None
        self.updateBoundObject(self._boundObject, self._input.document().toPlainText())

    def setHeight(self, rows: int):
        document: QTextDocument = self._input.document()
        fontMetrics: QFontMetrics = self._input.fontMetrics()
        margins: QMargins = self._input.contentsMargins()

        height = (
            fontMetrics.lineSpacing() * rows
            + (document.documentMargin() + self._input.frameWidth()) * 2
            + margins.top()
            + margins.bottom()
        )

        self._input.setFixedHeight(int(height))
