# Standard Library
import abc
import typing
from abc import abstractmethod
from enum import Enum, auto, unique
from typing import Any, Generic, TypeAlias, TypeVar, cast, no_type_check, overload
import logging

# Framework imports
from PySide6.QtCore import (
    QAbstractItemModel,
    QAbstractListModel,
    QAbstractTableModel,
    Qt,
    QRegularExpression,
)
from PySide6.QtGui import (
    QFont,
    QMovie,
    QPixmap,
    QPalette,
    QColor,
    QRegularExpressionValidator,
)
from PySide6.QtWidgets import (
    QComboBox,
    QDateTimeEdit,
    QLabel,
    QLineEdit,
    QPlainTextEdit,
    QVBoxLayout,
    QWidget,
    QCompleter,
)

# Application imports
from app.gui.components.models.ProfessionListModel import ProfessionListModel
from app.models import Model
from app.models.Profession import Profession
from app.types import T
from app.utilities.mixins.ObjectMixin import ObjectMixin

WidgetModel: TypeAlias = (
    ProfessionListModel | QAbstractItemModel | QAbstractListModel | QAbstractTableModel
)


@unique
class UpdateEvent(Enum):
    Change = auto()
    Enter = auto()


# https://stackoverflow.com/questions/4821104/dynamic-instantiation-from-string-name-of-a-class-in-dynamically-imported-module
class Input(Generic[T], QWidget, ObjectMixin):
    def __init__(self, component: T):
        super(Input, self).__init__()

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)

        self._input: T = component
        self._boundObject: None | Model = None
        self._boundProperty: None | str = None
        self._updateProperty: None | str = None
        self._updateEvent: UpdateEvent = UpdateEvent.Change

        self._label = QLabel()
        self._label.setBuddy(self._input)
        self._label.hide()
        labelFont = self._label.font()
        labelFont.setPointSize(11)
        labelFont.setCapitalization(QFont.SmallCaps)
        self._label.setFont(labelFont)

        self._layout.addWidget(self._label)
        self._layout.addWidget(self._input)

        self.setLayout(self._layout)

    def setModel(self, model: WidgetModel):
        self._input.setModel(model)

    @property
    @no_type_check
    def dataModel(self) -> WidgetModel:
        return self._input.model()
        # if hasattr(self._input, "model") and isinstance(
        #     self._input.model(), QAbstractListModel
        # ):
        #     return cast(QAbstractListModel, self._input.model())
        # else:
        #     return None

    def setLabel(self, label: str):
        self._label.setText(label)
        self._label.show()

    def getLabel(self) -> QLabel | None:
        return self._label

    def setPlaceholderText(self, text: str):
        self._input.setPlaceholderText(text)

    def setCompleter(self, completer: QCompleter):
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)
        self._input.setCompleter(completer)

    def setInputMask(self, mask: str):
        # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLineEdit.html#PySide6.QtWidgets.PySide6.QtWidgets.QLineEdit.setInputMask
        self._input.setInputMask(mask)

    def setValidator(self, v):
        pass
        # https://doc.qt.io/qtforpython/PySide6/QtGui/QValidator.html
        # https://doc.qt.io/qtforpython/PySide6/QtGui/QRegularExpressionValidator.html
        # https://doc.qt.io/qtforpython/PySide6/QtCore/QRegularExpression.html
        # QRegExp, QRegExpValidator
        # validator = QRegularExpressionValidator(QRegularExpression("[0-9A-Fa-f]{6}"))
        # self._input.setValidator(validator)

        # self.qle.editingFinished.connect(self.onEditingFinished)

    def setBinding(
        self,
        object: Any,
        property: str,
        updateProperty: str | None = None,
        updateEvent: UpdateEvent = UpdateEvent.Change,
    ) -> None:
        raise NotImplementedError

    def setUpdateBinding(self, object: Any, property: str):
        self._boundUpdateObject = object
        self._boundUpdateProperty = property

    def hasBoundUpdateProperty(self) -> bool:
        return self.attrexists("_boundUpdateProperty") and self.attrexists(
            "_boundUpdateObject"
        )

    def updateBoundObject(self, updateObject: Profession, value: Any):
        if self.hasBoundUpdateProperty():
            updateObject = self._boundUpdateObject
            updateProperty = self._boundUpdateProperty
        else:
            updateObject = self._boundObject
            updateProperty = self._boundProperty

        updateArgs = dict(zip([updateProperty], [value]))

        debug(updateObject, updateArgs)

        setattr(updateObject, updateProperty, value)

    # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QDataWidgetMapper.html
    #
    # TODO Use QDataWidgetMapper to map
