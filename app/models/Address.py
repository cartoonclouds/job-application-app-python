from masoniteorm.models import Model
from masoniteorm.query import QueryBuilder
from masoniteorm.scopes import scope
from masoniteorm.relationships import belongs_to, has_many
import inflect


class Address(Model):

    @has_many('id', 'address_id')
    def companies(self):
        from app.models.Company import Company
        return Company

    @has_many('id', 'address_id')
    def jobs(self):
        from app.models.Job import Job
        return Job

    @scope
    def has(self, query, relationship):
        p = inflect.engine()

        # if p.get_count(relationship) == 0:
        relationTable = p.plural_noun(relationship)

        hasColumn = QueryBuilder().statement(
            "SELECT 1 FROM pragma_table_info('?') WHERE name = '?'", [self.get_table_name(), relationTable + '_id'])

        if hasColumn is None:
            return query.join(relationTable, relationTable + ".id", '=', self.get_table_name() + "." + relationship + '_id')
        else:
            return query.join(relationTable, relationTable + '.' + self.__class__.__name__.lower() + '_id', '=', self.get_table_name() + "." + self.get_primary_key())
