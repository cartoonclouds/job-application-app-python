from orator.seeds import Seeder
from app.models.Company import Company
from app.models.Job import Job

from app.models.JobApplication import JobApplication
from app.models.Action import Action
from app.repositories.JobApplicationRepository import JobApplicationRepository

# from seeds.job_application_table_seeder import JobApplicationTableSeeder
from seeds.factories import factory
from config.database import db


class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        # Create 5 job applications with associated relations
        jobApplications = factory(JobApplication, 2).create()
        jobApplications.each(
            lambda ja: ja.job().save(factory(Action).make())
        )

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

        # ja = factory(JobApplication).create()
        # ja = JobApplication.first()

        # print(JobApplication.first().get_table_column_count())

        # print({"Deleted At"}.issubset(
        #     {"Created At", "Updated At", "Deleted At"}))

        # jar.load_all()
        # i = list(jar.items())[0]

        # jobApp = i[1]

        # print(getattr(jobApp, 'title'))

        # SELECT name FROM PRAGMA_table_info("job_applications")

        # a = columns.items()
        # print(list(a.values()))

        # new_list = list(d.values())
        # print(new_list)

        # print(*columns, sep="\n")
        # print('\n'.join(map(str, columns)))

        # print(db.raw('SELECT * FROM PRAGMA_TABLE_INFO("?")',
        #       [JobApplication.__table__]))
        # print(JobApplication.__table__)
        # jar = JobApplicationRepository(jas)
        # jar.load_all()
        #
        # print('\n'.join(map(str, jar.values())))
        # print(jar[2])
