from masoniteorm.connections import ConnectionResolver

DATABASES = {
    'default': 'sqlite',
    'sqlite': {
        'driver': 'sqlite',
        'database': 'jaa_database.sqlite',
        'prefix': '',
        'log_queries': True
    }
}

DB = ConnectionResolver().set_connection_details(DATABASES)
