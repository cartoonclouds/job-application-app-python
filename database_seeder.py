from orator.seeds import Seeder

from .seeds.jobs_table_seeder import JobsTableSeeder
from .seeds.job_applications_table_seeder import JobApplicationsTableSeeder


class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        # self.call(JobApplicationsTableSeeder)
        self.call(JobsTableSeeder)
