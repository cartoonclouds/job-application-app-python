
import collections
from typing import Iterable, MutableMapping
from app.models.JobApplication import JobApplication
from app.repositories.Repository import Repository
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

    def __init__(self, d: MutableMapping[str | int, JobApplication] | Iterable[JobApplication] | None = None) -> None:
        """Constructs the job application repository.

        Args:
            d (MutableMapping[str | int, JobApplication] | Iterable[JobApplication], optional): [description]. Defaults to None.
        """
        if not isinstance(d, dict) and d is not None:
            d = CollectionUtility.key_by('id', d)

        super().__init__(d)

    def loadAll(self) -> bool:
        try:
            jobApplications = JobApplication.get()
        except:
            return False

        keyedJobApplications = CollectionUtility.key_by(
            'id', jobApplications)

        self.data = dict(keyedJobApplications)

        return True
