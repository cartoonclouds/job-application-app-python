
from masoniteorm.scopes import SoftDeletesMixin
from masoniteorm.relationships import has_one, belongs_to, morph_to

from app.models.Model import Model
from app.models.Action import Action


class Job(SoftDeletesMixin, Model):
    __guarded__ = []

    @belongs_to('id', 'job_id')
    def job_application(self):
        from app.models.JobApplication import JobApplication
        return JobApplication

    @has_one('id', 'profession_id')
    def profession(self):
        from app.models.Profession import Profession
        return Profession

    @has_one('id', 'address_id')
    def address(self):
        from app.models.Address import Address
        return Address

    @morph_to('actionable')
    def actions(self):
        return Action
