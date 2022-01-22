from orator import Model
from orator.orm import belongs_to, has_many


class Address(Model):

    @has_many
    def companies(self):
        return company.Company

    @has_many
    def jobs(self):
        return job.Job
