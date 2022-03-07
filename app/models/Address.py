# Standard Library
from typing import TYPE_CHECKING

# Third party imports
from orator.orm import utils

# Application imports
from app.models.Model import Model


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

    @utils.has_many
    def companies(self):
        # Application imports
        from app.models.Company import Company

        return Company

    @utils.has_many
    def jobs(self):
        # Application imports
        from app.models.Job import Job

        return Job
