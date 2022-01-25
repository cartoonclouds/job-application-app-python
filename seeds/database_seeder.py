from orator.seeds import Seeder
from app.models.Job import Job

from app.models.JobApplication import JobApplication
from app.models.Action import Action

# from seeds.job_application_table_seeder import JobApplicationTableSeeder
from seeds.factories import factory


class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        # self.call(JobApplicationTableSeeder)
        # factory(JobApplication, 5).create()

        # factory(Action).create()

        print(Action.find(4).id, Action.find(4).title)
        print(Action.find(4).following_actions.first().id,
              Action.find(4).following_actions.first().title)
        # print(Job.find(12).actions.first().contact_method)

        # users = factory(User, 3).create()
        # users.each(lambda u: u.save(factory(Post).make()))
