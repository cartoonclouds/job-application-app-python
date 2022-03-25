# Framework imports
from PySide6.QtCore import Qt, Signal, QSize
from PySide6.QtGui import (
    QFont,
    QPixmap,
    QResizeEvent,
    QScreen,
    QGuiApplication,
    QPalette,
)
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QWidget,
    QApplication,
    QSizePolicy,
)

# Application imports
from app.gui.components.EditableLabel.EditableLabel import EditableLabel
from app.constants import WIDGET_SPACING, WIDGET_MARGINS, ZERO_MARGINS
from app.utils.object_functions import formatObjectName
from inflection import parameterize


class TabHeader(QWidget):
    textChanged = Signal(str)

    def __init__(
        self, text: str, icon: QPixmap | None = None, editable: bool = False
    ) -> None:
        super().__init__()
        self.setObjectName(
            formatObjectName(
                __class__.__name__,
                parameterize(text or "", "_").lower(),
            )
        )

        self._text = text
        self._editable = editable
        self._icon = icon

        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.setContentsMargins(ZERO_MARGINS)

        self.label = self.createLabel(text)

        if isinstance(icon, QPixmap) and not self._editable:
            iconLabel = self.createIcon(icon)
            layout.addWidget(iconLabel)

        layout.addWidget(self.label)
        self.setLayout(layout)

    def setText(self, text: str):
        self._text = text
        self.label.setText(text)

    def createLabel(self, text: str):
        if self._editable:
            # create the editable label
            label = EditableLabel(text, icon=self._icon)

            # connect our custom signal
            label.textChanged.connect(lambda t: self.textChanged.emit(t))
        else:
            label = QLabel(text)

        label.setFont(QFont(["Helvetica", "SansSerif"], 18))

        return label

    def createIcon(self, icon: QPixmap) -> QLabel:
        labelIcon = QLabel("")
        labelIcon.setPixmap(icon)

        return labelIcon
