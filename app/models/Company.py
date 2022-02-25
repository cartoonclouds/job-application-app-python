from typing import TYPE_CHECKING

from app.models.Model import Model
from orator.orm import *


class Company(SoftDeletes, Model):
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

    @has_many
    def jobApplications(self):
        from app.models.JobApplication import JobApplication

        return JobApplication

    @belongs_to
    def address(self):
        from app.models.Address import Address

        return Address

    @belongs_to
    def person(self):
        from app.models.Person import Person

        return Person

    def displayLabel(self) -> str:
        return f"{self.name} (ID {self.id})"
