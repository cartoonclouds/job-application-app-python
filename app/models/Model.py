
from masoniteorm.models import Model as mModel
from masoniteorm.query import QueryBuilder
import inflect


class Model(mModel):

    def has(self, query, relationship):
        p = inflect.engine()
        modelClass = self.__class__.__name__.lower()

        modelTable = p.plural(modelClass)
        relationTable = p.plural(relationship)

        hasColumn = QueryBuilder().statement(
            "SELECT 1 FROM pragma_table_info('?') WHERE name = '?'", [modelTable, relationship + '_id'])

        if hasColumn is None:
            return query.join(relationTable, relationTable + '.' + modelClass + '_id', '=', modelTable + "." + self.get_primary_key())
        else:
            return query.join(relationTable, relationTable + ".id", '=', modelTable + "." + relationship + '_id')
