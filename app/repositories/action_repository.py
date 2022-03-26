# Application imports
from app.gui.services.statusbar_service import StatusBarServiceProvider
from app.models.Action import Action
from app.repositories.db_repository import DBRepository


class _ActionRepository(DBRepository[Action]):
    """A repository which helps dealing with Actions."""

    def __init__(self) -> None:
        super().__init__(Action)

    def load_all(self):
        StatusBarServiceProvider.message("Loading Actions ...")

        actions = super().load_all()

        StatusBarServiceProvider.message("Loading Actions ... Done!")

        return actions

ActionRepository = _ActionRepository()
