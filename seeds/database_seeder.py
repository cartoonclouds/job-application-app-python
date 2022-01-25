from orator.seeds import Seeder
from app.models.Company import Company
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
        # Create 5 job applications with associated relations
        # jobApplications = factory(JobApplication, 5).create()
        # jobApplications.each(
        #     lambda ja: ja.job().save(factory(Action).make())
        # )

        # Get jobs and add 3 actions to each
        # jobs = Job.get()
        # jobs.each(
        #     lambda j: j.actions().save(factory(Action).make())
        # )
        # jobs.each(
        #     lambda j: j.actions().save(factory(Action).make())
        # )
        # jobs.each(
        #     lambda j: j.actions().save(factory(Action).make())
        # )

        # Get half the actions and add 2 child actions
        # actions = Action.get().take(int(Action.count() / 2))
        # actions.each(
        #     lambda a: a.child_actions().save(factory(Action).make())
        # )
        # actions.each(
        #     lambda a: a.child_actions().save(factory(Action).make())
        # )
        # job = factory(Job).create()

        # job.job_application().save(
        #     factory(JobApplication).make()
        # )
        print(Company.find(1).address.id)
