import typing

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from app import types

from app.gui.components.datatable.Datatable import Datatable
from app.gui.components.datatable.ModelPresenter import ModelPresenter
from app.storage import Storage
from app.types import ColumnHeaders
from app.utilities.IconUtility import IconUtility


class DatatableModel(QAbstractTableModel):
    """A Datatable model baseclass.

    URL: https://doc.qt.io/qtforpython/PySide6/QtCore/QAbstractTableModel.html

    Raises:
        ValueError: [description]
        TypeError: [description]
        AttributeError: [description]
    """

    # _avg_font_w: int = 5
    # _resize_data = dict(int)

    # auto_resize: bool = False

    def __init__(self, data: typing.Sequence[ModelPresenter], columnHeaders: ColumnHeaders | None = None) -> None:
        super().__init__()

        # Set instance variables
        self._data = data
        self._headers: types.TableHeaders = []
        self._columns: types.ColumnNames = []
        self._parent_table: QTableView | None = None

        self.resizeColumns()

        self.btn_sell = QPushButton('Edit')
        # self.btn_sell.clicked.connect(self.headerPressed)

        if columnHeaders:
            self.setHeaders(list(columnHeaders.values()))
            self.setColumns(list(columnHeaders.keys()))

    def setHeaders(self, headers: types.TableHeaders):
        self._headers = headers
        self.resizeColumns()

    def setColumns(self, columns: types.ColumnNames):
        self._columns = columns
        self.resizeColumns()

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> typing.Any:
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
        if self._columns:
            return len(self._columns)
        else:
            return self._data[0].columnCount

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int) -> typing.Any:
        colIdx = index.column()
        rowIdx = index.row()
        rowModel: ModelPresenter = self._data[rowIdx]
        colName = self._columns[colIdx]

        # Adds widget to cell
        if colIdx == 0 and rowIdx == 0:
            w = QWidget()
            l = QHBoxLayout()
            la = QLabel()
            la.setPixmap(IconUtility.getIcon("tick-32"))
            w.setLayout(l)
            l.addWidget(la)
            self._parent_table.setIndexWidget(index, w)
            
            
        return rowModel.getFormattedAt(colName, role)

    def setParentTable(self, datatable: Datatable):
        """
        Sets the parent table widget so that we can get its font metrics for setting our column width with autoResize.

        Args:
            datatable (Datatable)

        Raises:
            TypeError
        """
        self._parent_table = datatable
        self.resizeColumns()

    # Width int | "fill" (fill the remaining space) | ""
    def resizeColumns(self):
        """Resizes columns one of three ways:
        1. Width - sets the width to be a specific number
        2. Column to contents - the width will be that of the column with the largest content
        3. Fill remaining - sets the width to fill the remaining space available (after the first two options are set)
        """
        if self._parent_table is None:
            return

        tableWidth = Storage.WINDOW_WIDTH
        colWidths = 0
        for colIdx in range(self.columnCount()):
            if self._columns[colIdx] in ["id", "requires_followup", "pinned", "created_at", "updated_at", "deleted_at"]:
                self._parent_table.resizeColumnToContents(colIdx)
                # 4 pixels for padding
                colWidths += self._parent_table.columnWidth(colIdx) + 4

        for colIdx in range(self.columnCount()):
            if self._columns[colIdx] in ["title", "job_id", "company_id"]:

                colWidth = int((tableWidth - colWidths) / 3) - 4

                self._parent_table.setColumnWidth(colIdx, colWidth)

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

    # def setData(self, index, cell_data, role=QtCore.Qt.EditRole):
    #     """
    #     When table cell is edited
    #     """

    #     row = index.row()
    #     column = index.column()

    #     if role == QtCore.Qt.EditRole:

    #         if column == 1:
    #             self._data[row].name = cell_data

    # emit(dataChanged(index, index));

    #     if self.auto_resize:
    #         self._autoSingleResizeData(data)
    #         self._doColumnResize()

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

    # def setAutoResize(self, b):
    #     """
    #     Turns on or off auto resize for the table. This gathers the font metrics of the parent table, and then loops
    #     over any current data, or newly added data (including table headers) to get the widest item, and sets the
    #     column width to fit this.

    #     Args:
    #         b (bool)

    #     Raise:
    #         AttributeError
    #     """
    #     if not self._parent_table:
    #         raise AttributeError(
    #             'You must call set parent table first to set the parent TableView item')

    #     self.auto_resize = b
    #     if b:
    #         self._autoAllResizeData()
    #         self._doColumnResize()
    #     else:
    #         self._resize_data = dict()

    # def autoResizeAt(self, index: int | Sequence[int]):
    #     """Sets the column to fill the remaining space.

    #     Args:
    #         index (int): Index of column to resize
    #     """
    #     pass

    # def updateSize(self):
    #     """
    #     Force the table size to update to the current size data.
    #     """
    #     self._doColumnResize()

    # def updateSizeAt(self, index: int):
    #     """
    #     Force a column to update to the current size data.
    #     """
    #     txt = self._headers[index]
    #     self._parent_table.setColumnWidth(index, self._resize_data.get(txt))

    # def updateSizeData(self):
    #     """
    #     Force an update/regathering of all the size data for each row and column.
    #     """
    #     self._autoAllResizeData(True)
    #     self._doColumnResize()

    # def _doColumnResize(self):
    #     for i in range(len(self._headers)):
    #         txt = self._headers[i]
    #         self._parent_table.setColumnWidth(i, self._resize_data.get(txt))

    # def _getKeyList(self):
    #     if self._headers:
    #         return self._headers
    #     elif self._data:
    #         return self._data.getColumns()

    # def _getTableFontWidth(self):
    #     self._avg_font_w = self._parent_table.fontMetrics().averageCharWidth()

    # def _autoAllResizeData(self, reset=False):
    #     if not self._resize_data or reset is True:
    #         self._resize_data = dict(int)

    #         key_list = self._getKeyList()
    #         for header in key_list:
    #             header_width = len(header) * self._avg_font_w
    #             if header_width > self._resize_data[header]:
    #                 self._resize_data[header] = header_width

    #             for item in self._data.values():
    #                 value = getattr(item, StringUtility.columnerize(header))
    #                 width = len(str(value)) * self._avg_font_w
    #                 if width > self._resize_data[header]:
    #                     self._resize_data[header] = width

    # def _autoSingleResizeData(self, data):
    #     key_list = self._getKeyList()
    #     for header in key_list:
    #         value = getattr(data, StringUtility.columnerize(header))
    #         if value:
    #             width = len(str(value)) * self._avg_font_w
    #             if width > self._resize_data[header]:
    #                 self._resize_data[header] = width
