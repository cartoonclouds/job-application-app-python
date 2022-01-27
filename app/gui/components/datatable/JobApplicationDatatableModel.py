
from datetime import datetime
import inflection
from typing import Any, Union
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from app.gui.components.datatable.DatatableModel import DataTableData, DatatableModel
from app.models.Model import Model
from app.repositories.Repository import Repository
from app.utilities.IconUtility import IconUtility
from app.utilities.StringUtility import StringUtility


class JobApplicationDataTableModel(DatatableModel):
    """A datatable model representing Job Applications.

    URL: https://doc.qt.io/qtforpython/PySide6/QtCore/QAbstractTableModel.html

    Attributes:
        data (Repository): A diciontary holding the Job Application data
    """

    def __init__(self, data: Repository):
        super(JobApplicationDataTableModel, self).__init__()

        self._data = data

        # Generate headers
        self.setHeaders(
            list(map(lambda c: inflection.titleize(c), self._data.get_columns())))

    def data(self, index: Union[QModelIndex, QPersistentModelIndex], role: int) -> Any:
        column = index.column()
        row = index.row()
        model: Model = self._data.get_at_index(row)
        columnName = model.get_table_columns()[column]
        value = getattr(model, columnName)

        details = DataTableData(
            index.column(),
            index.row(),
            index,
            model,
            columnName,
            value
        )

        if role == Qt.DisplayRole:
            return self._handle_display_role(details)
        elif role == Qt.TextAlignmentRole:
            return self._handle_text_alignment_role(details)
        elif role == Qt.DecorationRole:
            return self._handle_decoration_role(details)
        # elif role == Qt.SizeHintRole:
        #     return self._handle_size_hint_role(details)

    # def _handle_size_hint_role(self, details: DataTableData):
    #     pass

    def _handle_decoration_role(self, details: DataTableData):
        if type(details.value) == bool:
            if details.value:
                return IconUtility.get_icon("tick-32")
            else:
                return IconUtility.get_icon("tick-32")

    def _handle_display_role(self, details: DataTableData):
        # Perform per-type checks and render accordingly.
        if isinstance(details.value, datetime):
            # Render time to YYY-MM-DD.
            return details.value.strftime("%Y-%m-%d")

        if isinstance(details.value, float):
            # Render float to 2 dp
            # return "%.2f" % value
            return details.value

        if type(details.value) == bool:
            if details.value:
                return IconUtility.get_icon("tick-32")
            else:
                return IconUtility.get_icon("tick-32")

        if details.columnName == "job_id":
            return details.model.job.display_label()

        if details.columnName == "company_id":
            return details.model.company.display_label()

        return details.value

    def _handle_text_alignment_role(self, details: DataTableData):
        if details.column == 0:
            return Qt.AlignCenter

        if type(details.value) == bool:
            return Qt.AlignCenter

        if isinstance(details.value, datetime):
            return Qt.AlignVCenter + Qt.AlignRight
