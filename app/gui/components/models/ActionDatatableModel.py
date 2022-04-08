# Standard Library
import datetime
from typing import Any, Mapping, Sequence, Type

# Framework imports
from PySide6.QtCore import QModelIndex, QPersistentModelIndex, Qt

# Application imports
from app.gui.components.datatable.DatatableModel import DatatableModel, ModelData
from app.models.Action import Action
from app.repositories.action_repository import ActionRepository


class ActionDatatableModel(DatatableModel[Action]):
    """A datatable model for Actions.

    URL: https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTableWidgetItem.html
    """

    def __init__(self) -> None:
        columnHeaders: Mapping[str, str] = dict(
            zip(
                [
                    "id",
                    "title",
                ],
                [
                    "ID",
                    "Title",
                ],
            )
        )

        data = ActionRepository.items()

        super().__init__(data, columnHeaders)
