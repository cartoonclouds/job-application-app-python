from orator.migrations import Migration
from orator.schema.blueprint import Blueprint


class CreateCompaniesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        self.schema.drop_if_exists("companies")

        with self.schema.create('companies') as table:
            table: Blueprint
            
            table.increments('id')
            table.text('name')
            table.text('email').nullable()
            table.integer('phone').nullable()
            table.integer('mobile').nullable()
            table.text('website').nullable()
            table.long_text('comments').nullable()

            # Relations
            table.integer('address_id').unsigned()
            table.integer('person_id').unsigned().nullable()

            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('companies')
