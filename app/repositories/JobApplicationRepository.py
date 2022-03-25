# Third party imports
from orator import orm

# Application imports
from app.gui.services.StatusBarService import StatusBarServiceProvider
from app.models.JobApplication import JobApplication
from app.repositories.DBRepository import DBRepository
from app.utils.CollectionUtility import CollectionUtility


class JobApplicationRepository(DBRepository[JobApplication]):
    """A repository which helps dealing with Job Applications."""

    def __init__(self, data: dict[str, JobApplication] | None = None) -> None:
        super().__init__(data or self.loadAll())

    def loadAll(self) -> DBRepository[JobApplication]:
        StatusBarServiceProvider.message("Loading Job Applications ...")

        jobApplications: orm.collection.Collection = JobApplication.all()

        keyedJobApplications = CollectionUtility.keyBy("id", jobApplications)

        StatusBarServiceProvider.message("Loading Job Applications ... Done!")

        return dict(keyedJobApplications)  # type: ignore
