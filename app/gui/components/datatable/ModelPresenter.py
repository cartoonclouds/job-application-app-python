
import datetime
import typing
from dataclasses import dataclass
from PySide6.QtCore import Qt

from app.models.Model import Model
from app.utilities.IconUtility import IconUtility


@dataclass
class ModelData:
    colIdx: int
    colName: str
    value: typing.Any


class ModelPresenter:
    """A datatable model representing Job Applications.

    Attributes:
        data (Repository): A diciontary holding the Job Application data
    """

    def __init__(self, model: Model):
        self._model = model

    @property
    def columns(self):
        return self._model.getTableColumns()

    def getFormattedAt(self, colIdx: int, role):
        details = ModelData(
            colIdx,
            self.columns[colIdx],
            getattr(self._model, self.columns[colIdx])
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
            if details.value:
                return IconUtility.getIcon("tick-32")
            else:
                return IconUtility.getIcon("tick-32")

        if details.colName == "job_id":
            return self._model.job.displayLabel()

        if details.colName == "company_id":
            return self._model.company.displayLabel()

        return details.value

    def _handleTextAlignmentRole(self, details: ModelData):
        if details.colIdx == 0:
            return Qt.AlignCenter

        if type(details.value) == bool:
            return Qt.AlignCenter

        if isinstance(details.value, datetime.datetime):
            return Qt.AlignVCenter + Qt.AlignRight

    def _handleSizeHintRole(self, details: ModelData):
        pass

    def _handle_size_hint_role(self, details: ModelData):
        pass

    def _handleDecorationRole(self, details: ModelData):
        pass
        # if type(value) == bool:
        #     if value:
        #         return IconUtility.getIcon("tick-32")
        #     else:
        #         return IconUtility.getIcon("tick-32")
