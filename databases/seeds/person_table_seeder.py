"""PersonTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from config.factories import Factory

from app.models.Person import Person
from app.models.Company import Company


class PersonTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        companies = Company.get().all()

        for company in companies:
            company.attach('person', Factory(Person).make())
