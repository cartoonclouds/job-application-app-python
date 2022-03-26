import sys
from random import random
from PySide6.QtWidgets import QMessageBox
from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import QApplication


class DatabaseConnectionMixin:
    _dbs: dict[str, QSqlDatabase] = {}

    def __init__(self) -> None:
        self._databaseName: str | None = None

    def _setup(self, databaseName: str | None = None):
        self._databaseName = (
            self._databaseName or databaseName or "db:" + str(int(random() * 100))
        )

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(self._databaseName + ".sqlite")
        db.open()

        # Try to open the connection and handle possible errors
        if not db.open():
            QMessageBox.critical(
                QApplication.activeWindow(),
                "App Name - Error!",
                "Database Error: %s" % db.lastError().databaseText(),
            )
            sys.exit(1)

        self._dbs[self._databaseName] = db

        return db

    def db(self, databaseName: str | None = None) -> QSqlDatabase:
        databaseName = databaseName or self._databaseName

        if databaseName is not None and databaseName in self._dbs:
            return self._dbs[databaseName]
        else:
            return self._setup(databaseName)
