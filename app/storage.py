

from app.repositories.JobApplicationRepository import JobApplicationRepository


class Storage:
    jobApplications = JobApplicationRepository()
    jobApplications.loadAll()
