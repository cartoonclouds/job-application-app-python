from orator.migrations import Migration


class CreateAddressesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        self.schema.drop_if_exists("addresses")

        with self.schema.create("addresses") as table:
            table.increments("id")
            table.text("address_line_1")
            table.text("address_line_2").nullable()
            table.text("suburb").nullable()
            table.text("city").nullable()
            table.text("state").nullable()
            table.integer("postcode").nullable()
            table.text("country").nullable()
            table.boolean("is_user").default(False)

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("addresses")
