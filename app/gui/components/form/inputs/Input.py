# Standard Library
from abc import ABC, abstractmethod, abstractproperty
import inspect
from typing import Any, Dict, Generic, Type, TypeVar

# Framework imports
from PySide6.QtCore import QMargins, Qt, Signal
from PySide6.QtWidgets import QCompleter, QHBoxLayout, QLabel, QWidget

# Third party imports
from inflection import parameterize

# Application imports
from app.constants import WIDGET_SPACING, ZERO_MARGINS
from app.utils.mixins.bindable import Bindable
from app.utils.object_functions import format_object_name

I = TypeVar("I", bound=QWidget, covariant=True)


class InputAbstract(ABC):
    pass


class Input(Generic[I], Bindable):
    # https://stackoverflow.com/questions/9575409/calling-parent-class-init-with-multiple-inheritance-whats-the-right-way
    modified = Signal(bool)

    # @overload

    def __init__(self, label: str | None = None) -> None:
        super().__init__()

        # self.setObjectName(
        #     formatObjectName(
        #         __class__.__name__,
        #         type(self).__name__,
        #         type(baseWidget).__name__,
        #         parameterize(name or "", "_").lower(),
        #     )
        # )
        #         # self._layout.setAlignment(Qt.AlignTop)
        #         # self._layout.setContentsMargins(ZERO_MARGINS)
        #         # self._layout.setSpacing(WIDGET_SPACING)

        if label is not None:
            self.set_label(label)

    @property
    def label(self) -> QLabel:
        return self._label

    @label.setter
    def label(self, label: QLabel | str):
        if isinstance(label, QLabel):
            self._label = label
        else:
            self._label = self.set_label(label)

    def set_label(self, label: str):
        if isinstance(label, QLabel):
            self.label.setText(label)
        else:
            self.label = self.create_label(label)
            self.label.setParent(self)

        self.label.show()

        return self.label

    def get_label(self) -> QLabel:
        return self._label

    def create_label(self, text: str) -> QLabel:
        label = QLabel(text)
        label.setBuddy(self)
        labelFont = label.font()
        # labelFont.setPointSize(FORM_LABEL_SIZE)
        # labelFont.setCapitalization(QFont.SmallCaps)
        label.setFont(labelFont)

        return label

    # #### TOFIX Not available for all
    def configureCompleter(self, completer: QCompleter):
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)
        self.setCompleter(completer)

    # def setInputMask(self, mask: str):
    # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLineEdit.html#PySide6.QtWidgets.PySide6.QtWidgets.QLineEdit.setInputMask

    # def setValidator(self, v):
    #     pass
    # https://doc.qt.io/qtforpython/PySide6/QtGui/QValidator.html
    # https://doc.qt.io/qtforpython/PySide6/QtGui/QRegularExpressionValidator.html
    # https://doc.qt.io/qtforpython/PySide6/QtCore/QRegularExpression.html
    # QRegExp, QRegExpValidator
    # validator = QRegularExpressionValidator(QRegularExpression("[0-9A-Fa-f]{6}"))
    # self._baseWidget.setValidator(validator)

    # self.qle.editingFinished.connect(self.onEditingFinished)


#         # TODO Get list of all subclasses of this instance to
#         # generate object name
#         # https://stackoverflow.com/questions/1401661/list-all-base-classes-in-a-hierarchy-of-given-class
#         # "How to get the entire inheritance tree"

#     # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QDataWidgetMapper.html
#     #
#     # TODO Use QDataWidgetMapper to map
