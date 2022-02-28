"""CreateJobApplicationsTable Migration."""

from orator.migrations import Migration


class CreateJobApplicationsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        self.schema.drop_if_exists("job_applications")

        with self.schema.create("job_applications") as table:
            table.increments("id")
            table.text("title").nullable()
            table.boolean("requires_followup").default(False)
            table.boolean("pinned").default(False)

            # Relations
            table.integer("company_id").unsigned()

            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("job_applications")
