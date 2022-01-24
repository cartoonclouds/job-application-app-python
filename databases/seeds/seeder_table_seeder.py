"""SeederTableSeeder Seeder."""

# from colorama import init, deinit, Fore, Back, Style
from masoniteorm.seeds import Seeder
from app.models.Address import Address
from app.models.Company import Company
from config.factories import Factory
from masoniteorm.query import QueryBuilder

from app.models.JobApplication import JobApplication


class SeederTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        # init()

        # Creates job applications with relationships (eg, jobs, addresses, companies)
        # Factory(JobApplication, 10).create()
        # print(Fore.GREEN + 'JobApplicationTableSeeder seeded!')

        hasColumn = QueryBuilder().statement(
            "SELECT 1 FROM pragma_table_info('companies') WHERE name = '?'", ['address_id'])

        print(hasColumn)
        # print(Address.hasWith('jobs').all().random().id)

        # deinit()
