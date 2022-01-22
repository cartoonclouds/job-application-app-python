from orator import Model
from orator.orm import has_many

class Profession(Model):

    @has_many
    def jobs(self):
        return job.Job
