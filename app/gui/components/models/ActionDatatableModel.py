# Standard Library
import datetime
from typing import Any, Mapping, Sequence

# Framework imports
from PySide6.QtCore import QModelIndex, QPersistentModelIndex, Qt

# Application imports
from app.gui.components.datatable.DatatableModel import DatatableModel, ModelData
from app.models.Action import Action
from app.repositories.ActionRepository import ActionRepository


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

        actionRepo = ActionRepository()
        data: Sequence[Action] = actionRepo.values()

        super().__init__(data, columnHeaders)

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int) -> Any:
        modelData = self.getModelData(index)

        match role:
            case Qt.DisplayRole:
                return self._handleDisplayRole(modelData)

            case Qt.TextAlignmentRole:
                return self._handleTextAlignmentRole(modelData)

            # case Qt.DecorationRole:
            # case Qt.SizeHintRole:
            # case Qt.EditRole:
            # case Qt.ToolTipRole:
            # case Qt.StatusTipRole:
            # case Qt.WhatsThisRole:

    def _handleDisplayRole(self, modelData: ModelData) -> Any:
        assert isinstance(modelData.model, Action)
        model: Action = modelData.model

        # Perform per-type checks and render accordingly.
        if isinstance(modelData.value, datetime.datetime):
            # Render time to YYY-MM-DD.
            return modelData.value.strftime("%Y-%m-%d")

        if isinstance(modelData.value, float):
            # Render float to 2 dp
            # return "%.2f" % value
            return modelData.value

        if type(modelData.value) == bool:
            return

        return modelData.value

    def _handleTextAlignmentRole(self, modelData: ModelData) -> Any:
        if modelData.column == "id":
            return Qt.AlignCenter

        if type(modelData.value) == bool:
            return Qt.AlignCenter

        if isinstance(modelData.value, datetime.datetime):
            return Qt.AlignVCenter + Qt.AlignRight
