"""ProfessionTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from config.factories import Factory

from app.models.Profession import Profession


class ProfessionTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Factory(Profession, 10).create()
