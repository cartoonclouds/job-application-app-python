from typing import TYPE_CHECKING

from app.models.Model import Model
from orator.orm import *


class JobApplication(SoftDeletes, Model):
    if TYPE_CHECKING:
        id: int
        title: str
        requires_followup: bool
        pinned: bool
        company_id: int

    __fillable__ = ["*"]

    __with__ = ["job", "company"]

    __casts__ = {"requires_followup": "bool", "pinned": "bool"}

    __dates__ = ["deleted_at"]

    @has_one
    def job(self):
        from app.models.Job import Job

        return Job

    @belongs_to
    def company(self):
        from app.models.Company import Company

        return Company
