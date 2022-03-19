# Standard Library
from enum import Enum, auto, unique
from typing import Any, Generic, Optional, TypeAlias, no_type_check, overload

# Framework imports
from PySide6.QtCore import (
    QAbstractItemModel,
    QAbstractListModel,
    QAbstractTableModel,
    QRegularExpression,
    Qt,
    QMargins,
    Signal,
)
from PySide6.QtGui import QFont, QRegularExpressionValidator
from PySide6.QtWidgets import QCompleter, QLabel, QVBoxLayout, QWidget, QHBoxLayout

# Application imports
from app.gui.components.models.ProfessionListModel import ProfessionListModel
from app.models.Profession import Profession
from app.storage import Storage
from app.types import T, TModel
from app.utils.mixins.ObjectMixin import ObjectMixin

WidgetModel: TypeAlias = (
    ProfessionListModel | QAbstractItemModel | QAbstractListModel | QAbstractTableModel
)

# https://stackoverflow.com/questions/4821104/dynamic-instantiation-from-string-name-of-a-class-in-dynamically-imported-module
class Input(Generic[T], QWidget, ObjectMixin):
    modified = Signal(bool)

    def __init__(self, component: T):
        super(Input, self).__init__()
        self.setObjectName("Input")

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(Storage.ZERO_MARGINS)
        self._layout.setSpacing(Storage.WIDGET_SPACING)

        self._input: T = component
        self._inputModel: Optional[WidgetModel] = None
        self._boundObject: Optional[TModel] = None
        self._boundProperty: Optional[str] = None
        self._updateProperty: Optional[str] = None

        self._label = Input.createLabel("", self._input)
        self._label.setParent(self)
        self._label.hide()

        self._layout.addWidget(self._input)

        self.setLayout(self._layout)

    def setAlignment(self, alignment: Qt.Alignment):
        self._layout.setAlignment(alignment)

    def contentsMargins(self) -> QMargins:
        return self._layout.contentsMargins()

    def setContentsMargins(self, margins: QMargins) -> None:
        return self._layout.setContentsMargins(margins)

    def hasModel(self) -> bool:
        return isinstance(self._inputModel, WidgetModel)

    def setModel(self, model: WidgetModel):
        self._inputModel = model
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

    def getInput(self) -> T:
        return self._input

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

    def isModified(self) -> bool:
        return NotImplementedError

    def setBinding(
        self,
        object: Any,
        property: str,
        updateProperty: str | None = None,
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
        value = value if value != None else ""

        if self.hasBoundUpdateProperty():
            updateObject = self._boundUpdateObject
            updateProperty = self._boundUpdateProperty
        elif self._boundProperty is not None:
            updateObject = self._boundObject
            updateProperty = self._boundProperty
        else:
            raise Exception("Bound object or property not set")

        # debug(updateObject, dict(zip([updateProperty], [value])))

        setattr(updateObject, updateProperty, value)

    @classmethod
    def createLabel(cls, text: str, input: T | QWidget) -> QLabel:
        label = QLabel(text)
        label.setBuddy(input)
        labelFont = label.font()
        labelFont.setPointSize(Storage.FORM_LABEL_SIZE)
        # labelFont.setCapitalization(QFont.SmallCaps)
        label.setFont(labelFont)

        return label

    # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QDataWidgetMapper.html
    #
    # TODO Use QDataWidgetMapper to map
