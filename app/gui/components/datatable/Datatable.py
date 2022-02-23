from typing import TYPE_CHECKING

from PySide6.QtGui import QResizeEvent
from PySide6.QtWidgets import QAbstractItemView, QTableView

if TYPE_CHECKING:
    from app.gui.components.datatable.DatatableModel import DatatableModel


class Datatable(QTableView):
    """A datatable view model.

    URL: 
        https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTableView.html
        https://doc.qt.io/qtforpython/tutorials/datavisualize/add_tableview.html
        https://www.pythonguis.com/tutorials/qtableview-modelviews-numpy-pandas/
    """

    def __init__(self) -> None:
        super().__init__()

        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.verticalHeader().setMinimumSectionSize(50)
        self.setAlternatingRowColors(True)
        self.setWordWrap(False)

        # Remove vertical gridlines
        self.setShowGrid(False)
        self.setStyleSheet(
            'QTableView::item {border-bottom: 1px solid #d6d9dc;}')

    # https://wiki.qt.io/Qt_for_Python_Signals_and_Slots
    # @Slot()

    def resizeEvent(self, event: QResizeEvent) -> None:
        model: 'DatatableModel' = self.model()
        model.resizeColumns()

        return super().resizeEvent(event)
