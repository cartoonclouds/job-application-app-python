import datetime

from typing import Mapping, Any, Sequence
from app.gui.components.datatable.models.DatatableModel import DatatableModel, ModelData
from app.models.JobApplication import JobApplication
from PySide6.QtCore import QModelIndex, QPersistentModelIndex, Qt

# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTableWidgetItem.html


class JobApplicationDatatableModel(DatatableModel):
    """A datatable model for Job Applications."""

    def __init__(
        self, data: Sequence[JobApplication], columnHeaders: Mapping[str, str]
    ) -> None:
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
        model: JobApplication = modelData.model

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

        if modelData.column == "job":
            return model.job.displayLabel()

        if modelData.column == "company":
            return model.company.displayLabel()

        return modelData.value

    def _handleTextAlignmentRole(self, modelData: ModelData) -> Any:
        if modelData.column == "id":
            return Qt.AlignCenter

        if type(modelData.value) == bool:
            return Qt.AlignCenter

        if isinstance(modelData.value, datetime.datetime):
            return Qt.AlignVCenter + Qt.AlignRight
