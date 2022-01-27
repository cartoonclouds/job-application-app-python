
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from app.gui.components.datatable.JobApplicationDatatableModel import JobApplicationDataTableModel
from app.gui.components.datatable.DataTable import DataTable

from app.storage import Storage
from app.gui.components.tabs.Tab import Tab


class SummaryTab(Tab):
    def __init__(self,
                 label: str,
                 tooltip: str = None,
                 whatsThis: str = None,
                 icon: QIcon = None,
                 closable: bool = True
                 ):

        super(SummaryTab, self).__init__()

        self.label = label
        self.tooltip = tooltip
        self.tab_whatsThis = whatsThis
        self.icon = icon
        self.closable = False

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        # Table setup
        tableModel = JobApplicationDataTableModel(Storage.jobAppRepository)
        self.table = DataTable(tableModel)
        tableModel.updateSizeAt(0)
        tableModel.updateSizeAt(1)
        tableModel.updateSizeAt(2)
        tableModel.updateSizeAt(3)

        self.layout.addWidget(self.table)
