from masoniteorm.models import Model
from masoniteorm.relationships import morph_to


class Action(Model):

    __casts__ = {
        "requires_followup": "boolean",
    }

    @morph_to
    def actionable(self):
        return

    # @morph_many('actionable')
    # def parent_action(self):
    #     return Action
