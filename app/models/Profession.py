
from masoniteorm.relationships import has_many

from app.models.Model import Model


class Profession(Model):
    __timestamps__ = False


    @has_many("id", "profession_id")
    def jobs(self):
        from app.models.Job import Job
        return Job
