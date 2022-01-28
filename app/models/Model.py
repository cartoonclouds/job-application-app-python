from orator.orm.model import Model as oratorModel
from orator.query.builder import QueryBuilder  # or maybe QueryBuilder
from orator.orm.utils import scope

import inflection

from config.database import db


class Model(oratorModel):

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
        return db.table(
            db.raw('PRAGMA_TABLE_INFO("' + cls.getTableName() + '")')
        ).select('name').get().pluck('name').all()

    @ classmethod
    def getTableColumnCount(cls) -> int:
        """Returns a count of columns for this table.

        Returns:
            (int)
        """
        return db.table(
            db.raw('PRAGMA_TABLE_INFO("' + cls.getTableName() + '")')
        ).select('name').get().pluck('name').count()

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
