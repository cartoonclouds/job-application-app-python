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
from PySide6.QtGui import QMouseEvent, QPalette
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QFrame

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
from app.gui.components.statistics.StatisticGroup import StatisticGroup
from app.gui.components.tabs.Tab import Tab
from app.gui.services.TabService import TabService
from app.models.JobApplication import JobApplication
from app.storage import Storage
from app.utilities.IconUtility import IconUtility


class SummaryTab(Tab):
    def __init__(self, label: str, **kwargs) -> None:
        super().__init__(label=label, **kwargs)

        self.setObjectName("Tab:Summary")
        self.mainLayout = QVBoxLayout(self)
        # *([10] * 4)
        self.setContentsMargins(10, 0, 10, 0)

        # Header
        header = Header("Applications Summary")

        # Setup stats
        self.statisticsSection = StatisticGroup()

        # Setup table
        self.datatable = self._setupTable()

        self.mainLayout.addWidget(header)
        self.mainLayout.addWidget(self.statisticsSection)
        self.mainLayout.addWidget(self.datatable)

        # self.mainLayout.setStretchFactor(widget, 0)

    def _setupTable(self):
        frame = QFrame()
        frame.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        frame.setStyleSheet(
            """
            QFrame {
                background-color: #FFF
            }
        """
        )

        layout = QHBoxLayout(frame)
        layout.setContentsMargins(*([20] * 4))

        columHeaders = dict(
            zip(
                [
                    "id",
                    "title",
                    "requires_followup",
                    "company",
                    "job",
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

        # TABLE EDITING
        # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QItemEditorFactory.html
        # https://doc.qt.io/qtforpython/overviews/qtwidgets-itemviews-coloreditorfactory-example.html
        # https://programmer.group/qt-custom-delegation-draws-control-picture-and-text-in-qtableview.html
        # https://stackoverflow.com/questions/62414356/add-a-checkbox-to-text-in-a-qtableview-cell-using-delegate

        # FROZEN COLUMNS
        # https://doc.qt.io/qtforpython/overviews/qtwidgets-itemviews-frozencolumn-example.html

        datatable.openModel.connect(self.openTab)

        layout.addWidget(datatable)

        return frame

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
