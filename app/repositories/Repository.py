
from app.models.Model import Model


class Repository:
    def loadAll(self) -> bool:
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

    def getColumns(self) -> list[str]:
        model: Model = self.getAtIndex(0)

        return model.getTableColumns()

    def saveChanges(self):
        """
        Saves all changes made to the database 
        """
        pass
