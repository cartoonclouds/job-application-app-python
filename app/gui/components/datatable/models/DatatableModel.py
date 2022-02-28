from typing import Sequence, Any, TYPE_CHECKING, Optional, Mapping
from dataclasses import dataclass

from app.models.Model import Model
from PySide6.QtCore import QAbstractTableModel, QModelIndex, QPersistentModelIndex, Qt

if TYPE_CHECKING:
    from app.gui.components.datatable.Datatable import Datatable


@dataclass(frozen=True)
class ModelData:
    column: str
    model: Model
    value: Any


class DatatableModel(QAbstractTableModel):
    """A Datatable model baseclass.

    URL: https://doc.qt.io/qtforpython/PySide6/QtCore/QAbstractTableModel.html

    Raises:
        ValueError
        TypeError
        AttributeError
    """

    def __init__(self, data: Sequence[Model], columnHeaders: Mapping[str, str]) -> None:
        super().__init__()

        # Set instance variables
        self._data = data
        self._headers: Sequence[str] = list(columnHeaders.values())
        self._columns: Sequence[str] = list(columnHeaders.keys())
        self._parentTable: Datatable

    def setParentTable(self, datatable: "Datatable"):
        """
        Sets the parent table widget so that we can get its font metrics for setting our column width with autoResize.

        Args:
            datatable (Datatable)

        Raises:
            TypeError
        """
        self._parentTable = datatable

    @property
    def datatable(self):
        return self._parentTable

    @property
    def columns(self):
        return self._columns

    def _triggerParentResize(self):
        if self.datatable:
            self.datatable.resizeEvent()

    def getColumnName(self, colIdx: int) -> str:
        return self._columns[colIdx]

    def setHeaders(self, headers: Sequence[str]):
        self._headers = headers
        self._triggerParentResize()

    def setColumns(self, columns: Sequence[str]):
        self._columns = columns
        self._triggerParentResize()

    def headerData(self, section: int, orientation: Qt.Orientation, role: int) -> Any:
        """
        Sets the header data based on our header key list.
        """
        if orientation == Qt.Horizontal:
            if role == Qt.DisplayRole:
                return self._headers[section]

    def rowCount(
        self, parent: Optional[QModelIndex | QPersistentModelIndex] = None
    ) -> int:
        """
        Return the row count.
        """
        return len(self._data)

    def columnCount(
        self, parent: Optional[QModelIndex | QPersistentModelIndex] = None
    ) -> int:
        """
        Return the column count.
        """
        return len(self._columns)

    # def data(self, index: QModelIndex | QPersistentModelIndex, role: int) -> Any:
    #     match role:
    #         case Qt.DisplayRole:
    #         case Qt.DecorationRole:
    #         case Qt.EditRole:
    #         case Qt.ToolTipRole:
    #         case Qt.StatusTipRole:
    #         case Qt.WhatsThisRole:
    #         case Qt.TextAlignmentRole:
    #         case Qt.SizeHintRole:

    def modelAtIndex(self, index: QModelIndex | QPersistentModelIndex) -> Model | None:
        """Finds the data Model of row at the given index.

        Args:
            index (QModelIndex)

        Returns:
            Model
        """
        return self._data[index.row()] if index.row() > 0 else None

    def getModelData(self, index: QModelIndex | QPersistentModelIndex) -> ModelData:
        """Constructs a data class with details at the given index.

        Args:
            index (QModelIndex)

        Returns:
            ModelData A small class containing the column name, value and Model
        """
        colIdx = index.column()
        rowModel = self.modelAtIndex(index)
        colName = self._columns[colIdx]

        return ModelData(colName, rowModel, getattr(rowModel, colName))

    # def setHeaders(self, items):
    #     """
    #     This allows you to set your header item text

    #     Args:
    #         items: a list of header text, ie ['Name', 'Email', 'Department']
    #     """
    #     lastCount = self.columnCount(QModelIndex())
    #     self._headers = items

    #     self.beginRemoveColumns(QModelIndex(), 0, lastCount)
    #     for x in range(lastCount):
    #         self.removeColumn(x)
    #     self.endRemoveColumns()

    #     self.beginInsertColumns(QModelIndex(), 0, len(items)-1)
    #     self.endInsertColumns()

    # def addRow(self, data: Model):
    #     """
    #     Accepts data to add to the data model.

    #     Args:
    #         data (Model)
    #     """
    #     row = self.rowCount()
    #     self.beginInsertRows(QModelIndex(), row, row)
    #     self._data.update({data.id, data})
    #     self.endInsertRows()

    # emit(dataChanged(index, index));
    # layoutChanged.emit()

    # def addRows(self, data: Mapping[str | Model]):
    #     """
    #     Accepts a list of dicts to add them all to the table.

    #     Args:
    #         data (Mapping[str, Model]): list of dicts

    #     Raises:
    #         ValueError
    #     """
    #     if not isinstance(data, Repository):
    #         raise ValueError(
    #             'Datatable model data must be of type Repository!')

    #     start_row = len(self._data)
    #     end_row = len(data) + start_row - 1

    #     self.beginInsertRows(QModelIndex(), start_row, end_row)
    #     self._data.update(data)
    #     self.endInsertRows()

    #     if self.auto_resize:
    #         for item in data:
    #             self._autoSingleResizeData(item)
    #             self._doColumnResize()

    # def removeRow(self, row):
    #     """
    #     Remove the row at index 'row'.

    #     Args:
    #         row (int):
    #     """
    #     self.beginRemoveRows(QModelIndex(), row, row)
    #     self._data.pop(row)
    #     self.endRemoveRows()

    # def clear(self):
    #     """
    #     Clear all table data and start fresh.
    #     """
    #     rows = self.rowCount(QModelIndex())
    #     self.beginRemoveRows(QModelIndex(), 0, rows)
    #     self._data = []
    #     self.endRemoveRows()

    #     cols = self.columnCount(QModelIndex())
    #     self.beginRemoveColumns(QModelIndex(), 0, cols)
    #     self._headers = []
    #     self.endRemoveColumns()

    # def intGetData(self, row, col):
    #     """
    #     Gets the data at 'row' and 'col'.
    #     :param row: int
    #     :param col: int
    #     :return: QVariant() data.
    #     """
    #     try:
    #         return None
    #     except:
    #         return None
