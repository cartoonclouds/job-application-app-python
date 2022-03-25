# Standard Library
from typing import Any, Generic, Type

# Framework imports
from PySide6.QtCore import QMargins, Qt, Signal
from PySide6.QtWidgets import QCompleter, QHBoxLayout, QLabel, QWidget

# Third party imports
from inflection import parameterize

# Application imports
from app.constants import WIDGET_SPACING, ZERO_MARGINS
from app.models.Model import Model
from app.typings.types import T
from app.utils.mixins.ObjectMixin import ObjectMixin
from app.utils.object_functions import formatObjectName

# QInputWidget = TypeVar(
#     "QInputWidget",
#     QComboBox,
#     QPlainTextEdit,
#     QLineEdit,
#     QDateTimeEdit,
#     QPushButton,
#     QDoubleSpinBox,
#     QCheckBox,
# )

# T = built-in component type
# _boundObject / M = database model type
# component = custom component type


# https://stackoverflow.com/questions/4821104/dynamic-instantiation-from-string-name-of-a-class-in-dynamically-imported-module
class Input(Generic[T], QWidget, ObjectMixin):
    modified = Signal(bool)

    # make ABC
    # in constrcutor pass in boundObject[M] and boundProperty[str]
    # overload constrcutor pass in boundObject[M] and boundProperty[str] with (updateObject?) updateProperty

    def __init__(self, component: T, objectName: str):
        super(Input, self).__init__()
        self.setObjectName(
            formatObjectName(
                __class__.__name__,
                type(self).__name__,
                type(component).__name__,
                parameterize(objectName or "", "_").lower(),
            )
        )
        
        # TODO Get list of all subclasses of this instance to
        # generate object name
        # https://stackoverflow.com/questions/1401661/list-all-base-classes-in-a-hierarchy-of-given-class
        # "How to get the entire inheritance tree"

        self._layout = QHBoxLayout()
        self._layout.setAlignment(Qt.AlignTop)
        self._layout.setContentsMargins(ZERO_MARGINS)
        self._layout.setSpacing(WIDGET_SPACING)

        self._input = component
        self._boundObject: Type[Model] | None = None
        self._boundProperty: str | None = None
        self._updateProperty: str | None = None

        self._label = self.createLabel("")
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

    def getInput(self):
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
        assert self._boundObject is not None
        return self._boundObject.is_dirty()

    def setBinding(
        self,
        object: Type[Model],
        property: str,
        updateProperty: str | None = None,
    ) -> None:
        raise NotImplementedError

    def setUpdateBinding(self, object: Type[Model], property: str):
        self._boundUpdateObject = object
        self._boundUpdateProperty = property

    # Type guard here?
    def hasBoundUpdateProperty(self) -> bool:
        return self.attrexists("_boundUpdateProperty") and self.attrexists(
            "_boundUpdateObject"
        )

    def updateBoundObject(self, updateObject: Type[Model], value: Any):
        assert self._boundObject is not None
        value = value if value != None else ""

        if self.hasBoundUpdateProperty():
            updateObject = self._boundUpdateObject
            updateProperty = self._boundUpdateProperty
        elif self._boundProperty is not None:
            updateObject = self._boundObject
            updateProperty = self._boundProperty
        else:
            raise Exception("Bound object or property not set")

        debug(updateObject, dict(zip([updateProperty], [value])))

        setattr(updateObject, updateProperty, value)
        
        self.modified.emit(self.isModified())

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
