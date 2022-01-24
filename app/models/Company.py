from masoniteorm.models import Model
from masoniteorm.scopes import scope
from masoniteorm.scopes import SoftDeletesMixin
from masoniteorm.relationships import has_one, has_many
from masoniteorm.query import QueryBuilder
import inflect


class Company(SoftDeletesMixin, Model):

    @has_many('id', 'company_id')
    def job_applications(self):
        from app.models.JobApplication import JobApplication
        return JobApplication

    @has_one('id', 'address_id')
    def address(self):
        from app.models.Address import Address
        return Address

    @has_one('id', 'person_id')
    def person(self):
        from app.models.Person import Person
        return Person

    @scope
    def hasWith(self, query, relationship):
        p = inflect.engine()
        relationTable = p.plural(relationship)

        hasColumn = QueryBuilder().statement(
            "SELECT 1 FROM pragma_table_info('?') WHERE name = '?'", [self.get_table_name(), relationship + '_id'])

        print(")))))))))))))))))", hasColumn)

        if hasColumn is None:
            return query.join(relationTable, relationTable + '.' + self.__class__.__name__.lower() + '_id', '=', self.get_table_name() + "." + self.get_primary_key())
        else:
            return query.join(relationTable, relationTable + ".id", '=', self.get_table_name() + "." + relationship + '_id')
