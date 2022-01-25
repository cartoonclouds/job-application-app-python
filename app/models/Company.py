from orator import SoftDeletes
from orator.orm import has_one, has_many, scope

from app.models.Model import Model


class Company(SoftDeletes, Model):
    __fillable__ = ["*"]

    __dates__ = ['deleted_at']

    @has_many
    def job_applications(self):
        from app.models.JobApplication import JobApplication
        return JobApplication

    @has_one
    def address(self):
        from app.models.Address import Address
        return Address

    @has_one
    def person(self):
        from app.models.Person import Person
        return Person

    # @scope
    # def has(self, query, relationship):
    #     return super().has(query, relationship)
