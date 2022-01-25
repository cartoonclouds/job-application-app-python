
from app.models.Address import Address
from app.models.Job import Job
from app.models.Company import Company

from seeds.factories import factory

import pytest


class TestAddress():
    # Constants

    # Fixtures
    @pytest.fixture(scope="function", autouse=True)
    def setup_teardown(self):
        # Setup
        address = factory(Address).create()

        yield address

        # Teardown

    # Helpers

    # Test Cases
    def test_address_has_many_companies(self, setup_teardown):
        address = setup_teardown

        address.companies().save_many([
            factory(Company).make(),
            factory(Company).make()
        ])

        assert address.companies.count() == 2
        assert isinstance(address.companies.get(0), Company)

    def test_address_has_many_jobs(self, setup_teardown):
        address = setup_teardown

        address.jobs().save_many([
            factory(Job).make(),
            factory(Job).make()
        ])

        assert address.jobs.count() == 2
        assert isinstance(address.jobs.get(0), Job)
