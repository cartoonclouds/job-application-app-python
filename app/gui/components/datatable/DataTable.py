

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from app.gui.components.datatable.JobApplicationDatatableModel import JobApplicationDataTableModel


class DataTable(QTableView):
    def __init__(self, dataTableModel: JobApplicationDataTableModel):
        super(DataTable, self).__init__()

        self.setModel(dataTableModel)

        # TODO Statically set window width. Need to get initially get window width
        self.horizontalHeader().setDefaultSectionSize(
            int(1500 / self.model().columnCount(self)))
        self.horizontalHeader().setStretchLastSection(True)
        self.horizontalHeader().sectionPressed.connect(self.header_pressed)

        self.verticalHeader().setMinimumSectionSize(50)

        self.setAlternatingRowColors(True)
        
        # Use to customise setItemDelegate cell display
        #  

        # Remove vertical gridlines
        self.setShowGrid(False)
        self.setStyleSheet(
            'QTableView::item {border-bottom: 1px solid #d6d9dc;}')

        # for loop over columnCount
        dataTableModel.set_column_widths(self)

    def header_pressed(self, logicalIndex: int):
        print('presseed')
