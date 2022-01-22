from masoniteorm.models import Model
from masoniteorm.relationships import has_many


class Profession(Model):
    __timestamps__ = False

    @has_many("id", "profession_id")
    def jobs(self):
        from app.models.Job import Job
        return Job
