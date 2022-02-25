from typing import TYPE_CHECKING
from orator.orm.scopes.soft_deleting import SoftDeletingScope
from orator.orm.utils import belongs_to, morph_many

from app.models.Model import Model
from app.models.Action import Action


class Job(SoftDeletingScope, Model):
    if TYPE_CHECKING:
        id: int
        title: str
        requires_followup: bool
        pinned: bool
        company_id: int

    __fillable__ = ["*"]

    __dates__ = ['closing_date', 'deleted_at']

    @belongs_to
    def jobApplication(self):
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

    def displayLabel(self) -> str:
        return f"{self.title} (ID {self.id})"
