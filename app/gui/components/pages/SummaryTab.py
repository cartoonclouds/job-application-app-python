# Standard Library
from typing import Any

# Framework imports
from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout

# Application imports
from app.gui.components.datatable.Datatable import Datatable
from app.gui.components.datatable.DatatableSortModel import DatatableSortModel
from app.gui.components.datatable.JobApplicationDatatableItemDelegate import (
    JobApplicationDatatableItemDelegate,
)
from app.gui.components.models.JobApplicationDatatableModel import (
    JobApplicationDatatableModel,
)
from app.gui.components.pages.JobApplicationTab import JobApplicationTab
from app.gui.components.pages.TabHeader import TabHeader
from app.gui.components.statistics.StatisticGroup import StatisticGroup
from app.gui.components.tabs.Tab import Tab
from app.gui.services.tab_service import TabServiceProvider
from app.models.JobApplication import JobApplication
from app.utils.icon_utility import IconUtility


class SummaryTab(Tab):
    def __init__(self, label: str, **kwargs: Any) -> None:
        super().__init__(label=label, **kwargs)

        self.mainLayout = QVBoxLayout(self)

        # Setup header
        header = TabHeader(
            "Applications Summary", IconUtility.getFileIconAsPixmap("gear")
        )

        # Setup stats
        self.statisticsSection = StatisticGroup()

        # Setup table
        self.datatable = self._setupTable()

        self.mainLayout.addWidget(header)
        self.mainLayout.addWidget(self.statisticsSection)
        self.mainLayout.addWidget(self.datatable)

    def _setupTable(self):
        frame = QFrame()
        frame.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        # frame.setStyleSheet(
        #     """
        #     QFrame {
        #         background-color: #FFF
        #     }
        # """
        # )

        layout = QHBoxLayout(frame)

        datatableModel = JobApplicationDatatableModel()
        datatable = Datatable(datatableModel, JobApplicationDatatableItemDelegate())

        datatable.openModel.connect(self.openTab)

        layout.addWidget(datatable)

        return frame

    @Slot(JobApplication)
    def openTab(self, model: JobApplication):
        TabServiceProvider.addTab(
            JobApplicationTab(
                f"{model.title}, {model.company.name} (ID {model.id})",
                model,
                icon=IconUtility.getFileIconAsPixmap("blue-folder-32"),
            )
        )

    def openEmptyTab(self):
        TabServiceProvider.addTab(
            JobApplicationTab(
                f"New Application {TabServiceProvider.tabCount() + 1}",
                JobApplication(),
                icon=IconUtility.getFileIconAsPixmap("blue-folder-32"),
            )
        )
