from typing import Any, Sequence
from app.gui.services.StatusBarService import StatusBarServiceProvider
from app.models.Model import Model
from app.types import M
from app.utils.Metaclasses.Singleton import Singleton

from pendulum import Pendulum

# ChainMap(class) Self

# instead of M
# T = TypeVar("T", bound=Model)


class DBRepository(dict[str, M], metaclass=Singleton):
    def __init__(self, data: dict[str, M]) -> None:
        """Constructs the job application repository.

        Args:
           data dict[str, M]: [description].
        """
        super().__init__(data)

    @classmethod
    def loadAll(cls) -> Any:
        """Loads all models from the database.

        NOTE: This will clear any models already present!

        Returns:
            (bool) The success of loading from the database
        """
        pass

    def count(self) -> int:
        """Returns the number of loaded Job Applications

        Returns:
            count (int)
        """
        return len(self)

    def values(self) -> Sequence[M]:  # type: ignore
        """Returns values only of keyed dictionary.

        Returns:
            Sequence[M]
        """
        return list(super().values())

    def getAtIndex(self, index: int) -> M | bool:
        """Gets the model at index. If there's nothing at index, False is returned.

        Returns:
            Model | bool: A model
        """
        modelList = self.values()

        try:
            model: M = modelList[index]
        except:
            return False

        return model

    def getColumns(self) -> list[str]:
        """Returns an array of column names for the model of this repository.

        Returns:
            list[str]: The list of columns
        """
        model: M | bool = self.getAtIndex(0)

        return model.getTableColumns() if isinstance(model, Model) else []

    def saveAll(self):
        """
        Saves all changes made to the model instances

        TODO Put onto a separate thread
        """
        modifiedModels = [model for model in self.values()]

        if len(modifiedModels) > 0:
            for model in modifiedModels:
                model.push()  # type: ignore

            StatusBarServiceProvider.message(
                "Last Saved " + str(Pendulum.now().to_time_string()), False
            )
