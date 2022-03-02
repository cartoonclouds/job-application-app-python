from typing import Any, Sequence, TypeVar, Generic
from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex, QPersistentModelIndex

from app.models.Profession import Profession
from app.models.Job import Job


M = TypeVar("M", Profession, Job)


class ListModel(Generic[M], QAbstractListModel):
    def __init__(self, parentWidget, data: Sequence[M], *args, **kwargs):
        super(ListModel, self).__init__(*args, **kwargs)

        self._data: Sequence[M] = data

        self.setParentList(parentWidget)

    def setParentList(self, parentWidget):
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

    def __getitem__(self, __name: str) -> Any:
        if isinstance(__name, int):
            return self._data[__name]

        return super().__getattribute__(__name)
