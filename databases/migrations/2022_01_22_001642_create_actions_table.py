from masoniteorm.migrations import Migration


class CreateActionsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        self.schema.drop_table_if_exists("actions")

        with self.schema.create('actions') as table:
            table.increments('id')
            table.text('title').nullable()
            table.boolean('requires_followup').default(False)
            table.boolean('pinned').default(False)
            table.text('contact_method').nullable()

            table.morphs('actionable')

            # Relations
            table.unsigned_integer('person_id').nullable()

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('actions')
