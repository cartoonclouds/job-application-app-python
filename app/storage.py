

from app.repositories.JobApplicationRepository import JobApplicationRepository


jobAppRepository = JobApplicationRepository()
jobAppRepository.load_all()
