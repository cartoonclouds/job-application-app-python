
from PySide6.QtWidgets import QTableView, QAbstractItemView

# from app.gui.components.datatable.DatatableModel import DatatableModel


class Datatable(QTableView):
    """A datatable view model.

    URL: 
        https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTableView.html
        https://doc.qt.io/qtforpython/tutorials/datavisualize/add_tableview.html
        https://www.pythonguis.com/tutorials/qtableview-modelviews-numpy-pandas/
    """

    def __init__(self, dataTableModel: None = None) -> None:
        super().__init__()

        if dataTableModel:
            self.setModel(dataTableModel)
            dataTableModel.setParentTable(self)

        # TODO Statically set window width. Need to get initially get window width
        # self.horizontalHeader().setDefaultSectionSize(
        #     int(Storage.WINDOW_WIDTH / self.model().columnCount(self)))
        # self.horizontalHeader().setStretchLastSection(True)
        self.horizontalHeader().sectionPressed.connect(self.headerPressed)

        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.verticalHeader().setMinimumSectionSize(50)
        self.setAlternatingRowColors(True)

        # Use to customise setItemDelegate cell display
        #

        # Remove vertical gridlines
        self.setShowGrid(False)
        self.setStyleSheet(
            'QTableView::item {border-bottom: 1px solid #d6d9dc;}')

        # for loop over columnCount
        # dataTableModel.set_column_widths(self)

    def headerPressed(self, logicalIndex: int):
        print('presseed')
