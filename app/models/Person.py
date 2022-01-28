from orator.orm.scopes.soft_deleting import SoftDeletingScope
from orator.orm.utils import has_many

from app.models.Model import Model


class Person(SoftDeletingScope, Model):
    __fillable__ = ["*"]

    __dates__ = ['deleted_at']

    @has_many
    def companies(self):
        from app.models.Company import Company
        return Company
