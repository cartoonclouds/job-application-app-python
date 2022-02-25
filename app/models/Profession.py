
from typing import TYPE_CHECKING
from orator.orm.utils import has_many

from app.models.Model import Model


class Profession(Model):
    if TYPE_CHECKING:
        id: int
        profession: str
        
    __fillable__ = ["*"]

    __timestamps__ = False

    @has_many
    def jobs(self):
        from app.models.Job import Job
        return Job
