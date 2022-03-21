from copy import copy, deepcopy
from app.models.JobApplication import JobApplication
from app.repositories.DBRepository import DBRepository
from seeds.factories import factory
import pytest


class TestDBRepository:
    # Constants
    JOB_APPLICATION_COUNT = 8

    # Fixtures
    @pytest.fixture(scope="function", autouse=True)
    def setup_teardown(self):
        JobApplication.truncate()

        jobApplications = factory(
            JobApplication, DBRepository.JOB_APPLICATION_COUNT
        ).create()
        dbRepository = DBRepository(jobApplications)

        yield dbRepository

        # Teardown
        JobApplication.truncate()

    # Helpers

    # Test Cases
    def test_repository_is_singleton(self):
        repoDict = {"": ""}
        dbRepository = DBRepository(repoDict)

        assert (
            id(dbRepository)
            == id(DBRepository(repoDict))
            == id(copy(DBRepository(repoDict)))
            == id(deepcopy(DBRepository(repoDict)))
        )
