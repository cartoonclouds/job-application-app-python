from orator.migrations import Migration
from orator.schema.blueprint import Blueprint


class CreateJobsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        self.schema.drop_if_exists("jobs")

        with self.schema.create("jobs") as table:
            table: Blueprint

            table.increments("id")
            table.text("title").nullable()
            table.text("website").nullable()
            table.datetime("closing_date").nullable()
            table.enum("pay_option", ["salary", "rate"]).default()
            table.double("salary", 8, 0).nullable()
            table.double("rate", 8, 0).nullable()
            table.text("rate_unit").nullable()
            table.text("employment_type").nullable()
            table.long_text("comments").nullable()

            # Relations
            table.integer("job_application_id").unsigned()
            table.integer("profession_id").unsigned().nullable()
            table.integer("address_id").unsigned().nullable()

            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("jobs")
