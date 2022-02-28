from seeds.factories import factory
import pytest

from app.repositories.JobApplicationRepository import JobApplicationRepository
from app.models.JobApplication import JobApplication


class TestJobApplicationRepository():
    # Constants
    JOB_APPLICATION_COUNT = 8

    # Fixtures
    @pytest.fixture(scope="function", autouse=True)
    def setup_teardown(self) -> JobApplicationRepository:
        # Setup
        JobApplication.truncate()
        jobApplications = factory(
            JobApplication, TestJobApplicationRepository.JOB_APPLICATION_COUNT).create()
        jobApplicationRepository = JobApplicationRepository(jobApplications)

        yield jobApplicationRepository

        # Teardown
        JobApplication.truncate()

    # Helpers

    # Test Cases

    def test_job_application_repository_has_correct_count(self, setup_teardown: JobApplicationRepository):
        jobApplicationRepository = setup_teardown

        assert jobApplicationRepository.count(
        ) == TestJobApplicationRepository.JOB_APPLICATION_COUNT

    def test_job_application_repository_can_load_all(self, setup_teardown: JobApplicationRepository):
        jobApplicationRepository = setup_teardown

        jobApplicationRepository.clear()

        ret = jobApplicationRepository.loadAll()

        assert ret == True
        assert jobApplicationRepository.count(
        ) == TestJobApplicationRepository.JOB_APPLICATION_COUNT
