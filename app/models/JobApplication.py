
from orator import SoftDeletes
from orator.orm import belongs_to, has_one

from app.models.Model import Model


class JobApplication(SoftDeletes, Model):
    __fillable__ = ["*"]

    __with__ = ['job', 'company']

    __casts__ = {
        "requires_followup": "bool",
        "pinned": "bool"
    }

    __dates__ = ['deleted_at']

    @belongs_to
    def job(self):
        from app.models.Job import Job
        return Job

    @belongs_to
    def company(self):
        from app.models.Company import Company
        return Company
