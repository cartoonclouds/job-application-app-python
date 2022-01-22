from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin
from masoniteorm.relationships import has_many


class Person(SoftDeletesMixin, Model):

    @has_many("id", "person_id")
    def companies(self):
        from app.models.Company import Company
        return Company

    # @has_many
    # def actions(self):
    #     from app.models.Action import ComActionpany
    #     return Action
