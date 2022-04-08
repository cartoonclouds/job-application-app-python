# Standard Library
from copy import copy, deepcopy
from datetime import datetime
from typing import Any, Mapping, Sequence

# Framework imports
from PySide6.QtCore import QModelIndex, QPersistentModelIndex, Qt

# Application imports
from app.gui.components.datatable.DatatableModel import DatatableModel, ModelData
from app.models.JobApplication import JobApplication
from app.repositories.job_application_repository import JobApplicationRepository


class JobApplicationDatatableModel(DatatableModel[JobApplication]):
    """A datatable model for Job Applications."""

    def __init__(self) -> None:
        columnHeaders: Mapping[str, str] = dict(
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

        data = JobApplicationRepository.items()

        super().__init__(data, columnHeaders)

    def data(
        self, index: QModelIndex | QPersistentModelIndex, role: int = Qt.DisplayRole
    ) -> Any:
        modelData = self.getModelData(index)

        if role == Qt.DisplayRole:
            return self._handleDisplayRole(modelData)

        return super().data(index, role)

    def _handleDisplayRole(self, modelData: ModelData) -> Any:
        assert isinstance(modelData.model, JobApplication)
        model: JobApplication = modelData.model

        match modelData.column:
            case "job":
                return (
                    model.job.displayLabel()
                    if hasattr(model.job, "displayLabel")
                    else ""
                )

            case "company":
                return (
                    model.company.displayLabel()
                    if hasattr(model.company, "displayLabel")
                    else ""
                )

        return super()._handleDisplayRole(modelData)

    def sort(
        self, column: int, order: Qt.SortOrder = Qt.SortOrder.AscendingOrder
    ) -> None:
        self._data.sort(
            key=lambda j: self._sortFn(j, self._columns[column]),
            reverse=order == Qt.SortOrder.DescendingOrder,
        )

        self.layoutChanged.emit()

    def _sortFn(self, jobApplication: JobApplication, column: str) -> str | bool | int:
        match column:
            case "job":
                return (
                    jobApplication.job.displayLabel()
                    if hasattr(jobApplication.job, "displayLabel")
                    else ""
                )

            case "company":
                return (
                    jobApplication.company.displayLabel()
                    if hasattr(jobApplication.company, "displayLabel")
                    else ""
                )

        return getattr(jobApplication, column)
