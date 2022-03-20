from collections import UserDict
from typing import Generic, Mapping, MutableMapping, Sequence
from typing_extensions import Self
from app.models.Model import Model
from app.types import M

# ChainMap(class) Self
# See https://mypy.readthedocs.io/en/stable/common_issues.html#variables-vs-type-aliases


class Repository(dict[str, M]):
    def __init__(self, data: dict[str, M] | None = None) -> None:
        """Constructs the job application repository.

        Args:
           data dict[str, M] | None: [description]. Defaults to None.
        """
        if data is not None:
            super().__init__(data)

    @classmethod
    def loadAll(cls) -> Self:
        """Loads all models from the database.

        NOTE: This will clear any models already present!

        Returns:
            (bool) The success of loading from the database
        """
        pass

    @classmethod
    def count(self) -> int:
        """Returns the number of loaded Job Applications

        Returns:
            count (int)
        """
        return len(self)

    def getAtIndex(self, index: int) -> Model | bool:
        """Gets the Job Application at index. If there's nothing at index, False is returned.

        Returns:
            (JobApplication | bool): A Job Application
        """
        modelList = list(self.items())

        try:
            model: Model = modelList[index][1]
        except:
            return False

        return model

    def getColumns(self):
        model: Model | bool = self.getAtIndex(0)

        if isinstance(model, Model):
            return model.getTableColumns()

    def saveChanges(self):
        """
        Saves all changes made to the database
        """
        pass

    def values(self) -> Sequence[M]:
        return list(super().values())
