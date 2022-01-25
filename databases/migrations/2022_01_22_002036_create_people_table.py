from orator.migrations import Migration


class CreatePeopleTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        self.schema.drop_if_exists("people")

        with self.schema.create('people') as table:
            table.increments('id')
            table.text('name')
            table.text('title').nullable()
            table.text('email').nullable()

            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('people')
