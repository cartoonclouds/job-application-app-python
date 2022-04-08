from orator.orm.model import Model
from orator.schema import Schema
from orator.database_manager import DatabaseManager

from app.services.settings_service import SettingsServiceProvider

settings = SettingsServiceProvider()

databases = {
    "sqlite": {
        "driver": "sqlite",
        "database": settings.database.name,
        "prefix": "",
        "log_queries": False,
    },
}

db = DatabaseManager(databases)
schema = Schema(db)

Model.set_connection_resolver(db)