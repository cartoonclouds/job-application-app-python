from orator import Model
from orator.orm import has_many


class EmploymentType(Model):

    @has_many
    def jobs(self):
        return job.Job
