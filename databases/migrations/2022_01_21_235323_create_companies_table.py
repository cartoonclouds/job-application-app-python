from masoniteorm.migrations import Migration


class CreateCompaniesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        self.schema.drop_table_if_exists("companies")
        
        with self.schema.create('companies') as table:
            table.increments('id')
            table.text('name')
            table.text('email').nullable()
            table.integer('phone').nullable()
            table.text('website').nullable()
            table.long_text('comments').nullable()

            # Relations
            table.unsigned_integer('address_id')
            table.unsigned_integer('person_id').nullable()

            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('companies')
