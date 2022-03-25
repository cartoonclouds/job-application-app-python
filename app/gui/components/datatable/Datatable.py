# Framework imports
from PySide6.QtCore import QModelIndex, QPersistentModelIndex, Qt, Signal
from PySide6.QtGui import QAction, QContextMenuEvent, QCursor, QMouseEvent, QResizeEvent
from PySide6.QtWidgets import QAbstractItemView, QMenu, QStyledItemDelegate, QTableView

# Application imports
from app.config.App import Sizing
from app.gui.components.datatable.DatatableModel import DatatableModel
from app.models.Model import Model
from app.typings.types import M, Models


class Datatable(QTableView):
    """A datatable view model.

    URL:
        https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTableView.html
        https://doc.qt.io/qtforpython/PySide6/QtWidgets/QAbstractItemView.html
        https://doc.qt.io/qtforpython/tutorials/datavisualize/add_tableview.html
        https://www.pythonguis.com/tutorials/qtableview-modelviews-numpy-pandas/

        https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTableWidgetItem.html

        https://wiki.qt.io/Qt_for_Python_Signals_and_Slots
    """

    # Signal(Model)
    openModel = Signal(Model)
    openModelWithEvent = Signal(Model, QMouseEvent)

    # QMouseEvent

    def __init__(
        self,
        datatableModel: DatatableModel[Models],
        datatableItemDelegate: QStyledItemDelegate | None = None,
    ) -> None:
        super().__init__()

        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setAlternatingRowColors(True)
        self.setWordWrap(False)
        self.horizontalHeader().setSectionsMovable(True)
        self.verticalHeader().hide()
        self.verticalHeader().setMinimumSectionSize(50)
        self.setShowGrid(False)
        # self.setSortingEnabled(True)

        # https://doc.qt.io/qtforpython/overviews/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar
        # self.setStyleSheet(
        #     """
        #     QTableView {
        #         border: none;
        #     }
        #     QHeaderView::section {
        #         border: none;
        #         padding: 12px
        #     }
        #     QTableView::item {
        #     }
        # """
        # )
        # SET STYLESHEET

        self.setModel(datatableModel)

        datatableModel.dataUpdated.connect(self.resizeEvent())

        if datatableItemDelegate is not None:
            self.setItemDelegate(datatableItemDelegate)
            datatableItemDelegate.setParent(self)

    def model(self) -> DatatableModel[Models]:
        return super().model()

    def _getModelAtSelection(self):
        index = self.selectionModel().currentIndex()

        return self._getModelAtIndex(index)

    def _getModelAtIndex(self, index: QModelIndex | QPersistentModelIndex):
        datatableModel = self.model()

        return datatableModel.modelAtIndex(index)

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            rowModel = self._getModelAtSelection()

            if rowModel:
                self.openModel.emit(rowModel)
                self.openModelWithEvent.emit(rowModel, event)

        return super().mouseDoubleClickEvent(event)

    # TODO Set context menu on sub-class JobApplicationDatatable?

    @property
    def indexAtCursor(self) -> QModelIndex | QPersistentModelIndex:
        return self.indexAt(self.viewport().mapFromGlobal(QCursor.pos()))

    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        index = self.indexAt(event.pos())

        if not index.isValid():
            return

        rowModel = self._getModelAtIndex(index)

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

    def resizeEvent(self, event: QResizeEvent | None = None) -> None:
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
            if not hasattr(datatableModel.columns, column):
                continue

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
