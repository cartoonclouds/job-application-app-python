
from masoniteorm.scopes import scope
from masoniteorm.scopes import SoftDeletesMixin
from masoniteorm.relationships import has_one, has_many

from app.models.Model import Model


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
    def has(self, query, relationship):
        return super().has(query, relationship)
