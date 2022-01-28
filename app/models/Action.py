"""Actions model"""

from orator.orm import morph_to, morph_many, has_one

from app.models.Model import Model


class Action(Model):
    __fillable__ = ["*"]

    __casts__ = {
        "requires_followup": "boolean",
        "pinned": "boolean",
    }

    @morph_to
    def actionable(self):
        return

    @morph_many('actionable')
    def childActions(self):
        return Action

    @has_one('id', 'actionable_id')
    def parentAction(self):
        return Action
