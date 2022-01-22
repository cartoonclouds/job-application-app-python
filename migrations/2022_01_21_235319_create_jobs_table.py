from orator.migrations import Migration


class CreateJobsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('jobs') as table:
            table.increments('id')
            table.medium_text('website').nullable()
            table.long_text('comments').nullable()
            table.text('title').nullable()
            table.datetime('closing_date').nullable()
            table.double('salary', 15, 4).nullable()
            table.double('rate', 15, 4).nullable()
            table.text('rate_unit').nullable()

            # Relations
            table.integer('profession_id').unsigned().nullable()  # one-to-one
            table.integer('employment_type_id').unsigned(
            ).nullable()  # one-to-one
            table.integer('address_id').unsigned().nullable()  # one-to-one

            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('jobs')
