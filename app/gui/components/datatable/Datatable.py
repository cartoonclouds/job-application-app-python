from typing import Generic, Optional
from PySide6.QtGui import QResizeEvent, QMouseEvent, QContextMenuEvent, QAction, QCursor
from PySide6.QtWidgets import QAbstractItemView, QTableView, QMenu
from PySide6.QtCore import Signal, Qt, QModelIndex, QPersistentModelIndex, QPoint
from app.config.App import Sizing

from app.gui.components.datatable.models.DatatableModel import DatatableModel
from app.models.Model import Model
from app.types import DTM


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

    def __init__(self, datatableModel: DatatableModel) -> None:
        super().__init__()

        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.verticalHeader().setMinimumSectionSize(50)
        self.verticalHeader().setSectionsMovable(False)
        self.setAlternatingRowColors(True)
        self.setWordWrap(False)

        # Remove vertical gridlines
        self.setShowGrid(False)
        self.setStyleSheet(
            """
            QTableView {
                border: none;
            }
            QHeaderView::section {
            }
            QTableView::item {
                border-bottom: none;
            }
        """
        )

        self.setModel(datatableModel)
        datatableModel.setParentTable(self)

    def _getModelAtSelection(self) -> Model:
        index = self.selectionModel().currentIndex()

        return self._getModelAtIndex(index)

    def _getModelAtIndex(self, index: QModelIndex | QPersistentModelIndex) -> Model:
        datatableModel: DatatableModel = self.model()

        return datatableModel.modelAtIndex(index)

    def model(self) -> DatatableModel:
        return super().model()  # type: ignore

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            rowModel = self._getModelAtSelection()

            self.openModel.emit(rowModel)
            self.openModeWithEvent.emit(rowModel, event)

        return super().mouseDoubleClickEvent(event)

    # TODO Set context menu on sub-class JobApplicationDatatable?

    @property
    def indexAtCursor(self) -> QModelIndex | QPersistentModelIndex:
        return self.indexAt(self.viewport().mapFromGlobal(QCursor.pos()))

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

        self.contextMenu.addActions(
            [
                separator,
                openAction,
                title,
            ]
        )

        self.contextMenu.popup(self.mapToGlobal(event.pos()))

        # return super().contextMenuEvent(arg__1)

    def resizeEvent(self, event: Optional[QResizeEvent] = None) -> None:
        """Resizes columns one of three ways:
        1. Width - sets the width to be a specific number
        2. Column to contents - the width will be that of the column with the largest content
        3. Fill remaining - sets the width to fill the remaining space available (after the first two options are set)
        """
        datatableModel = self.model()
        tableWidth = self.width()
        colWidths = 0

        fitByContents = [
            "id",
            "requires_followup",
            "created_at",
            "updated_at",
        ]

        for index, column in enumerate(fitByContents):
            index = datatableModel.columns.index(column)

            self.resizeColumnToContents(index)
            colWidth = self.columnWidth(index) + Sizing.TABLE_X_PADDING
            self.setColumnWidth(index, colWidth)

            colWidths += colWidth

        remainingColumnSpace = tableWidth - colWidths
        remainingColumns = [
            col for col in datatableModel.columns if col not in fitByContents
        ]

        for index, column in enumerate(remainingColumns):
            colIndex = datatableModel.columns.index(column)

            remainingColumnCount = len(remainingColumns) - index

            colWidth = (
                remainingColumnSpace / remainingColumnCount
            ) + Sizing.TABLE_X_PADDING

            remainingColumnSpace = remainingColumnSpace - colWidth

            self.setColumnWidth(colIndex, int(colWidth))

        # TODO Work out why exactly 40 pixels
        self.setColumnWidth(1, self.columnWidth(1) - 40)
