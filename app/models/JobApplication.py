from orator.orm.scopes.soft_deleting import SoftDeletingScope
from orator.orm.utils import belongs_to, has_one
from orator.orm.scopes.scope import Scope
from PySide6.QtCore import Signal, QObject

from app.models.Model import Model


class JobApplication(SoftDeletingScope, Model):
    __fillable__ = ["*"]

    __with__ = ['job', 'company']

    __casts__ = {
        "requires_followup": "bool",
        "pinned": "bool"
    }

    __dates__ = ['deleted_at']

    @has_one
    def job(self):
        from app.models.Job import Job
        return Job

    @belongs_to
    def company(self):
        from app.models.Company import Company
        return Company
