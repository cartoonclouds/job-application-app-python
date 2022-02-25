from typing import TYPE_CHECKING

from app.models.Model import Model
from orator.orm import *


class Address(Model):
    if TYPE_CHECKING:
        id: int
        address_line_1: str
        address_line_2: str
        suburb: str
        city: str
        state: str
        postcode: int
        country: str
        is_user: bool

    __fillable__ = ["*"]

    @has_many
    def companies(self):
        from app.models.Company import Company

        return Company

    @has_many
    def jobs(self):
        from app.models.Job import Job

        return Job
