
from app.models.Address import Address
from app.models.Company import Company
from app.models.JobApplication import JobApplication
from app.models.Person import Person

from seeds.factories import factory

import pytest


class TestCompany():
    pass
    # Constants

    # Fixtures
    @pytest.fixture(scope="function", autouse=True)
    def setup_teardown(self):
        # Setup
        company = factory(Company).create()

        yield company

        # Teardown

    # Helpers

    # Test Cases
    def test_company_has_many_job_applications(self, setup_teardown):
        company = setup_teardown

        company.job_applications().save_many([
            factory(JobApplication).make(),
            factory(JobApplication).make()
        ])

        assert company.job_applications.count() == 2
        assert isinstance(company.job_applications.get(0), JobApplication)

    def test_company_has_an_address(self, setup_teardown):
        company = setup_teardown

        company.address().associate(
            factory(Address).create()
        )

        assert isinstance(company.address, Address)

    def test_company_has_a_person(self, setup_teardown):
        company = setup_teardown

        company.person().associate(
            factory(Person).create()
        )

        assert isinstance(company.person, Person)
