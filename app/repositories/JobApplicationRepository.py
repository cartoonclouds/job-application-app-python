import collections
from typing import Mapping, MutableMapping, Sequence
from typing_extensions import Self
from orator import orm

from app.models.JobApplication import JobApplication
from app.repositories.Repository import Repository
from app.utils.CollectionUtility import CollectionUtility

# https://docs.python.org/3/library/collections.html#collections.UserDict
# https://stackoverflow.com/questions/7148419/subclass-dict-userdict-dict-or-abc
# https://stackoverflow.com/questions/61112684/how-to-subclass-a-dictionary-so-it-supports-generic-type-hints

# https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings


# https://github.com/sdispater/backpack


class _JobApplicationRepository(Repository[JobApplication]):
    """A repository which helps dealing with Job Applications.

    Attributes:
        table_columns (list[str]): A list of table columns

    Methods:
        loadAll(): Loads all Job Applications from the database and returns the repository instance.
    """

    @classmethod
    def loadAll(cls) -> Self:
        jobApplications: orm.collection.Collection = JobApplication.all()

        keyedJobApplications = CollectionUtility.keyBy("id", jobApplications)

        return _JobApplicationRepository(dict(keyedJobApplications))


JobApplicationRepository = _JobApplicationRepository.loadAll()
