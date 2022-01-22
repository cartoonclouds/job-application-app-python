from orator import Model, SoftDeletes
from orator.orm import has_many


class Person(SoftDeletes, Model):

    @has_many
    def companies(self):
        return models.company.Company

    @has_many
    def actions(self):
        return models.action.Action
