

from app.repositories.JobApplicationRepository import JobApplicationRepository


class Storage:
    jobAppRepository = JobApplicationRepository()
    jobAppRepository.loadAll()
