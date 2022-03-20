from orator.migrations import Migration
from orator.schema.blueprint import Blueprint


class CreateActionsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        self.schema.drop_if_exists("actions")

        with self.schema.create('actions') as table:
            table: Blueprint
            
            table.increments('id')
            table.text('title').nullable()
            table.boolean('requires_followup').default(False)
            table.boolean('awaiting_response').default(False)
            table.boolean('pinned').default(False)
            table.text('contact_method').nullable()

            # morphs
            table.integer('actionable_id').unsigned().nullable()
            table.text('actionable_type').nullable()

            # Relations
            table.integer('person_id').unsigned().nullable()

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('actions')
