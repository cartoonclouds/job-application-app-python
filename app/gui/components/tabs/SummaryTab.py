
import inflection
from PySide6.QtWidgets import QHBoxLayout

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

        columHeaders = {
            c: inflection.titleize(c)
            for c in dataModels[0].columns
        }

        # columHeaders = dict(zip(
        #     ["id", "title", "pinned", "job_id", "updated_at"],
        #     ["ID", "Title", "Pinned", "Job", "Updated At"]
        # ))

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

        self.mainLayout.addWidget(self.table)

        # qlabel = QLabel()
        # qlabel.setMaximumSize(32, 32)
        # qlabel.setScaledContents(True)
        # qlabel.setPixmap(IconUtility.getIcon("tick-32"))
        # self.table.setCornerWidget(qlabel)
