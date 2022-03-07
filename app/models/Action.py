"""Actions model"""
# Standard Library
from typing import TYPE_CHECKING

# Third party imports
from orator.orm import utils

# Application imports
from app.models.Model import Model


class Action(Model):
    if TYPE_CHECKING:
        id: int
        title: str
        requires_followup: bool
        pinned: bool
        contact_method: str
        actionable_id: int
        actionable_type: str
        person_id: int

    __fillable__ = ["*"]

    __casts__ = {
        "requires_followup": "boolean",
        "pinned": "boolean",
    }

    @utils.morph_to
    def actionable(self):
        return

    @utils.morph_many("actionable")
    def childActions(self):
        return Action

    @utils.has_one("id", "actionable_id")
    def parentAction(self):
        return Action
