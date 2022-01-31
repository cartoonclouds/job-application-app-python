
from PySide6.QtWidgets import QTableView, QAbstractItemView, QPushButton
from PySide6.QtCore import QAbstractTableModel, Slot, QSortFilterProxyModel
from PySide6.QtGui import QResizeEvent
# from app.gui.components.datatable.DatatableModel import DatatableModel


class Datatable(QTableView):
    """A datatable view model.

    URL: 
        https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTableView.html
        https://doc.qt.io/qtforpython/tutorials/datavisualize/add_tableview.html
        https://www.pythonguis.com/tutorials/qtableview-modelviews-numpy-pandas/
    """

    def __init__(self, dataTableModel: QAbstractTableModel | QSortFilterProxyModel | None = None) -> None:
        super().__init__()

        if dataTableModel:
            self.setModel(dataTableModel)
            dataTableModel.setParentTable(self)

        self.horizontalHeader().sectionPressed.connect(self.headerPressed)

        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.verticalHeader().setMinimumSectionSize(50)
        self.setAlternatingRowColors(True)
        self.setWordWrap(False)

        # Use to customise setItemDelegate cell display
        #

        # Remove vertical gridlines
        self.setShowGrid(False)
        self.setStyleSheet(
            'QTableView::item {border-bottom: 1px solid #d6d9dc;}')

    # https://wiki.qt.io/Qt_for_Python_Signals_and_Slots
    # @Slot()

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.model().resizeColumns()

        return super().resizeEvent(event)

    def headerPressed(self, logicalIndex: int):
        print('presseed')
