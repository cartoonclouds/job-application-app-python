# Standard Library
from datetime import datetime
from typing import TYPE_CHECKING, Any, Mapping, Sequence, Type, TypeAlias, TypeVar, cast

# Framework imports
from PySide6.QtCore import QObject, Signal

# Third party imports
import inflection
from config.database import db
from orator import orm, query
from orator.orm import utils
from orator.orm.model import Model as oratorModel


class Model(oratorModel):
    if TYPE_CHECKING:
        created_at: datetime
        updated_at: datetime
        deleted_at: datetime

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
        modified = Signal(oratorModel)

    _modelCommunicator = _ModelCommunicator()

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
    modifiedEvent = _modelCommunicator.modified

    # def __setattr__(self, key, value):
    #     Model.modifiedEvent.emit(self)  # type: ignore

    #     return super().__setattr__(key, value)

    # Class variables are accessed with the instance.variable or class_name.variable syntaxes.

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

    @classmethod
    def allKeyedBy(cls, key: str = oratorModel.__primary_key__) -> dict[str, "Model"]:
        return dict(map(lambda x: (getattr(x, key), x), super().all().items))

    def get_key(self) -> str:
        """
        Get the value of the model's primary key.
        """
        return cast(str, super().get_key())

    # Scopes

    # @utils.scope
    # def starts_with(
    #     cls, query: schema.query.QueryBuilder, column: query.QueryBuilder | str, text: str
    # ) -> query.QueryBuilder:
    #     return query.where(column, "LIKE", "{}%".format(text))

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
