
import collections
from typing import Collection, Dict, Iterable, MutableMapping, NewType, Union
from app.models.JobApplication import JobApplication
from app.repositories.IRepository import Repository
from app.utilities.CollectionUtility import CollectionUtility

# https://docs.python.org/3/library/collections.html#collections.UserDict
# https://stackoverflow.com/questions/7148419/subclass-dict-userdict-dict-or-abc
# https://stackoverflow.com/questions/61112684/how-to-subclass-a-dictionary-so-it-supports-generic-type-hints

# https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings


class JobApplicationRepository(collections.UserDict, Repository):
    """A repository which helps dealing with Job Applications.

        Attributes:
            table_columns (list[str]): A list of table columns

        Methods:
            loadAll(): Loads all Job Applications from the database.
    """

    def __init__(self, d: Union[MutableMapping[Union[str, int], JobApplication], Iterable[JobApplication]] = None) -> None:
        """Constructs the job application repository.

        Args:
            d (Union[MutableMapping[Union[str, int], JobApplication], Iterable[JobApplication]], optional): [description]. Defaults to None.
        """
        if not isinstance(d, dict) and d is not None:
            d = CollectionUtility.key_by('id', d)

        super().__init__(d)

    def load_all(self) -> bool:
        """Loads all Job Applications from the database.

            NOTE: This will clear any Job Applications already present!

            Returns:
                (bool) The success of loading from the database
        """
        try:
            jobApplications = JobApplication.get()
        except:
            return False

        keyedJobApplications = CollectionUtility.key_by(
            'id', jobApplications)

        self.data = dict(keyedJobApplications)

        return True

    def count(self) -> int:
        """Returns the number of loaded Job Applications

            Returns:
                count (int)
        """
        return len(self)

    def getAtIndex(self, index: int) -> Union[JobApplication, bool]:
        """Gets the Job Application at index. If there's nothing at index, False is returned.

        Returns:
            (Union[JobApplication, bool]): A Job Application
        """
        jobAppList = list(self.items())

        try:
            model: JobApplication = jobAppList[index][1]
        except:
            return False

        return model

    def get_columns(self):
        model: JobApplication = self.getAtIndex(0)

        return model.get_table_columns()
