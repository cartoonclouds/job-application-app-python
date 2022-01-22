from orator.migrations import Migration


class CreateJobApplicationsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('job_applications') as table:
            table.increments('id')
            table.boolean('requires_followup').default(False)
            table.boolean('pinned').default(False)

            # Relations
            table.integer('job_id').unsigned()  # belongs-to-one
            table.integer('company_id').unsigned()  # belongs-to-one

            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('job_applications')
