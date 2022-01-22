from orator import DatabaseManager, Schema

databases = {
    'default': 'sqlite',
    'sqlite': {
        'driver': 'sqlite',
        'database': 'jaa_database.sqlite',
        'prefix': '',
        'log_queries': True
    }
}

db = DatabaseManager(databases)
# https://orator-orm.com/docs/0.9/schema_builder.html#adding-columns
schema = Schema(db)
