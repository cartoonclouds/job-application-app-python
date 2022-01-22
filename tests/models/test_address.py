
from app.models.Job import Job
from app.models.Company import Company


class TestAddress():
    # Constants

    # Fixtures

    # Helpers

    # Test Cases
    def test_address_has_many_companies(self, get_address, capsys):
        address = get_address()
        companies = address.companies

        assert companies.count() > 0
        assert isinstance(companies.get(0), Company)

    def test_address_has_many_jobs(self, get_address, capsys):
        address = get_address()
        jobs = address.jobs

        assert jobs.count() > 0
        assert isinstance(jobs.get(0), Job)
