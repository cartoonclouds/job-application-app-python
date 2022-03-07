# Standard Library
from typing import TYPE_CHECKING

# Third party imports
from orator.orm import utils

# Application imports
from app.models.Model import Model


class Profession(Model):
    if TYPE_CHECKING:
        id: int
        profession: str

    __fillable__ = ["*"]

    __timestamps__ = False

    @utils.has_many
    def jobs(self):
        # Application imports
        from app.models.Job import Job

        return Job
