
import inflection
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtCore import QSortFilterProxyModel

from app.storage import Storage
from app.types import TabDetails

from app.gui.components.tabs.Tab import Tab
from app.gui.components.datatable.ModelPresenters.JobApplication import JobApplicationModelPresenter
from app.gui.components.datatable.Datatable import Datatable
from app.gui.components.datatable.DatatableModel import DatatableModel


class SummaryTab(Tab):
    def __init__(self, label: str, **kwargs: TabDetails) -> None:
        super().__init__(label=label, **kwargs)

        self.mainLayout = QHBoxLayout()
        self.setLayout(self.mainLayout)

        # Table setup
        dataModels = [
            JobApplicationModelPresenter(jobApp)
            for jobApp in Storage.jobApplications.values()
        ]

        columHeaders = dict(zip(
            ["id", "title", "requires_followup", "company_id", "job_id", "created_at", "updated_at"],
            ["ID", "Title", "Requires Followup", "Company", "Job", "Created At", "Updated At"]
        ))

        dataTableModel = DatatableModel(dataModels, columHeaders)
        self.table = Datatable(dataTableModel)

        # proxyModel = CustomSortModel()
        # proxyModel.setSourceModel(dataTableModel)
        # self.table = DataTable(dataTableModel)

        self.mainLayout.addWidget(self.table)
