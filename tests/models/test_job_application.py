
from app.models.Job import Job
from app.models.Company import Company
from app.models.JobApplication import JobApplication

from seeds.factories import factory

import pytest


class TestJobApplication():
    # Constants

    # Fixtures
    @pytest.fixture(scope="function", autouse=True)
    def setup_teardown(self):
        # Setup
        jobApplication = factory(JobApplication).create()

        yield jobApplication

        # Teardown

    # Helpers

    # Test Cases

    # https://stackoverflow.com/questions/14549405/python-check-instances-of-classes
    def test_job_application_belongs_to_job(self, setup_teardown):
        jobApplication = setup_teardown

        jobApplication.job().associate(
            factory(Job).create()
        )

        assert jobApplication.job is not None
        assert isinstance(jobApplication.job, Job)

    def test_job_application_belongs_to_company(self, setup_teardown):
        jobApplication = setup_teardown

        jobApplication.company().associate(
            factory(Company).create()
        )

        assert jobApplication.company is not None
        assert isinstance(jobApplication.company, Company)
