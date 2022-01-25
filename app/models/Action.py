"""Actions model"""

from orator.orm import morph_to, morph_one, morph_many

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
    def following_actions(self):
        return Action
