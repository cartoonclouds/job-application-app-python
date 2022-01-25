
from orator.seeds import Seeder

from app.models.JobApplication import JobApplication
from seeds.factories import factory


class JobApplicationTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        # self.factory(JobApplication, 5).create()
        # .each(
        #     lambda u: u.posts().save(self.factory(Post).make())
        # )
