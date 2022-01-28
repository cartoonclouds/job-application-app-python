from orator.orm.scopes.soft_deleting import SoftDeletingScope
from orator.orm.utils import belongs_to, has_many

from app.models.Model import Model


class Company(SoftDeletingScope, Model):
    __fillable__ = ["*"]

    __dates__ = ['deleted_at']

    @has_many
    def jobApplications(self):
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

    def displayLabel(self):
        return f"#{self.id} {self.name}"
