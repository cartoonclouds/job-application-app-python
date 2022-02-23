
from app import types
from app.gui.components.datatable.Datatable import Datatable
from app.gui.components.datatable.DatatableItemDelegates.FollowUpItemDelegate import \
    FollowUpItemDelegate
from app.gui.components.datatable.JobApplicationDatatableModel import \
    JobApplicationDatatableModel
from app.gui.components.TabHeader import Header
from app.gui.components.tabs.JobApplicationTab import JobApplicationTab
from app.gui.components.tabs.Tab import Tab
from app.gui.services.TabService import TabService
from app.models.JobApplication import JobApplication
from app.storage import Storage
from PySide6.QtCore import (QModelIndex, QPersistentModelIndex,
                            QSortFilterProxyModel)
from PySide6.QtWidgets import QVBoxLayout

from app.utilities.IconUtility import IconUtility


class SummaryTab(Tab):
    def __init__(self, label: str, **kwargs: types.TabDetails) -> None:
        super().__init__(label=label, **kwargs)

        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)

        # Setup stats

        # Setup table
        self.datatable = self._setupTable()

        self.mainLayout.addWidget(Header('Job Applications Summary'))
        self.mainLayout.addWidget(self.datatable)

    def _setupTable(self):

        columHeaders = dict(zip(
            ["id", "title", "requires_followup", "company_id",
                "job_id", "created_at", "updated_at"],
            ["ID", "Title", "Requires Followup", "Company",
                "Job", "Created At", "Updated At"]
        ))

        datatable = Datatable()

        datatableModel = JobApplicationDatatableModel(
            list(Storage.jobApplications.values()),
            columHeaders
        )

        datatable.setModel(datatableModel)
        datatableModel.setParentTable(datatable)

        datatable.setItemDelegateForColumn(
            2, FollowUpItemDelegate(datatableModel))

        # debug(list(Storage.jobApplications.values()))

        # proxyModel = CustomSortModel()
        # proxyModel.setSourceModel(dataTableModel)
        # self.table = DataTable(dataTableModel)
        # .setSortingEnabled(True)

        datatable.doubleClicked.connect(self.openTab)

        return datatable

    def openTab(self, index: QModelIndex | QPersistentModelIndex):
        datatableModel: JobApplicationDatatableModel = self.datatable.model()
        jobApplication: JobApplication = datatableModel.modelAtIndex(index)

        TabService.openTab(JobApplicationTab(
            f"{jobApplication.title}, {jobApplication.company.name} (ID {jobApplication.id})", model=jobApplication, icon=IconUtility.getFileIcon("blue-folder-32")))

    def openEmptyTab(self):
        TabService.openTab(JobApplicationTab(
            f"New Application {TabService.tabCount() + 1}", icon=IconUtility.getFileIcon("blue-folder-32")))
