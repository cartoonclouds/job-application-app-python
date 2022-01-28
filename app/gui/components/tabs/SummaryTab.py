
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from app.gui.components.datatable.DatatableModel import DatatableModel
from app.models.JobApplication import JobApplication
from app.repositories.JobApplicationRepository import JobApplicationRepository
import inflection
from app.storage import Storage
from app.utilities.IconUtility import IconUtility

from app.gui.components.tabs.Tab import Tab
from app.gui.components.datatable.DatatableSortModel import CustomSortModel
from app.gui.components.datatable.ModelPresenter import ModelPresenter
from app.gui.components.datatable.Datatable import Datatable


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
        dataModels = [
            ModelPresenter(jobApp)
            for jobApp in Storage.jobApplications.values()
        ]

        columHeaders = {
            c: inflection.titleize(c)
            for c in dataModels[0].columns
        }

        # print(*columHeaders.values(), sep="\n")
        # print(type(columHeaders.values()))
        # exit()

        dataTableModel = DatatableModel(dataModels, columHeaders)
        self.table = Datatable(dataTableModel)

        # proxyModel = CustomSortModel()
        # proxyModel.setSourceModel(dataTableModel)
        # self.table = DataTable(dataTableModel)

        # dataTableModel.updateSizeAt(0)
        # dataTableModel.updateSizeAt(1)
        # dataTableModel.updateSizeAt(2)
        # dataTableModel.updateSizeAt(3)

        # dataTableModel.autoResizeAt([4, 5])

        self.layout.addWidget(self.table)

        label = QLabel()
        label.setMaximumSize(32, 32)
        label.setScaledContents(True)
        label.setPixmap(IconUtility.getIcon("tick-32"))
        self.table.setCornerWidget(label)
