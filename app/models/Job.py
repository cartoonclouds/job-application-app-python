# Standard Library
from typing import TYPE_CHECKING

# Third party imports
from orator.orm import mixins, utils

# Application imports
from app.models.Model import Model


class Job(mixins.SoftDeletes, Model):
    if TYPE_CHECKING:
        id: int
        title: str
        requires_followup: bool
        pinned: bool
        company_id: int

    __fillable__ = ["*"]

    __dates__ = ["closing_date", "deleted_at"]

    @utils.belongs_to
    def jobApplication(self):
        # Application imports
        from app.models.JobApplication import JobApplication

        return JobApplication

    @utils.belongs_to
    def profession(self):
        # Application imports
        from app.models.Profession import Profession

        return Profession

    @utils.belongs_to
    def address(self):
        # Application imports
        from app.models.Address import Address

        return Address

    @utils.morph_many("actionable")
    def actions(self):
        # Application imports
        from app.models.Action import Action

        return Action

    def displayLabel(self) -> str:
        return f"{self.title} (ID {self.id})"
