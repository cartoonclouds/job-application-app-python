from orator.migrations import Migration


class CreateCompaniesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('companies') as table:
            table.increments('id')
            table.text('name')
            table.text('email').nullable()
            table.integer('phone').nullable()
            table.medium_text('website').nullable()
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
