from orator.seeds import Seeder

from .factories import job_applications_factory, job_factory, company_factory
from .models.job import Job
from .models.job_application import JobApplication
from .models.company import Company


class JobsTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.factory.register(
            JobApplication, job_applications_factory)
        self.factory.register(Job, job_factory)
        self.factory.register(Company, company_factory)

        self.factory(Job, 2).create().each(
            lambda u: u.job_application().save(self.factory(JobApplication).make())
        )
