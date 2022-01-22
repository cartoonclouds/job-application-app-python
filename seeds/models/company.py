from email.headerregistry import Address
from orator import Model, SoftDeletes
from orator.orm import belongs_to, has_many


class Company(SoftDeletes, Model):

    @has_many
    def job_application(self):
        return job_application.JobApplication

    @belongs_to
    def address(self):
        return address.Address

    @belongs_to
    def person(self):
        return person.Person
