
from app.models import Address
from app.models.Job import Job
from app.models.Company import Company


class TestAddress():
    pass
    # Constants

    # Fixtures

    # Helpers

    # Test Cases
    # def test_address_has_many_companies(self, get_address, capsys):
    #     address = get_address('company')
    #     companies = address.companies

    #     if (companies.count() <= 0):
    #         with capsys.disabled():
    #             print('Address ID without companies: ' + str(address.id))

    #     assert companies.count() > 0
    #     assert isinstance(companies.get(0), Company)

    # def test_address_has_many_jobs(self, get_address, capsys):
    #     address = get_address('job')
    #     jobs = address.jobs

    #     assert jobs.count() > 0
    #     assert isinstance(jobs.get(0), Job)
