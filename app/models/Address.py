
from app.models.Model import Model
from orator.orm import has_many


class Address(Model):
    __fillable__ = ["*"]

    @has_many
    def companies(self):
        from app.models.Company import Company
        return Company

    @has_many
    def jobs(self):
        from app.models.Job import Job
        return Job
