
from app.models.Job import Job


class TestProfession():
    # Constants

    # Fixtures

    # Helpers

    # Test Cases
    def test_profession_has_many_jobs(self, get_profession):
        profession = get_profession()
        jobs = profession.jobs

        assert jobs.count() > 0
        assert isinstance(jobs.get(0), Job)
