"""AddressTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from config.factories import Factory

from app.models.Address import Address


class AddressTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        jobs = Job.get().all()
        companies = Company.get().all()

        for job in jobs:
            job.attach('address', Factory(Address).make())

        for company in companies:
            company.attach('address', Factory(Address).make())
