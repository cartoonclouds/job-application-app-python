"""JobApplicationsTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from config.factories import Factory

from app.models.JobApplication import JobApplication
from app.models.Job import Job
from app.models.Profession import Profession


class JobTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        professions = Profession.get()
        jobApplications = JobApplication.get().all()

        for jobApplication in jobApplications:
            jobApplication.attach('job', Factory(Job).make({
                'profession_id': professions.random().id
            }))
