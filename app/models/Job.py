
from orator import SoftDeletes
from orator.orm import has_one, belongs_to, morph_many

from app.models.Model import Model
from app.models.Action import Action


class Job(SoftDeletes, Model):
    __fillable__ = ["*"]

    # __dates__ = ['closing_date', 'deleted_at']
    __dates__ = ['deleted_at']

    @has_one
    def job_application(self):
        from app.models.JobApplication import JobApplication
        return JobApplication

    @belongs_to
    def profession(self):
        from app.models.Profession import Profession
        return Profession

    @belongs_to
    def address(self):
        from app.models.Address import Address
        return Address

    @morph_many('actionable')
    def actions(self):
        return Action
