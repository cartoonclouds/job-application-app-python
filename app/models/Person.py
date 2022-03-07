# Standard Library
from typing import TYPE_CHECKING

# Third party imports
from orator.orm import utils, mixins

# Application imports
from app.models.Model import Model


class Person(mixins.SoftDeletes, Model):
    if TYPE_CHECKING:
        id: int
        name: str
        title: str
        email: str

    __fillable__ = ["*"]

    __dates__ = ["deleted_at"]

    @utils.has_many
    def companies(self):
        # Application imports
        from app.models.Company import Company

        return Company
