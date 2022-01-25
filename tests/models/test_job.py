
from app.models.Action import Action
from app.models.Address import Address
from app.models.Job import Job
from app.models.JobApplication import JobApplication
from app.models.Profession import Profession

from seeds.factories import factory

import pytest


class TestJob():
    # Constants

    # Fixtures
    @pytest.fixture(scope="function", autouse=True)
    def setup_teardown(self):
        # Setup
        job = factory(Job).create()

        yield job

        # Teardown

    # Helpers

    # Test Cases

    def test_job_has_a_job_application(self, setup_teardown):
        job = setup_teardown

        job.job_application().save(
            factory(JobApplication).make()
        )

        assert job.jobApplication is not None
        assert isinstance(job.jobApplication, JobApplication)

    def test_job_belongs_to_profession(self, setup_teardown):
        job = setup_teardown

        job.profession().associate(
            factory(Profession).create()
        )

        assert job.profession is not None
        assert isinstance(job.profession, Profession)

    def test_job_belongs_to_address(self, setup_teardown):
        job = setup_teardown

        job.address().associate(
            factory(Address).create()
        )

        assert job.address is not None
        assert isinstance(job.address, Address)

    def test_job_has_many_actions(self, setup_teardown):
        job = setup_teardown

        job.actions().save_many([
            factory(Action).make(),
            factory(Action).make()
        ])

        assert job.actions.count() == 2
        assert isinstance(job.actions.get(0), Action)
