from orator.orm.model import Model
from orator.schema import Schema
from orator.database_manager import DatabaseManager


databases = {
    "sqlite": {
        "driver": "sqlite",
        "database": "jaa_database.sqlite",
        "prefix": "",
        "log_queries": False,
    },
}

db = DatabaseManager(databases)
schema = Schema(db)

Model.set_connection_resolver(db)
