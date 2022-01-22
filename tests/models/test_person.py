
from app.models.Company import Company


class TestPerson():
    # Constants

    # Fixtures

    # Helpers

    # Test Cases
    def test_person_has_many_companies(self, get_person):
        person = get_person()
        companies = person.companies

        assert companies.count() > 0
        assert isinstance(companies.get(0), Company)
