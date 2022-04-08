# Standard Library
from distutils import file_util
import json
import os
from collections import defaultdict
from typing import Any

from app.constants import SETTINGS_FILE_PATH
from app.utils.Metaclasses.Singleton import Singleton
from app.utils.dict_wrap import DictWrap


# APP SETTINGS
# ///////////////////////////////////////////////////////////////
class SettingsServiceProvider(metaclass=Singleton):
    """Settings repository

    URL: https://doc.qt.io/qtforpython/PySide6/QtCore/QSettings.html
    """

    # APP PATH
    # ///////////////////////////////////////////////////////////////
    app_path = os.path.abspath(os.getcwd())

    settings_path = os.path.normpath(os.path.join(app_path, SETTINGS_FILE_PATH))

    if not os.path.isfile(settings_path):
        print(
            f'WARNING: "settings.json" not found! check in the folder {settings_path}'
        )

    # INIT SETTINGS
    # ///////////////////////////////////////////////////////////////
    def __init__(self):
        super(SettingsServiceProvider, self).__init__()

        # Just to have objects references
        self.items = DictWrap()

        # DESERIALIZE
        self.deserialize()

    # SERIALIZE JSON
    # ///////////////////////////////////////////////////////////////
    def serialize(self):
        # WRITE JSON FILE
        with open(self.settings_path, "w", encoding="utf-8") as write:
            write.write(self.items.toJson())

    # DESERIALIZE JSON
    # ///////////////////////////////////////////////////////////////
    def deserialize(self):
        # READ JSON FILE
        with open(self.settings_path, "r", encoding="utf-8") as reader:
            settings = json.loads(reader.read())
            self.items = DictWrap(settings)

    def __getattr__(self, name: str) -> Any:
        return self.items[name]
