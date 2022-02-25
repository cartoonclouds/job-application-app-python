from typing import TYPE_CHECKING

from app.models.Model import Model
from orator.orm import *


class Person(SoftDeletes, Model):
    if TYPE_CHECKING:
        id: int
        name: str
        title: str
        email: str

    __fillable__ = ["*"]

    __dates__ = ["deleted_at"]

    @has_many
    def companies(self):
        from app.models.Company import Company

        return Company
