
import datetime
from PySide6.QtCore import Qt

from app.gui.components.datatable.ModelPresenter import ModelData, ModelPresenter
from app.models.Model import Model
from app.utilities.IconUtility import IconUtility


class JobApplicationModelPresenter(ModelPresenter):
    """
    A datatable model presenter for Job Applications.
    """

    def __init__(self, model: Model) -> None:
        self._model = model

    def getFormattedAt(self, column: str, role):
        details = ModelData(
            column,
            getattr(self._model, column)
        )

        if role == Qt.DisplayRole:
            return self._handleDisplayRole(details)
        elif role == Qt.TextAlignmentRole:
            return self._handleTextAlignmentRole(details)
        elif role == Qt.DecorationRole:
            return self._handleDecorationRole(details)
        elif role == Qt.SizeHintRole:
            return self._handleSizeHintRole(details)

    def _handleDisplayRole(self, details: ModelData):
        # Perform per-type checks and render accordingly.
        if isinstance(details.value, datetime.datetime):
            # Render time to YYY-MM-DD.
            return details.value.strftime("%Y-%m-%d")

        if isinstance(details.value, float):
            # Render float to 2 dp
            # return "%.2f" % value
            return details.value

        if type(details.value) == bool:
            return

        if details.column == "job_id":
            return self._model.job.displayLabel()

        if details.column == "company_id":
            return self._model.company.displayLabel()

        return details.value

    def _handleTextAlignmentRole(self, details: ModelData):
        if details.column == "id":
            return Qt.AlignCenter

        if type(details.value) == bool:
            return Qt.AlignCenter

        if isinstance(details.value, datetime.datetime):
            return Qt.AlignVCenter + Qt.AlignRight

    def _handleSizeHintRole(self, details: ModelData):
        pass

    def _handleDecorationRole(self, details: ModelData):
        if type(details.value) == bool:
            if details.value:
                return IconUtility.getIcon("tick-32")
            else:
                return IconUtility.getIcon("tick-32")
