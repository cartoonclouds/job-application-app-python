from orator import SoftDeletes
from orator.orm import belongs_to, has_many, scope

from app.models.Model import Model


class Company(SoftDeletes, Model):
    __fillable__ = ["*"]

    __dates__ = ['deleted_at']

    @has_many
    def job_applications(self):
        from app.models.JobApplication import JobApplication
        return JobApplication

    @belongs_to
    def address(self):
        from app.models.Address import Address
        return Address

    @belongs_to
    def person(self):
        from app.models.Person import Person
        return Person
