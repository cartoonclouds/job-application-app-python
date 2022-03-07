import collections
import typing

from app.models.JobApplication import JobApplication
from app.repositories.Repository import Repository
from app.utils.CollectionUtility import CollectionUtility

# https://docs.python.org/3/library/collections.html#collections.UserDict
# https://stackoverflow.com/questions/7148419/subclass-dict-userdict-dict-or-abc
# https://stackoverflow.com/questions/61112684/how-to-subclass-a-dictionary-so-it-supports-generic-type-hints

# https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings


# https://github.com/sdispater/backpack


class JobApplicationRepository(
    collections.UserDict[str | int, JobApplication], Repository
):
    """A repository which helps dealing with Job Applications.

    Attributes:
        table_columns (list[str]): A list of table columns

    Methods:
        loadAll(): Loads all Job Applications from the database.
    """

    def __init__(
        self,
        d: typing.MutableMapping[str | int, JobApplication]
        | typing.Iterable[JobApplication]
        | None = None,
    ) -> None:
        """Constructs the job application repository.

        Args:
            d (typing.MutableMapping[str | int, JobApplication] | typing.Iterable[JobApplication], optional): [description]. Defaults to None.
        """
        if not isinstance(d, dict) and d is not None:
            d = CollectionUtility.keyBy("id", d)

        super().__init__(d)

    def loadAll(self) -> bool:
        try:
            jobApplications: JobApplication = JobApplication.get()
        except:
            return False

        keyedJobApplications = CollectionUtility.keyBy("id", jobApplications)

        self.data = dict(keyedJobApplications)

        return True

    def values(self) -> typing.ValuesView[JobApplication]:
        return super().values()
