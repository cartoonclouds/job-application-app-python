from orator.migrations import Migration


class CreateActionsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('actions') as table:
            table.increments('id')
            table.boolean('requires_followup').default(False)
            table.text('title').nullable()
            table.text('contact_method').nullable()

            table.morphs('actionable')

            # Relations
            table.integer('person_id').unsigned().nullable()

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('actions')
