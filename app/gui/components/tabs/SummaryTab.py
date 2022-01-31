
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtCore import QSortFilterProxyModel

from app.storage import Storage
from app import types

from app.gui.components.tabs.Tab import Tab
from app.gui.components.datatable.ModelPresenters.JobApplication import JobApplicationDatatableModel
from app.gui.components.datatable.Datatable import Datatable


class SummaryTab(Tab):
    def __init__(self, label: str, **kwargs: types.TabDetails) -> None:
        super().__init__(label=label, **kwargs)

        self.mainLayout = QHBoxLayout()
        self.setLayout(self.mainLayout)

        # Setup table
        self.table = self._setupTable()

        # Setup stats

        self.mainLayout.addWidget(self.table)

    def _setupTable(self):
        columHeaders = dict(zip(
            ["id", "title", "requires_followup", "company_id",
                "job_id", "created_at", "updated_at"],
            ["ID", "Title", "Requires Followup", "Company",
                "Job", "Created At", "Updated At"]
        ))

        dataTableModel = JobApplicationDatatableModel(
            list(Storage.jobApplications.values()),
            columHeaders
        )

        # proxyModel = CustomSortModel()
        # proxyModel.setSourceModel(dataTableModel)
        # self.table = DataTable(dataTableModel)

        return Datatable(dataTableModel)
