from masoniteorm.migrations import Migration


class CreateJobsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        self.schema.drop_table_if_exists("jobs")

        with self.schema.create('jobs') as table:
            table.increments('id')
            table.text('title').nullable()
            table.text('website').nullable()
            table.datetime('closing_date').nullable()
            table.double('salary', 8).nullable()
            table.double('rate', 8).nullable()
            table.text('rate_unit').nullable()
            table.text('employment_type').nullable()
            table.long_text('comments').nullable()

            # Relations
            table.unsigned_integer('profession_id').nullable()  # one-to-one
            table.unsigned_integer('address_id').nullable()  # one-to-one

            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('jobs')
