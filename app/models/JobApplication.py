from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin
from masoniteorm.relationships import belongs_to, has_one


class JobApplication(SoftDeletesMixin, Model):
    __guarded__ = []

    __with__ = ['job', 'company']

    __casts__ = {
        "requires_followup": "bool",
        "pinned": "bool"
    }

    @has_one('id', 'job_id')
    def job(self):
        from app.models.Job import Job
        return Job

    @has_one('id', 'company_id')
    def company(self):
        from app.models.Company import Company
        return Company
