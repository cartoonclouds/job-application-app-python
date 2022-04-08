# Application imports
from app.gui.services.statusbar_service import StatusBarServiceProvider
from app.models.Profession import Profession
from app.repositories.db_repository import DBRepository


class _ProfessionRepository(DBRepository[Profession]):
    """A repository which helps dealing with Professions."""

    def __init__(self) -> None:
        super().__init__(Profession)

    def load_all(self):
        StatusBarServiceProvider.message("Loading Professions ...")

        professions = super().load_all()

        StatusBarServiceProvider.message("Loading Professions ... Done!")

        return professions


ProfessionRepository = _ProfessionRepository()
