"""SeederTableSeeder Seeder."""

# from colorama import init, deinit, Fore, Back, Style
from masoniteorm.seeds import Seeder

from databases.seeds.job_application_table_seeder import JobApplicationTableSeeder
from databases.seeds.job_table_seeder import JobTableSeeder
from databases.seeds.company_table_seeder import CompanyTableSeeder
from databases.seeds.person_table_seeder import PersonTableSeeder
from databases.seeds.profession_table_seeder import ProfessionTableSeeder
from databases.seeds.address_table_seeder import AddressTableSeeder


class SeederTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        # init()

        ProfessionTableSeeder(Seeder).run()
        # # print(Fore.GREEN + 'ProfessionTableSeeder seeded!')

        # JobApplicationTableSeeder(Seeder).run()
        # # print(Fore.GREEN + 'JobApplicationTableSeeder seeded!')

        # JobTableSeeder(Seeder).run()
        # # print(Fore.GREEN + 'JobTableSeeder seeded!')

        # CompanyTableSeeder(Seeder).run()
        # # print(Fore.GREEN + 'CompanyTableSeeder seeded!')

        # AddressTableSeeder(Seeder).run()
        # # print(Fore.GREEN + 'AddressTableSeeder seeded!')

        # PersonTableSeeder(Seeder).run()
        # print(Fore.GREEN + 'PersonTableSeeder seeded!')

        # print(Style.RESET_ALL)
        # deinit()
