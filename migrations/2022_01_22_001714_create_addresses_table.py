from orator.migrations import Migration


class CreateAddressesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('addresses') as table:
            table.increments('id')
            table.medium_text('address_line_1')
            table.medium_text('address_line_2').nullable()
            table.text('suburb').nullable()
            table.text('state').nullable()
            table.text('postcode').nullable()
            table.text('country').nullable()

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('addresses')
