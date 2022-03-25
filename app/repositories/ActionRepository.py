# Third party imports
from orator import orm

# Application imports
from app.gui.services.StatusBarService import StatusBarServiceProvider
from app.models.Action import Action
from app.repositories.DBRepository import DBRepository
from app.utils.CollectionUtility import CollectionUtility


class ActionRepository(DBRepository[Action]):
    """A repository which helps dealing with Actions."""

    def __init__(self, data: dict[str, Action] | None = None) -> None:
        super().__init__(data or self.loadAll())

    def loadAll(self) -> DBRepository[Action]:
        StatusBarServiceProvider.message("Loading Actions ...")

        actions: orm.collection.Collection = Action.all()

        keyedActions = CollectionUtility.keyBy("id", actions)

        StatusBarServiceProvider.message("Loading Actions ... Done!")

        return dict(keyedActions)  # type: ignore
