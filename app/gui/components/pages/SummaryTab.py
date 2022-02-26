# Standard Library
from functools import partial

# Framework imports
from PySide6.QtCore import (
    QModelIndex,
    QPersistentModelIndex,
    QSortFilterProxyModel,
    Slot,
    QMargins,
)
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QVBoxLayout

# Application imports
from app.gui.components.datatable.Datatable import Datatable
from app.gui.components.datatable.delegates.JobApplicationDatatableItemDelegate import (
    JobApplicationDatatableItemDelegate,
)
from app.gui.components.datatable.models.JobApplicationDatatableModel import (
    JobApplicationDatatableModel,
)
from app.gui.components.pages.Header import Header
from app.gui.components.pages.JobApplicationTab import JobApplicationTab
from app.gui.components.tabs.Tab import Tab
from app.gui.services.TabService import TabService
from app.models.JobApplication import JobApplication
from app.storage import Storage
from app.utilities.IconUtility import IconUtility


class SummaryTab(Tab):
    def __init__(self, label: str, **kwargs) -> None:
        super().__init__(label=label, **kwargs)

        self.mainLayout = QVBoxLayout()
        MARGINS = [20] * 4
        self.setContentsMargins(*MARGINS)
        self.setLayout(self.mainLayout)

        # Setup stats11111111111111111111

        # Setup table
        self.datatable = self._setupTable()

        self.mainLayout.addWidget(Header("Applications Summary"))
        self.mainLayout.addWidget(self.datatable)

    def _setupTable(self):

        columHeaders = dict(
            zip(
                [
                    "id",
                    "title",
                    "requires_followup",
                    "company_id",
                    "job_id",
                    "created_at",
                    "updated_at",
                ],
                [
                    "ID",
                    "Title",
                    "Requires Followup",
                    "Company",
                    "Job",
                    "Created At",
                    "Updated At",
                ],
            )
        )

        datatableModel = JobApplicationDatatableModel(
            list(Storage.jobApplications.values()), columHeaders
        )

        datatable = Datatable(datatableModel)
        datatable.setItemDelegate(JobApplicationDatatableItemDelegate(datatableModel))

        # debug(list(Storage.jobApplications.values()))

        # proxyModel = CustomSortModel()
        # proxyModel.setSourceModel(dataTableModel)
        # self.table = DataTable(dataTableModel)
        # .setSortingEnabled(True)

        datatable.openModel.connect(self.openTab)

        return datatable

    @Slot(JobApplication)
    @Slot(JobApplication, QMouseEvent)
    def openTab(self, model: JobApplication):
        TabService.openTab(
            JobApplicationTab(
                f"{model.title}, {model.company.name} (ID {model.id})",
                model=model,
                icon=IconUtility.getFileIconAsPixmap("blue-folder-32"),
            )
        )

    def openEmptyTab(self):
        TabService.openTab(
            JobApplicationTab(
                f"New Application {TabService.tabCount() + 1}",
                icon=IconUtility.getFileIconAsPixmap("blue-folder-32"),
            )
        )
