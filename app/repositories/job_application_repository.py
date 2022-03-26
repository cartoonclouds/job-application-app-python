# Application imports
from app.gui.services.statusbar_service import StatusBarServiceProvider
from app.models.JobApplication import JobApplication
from app.repositories.db_repository import DBRepository


class _JobApplicationRepository(DBRepository[JobApplication]):
    """A repository which helps dealing with Job Applications."""

    def __init__(self) -> None:
        super().__init__(JobApplication)

    def load_all(self):
        StatusBarServiceProvider.message("Loading Job Applications ...")

        jobApplications = super().load_all()

        StatusBarServiceProvider.message("Loading Job Applications ... Done!")

        return jobApplications


JobApplicationRepository = _JobApplicationRepository()
