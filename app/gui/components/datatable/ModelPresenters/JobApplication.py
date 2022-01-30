
from dataclasses import dataclass
import datetime
import typing
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from app.gui.components.datatable.DatatableModel import DatatableModel
# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTableWidgetItem.html

from app.models.JobApplication import JobApplication
from app.types import ColumnHeaders


@dataclass
class ModelData:
    column: str
    model: JobApplication
    value: typing.Any


class JobApplicationDatatableModel(DatatableModel):
    """
    A datatable model for Job Applications.
    """

    def __init__(self, data: typing.Sequence[JobApplication], columnHeaders: ColumnHeaders) -> None:
        super().__init__(data, columnHeaders)

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int) -> typing.Any:
        colIdx = index.column()
        rowIdx = index.row()
        jobApp: JobApplication = self._data[rowIdx]
        colName = self._columns[colIdx]

        details = ModelData(colName, jobApp, getattr(jobApp, colName))

        match role:
            case Qt.DisplayRole:
                return self._handleDisplayRole(details)

            case Qt.DecorationRole:
                return self._handleDecorationRole(details)

            # case Qt.EditRole:
            # case Qt.ToolTipRole:
            # case Qt.StatusTipRole:
            # case Qt.WhatsThisRole:

            case Qt.TextAlignmentRole:
                return self._handleTextAlignmentRole(details)

            case Qt.SizeHintRole:
                return self._handleSizeHintRole(details)

    def _handleDisplayRole(self, details: ModelData):
        # Perform per-type checks and render accordingly.
        if isinstance(details.value, datetime.datetime):
            # Render time to YYY-MM-DD.
            return details.value.strftime("%Y-%m-%d")

        if isinstance(details.value, float):
            # Render float to 2 dp
            # return "%.2f" % value
            return details.value

        if type(details.value) == bool:
            return

        if details.column == "job_id":
            return details.model.job.displayLabel()

        if details.column == "company_id":
            return details.model.company.displayLabel()

        return details.value

    def _handleTextAlignmentRole(self, details: ModelData):
        if details.column == "id":
            return Qt.AlignCenter

        if type(details.value) == bool:
            return Qt.AlignCenter

        if isinstance(details.value, datetime.datetime):
            return Qt.AlignVCenter + Qt.AlignRight

    def _handleSizeHintRole(self, details: ModelData):
        pass

    def _handleDecorationRole(self, details: ModelData):
        pass
