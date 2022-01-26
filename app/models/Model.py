
from orator import Model as oratorModel
import inflection

from config.database import db


class Model(oratorModel):

    @classmethod
    def table_name(self) -> str:
        """Returns the table name for this model.

        Returns:
            (str)
        """
        return inflection.tableize(self.__name__)

    @classmethod
    def get_table_columns(self) -> list[str]:
        """Returns a list of column names.

        Returns:
            (list)
        """
        return db.table(db.raw('PRAGMA_TABLE_INFO("' + self.table_name() + '")')
                        ).select('name').get().pluck('name').all()

    @classmethod
    def get_table_column_count(self) -> int:
        """Returns a count of columns for this table.

        Returns:
            (int)
        """
        return db.table(db.raw('PRAGMA_TABLE_INFO("' + self.table_name() + '")')
                        ).select('name').get().pluck('name').count()
