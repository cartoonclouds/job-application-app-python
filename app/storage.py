import typing
from PySide6.QtCore import QMargins

from app.repositories.JobApplicationRepository import JobApplicationRepository


class Storage:
    jobApplications = JobApplicationRepository()
    jobApplications.loadAll()

    WINDOW_WIDTH: typing.Final = 1500
    WINDOW_HEIGHT: typing.Final = 800

    FORM_LABEL_SIZE = 11

    WIDGET_SPACING = 6

    ZERO_MARGINS = QMargins(0, 0, 0, 0)
