from abc import abstractmethod
import abc
from typing import Any, TypeAlias, cast, no_type_check, overload
from enum import Enum, unique, auto
import typing
from PySide6.QtGui import QPixmap, QMovie, QFont
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QPlainTextEdit,
    QComboBox,
    QDateTimeEdit,
)
from PySide6.QtCore import (
    QAbstractListModel,
    QAbstractItemModel,
    QAbstractTableModel,
)
from typing import TypeVar, Generic
from app.gui.components.models.ProfessionListModel import ProfessionListModel

from app.models import Model

T = TypeVar("T", QComboBox, QPlainTextEdit, QLineEdit, QDateTimeEdit)

WidgetModel: TypeAlias = (
    ProfessionListModel | QAbstractItemModel | QAbstractListModel | QAbstractTableModel
)


@unique
class UpdateEvent(Enum):
    Change = auto()
    Enter = auto()


# https://stackoverflow.com/questions/4821104/dynamic-instantiation-from-string-name-of-a-class-in-dynamically-imported-module
class Input(Generic[T], QWidget):
    def __init__(self, component: T):
        super(Input, self).__init__()

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)

        self._input: T = component
        self._boundObject: None | Model = None
        self._boundProperty: None | str = None
        self._updatePropery: None | str = None
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
    def dataModel(self) -> None | WidgetModel:
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

    def setBinding(
        self,
        object: Any,
        property: str,
        updatePropery: str | None = None,
        updateEvent: UpdateEvent = UpdateEvent.Change,
    ) -> None:
        raise NotImplementedError

    def getBinding(self):
        return [self._boundObject, self._boundProperty]

    def hasBoundProperty(self) -> bool:
        return self._boundObject != None and self._boundProperty != None

    def updateBoundObject(self, value: Any):
        if self.hasBoundProperty:
            isRelation = callable(getattr(self._boundObject, self._boundProperty))

            if isRelation:
                updateArgs = dict(zip([self._boundProperty], [value]))

                self._boundObject.update(updateArgs)
            else:
                setattr(
                    self._boundObject,
                    self._boundProperty,
                    value,
                )
        else:
            setattr(self._boundObject, self._boundProperty, value)
