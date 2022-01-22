from orator import Model
from orator.orm import morph_to, morph_many


class Action(Model):

    @morph_to
    def actionable(self):
        return

    @morph_many('actionable')
    def parent_action(self):
        return action.Action
