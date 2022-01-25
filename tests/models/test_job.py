
from app.models.Address import Address
from app.models.JobApplication import JobApplication
from app.models.Profession import Profession


class TestJob():
    # Constants

    # Fixtures

    # Helpers

    # Test Cases
    def test_job_belongs_to_job_application(self, get_job):
        job = get_job()
        jobApplication = job.job_application

        assert isinstance(jobApplication, JobApplication)

    def test_job_has_a_profession(self, get_job):
        job = get_job()
        profession = job.profession

        assert isinstance(profession, Profession)

    def test_job_has_an_address(self, get_job):
        job = get_job()
        address = job.address

        assert isinstance(address, Address)
