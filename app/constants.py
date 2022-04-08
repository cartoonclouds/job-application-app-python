from typing import Final
from PySide6.QtCore import QMargins


"""
    Holds constant variables which won't change with settings.
"""
WINDOW_WIDTH: Final = 1500
WINDOW_HEIGHT: Final = 800

TABLE_X_PADDING = 20  # left and right padding

WIDGET_SPACING: Final = 6
WIDGET_MARGINS: Final = QMargins(
    WIDGET_SPACING, WIDGET_SPACING, WIDGET_SPACING, WIDGET_SPACING
)

ZERO_MARGINS: Final = QMargins(0, 0, 0, 0)

# https://www.w3schools.com/python/python_datetime.asp
# https://codetorial.net/en/pyqt5/basics/datetime.html
DATE_FORMAT_1: Final = "ddd dd MMM, yyyy hh:mm a"

SETTINGS_FILE_PATH: Final = "app/settings.json"
