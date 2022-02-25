from datetime import datetime
from typing import TYPE_CHECKING

import inflection
from config.database import db
from orator.orm import *
from orator.orm.model import Model as oratorModel
from PySide6.QtCore import QObject, Signal


class _ModelCommunicator(QObject):
    creating = Signal(oratorModel)
    created = Signal(oratorModel)
    updating = Signal(oratorModel)
    updated = Signal(oratorModel)
    saving = Signal(oratorModel)
    saved = Signal(oratorModel)
    deleting = Signal(oratorModel)
    deleted = Signal(oratorModel)
    # restoring = Signal(oratorModel)
    # restored = Signal(oratorModel)


_modelCommunicator = _ModelCommunicator()


class Model(oratorModel):
    if TYPE_CHECKING:
        created_at: datetime
        updated_at: datetime
        deleted_at: datetime

    creatingEvent = _modelCommunicator.creating
    createdEvent = _modelCommunicator.created
    updatingEvent = _modelCommunicator.updating
    updatedEvent = _modelCommunicator.updated
    savingEvent = _modelCommunicator.saving
    savedEvent = _modelCommunicator.saved
    deletingEvent = _modelCommunicator.deleting
    deletedEvent = _modelCommunicator.deleted
    # restoringEvent = _modelCommunicator.restoring
    # restoredEvent = _modelCommunicator.restored

    @classmethod
    def _boot(cls):
        cls.creating(lambda m: cls.creatingEvent.emit(m))  # type: ignore
        cls.created(lambda m: cls.createdEvent.emit(m))  # type: ignore
        cls.updating(lambda m: cls.updatingEvent.emit(m))  # type: ignore
        cls.updated(lambda m: cls.updatedEvent.emit(m))  # type: ignore
        cls.saving(lambda m: cls.savingEvent.emit(m))  # type: ignore
        cls.saved(lambda m: cls.savedEvent.emit(m))  # type: ignore
        cls.deleting(lambda m: cls.deletingEvent.emit(m))  # type: ignore
        cls.deleted(lambda m: cls.deletedEvent.emit(m))  # type: ignore
        # cls.restoring(lambda m: cls.restoringEvent.emit(m))  # type: ignore
        # cls.restored(lambda m: cls.restoredEvent.emit(m))   # type: ignore

        super()._boot()

    @classmethod
    def getTableName(cls) -> str:
        """Returns the table name for this model.

        Returns:
            (str)
        """
        # print()
        # __class__
        # __table__
        # print(self.get_table())
        # print(self.__class__)
        # print(*dir(self), sep="\n")
        return inflection.tableize(cls.__name__)

    @classmethod
    def getTableColumns(cls) -> list[str]:
        """Returns a list of column names.

        Returns:
            (list)
        """
        return (
            db.table(db.raw('PRAGMA_TABLE_INFO("' + cls.getTableName() + '")'))
            .select("name")
            .get()
            .pluck("name")
            .all()
        )

    @classmethod
    def getTableColumnCount(cls) -> int:
        """Returns a count of columns for this table.

        Returns:
            (int)
        """
        return (
            db.table(db.raw('PRAGMA_TABLE_INFO("' + cls.getTableName() + '")'))
            .select("name")
            .get()
            .pluck("name")
            .count()
        )

    # Scopes

    # @scope
    # def starts_with(self, query, column, search) -> QueryBuilder:
    #     return query.where(column, 'LIKE', '{}%'.format(search))

    # @scope
    # def like(self, query, column, search) -> QueryBuilder:
    #     return query.where(column, 'LIKE', '%{}%'.format(search))

    # @scope
    # def ends_with(self, query, column, search) -> QueryBuilder:
    #     return query.where(column, 'LIKE', '%{}'.format(search))

    # Model methods

    # @scope
    # def displayLabel(self):
    #     return f"{__name__}#{self.id}"

    # https://wiki.qt.io/Qt_for_Python_Signals_and_Slots#New_syntax:_Signal.28.29_and_Slot.28.29
    # https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/
