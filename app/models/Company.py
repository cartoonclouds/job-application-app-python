from datetime import datetime
from orator.orm.scopes.soft_deleting import SoftDeletingScope
from orator.orm.utils import belongs_to, has_many

from app.models.Model import Model
from typing import TYPE_CHECKING

class Company(SoftDeletingScope, Model):
    if TYPE_CHECKING:
        id: int
        name: str
        email: str
        phone: int
        website: str
        comments: str
        address_id: int
        person_id: int
        created_at: datetime
        updated_at: datetime
        deleted_at: datetime
        
    __fillable__ = ["*"]

    __dates__ = ['deleted_at']

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
