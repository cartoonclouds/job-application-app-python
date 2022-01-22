"""CompanyTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from config.factories import Factory

from app.models.JobApplication import JobApplication
from app.models.Company import Company


class CompanyTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        jobApplications = JobApplication.get().all()

        for jobApplication in jobApplications:
            jobApplication.attach('company', Factory(Company).make())
