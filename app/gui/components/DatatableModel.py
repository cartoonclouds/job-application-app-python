

from datetime import datetime
import inflection
from typing import Any, Union
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from app.models.Model import Model
from app.repositories.IRepository import Repository


class DataTableModel(QAbstractTableModel):

    def __init__(self, data: Repository):
        super(DataTableModel, self).__init__()

        self._data = data
        self.horizontalHeaders = self._generate_headers(Qt.Horizontal)

    def _generate_headers(self, orientation):
        if orientation == Qt.Horizontal:
            return list(map(lambda c: inflection.humanize(c), self._data.get_columns()))

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if orientation == Qt.Horizontal:
            if role == Qt.DisplayRole:
                return self.horizontalHeaders[section]

    def rowCount(self, parent: Union[QModelIndex, QPersistentModelIndex]) -> int:
        return self._data.count()

    def columnCount(self, parent: Union[QModelIndex, QPersistentModelIndex]) -> int:
        model: Model = self._data.getAtIndex(0)

        return model.get_table_column_count()

    def data(self, index: Union[QModelIndex, QPersistentModelIndex], role: int) -> Any:
        column = index.column()
        row = index.row()
        model: Model = self._data.getAtIndex(row)
        columnName = model.get_table_columns()[column]
        value = getattr(model, columnName)

        details = {
            "column": index.column(),
            "row": index.row(),
            "index": index,
            "model": model,
            "columnName": columnName,
            "value": value,
        }

        if role == Qt.DisplayRole:
            return self._handle_display_role(details)
        elif role == Qt.TextAlignmentRole:
            return self._handle_text_alignment_role(details)
        elif role == Qt.DecorationRole:
            return self._handle_decoration_role(details)

    def _handle_decoration_role(self, details):
        return QIcon('tick.png')

    def _handle_display_role(self, details):
        # Perform per-type checks and render accordingly.
        if isinstance(details['value'], datetime):
            # Render time to YYY-MM-DD.
            return details['value'].strftime("%Y-%m-%d")

        if isinstance(details['value'], float):
            # Render float to 2 dp
            # return "%.2f" % value
            return details['value']

        if details["columnName"] == "job_id":
            return details["model"].job.display_label()

        if details["columnName"] == "company_id":
            return details["model"].company.display_label()

        return details['value']

    def _handle_text_alignment_role(self, details):
        if details['column'] == 0:
            return Qt.AlignCenter

        if isinstance(details['value'], datetime) or isinstance(details['value'], int) or isinstance(details['value'], float):
            return Qt.AlignVCenter + Qt.AlignRight
