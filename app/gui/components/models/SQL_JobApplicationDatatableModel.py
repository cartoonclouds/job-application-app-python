import datetime
from PySide6.QtSql import (
    QSqlDatabase,
    QSqlDriver,
    QSqlRelationalTableModel,
    QSqlRelation,
    QSqlTableModel,
    QSqlQuery,
)
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QFrame, QMessageBox
from typing import Mapping, Any, Sequence
from app.gui.components.datatable.DatatableModel import DatatableModel, ModelData
from app.models.JobApplication import JobApplication
from PySide6.QtCore import QModelIndex, QPersistentModelIndex, Qt
from app.utilities.mixins.DatabaseConnection import DatabaseConnectionMixin
from config.database import db

# https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTableWidgetItem.html


class JobApplicationDatatableModel(QSqlRelationalTableModel, DatabaseConnectionMixin):
    """A datatable model for Job Applications."""

    def __init__(self, table: str) -> None:
        # https://realpython.com/python-pyqt-database/
        # https://doc.qt.io/qtforpython/tutorials/qmlsqlintegration/qmlsqlintegration.html
        # https://doc.qt.io/qtforpython/overviews/sql-model.html
        # https://doc.qt.io/qtforpython/overviews/sql-presenting.html
        # https://doc.qt.io/qt-6/qtsql-sqlwidgetmapper-example.html
        # https://doc.qt.io/qt-6/qtwidgets-itemviews-combowidgetmapper-example.html
        # https://doc.qt.io/qt-6/examples-itemviews.html

        # https://doc.qt.io/qtforpython/examples/example_sql__books.html
        # https://doc.qt.io/qtforpython/overviews/qtsql-drilldown-example.html

        # https://doc.qt.io/qtforpython/PySide6/QtSql/QSqlQueryModel.html - A read-only model based on an arbitrary SQL query
        # https://doc.qt.io/qtforpython/PySide6/QtSql/QSqlTableModel.html - A read-write model that works on a single table
        # https://doc.qt.io/qtforpython/PySide6/QtSql/QSqlRelationalTableModel.html - A QSqlTableModel subclass with foreign key support
        #   QSqlRelationalDelegate
        #       https://doc.qt.io/qtforpython/PySide6/QtSql/QSqlRecord.html
        #           https://doc.qt.io/qtforpython-6/PySide6/QtSql/QSqlField.html
        super(JobApplicationDatatableModel, self).__init__(db=self.db())

        # self.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.setQuery(
            QSqlQuery(
                db.table("job_applications")
                .join("jobs", "job_applications.id", "=", "jobs.job_application_id")
                .select("job_applications.*", "jobs.job_application_id")
                .to_sql(),
                self.db(),
            )
        )

        # self.setHeaders()
        self.setRelationships()

        self.select()

        # debug(model.record(1).value("title"))

    @property
    def columns(self):
        return dict(
            zip(
                [
                    "id",
                    "title",
                    "requires_followup",
                    "company_id",
                    "job_application_id",
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

    def setRelationships(self):
        # self.setRelation(
        #     self.fieldIndex("job_application_id"),
        #     QSqlRelation("jobs", "job_application_id", "title"),
        # )
        self.setRelation(
            self.fieldIndex("company_id"), QSqlRelation("companies", "id", "name")
        )

    def setHeaders(self):
        for field, display in self.columns.items():
            self.setHeaderData(self.fieldIndex(field), Qt.Horizontal, display)

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int) -> Any:
        return super().data(index, role)
        modelData = self.getModelData(index)

        match role:
            case Qt.DisplayRole:
                return self._handleDisplayRole(modelData)

            case Qt.TextAlignmentRole:
                return self._handleTextAlignmentRole(modelData)

            # case Qt.DecorationRole:
            # case Qt.SizeHintRole:
            # case Qt.EditRole:
            # case Qt.ToolTipRole:
            # case Qt.StatusTipRole:
            # case Qt.WhatsThisRole:

    # def _handleDisplayRole(self, modelData: ModelData) -> Any:
    #     model: JobApplication = modelData.model

    #     # Perform per-type checks and render accordingly.
    #     if isinstance(modelData.value, datetime.datetime):
    #         # Render time to YYY-MM-DD.
    #         return modelData.value.strftime("%Y-%m-%d")

    #     if isinstance(modelData.value, float):
    #         # Render float to 2 dp
    #         # return "%.2f" % value
    #         return modelData.value

    #     if type(modelData.value) == bool:
    #         return

    #     if modelData.column == "job":
    #         return model.job.displayLabel()

    #     if modelData.column == "company":
    #         return model.company.displayLabel()

    #     return modelData.value

    # def _handleTextAlignmentRole(self, modelData: ModelData) -> Any:
    #     if modelData.column == "id":
    #         return Qt.AlignCenter

    #     if type(modelData.value) == bool:
    #         return Qt.AlignCenter

    #     if isinstance(modelData.value, datetime.datetime):
    #         return Qt.AlignVCenter + Qt.AlignRight
