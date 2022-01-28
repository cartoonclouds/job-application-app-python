
import typing
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

    @abstractmethod
    def getFormattedAt(self, column: str, role) -> typing.Any:
        pass
