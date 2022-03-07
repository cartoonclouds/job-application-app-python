import sys
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QFrame, QMessageBox
from PySide6.QtSql import (
    QSqlDatabase,
    QSqlDriver,
    QSqlRelationalTableModel,
    QSqlRelation,
    QSqlTableModel,
)
from PySide6.QtWidgets import QApplication, QStyle


class DatabaseConnectionMixin:
    _db: QSqlDatabase | None = None

    def _setup(self):
        self._db = QSqlDatabase.addDatabase("QSQLITE")
        self._db.setDatabaseName("jaa_database.sqlite")
        self._db.open()

        # Try to open the connection and handle possible errors
        if not self._db.open():
            QMessageBox.critical(
                QApplication.activeWindow(),
                "App Name - Error!",
                "Database Error: %s" % self._db.lastError().databaseText(),
            )
            sys.exit(1)

        return self._db

    def db(self) -> QSqlDatabase:
        return self._db if self._db else self._setup()
