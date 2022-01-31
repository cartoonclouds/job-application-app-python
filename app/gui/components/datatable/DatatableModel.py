import typing

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from app import types
from app.config.App import Sizing
import qtawesome as qta

from app.gui.components.datatable.Datatable import Datatable
from app.models.Model import Model
from app.utilities.IconUtility import IconUtility


class DatatableModel(QAbstractTableModel):
    """A Datatable model baseclass.

    URL: https://doc.qt.io/qtforpython/PySide6/QtCore/QAbstractTableModel.html

    Raises:
        ValueError: [description]
        TypeError: [description]
        AttributeError: [description]
    """

    def __init__(self, data: typing.Sequence[Model], columnHeaders: types.ColumnHeaders) -> None:
        super().__init__()

        # Set instance variables
        self._data = data
        self._headers: types.TableHeaders = list(columnHeaders.values())
        self._columns: types.ColumnNames = list(columnHeaders.keys())
        # self._parent_table: QTableView | None = None

        # self.resizeColumns()

    def setHeaders(self, headers: types.TableHeaders):
        self._headers = headers
        self.resizeColumns()

    def setColumns(self, columns: types.ColumnNames):
        self._columns = columns
        self.resizeColumns()

    def headerData(self, section: int, orientation: Qt.Orientation, role: int) -> typing.Any:
        """
        Sets the header data based on our header key list.
        """
        if orientation == Qt.Horizontal:
            if role == Qt.DisplayRole:
                return self._headers[section]

    def rowCount(self, parent: QModelIndex | QPersistentModelIndex | None = None) -> int:
        """Return the row count.

        Args:
            parent (QModelIndex | QPersistentModelIndex, optional): The parent table

        Returns:
            int
        """
        return len(self._data)

    def columnCount(self, parent: QModelIndex | QPersistentModelIndex | None = None) -> int:
        """ Return the column count.

        Args:
            parent (QModelIndex | QPersistentModelIndex, optional): The parent table

        Returns:
            int: [description]
        """
        return len(self._columns)

    # def data(self, index: QModelIndex | QPersistentModelIndex, role: int) -> typing.Any:
    #     match role:
    #         case Qt.DisplayRole:
    #         case Qt.DecorationRole:
    #         case Qt.EditRole:
    #         case Qt.ToolTipRole:
    #         case Qt.StatusTipRole:
    #         case Qt.WhatsThisRole:
    #         case Qt.TextAlignmentRole:
    #         case Qt.SizeHintRole:

    def setParentTable(self, datatable: Datatable):
        """
        Sets the parent table widget so that we can get its font metrics for setting our column width with autoResize.

        Args:
            datatable (Datatable)

        Raises:
            TypeError
        """
        self._parentTable = datatable
        self.resizeColumns()
        self.decorateCells()

    def decorateCells(self):
        for r in range(self.rowCount()):
            row = self._data[r]
            for c in range(self.columnCount()):
                column = self._columns[c]
                value = getattr(row, column)
                index = self.index(r, c)

                # w = qta.IconWidget('mdi.web', color='blue')
                # self._parentTable.setIndexWidget(index, w)

                if column in ["requires_followup"]:
                    if value:
                        self.addIconAtIndex(
                            index, IconUtility.getFileIcon("light-bulb-24"))
                    else:
                        self.addIconAtIndex(
                            index, IconUtility.getFileIcon("light-bulb-off-24"))

    def addIconAtIndex(self, index: QModelIndex | QPersistentModelIndex, icon: QPixmap):
        w = QWidget()
        l = QHBoxLayout()
        la = QLabel()
        la.setAlignment(Qt.AlignmentFlag.AlignCenter)
        la.setPixmap(icon)
        w.setLayout(l)
        l.addWidget(la)
        self._parentTable.setIndexWidget(index, w)

    # Width int | "fill" (fill the remaining space) | "stretch"

    def resizeColumns(self):
        """Resizes columns one of three ways:
        1. Width - sets the width to be a specific number
        2. Column to contents - the width will be that of the column with the largest content
        3. Fill remaining - sets the width to fill the remaining space available (after the first two options are set)
        """
        if self._parentTable is None:
            return

        tableWidth = self._parentTable.width()
        colWidths = 0

        for colIdx in range(self.columnCount()):
            if self._columns[colIdx] in ["id", "requires_followup", "pinned", "created_at", "updated_at", "deleted_at"]:
                self._parentTable.resizeColumnToContents(colIdx)
                colWidth = self._parentTable.columnWidth(colIdx)
                self._parentTable.setColumnWidth(
                    colIdx, colWidth + Sizing.TABLE_X_PADDING)

                colWidths += colWidth + Sizing.TABLE_X_PADDING

        for colIdx in range(self.columnCount()):
            if self._columns[colIdx] in ["title", "job_id", "company_id"]:

                # colWidth = int((tableWidth - colWidths) / 3)
                colWidth = int((tableWidth - colWidths -
                               (6 * Sizing.TABLE_X_PADDING)) / 3)

                self._parentTable.setColumnWidth(
                    colIdx, colWidth + Sizing.TABLE_X_PADDING)

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
