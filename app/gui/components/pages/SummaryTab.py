# Framework imports
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout

# Application imports
from app.gui.components.datatable.Datatable import Datatable
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
from app.gui.services.TabService import TabServiceProvider
from app.models.JobApplication import JobApplication
from app.utils.IconUtility import IconUtility


class SummaryTab(Tab):
    def __init__(self, label: str, **kwargs) -> None:
        super().__init__(label=label, **kwargs)

        self.setObjectName("Tab:Summary")
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

        # self.mainLayout.setStretchFactor(widget, 0)

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

        # proxyModel = CustomSortModel()
        # proxyModel.setSourceModel(dataTableModel)
        # self.table = DataTable(dataTableModel)

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
