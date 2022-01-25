"""SeederTableSeeder Seeder."""

# from colorama import init, deinit, Fore, Back, Style
from masoniteorm.seeds import Seeder
from config.factories import Factory

# from app.models.JobApplication import JobApplication
from app.models.Action import Action


class SeederTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        # init()

        # Creates job applications with relationships (eg, jobs, addresses, companies)
        # Factory(JobApplication, 10).create()
        # print(Fore.GREEN + 'JobApplicationTableSeeder seeded!')

        Factory(Action, 10).create()

        # from app.models.Job import Job
        # print(Job.find(1).actions())
        # deinit()
