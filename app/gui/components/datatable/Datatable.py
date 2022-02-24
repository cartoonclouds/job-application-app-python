
from PySide6.QtGui import QResizeEvent, QMouseEvent, QContextMenuEvent, QAction, QCursor
from PySide6.QtWidgets import QAbstractItemView, QTableView, QMenu
from PySide6.QtCore import Signal, Qt, QModelIndex, QPersistentModelIndex
from app.config.App import Sizing

from app.gui.components.datatable.models.DatatableModel import DatatableModel
from app.models.Model import Model


class Datatable(QTableView):
    """A datatable view model.

    URL: 
        https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTableView.html
        https://doc.qt.io/qtforpython/tutorials/datavisualize/add_tableview.html
        https://www.pythonguis.com/tutorials/qtableview-modelviews-numpy-pandas/

        https://wiki.qt.io/Qt_for_Python_Signals_and_Slots
    """

    # Signal(Model)
    openModel = Signal(Model)
    openModeWithEvent = Signal(Model, QMouseEvent)

    # QMouseEvent

    def __init__(self) -> None:
        super().__init__()

        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.verticalHeader().setMinimumSectionSize(50)
        self.setAlternatingRowColors(True)
        self.setWordWrap(False)

        # Remove vertical gridlines
        self.setShowGrid(False)
        self.setStyleSheet(
            'QTableView::item {border-bottom: 1px solid #d6d9dc;}')

    def hasDatatableModel(self) -> bool:
        return isinstance(self.model(), DatatableModel)

    def _getModelAtSelection(self) -> Model:
        index = self.selectionModel().currentIndex()

        return self._getModelAtIndex(index)

    def _getModelAtIndex(self, index: QModelIndex | QPersistentModelIndex) -> Model:
        datatableModel: DatatableModel = self.model()

        return datatableModel.modelAtIndex(index)

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            rowModel = self._getModelAtSelection()

            self.openModel.emit(rowModel)
            self.openModeWithEvent.emit(rowModel, event)

        return super().mouseDoubleClickEvent(event)

    # TODO Set context menu on sub-class JobApplicationDatatable?

    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        index = self.indexAt(event.pos())

        if not index.isValid():
            return

        rowModel: Model = self._getModelAtIndex(index)

        self.contextMenu = QMenu(self)

        title = QAction(rowModel.title, self)

        openAction = QAction("Open...", self)
        openAction.setStatusTip("Opens the job application in a new tab")
        openAction.triggered.connect(lambda: self.openModel.emit(rowModel))

        separator = QAction(self)
        separator.setSeparator(True)

        self.contextMenu.addActions([
            separator,
            openAction,
            title,
        ])

        self.contextMenu.popup(self.mapToGlobal(event.pos()))

        # return super().contextMenuEvent(arg__1)

    def resizeEvent(self, event: QResizeEvent | None = None) -> None:
        """Resizes columns one of three ways:
        1. Width - sets the width to be a specific number
        2. Column to contents - the width will be that of the column with the largest content
        3. Fill remaining - sets the width to fill the remaining space available (after the first two options are set)
        """
        if not self.hasDatatableModel():
            return

        datatableModel: DatatableModel = self.model()
        tableWidth = self.width()
        colWidths = 0

        for colIdx in range(datatableModel.columnCount()):
            if datatableModel.getColumnName(colIdx) in ["id", "requires_followup", "pinned", "created_at", "updated_at", "deleted_at"]:
                self.resizeColumnToContents(colIdx)
                colWidth = self.columnWidth(colIdx)
                self.setColumnWidth(
                    colIdx, colWidth + Sizing.TABLE_X_PADDING)

                colWidths += colWidth + Sizing.TABLE_X_PADDING

        for colIdx in range(datatableModel.columnCount()):
            if datatableModel.getColumnName(colIdx) in ["title", "job_id", "company_id"]:

                # colWidth = int((tableWidth - colWidths) / 3)
                colWidth = int((tableWidth - colWidths -
                               (6 * Sizing.TABLE_X_PADDING)) / 3)

                self.setColumnWidth(
                    colIdx, colWidth + Sizing.TABLE_X_PADDING)

        # self.horizontalHeader().setStretchLastSection(True)
