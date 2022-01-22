from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to, has_many


class Address(Model):

    @has_many('id', 'address_id')
    def companies(self):
        from app.models.Company import Company
        return Company

    @has_many('id', 'address_id')
    def jobs(self):
        from app.models.Job import Job
        return Job
