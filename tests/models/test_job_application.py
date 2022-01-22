
from app.models.Job import Job
from app.models.Company import Company


class TestJobApplication():
    # Constants

    # Fixtures

    # Helpers

    # Test Cases

    # https://stackoverflow.com/questions/14549405/python-check-instances-of-classes
    def test_job_application_has_a_job(self, get_job_application):
        jobApplication = get_job_application()
        job = jobApplication.job
        
        assert isinstance(job, Job)

    def test_job_application_has_a_company(self, get_job_application):
        jobApplication = get_job_application()
        company = jobApplication.company
        
        assert isinstance(company, Company)
