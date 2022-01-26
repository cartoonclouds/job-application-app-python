
from app.models.Company import Company
from app.models.Person import Person

from seeds.factories import factory

import pytest


class TestPerson():
    # Constants

    # Fixtures
    @pytest.fixture(scope="function", autouse=True)
    def setup_teardown(self):
        # Setup
        Person.truncate()
        person = factory(Person).create()

        yield person

        # Teardown
        Person.truncate()

    # Helpers

    # Test Cases
    def test_person_has_many_companies(self, setup_teardown):
        person = setup_teardown

        person.companies().save_many([
            factory(Company).make(),
            factory(Company).make()
        ])

        assert person.companies.count() == 2
        assert isinstance(person.companies.get(0), Company)
