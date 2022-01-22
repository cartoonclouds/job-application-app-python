"""JobApplicationsTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from config.factories import Factory
from config.database import DB

from app.models.JobApplication import JobApplication


class JobApplicationTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Factory(JobApplication, 9).create()
