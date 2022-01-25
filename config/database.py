from orator import DatabaseManager, Model, Schema


databases = {
    'sqlite': {
        'driver': 'sqlite',
        'database': 'jaa_database.sqlite',
        'prefix': '',
        'log_queries': True
    },
}

db = DatabaseManager(databases)
schema = Schema(db)

Model.set_connection_resolver(db)
