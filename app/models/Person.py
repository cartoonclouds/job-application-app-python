
from orator import SoftDeletes
from orator.orm import has_many

from app.models.Model import Model


class Person(SoftDeletes, Model):
    __fillable__ = ["*"]

    __dates__ = ['deleted_at']

    @has_many
    def companies(self):
        from app.models.Company import Company
        return Company

    # @has_many
    # def actions(self):
    #     from app.models.Action import ComActionpany
    #     return Action
