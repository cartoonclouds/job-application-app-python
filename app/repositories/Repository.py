
from typing import Union

from app.models.Model import Model


class Repository:
    def load_all(self) -> bool:
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

    def get_at_index(self, index: int) -> Union[Model, bool]:
        """Gets the Job Application at index. If there's nothing at index, False is returned.

        Returns:
            (Union[JobApplication, bool]): A Job Application
        """
        modelList = list(self.items())

        try:
            model: Model = modelList[index][1]
        except:
            return False

        return model

    def get_columns(self) -> list[str]:
        model: Model = self.get_at_index(0)

        return model.get_table_columns()
