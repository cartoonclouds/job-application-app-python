import collections
from typing import Mapping, MutableMapping, Sequence
from typing_extensions import Self
from orator import orm
from app.gui.services.StatusBarService import StatusBarServiceProvider

from app.models.JobApplication import JobApplication
from app.repositories.Repository import Repository
from app.utils.CollectionUtility import CollectionUtility

# https://docs.python.org/3/library/collections.html#collections.UserDict
# https://stackoverflow.com/questions/7148419/subclass-dict-userdict-dict-or-abc
# https://stackoverflow.com/questions/61112684/how-to-subclass-a-dictionary-so-it-supports-generic-type-hints

# https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings


# https://github.com/sdispater/backpack


class _JobApplicationRepository(Repository[JobApplication]):
    """A repository which helps dealing with Job Applications."""

    @classmethod
    def loadAll(cls) -> Repository[JobApplication]:
        # StatusBarServiceProvider.message("Loading Job Applications ...")

        jobApplications: orm.collection.Collection = JobApplication.all()

        keyedJobApplications = CollectionUtility.keyBy("id", jobApplications)

        # StatusBarServiceProvider.message("Loading Job Applications ... Done!")

        return _JobApplicationRepository(dict(keyedJobApplications))  # type: ignore


JobApplicationRepository = _JobApplicationRepository.loadAll()
