
from app.models.Model import Model
from masoniteorm.scopes import scope
from masoniteorm.relationships import has_many


class Address(Model):

    @has_many('id', 'address_id')
    def companies(self):
        from app.models.Company import Company
        return Company

    @has_many('id', 'address_id')
    def jobs(self):
        from app.models.Job import Job
        return Job

    @scope
    def has(self, query, relationship):
        return super().has(query, relationship)
