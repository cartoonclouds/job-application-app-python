"""Actions model"""
from typing import TYPE_CHECKING

from app.models.Model import Model
from orator.orm import *


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

    @morph_to
    def actionable(self):
        return

    @morph_many("actionable")
    def childActions(self):
        return Action

    @has_one("id", "actionable_id")
    def parentAction(self):
        return Action
