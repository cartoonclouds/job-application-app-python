
import typing
from PySide6.QtCore import Qt
from abc import ABC, abstractmethod
from dataclasses import dataclass

from app.models.Model import Model


@dataclass
class ModelData:
    column: str
    value: typing.Any


class ModelPresenter(ABC):
    """
        A datatable model presenter. Transforms a model to be viewable in a datatable.
    """

    def __init__(self, model: Model) -> None:
        self._model = model

    @property
    def columns(self):
        return self._model.getTableColumns()

    @property
    def columnCount(self):
        return self._model.getTableColumnCount()

    @abstractmethod
    def getFormattedAt(self, column: str, role: Qt.ItemDataRole) -> typing.Any:
        pass

    def __getattr__(self, name):
        return self._model.__getattr__(name)
