"""Actions model"""

from masoniteorm.relationships import morph_to

from app.models.Model import Model
# from app.models.Job import Job


class Action(Model):
    __casts__ = {
        "requires_followup": "boolean",
        "pinned": "boolean",
    }

    @morph_to
    def actionable(self):
        return
