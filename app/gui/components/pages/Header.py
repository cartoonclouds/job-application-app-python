from PySide6.QtWidgets import (
    QLabel,
    QHBoxLayout,
    QWidget,
    QFrame,
    QPlainTextEdit,
    QLayout,
)
from PySide6.QtGui import QFont, QFontMetrics
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QSizePolicy
from app.gui.components.EditableLabel.EditableLabel import EditableLabel

from app.utilities.IconUtility import IconUtility


class Header(QFrame):
    def __init__(self, text: str, editable: bool = False) -> None:
        super().__init__()

        self._text = text
        self._icon = IconUtility.getFileIconAsPixmap("gear")

        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)

        self.setEditable(editable)

        label = self.createLabel(text)

        icon = QLabel("")
        icon.setPixmap(self._icon)

        layout.addWidget(icon)
        layout.addWidget(label)

    def createLabel(self, text: str):
        if self._editable:
            # create the editable label
            label = EditableLabel(text)
            # connect our custom signal
            label.textChanged.connect(self.labelTextChangedAction)
        else:
            label = QLabel(text)

        label.setFont(QFont(["Helvetica", "SansSerif"], 18))

        fontMetrics: QFontMetrics = label.fontMetrics()
        textSize: QSize = fontMetrics.size(0, label.text())
        self.setMaximumHeight(textSize.height())

        return label

    def setEditable(self, editable: bool):
        self._editable = editable

    def labelTextChangedAction(self, text):
        debug('# label updated: "{0}"'.format(text))
