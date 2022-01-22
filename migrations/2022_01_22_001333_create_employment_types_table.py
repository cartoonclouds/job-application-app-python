from orator.migrations import Migration


class CreateEmploymentTypesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('employment_types') as table:
            table.increments('id')
            table.text('employment_type')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('employment_types')
