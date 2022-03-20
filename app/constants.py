import typing
from PySide6.QtCore import QMargins


class Constants:
    WINDOW_WIDTH: typing.Final = 1500
    WINDOW_HEIGHT: typing.Final = 800

    FORM_LABEL_SIZE = 11

    WIDGET_SPACING = 6
    WIDGET_MARGINS = QMargins(
        WIDGET_SPACING, WIDGET_SPACING, WIDGET_SPACING, WIDGET_SPACING
    )

    ZERO_MARGINS = QMargins(0, 0, 0, 0)

    # https://www.w3schools.com/python/python_datetime.asp
    # https://codetorial.net/en/pyqt5/basics/datetime.html
    DATE_FORMAT = "ddd dd MMM, yyyy hh:mm a"
