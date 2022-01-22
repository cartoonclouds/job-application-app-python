from orator import Model, SoftDeletes
from orator.orm import has_one, belongs_to, morph_many


class Job(SoftDeletes, Model):

    @has_one
    def job_application(self):
        return job_application.JobApplication

    @belongs_to
    def profession(self):
        return profession.Profession

    @belongs_to
    def employment_type(self):
        return employment_type.EmploymentType

    @belongs_to
    def address(self):
        return address.Address

    @morph_many('actionable')
    def actions(self):
        return action.Action
