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
    def hasWith(self, query, relationship):
        p = inflect.engine()
        relationTable = p.plural(relationship)

        return query.join(relationTable, relationTable + '.' + self.__class__.__name__.lower() + '_id', '=', self.get_table_name() + "." + self.get_primary_key())
