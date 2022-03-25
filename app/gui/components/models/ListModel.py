# Standard Library
from typing import Any, Generic, Sequence

# Framework imports
from PySide6.QtCore import QAbstractListModel, QModelIndex, QPersistentModelIndex, Qt

# Application imports
from app.gui.components.form.inputs.SelectBox import SelectBox
from app.typings.types import M


class ListModel(Generic[M], QAbstractListModel):
    def __init__(
        self, parentWidget: SelectBox, data: Sequence[M], *args: Any, **kwargs: Any
    ):
        super(ListModel, self).__init__(*args, **kwargs)

        self._data: Sequence[M] = data
        self._parentWidget: SelectBox = parentWidget

    def setParentList(self, parentWidget: SelectBox):
        self._parentWidget = parentWidget

    def rowCount(
        self, parent: QModelIndex | QPersistentModelIndex | None = None
    ) -> int:
        return len(self._data)

    @property
    def rawData(self):
        return self._data

    def findIndex(self, value: str) -> int:
        res1: int = self._parentWidget.findText(value, Qt.MatchWildcard)
        res2: int = self._findIndexContains(value)

        return res1 if res1 >= 0 else res2

    def _findIndexContains(self, value: str) -> int:
        return self._parentWidget.findText(value, Qt.MatchContains)

    def findItem(self, value: str) -> M:
        itemIndex = self.findIndex(value)

        return self.rawData[itemIndex]

    def getAt(self, index: int) -> M:
        return self._data[index]
