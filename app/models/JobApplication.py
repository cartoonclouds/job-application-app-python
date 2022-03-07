# Standard Library
from typing import TYPE_CHECKING

# Third party imports
from orator.orm import mixins, utils
from app.models.Company import Company
from app.models.Job import Job

# Application imports
from app.models.Model import Model


class JobApplication(mixins.SoftDeletes, Model):
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

    @utils.has_one
    def job(self):
        # Application imports
        from app.models.Job import Job

        return Job

    @utils.belongs_to
    def company(self):
        # Application imports
        from app.models.Company import Company

        return Company

    def createFullJobApplication(self) -> "JobApplication":
        jobApp = JobApplication()
        jobApp.job().save(Job())
        jobApp.company().associate(Company())

        return jobApp