
from orator.orm import has_many

from app.models.Model import Model


class Profession(Model):
    __fillable__ = ["*"]

    __timestamps__ = False

    @has_many
    def jobs(self):
        from app.models.Job import Job
        return Job
