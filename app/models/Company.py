# Standard Library
from typing import TYPE_CHECKING

# Third party imports
from orator.orm import mixins, utils

# Application imports
from app.models.Model import Model


class Company(mixins.SoftDeletes, Model):
    if TYPE_CHECKING:
        id: int
        name: str
        email: str
        phone: int
        website: str
        comments: str
        address_id: int
        person_id: int

    __fillable__ = ["*"]

    __dates__ = ["deleted_at"]

    @utils.has_many
    def jobApplications(self):
        # Application imports
        from app.models.JobApplication import JobApplication

        return JobApplication

    @utils.belongs_to
    def address(self):
        # Application imports
        from app.models.Address import Address

        return Address

    @utils.belongs_to
    def person(self):
        # Application imports
        from app.models.Person import Person

        return Person

    def displayLabel(self) -> str:
        return f"{self.name} (ID {self.id})"
