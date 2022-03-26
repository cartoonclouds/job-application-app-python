# Standard Library
from typing import Any, Generic

# Framework imports
from PySide6.QtCore import QMargins, Qt, Signal
from PySide6.QtWidgets import QCompleter, QHBoxLayout, QLabel, QWidget

# Third party imports
from inflection import parameterize

# Application imports
from app.constants import WIDGET_SPACING, ZERO_MARGINS
from app.typings.types import PySide6Input
from app.utils.mixins.bindable import Bindable
from app.utils.object_functions import formatObjectName


# https://stackoverflow.com/questions/4821104/dynamic-instantiation-from-string-name-of-a-class-in-dynamically-imported-module
class Input(Generic[PySide6Input], QWidget, Bindable):
    modified = Signal(bool)

    # make ABC

    def __init__(self, baseWidget: PySide6Input, label: str | None = None):
        super(Input, self).__init__()
        self.setObjectName(
            formatObjectName(
                __class__.__name__,
                type(self).__name__,
                type(baseWidget).__name__,
                parameterize(label or "", "_").lower(),
            )
        )

        # TODO Get list of all subclasses of this instance to
        # generate object name
        # https://stackoverflow.com/questions/1401661/list-all-base-classes-in-a-hierarchy-of-given-class
        # "How to get the entire inheritance tree"

        self._baseWidget = baseWidget

        self._label: QLabel | None = None

        if label is not None:
            self.setLabel(label)

        self._layout = QHBoxLayout()
        self._layout.setAlignment(Qt.AlignTop)
        self._layout.setContentsMargins(ZERO_MARGINS)
        self._layout.setSpacing(WIDGET_SPACING)
        self._layout.addWidget(self.baseWidget)

        self.setLayout(self._layout)

    @property
    def baseWidget(self) -> PySide6Input:
        return self._baseWidget

    def setAlignment(self, alignment: Qt.Alignment):
        self._layout.setAlignment(alignment)

    def contentsMargins(self) -> QMargins:
        return self._layout.contentsMargins()

    def setContentsMargins(self, margins: QMargins) -> None:  # type: ignore[override]
        return self._layout.setContentsMargins(margins)

    def updateBoundObject(self, value: Any):
        super().updateBoundObject(value)

        self.modified.emit(self.isModified())

    def setLabel(self, label: str):
        if self._label is None:
            self._label = self.createLabel(label)
            self._label.setParent(self)
        else:
            self._label.setText(label)

        self._label.show()

    def getLabel(self) -> QLabel | None:
        return self._label

    def createLabel(self, text: str) -> QLabel:
        label = QLabel(text)
        label.setBuddy(self)
        labelFont = label.font()
        # labelFont.setPointSize(FORM_LABEL_SIZE)
        # labelFont.setCapitalization(QFont.SmallCaps)
        label.setFont(labelFont)

        return label

    # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QDataWidgetMapper.html
    #
    # TODO Use QDataWidgetMapper to map

    # #### TOFIX Not available for all
    def setPlaceholderText(self, text: str):
        self.baseWidget.setPlaceholderText(text)

    def setCompleter(self, completer: QCompleter):
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)
        self.baseWidget.setCompleter(completer)

    def setInputMask(self, mask: str):
        # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLineEdit.html#PySide6.QtWidgets.PySide6.QtWidgets.QLineEdit.setInputMask
        self.baseWidget.setInputMask(mask)

    def setValidator(self, v):
        pass
        # https://doc.qt.io/qtforpython/PySide6/QtGui/QValidator.html
        # https://doc.qt.io/qtforpython/PySide6/QtGui/QRegularExpressionValidator.html
        # https://doc.qt.io/qtforpython/PySide6/QtCore/QRegularExpression.html
        # QRegExp, QRegExpValidator
        # validator = QRegularExpressionValidator(QRegularExpression("[0-9A-Fa-f]{6}"))
        # self._baseWidget.setValidator(validator)

        # self.qle.editingFinished.connect(self.onEditingFinished)
