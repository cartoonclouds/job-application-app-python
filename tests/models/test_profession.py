
from app.models.Job import Job
from app.models.Profession import Profession

from seeds.factories import factory

import pytest


class TestProfession():
    # Constants

    # Fixtures
    @pytest.fixture(scope="function", autouse=True)
    def setup_teardown(self):
        # Setup
        profession = factory(Profession).create()

        yield profession

        # Teardown

    # Helpers

    # Test Cases
    def test_profession_has_many_jobs(self, setup_teardown):
        profession = setup_teardown

        profession.jobs().save_many([
            factory(Job).make(),
            factory(Job).make()
        ])

        assert profession.jobs.count() == 2
        assert isinstance(profession.jobs.get(0), Job)
