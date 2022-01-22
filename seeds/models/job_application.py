from orator import Model, SoftDeletes
from orator.orm import belongs_to

class JobApplication(SoftDeletes, Model):

    @belongs_to
    def job(self):
        return job.Job

    @belongs_to
    def company(self):
        return company.Company
