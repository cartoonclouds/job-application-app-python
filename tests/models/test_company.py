
from app.models.Address import Address
from app.models.JobApplication import JobApplication
from app.models.Person import Person


class TestCompany():
    # Constants

    # Fixtures

    # Helpers

    # Test Cases
    def test_company_has_many_job_applications(self, get_company):
        company = get_company()
        job_applications = company.job_applications
        
        assert job_applications.count() > 0
        assert isinstance(job_applications.get(0), JobApplication)

    def test_job_has_an_address(self, get_company):
        company = get_company()
        address = company.address
        
        assert isinstance(address, Address)

    def test_job_has_a_person(self, get_company):
        company = get_company()
        person = company.person
        
        assert isinstance(person, Person)
