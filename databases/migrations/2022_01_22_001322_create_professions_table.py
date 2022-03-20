from orator.migrations import Migration
from orator.schema.blueprint import Blueprint


class CreateProfessionsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        self.schema.drop_if_exists("professions")

        with self.schema.create("professions") as table:
            table: Blueprint

            table.increments("id")
            table.text("profession")

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("professions")
